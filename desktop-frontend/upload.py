from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QMessageBox
)
from api import upload_csv as api_upload_csv
from analytics_dashboard import AnalyticsDashboardWindow


class UploadCSVWindow(QWidget):
    def __init__(self, on_success):
        print("✅ CORRECT UploadCSVWindow LOADED")
        super().__init__()
        self.on_success = on_success
        self.setWindowTitle("Upload CSV")

        layout = QVBoxLayout()

        upload_btn = QPushButton("Select CSV File")
        upload_btn.clicked.connect(self.select_file)

        layout.addWidget(upload_btn)
        self.setLayout(layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select CSV file",
            "",
            "CSV Files (*.csv)"
        )

        if not file_path:
            return

        response = api_upload_csv(file_path)

        if response.status_code not in (200, 201):
            QMessageBox.critical(self, "Upload Failed", response.text)
            return

        data = response.json()

        QMessageBox.information(self, "Success", "CSV processed successfully")

        # ✅ Pass data to analytics dashboard
        self.on_success(data)
        self.close()
