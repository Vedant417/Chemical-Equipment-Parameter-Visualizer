import React, { useEffect, useState } from "react";

function HistoryTable({ refreshKey }) {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchHistory = async () => {
      setLoading(true);
      try {
        const response = await fetch("http://127.0.0.1:8000/api/history/");
        const data = await response.json();
        setHistory(data);
      } catch (error) {
        console.error("Error fetching history:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchHistory();
  }, [refreshKey]);

  if (loading) {
    return <p>Loading history...</p>;
  }

  if (history.length === 0) {
    return <p>No upload history available.</p>;
  }

  return (
    <table style={{ width: "100%", borderCollapse: "collapse" }}>
      <thead>
        <tr>
          <th>File Name</th>
          <th>Total Equipment</th>
          <th>Avg Flowrate</th>
          <th>Avg Pressure</th>
          <th>Avg Temperature</th>
          <th>Uploaded At</th>
        </tr>
      </thead>
      <tbody>
        {history.map((item) => (
          <tr key={item.id}>
            <td>{item.filename}</td>
            <td>{item.total_equipment}</td>
            <td>{item.avg_flowrate}</td>
            <td>{item.avg_pressure}</td>
            <td>{item.avg_temperature}</td>
            <td>{new Date(item.uploaded_at).toLocaleString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default HistoryTable;