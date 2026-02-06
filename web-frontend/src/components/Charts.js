import React from "react";
import { Bar, Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend
);

function Charts({ summary }) {
  if (!summary) {
    return <p>No chart data available.</p>;
  }

  const barData = {
    labels: ["Flowrate", "Pressure", "Temperature"],
    datasets: [
      {
        label: "Average Values",
        data: [
          summary.avg_flowrate,
          summary.avg_pressure,
          summary.avg_temperature,
        ],
        backgroundColor: ["#3b82f6", "#10b981", "#f59e0b"],
      },
    ],
  };

  const pieData = {
    labels: Object.keys(summary.type_distribution),
    datasets: [
      {
        data: Object.values(summary.type_distribution),
        backgroundColor: [
          "#6366f1",
          "#ec4899",
          "#22c55e",
          "#f97316",
          "#06b6d4",
        ],
      },
    ],
  };

  return (
    <div className="charts-grid">
      <div className="glass-card chart-card">
        <h3>Average Parameters</h3>
        <Bar data={barData} />
      </div>

      <div className="glass-card chart-card">
        <h3>Equipment Type Distribution</h3>
        <Pie data={pieData} />
      </div>
    </div>
  );

}

export default Charts;