import sys
from PyQt5.QtWidgets import QApplication
from login import LoginWindow
from dashboard import DashboardWindow

app = QApplication(sys.argv)

# 🔒 GLOBAL reference (important!)
dashboard_window = None


def start_dashboard(user):
    global dashboard_window
    dashboard_window = DashboardWindow(user)
    dashboard_window.show()


login = LoginWindow(start_dashboard)
login.show()

sys.exit(app.exec_())
