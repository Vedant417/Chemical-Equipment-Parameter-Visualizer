import React, { useState } from "react";
import Charts from "../components/Charts";
import HistoryTable from "../components/HistoryTable";
import UploadCSV from "../components/UploadCSV";
import Header from "../components/Header";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";
import "../App.css";

function Dashboard() {
  const [reportData, setReportData] = useState(null);
  const [refreshKey, setRefreshKey] = useState(0);
  const [previousSummary, setPreviousSummary] = useState(null);

  const getPercentageChange = (current, previous) => {
    if (!previous || previous === 0) return null;
    return (((current - previous) / previous) * 100).toFixed(1);
  };

  const handleDownloadPDF = async () => {
    const element = document.getElementById("pdf-report");
    if (!element || !reportData) return;

    const canvas = await html2canvas(element, { scale: 2 });
    const imgData = canvas.toDataURL("image/png");

    const pdf = new jsPDF("p", "mm", "a4");
    const pdfWidth = pdf.internal.pageSize.getWidth();

    const fileName = reportData.fileName || "Uploaded CSV";
    const uploadedAt = reportData.uploadedAt
      ? new Date(reportData.uploadedAt).toLocaleString()
      : new Date().toLocaleString();

    pdf.setFontSize(14);
    pdf.text("Chemical Equipment Report", 14, 15);

    pdf.setFontSize(10);
    pdf.text(`File Name: ${fileName}`, 14, 22);
    pdf.text(`Uploaded At: ${uploadedAt}`, 14, 28);

    const imgY = 35;
    const imgHeight = (canvas.height * pdfWidth) / canvas.width;

    pdf.addImage(imgData, "PNG", 0, imgY, pdfWidth, imgHeight);

    pdf.save("Chemical_Equipment_Report.pdf");
  };

  return (
    <div className="app-container">
      <Header />

      <main className="main-content">
        {/* Upload */}
        <section id="upload-section" className="upload-section glass-card">
          <h2>Upload Equipment CSV</h2>
          <UploadCSV
            onUploadSuccess={(data) => {
              setPreviousSummary(reportData?.summary || null);
              setReportData(data);
              setRefreshKey((prev) => prev + 1);
            }}
          />
        </section>

        {reportData && (
          <section id="charts-section" className="charts-section glass-card">
            <div id="pdf-report">
              <div id="summary-anchor" className="scroll-anchor"></div>

              <h2>Summary</h2>
              <div className="summary-cards">
              <div className="summary-card">
                <span>🏭 Total Equipment</span>
                <span
                  className="info"
                  data-tip="Total number of uploaded equipment"
                >
                  ⓘ
                </span>
                <h3>{reportData.summary.total_equipment}
                {previousSummary && (
                  <small
                    style={{
                      color:
                        getPercentageChange(
                          reportData.summary.total_equipment,
                          previousSummary.total_equipment
                        ) >= 0
                          ? "#16a34a"
                          : "#dc2626",
                    }}
                  >
                    {getPercentageChange(
                      reportData.summary.total_equipment,
                      previousSummary.total_equipment
                    ) >= 0
                      ? "↑"
                      : "↓"}{" "}
                    {Math.abs(
                      getPercentageChange(
                        reportData.summary.total_equipment,
                        previousSummary.total_equipment
                      )
                    )}
                    %
                  </small>
                )}
                </h3>
              </div>

              <div className="summary-card">
                <span>🌊 Avg Flowrate</span>
                <span
                  className="info"
                  data-tip="Average flowrate across all equipment"
                >
                  ⓘ
                </span>
                <h3>
                  {reportData.summary.avg_flowrate}
                  <span className="unit"> L/min</span>
                </h3>
              </div>

              <div className="summary-card">
                <span>🧪 Avg Pressure</span>
                <span
                  className="info"
                  data-tip="Average pressure across all equipment"
                >
                  ⓘ
                </span>
                <h3>
                  {reportData.summary.avg_pressure}
                  <span className="unit"> bar</span>
                </h3>
              </div>

              <div className="summary-card">
                <span>🌡️ Avg Temperature</span>
                <span
                  className="info"
                  data-tip="Average temperature across all equipment"
                >
                  ⓘ
                </span>
                <h3>
                  {reportData.summary.avg_temperature}
                  <span className="unit"> °C</span>
                </h3>
              </div>
            </div>
            <h2>Charts</h2>
              <div id="charts-anchor" className="scroll-anchor"></div>
              <Charts summary={reportData.summary} />
            </div>

            <div className="download-card">
              <button className="primary-btn" onClick={handleDownloadPDF}>
                Download PDF
              </button>
            </div>
          </section>
        )}

        {/* History */}
        <section id="history-section" className="history-section glass-card">
          <h2>Upload History</h2>
          <HistoryTable refreshKey={refreshKey} />
        </section>
      </main>
    </div>
  );
}

export default Dashboard;