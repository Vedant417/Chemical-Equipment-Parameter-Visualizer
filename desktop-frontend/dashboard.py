from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFileDialog,
    QScrollArea, QFrame
)
from PyQt5.QtCore import Qt  
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_pdf import PdfPages
from api import upload_csv as api_upload_csv
from theme import GLASS_STYLE
from login import LoginWindow  
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from datetime import datetime

class DashboardWindow(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.data = None
        self.upload_history = []

        self.setWindowTitle("Equipment Analytics Dashboard")
        self.resize(1400, 900)     # desktop ratio
        self.setMinimumSize(1200, 800)
        self.setStyleSheet(GLASS_STYLE)
        self.showMaximized()

        # -------- SCROLL ROOT --------
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        root = QWidget()
        root_layout = QVBoxLayout(root)
        root_layout.setSpacing(32)
        root_layout.setContentsMargins(30, 30, 30, 30)

        # ================= HEADER =================
        header = QFrame()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 16, 20, 16)

        left_header = QVBoxLayout()
        right_header = QVBoxLayout()
        right_header.setAlignment(Qt.AlignTop | Qt.AlignRight)

        header_layout.addLayout(left_header)
        header_layout.addStretch()
        header_layout.addLayout(right_header)

        title = QLabel("ChemEquip <span style='color:#22c55e;'>Visualizer</span>")
        title.setStyleSheet("""
            font-size: 20px;
            font-weight: 800;
            color: #14532d;
        """)
        left_header.addWidget(title)

        left_header.addSpacing(6)
        left_header.addWidget(QLabel("✅ Login Successful"))
        left_header.addWidget(QLabel(f"Username: {user.get('username', 'User')}"))
        left_header.addWidget(QLabel(f"Email: {user.get('email', '')}"))

        # ✅ STATUS LABEL (CREATE FIRST)
        self.status_label = QLabel("📂 Upload a CSV file to view analytics")
        self.status_label.setStyleSheet("color:#4ade80; font-weight:bold;")
        left_header.addWidget(self.status_label)

        # ✅ LOGOUT BUTTON
        logout_btn = QPushButton("🚪 Logout")
        logout_btn.setFixedWidth(120)
        logout_btn.clicked.connect(self.logout)
        right_header.addWidget(logout_btn)

        root_layout.addWidget(header)


        # ================= ACTION BAR =================
        action_bar = QFrame()
        action_layout = QHBoxLayout(action_bar)

        action_layout.setSpacing(16)
        action_layout.setContentsMargins(16, 12, 16, 12)

        upload_btn = QPushButton("📂 Upload CSV File")
        upload_btn.clicked.connect(self.upload_csv)

        pdf_btn = QPushButton("📄 Download PDF Report")
        pdf_btn.clicked.connect(self.export_pdf)

        action_layout.addWidget(upload_btn)
        action_layout.addWidget(pdf_btn)

        root_layout.addWidget(action_bar)

        # ================= STATS =================
        stats_row = QHBoxLayout()
        stats_row.setSpacing(18)

        self.total_eq = self.stat_card("🏭 Total Equipment", "-")
        self.avg_flow = self.stat_card("🌊 Avg Flowrate", "-")
        self.avg_pressure = self.stat_card("🧪 Avg Pressure", "-")
        self.avg_temp = self.stat_card("🌡️ Avg Temperature", "-")

        for card in [self.total_eq, self.avg_flow, self.avg_pressure, self.avg_temp]:
            stats_row.addWidget(card)

        stats_frame = QFrame()
        stats_frame.setLayout(stats_row)
        root_layout.addWidget(stats_frame)

        # ================= CHARTS =================
        self.flow_canvas = self.create_canvas("Flowrate Trend")
        self.pressure_canvas = self.create_canvas("Pressure Distribution")
        self.type_canvas = self.create_canvas("Equipment Type Distribution")

        root_layout.addWidget(self.wrap_chart(self.flow_canvas))
        root_layout.addWidget(self.wrap_chart(self.pressure_canvas))
        root_layout.addWidget(self.wrap_chart(self.type_canvas))

        # ================= UPLOAD HISTORY =================
        history_frame = QFrame()
        history_layout = QVBoxLayout(history_frame)

        # ===== CUSTOM TABLE HEADER (FIXED & VISIBLE) =====
        header_row = QFrame()
        header_row.setStyleSheet("""
        QFrame {
            background-color: rgba(220, 252, 231, 0.95);
            border-radius: 12px;
        }
        """)

        header_layout = QHBoxLayout(header_row)
        header_layout.setContentsMargins(12, 10, 12, 10)
        header_layout.setSpacing(0)

        headers = [
            "File Name",
            "Total Equipment",
            "Avg Flowrate",
            "Avg Pressure",
            "Avg Temperature",
            "Uploaded At"
        ]

        for text in headers:
            lbl = QLabel(text)
            lbl.setStyleSheet("""
                color: #065f46;
                font-weight: 700;
                font-size: 14px;
            """)
            lbl.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            header_layout.addWidget(lbl, 1)

        history_layout.addWidget(header_row)

        history_layout.setSpacing(12)

        title = QLabel("📜 Upload History (Last 5)")
        title.setStyleSheet("font-size:18px; font-weight:700;")

        self.history_table = QTableWidget()
        self.history_table.setHorizontalHeaderLabels
        # -------- TABLE SETUP --------
        headers = [
            "File Name",
            "Total Equipment",
            "Avg Flowrate",
            "Avg Pressure",
            "Avg Temperature",
            "Uploaded At"
        ]

        self.history_table.setColumnCount(len(headers))
        self.history_table.setHorizontalHeaderLabels(headers)

        # -------- FORCE HEADER TO SHOW (CRITICAL FIX) --------
        header = self.history_table.horizontalHeader()
        header.setVisible(True)
        header.setMinimumHeight(52)
        header.setFixedHeight(52)     
        header.setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        from PyQt5.QtWidgets import QHeaderView
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setHighlightSections(False)



        # ---------- TABLE BEHAVIOR ----------
        self.history_table.verticalHeader().setVisible(False)
        self.history_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.history_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.history_table.setSelectionMode(QTableWidget.SingleSelection)
        self.history_table.setShowGrid(False)

        # ---------- STYLES ----------
        self.history_table.setStyleSheet("""
        QTableWidget {
            background-color: rgba(255,255,255,0.55);
            border-radius: 18px;
            font-size: 14px;
        }

        QHeaderView {
            background: transparent;
        }

        QHeaderView::section {
            background-color: rgba(220, 252, 231, 1);
            color: #065f46;
            padding: 14px;
            font-size: 14px;
            font-weight: 700;
            border: none;
        }

        QTableWidget::item {
            padding: 12px;
            color: #111827;
        }

        QTableWidget::item:selected {
            background-color: rgba(34,197,94,0.25);
        }
        """)


        history_layout.addWidget(title)
        history_layout.addWidget(self.history_table)
        root_layout.addWidget(history_frame)
        history_frame.setMinimumHeight(340)

        scroll.setWidget(root)
        main = QVBoxLayout(self)
        main.addWidget(scroll)

    # ---------- UI HELPERS ----------
    def stat_card(self, title, value):
        frame = QFrame()
        layout = QVBoxLayout(frame)

        t = QLabel(title)
        t.setStyleSheet("color:#93c5fd; font-size:14px;")

        v = QLabel(value)
        v.setStyleSheet("""
            font-size: 26px;
            font-weight: 700;
            font-weight:bold;
        """)

        layout.addWidget(t)
        layout.addWidget(v)
        return frame

    def wrap_chart(self, canvas):
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.addWidget(canvas)
        return frame

    def create_canvas(self, title):
        fig = Figure(figsize=(10, 4))  
        fig.subplots_adjust(
            top=0.88,
            bottom=0.18,
            left=0.07,
            right=0.97
        )

        ax = fig.add_subplot(111)
        ax.set_title(title, fontsize=16, pad=18, weight="bold")

        ax.text(
            0.5, 0.5,
            "Upload CSV to view data",
            ha="center", va="center",
            fontsize=13,
            alpha=0.6
        )

        canvas = FigureCanvas(fig)
        canvas.setMinimumHeight(340) 
        return canvas

    # ---------- CSV UPLOAD ----------
    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )
        if not file_path:
            self.status_label.setText("⚠️ Upload cancelled")
            return

        self.status_label.setText("⏳ Processing CSV...")
        response = api_upload_csv(file_path)

        if response.status_code not in (200, 201):
            self.status_label.setText("❌ Upload failed")
            return

        self.data = response.json()
        self.status_label.setText("✅ CSV uploaded successfully")

        # ---------- SAVE HISTORY ----------
        summary = self.data.get("summary", {})
        history_entry = {
            "file": file_path.split("/")[-1],
            "total": summary.get("total_equipment", 0),
            "flow": summary.get("avg_flowrate", 0),
            "pressure": summary.get("avg_pressure", 0),
            "temp": summary.get("avg_temperature", 0),
            "time": datetime.now().strftime("%d/%m/%Y, %I:%M:%S %p")
        }

        self.upload_history.insert(0, history_entry)
        self.upload_history = self.upload_history[:5]

        self.update_history_table()


        self.update_dashboard()

    # ---------- DASHBOARD UPDATE ----------
    def update_dashboard(self):
        summary = self.data.get("summary", {})
        records = summary.get("records", [])
        print("RECORD COUNT:", len(records))

        self.total_eq.findChildren(QLabel)[1].setText(
            str(summary.get("total_equipment", 0))
        )
        self.avg_flow.findChildren(QLabel)[1].setText(
            str(summary.get("avg_flowrate", 0))
        )
        self.avg_pressure.findChildren(QLabel)[1].setText(
            str(summary.get("avg_pressure", 0))
        )
        self.avg_temp.findChildren(QLabel)[1].setText(
            str(summary.get("avg_temperature", 0))
        )

        # Flowrate
        ax1 = self.flow_canvas.figure.axes[0]
        ax1.clear()
        flow = [r["Flowrate"] for r in records]
        ax1.plot(flow, marker="o")
        ax1.set_title("Flowrate Trend")
        self.flow_canvas.draw()

        # Pressure
        ax2 = self.pressure_canvas.figure.axes[0]
        ax2.clear()
        pressure = [r["Pressure"] for r in records]
        ax2.bar(range(len(pressure)), pressure)
        ax2.set_title("Pressure Distribution")
        self.pressure_canvas.draw()

        # Pie
        ax3 = self.type_canvas.figure.axes[0]
        ax3.clear()
        dist = summary.get("type_distribution", {})
        ax3.pie(
            dist.values(),
            labels=dist.keys(),
            autopct="%1.1f%%",
            radius=1.2,
            textprops={"fontsize": 13}
        )
        ax3.set_aspect("equal")
        ax3.set_title("Equipment Type Distribution")
        self.type_canvas.draw()

    # ---------- PDF ----------
    def export_pdf(self):
        if not self.data:
            self.status_label.setText("⚠️ Upload CSV first")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Report", "equipment_report.pdf", "PDF Files (*.pdf)"
        )
        if not file_path:
            return

        with PdfPages(file_path) as pdf:
            pdf.savefig(self.flow_canvas.figure)
            pdf.savefig(self.pressure_canvas.figure)
            pdf.savefig(self.type_canvas.figure)

        self.status_label.setText("📄 PDF saved successfully")

    def logout(self):
        self.close()
        self.login_window = LoginWindow(self.show_again)
        self.login_window.show()

    def show_again(self, user):
        self.__init__(user)
        self.show()

    def update_history_table(self):
        self.history_table.setRowCount(len(self.upload_history))

        for row, item in enumerate(self.upload_history):
            file_item = QTableWidgetItem(item["file"])
            file_item.setToolTip(item["file"])  # full name on hover
            self.history_table.setItem(row, 0, file_item)
            self.history_table.setItem(row, 1, QTableWidgetItem(str(item["total"])))
            self.history_table.setItem(row, 2, QTableWidgetItem(str(item["flow"])))
            self.history_table.setItem(row, 3, QTableWidgetItem(str(item["pressure"])))
            self.history_table.setItem(row, 4, QTableWidgetItem(str(item["temp"])))
            self.history_table.setItem(row, 5, QTableWidgetItem(item["time"]))