from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class AnalyticsDashboardWindow(QWidget):
    def __init__(self, data):
        super().__init__()

        self.setWindowTitle("ChemEquip Visualizer")
        self.setGeometry(300, 200, 900, 700)

        layout = QVBoxLayout()

        # ---------------- SAFE DATA ----------------
        summary = data.get("summary", {})
        records = data.get("records", [])

        avg_flow = summary.get("avg_flowrate", 0)
        avg_pressure = summary.get("avg_pressure", 0)
        avg_temp = summary.get("avg_temperature", 0)
        type_dist = summary.get("type_distribution", {})

        # ---------------- TEXT SUMMARY ----------------
        layout.addWidget(QLabel("📊 Equipment Analytics"))
        layout.addWidget(QLabel(f"Average Flowrate: {avg_flow}"))
        layout.addWidget(QLabel(f"Average Pressure: {avg_pressure}"))
        layout.addWidget(QLabel(f"Average Temperature: {avg_temp}"))

        # ---------------- FLOWRATE TREND ----------------
        flow_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        ax1 = flow_canvas.figure.add_subplot(111)

        if records:
            flowrates = [r.get("Flowrate", 0) for r in records]
            ax1.plot(flowrates, marker="o")
            ax1.set_title("Flowrate Trend")
            ax1.set_xlabel("Equipment Index")
            ax1.set_ylabel("Flowrate")
        else:
            ax1.text(0.5, 0.5, "No records found", ha="center", va="center")

        layout.addWidget(flow_canvas)

        # ---------------- PRESSURE DISTRIBUTION ----------------
        pressure_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        ax2 = pressure_canvas.figure.add_subplot(111)

        if records:
            pressures = [r.get("Pressure", 0) for r in records]
            ax2.bar(range(len(pressures)), pressures)
            ax2.set_title("Pressure Distribution")
            ax2.set_xlabel("Equipment Index")
            ax2.set_ylabel("Pressure")
        else:
            ax2.text(0.5, 0.5, "No records found", ha="center", va="center")

        layout.addWidget(pressure_canvas)

        # ---------------- EQUIPMENT TYPE PIE ----------------
        type_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        ax3 = type_canvas.figure.add_subplot(111)

        if type_dist:
            labels = list(type_dist.keys())
            sizes = list(type_dist.values())
            ax3.pie(sizes, labels=labels, autopct="%1.1f%%")
            ax3.set_title("Equipment Type Distribution")
        else:
            ax3.text(0.5, 0.5, "No records found", ha="center", va="center")

        layout.addWidget(type_canvas)

        self.setLayout(layout)
