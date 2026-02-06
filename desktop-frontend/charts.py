from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ChartCanvas(FigureCanvas):
    def __init__(self, records=None, chart_type="line"):
        self.figure = Figure(figsize=(6, 4))
        super().__init__(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.plot(records, chart_type)

    def plot(self, records, chart_type):
        self.ax.clear()

        if not records:
            self.ax.text(0.5, 0.5, "No records found",
                         ha="center", va="center")
            self.draw()
            return

        names = [r["Equipment Name"] for r in records]

        if chart_type == "line":
            values = [r["Flowrate"] for r in records]
            self.ax.plot(names, values, marker="o")
            self.ax.set_title("Flowrate by Equipment")
            self.ax.set_ylabel("Flowrate")

        elif chart_type == "bar":
            values = [r["Pressure"] for r in records]
            self.ax.bar(names, values)
            self.ax.set_title("Pressure by Equipment")
            self.ax.set_ylabel("Pressure")

        elif chart_type == "pie":
            from collections import Counter
            types = [r["Type"] for r in records]
            counts = Counter(types)
            self.ax.pie(
                counts.values(),
                labels=counts.keys(),
                autopct="%1.1f%%"
            )
            self.ax.set_title("Equipment Type Distribution")

        self.figure.tight_layout()
        self.draw()
