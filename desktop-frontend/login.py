from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QFrame
)
from PyQt5.QtCore import Qt
from api import login
from PyQt5.QtCore import QPropertyAnimation
from theme import GLASS_STYLE


class LoginWindow(QWidget):
    def __init__(self, on_success):
        super().__init__()
        self.on_success = on_success

        self.setWindowTitle("Sign In")
        self.setStyleSheet(GLASS_STYLE)
        
        # Desktop-like size
        self.resize(1200, 800)
        self.setMinimumSize(1000, 700)

        # Allow minimize / resize
        self.showMaximized()        

        root = QVBoxLayout(self)
        root.setAlignment(Qt.AlignCenter)
        root.setContentsMargins(0, 0, 0, 0)

        # -------- CARD --------
        card = QFrame()
        card.setObjectName("loginCard")
        card.setFixedWidth(420)
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(18)

        title = QLabel("🔐 Welcome Back")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: 800;
            letter-spacing: 1px;
        """)

        subtitle = QLabel("Sign in to access your dashboard")
        subtitle.setStyleSheet("""
            color: #94a3b8;
            font-size: 14px;
        """)

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.email.returnPressed.connect(self.handle_login)
        self.password.returnPressed.connect(self.handle_login)

        self.status_label = QLabel()
        self.status_label.hide()
        self.status_label.setStyleSheet("color: #fca5a5;")

        login_btn = QPushButton("Sign In")
        login_btn.clicked.connect(self.handle_login)

        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addWidget(self.email)
        card_layout.addWidget(self.password)
        card_layout.addWidget(self.status_label)
        card_layout.addWidget(login_btn)

        root.addWidget(card)

        self.fade_in()

    # -------- LOGIN HANDLER --------
    def handle_login(self):
        email = self.email.text().strip()
        password = self.password.text()

        if not email or not password:
            self.status_label.setText("⚠️ Email and password required")
            self.status_label.show()
            return

        try:
            res = login(email, password)
        except Exception:
            self.status_label.setText("❌ Backend not running")
            return

        if res.status_code != 200:
            self.status_label.setText("❌ Invalid credentials")
            return

        self.on_success(res.json())
        self.close()

    def fade_in(self):
        self.setWindowOpacity(0)
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(450)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.start()
