import React, { useState } from "react";

function UploadCSV({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [toast, setToast] = useState(null);

  const showToast = (message, type = "info") => {
    setToast({ message, type });
    setTimeout(() => setToast(null), 3000);
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;

    setFile(selectedFile);
    showToast("File selected. Click Upload CSV to upload.", "success");
  };

  const handleUpload = async () => {
    if (!file) {
      showToast("Please select a CSV file first", "error");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    showToast("Uploading file...", "info");

    try {
      const response = await fetch("http://127.0.0.1:8000/api/upload/", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Upload failed");
      }

      onUploadSuccess({
        summary: data.summary,
        fileName: file.name,
        uploadedAt: new Date().toLocaleString(),
      });
      setFile(null);
      showToast("CSV uploaded successfully", "success");
    } catch (err) {
      showToast(err.message, "error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-card">
      <div className="upload-actions">
        <label className="file-input">
          <input type="file" onChange={handleFileChange} />
          <span>Choose CSV file</span>
        </label>

        <button
          className="primary-btn"
          onClick={handleUpload}
          disabled={loading}
        >
          {loading ? "Uploading..." : "Upload CSV"}
        </button>
      </div>

      {toast && (
        <div className={`toast toast-${toast.type}`}>
          {toast.message}
        </div>
      )}
    </div>
  );
}

export default UploadCSV;