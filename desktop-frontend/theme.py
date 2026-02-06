GLASS_STYLE = """
QWidget {
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:1,
        stop:0 #c9f29b,
        stop:1 #e3f7c2
    );
    color: #14532d;
    font-family: 'Segoe UI';
    font-size: 15px;
}

/* ===== CARDS / PANELS ===== */
QFrame {
    background-color: rgba(255, 255, 255, 0.65);
    border-radius: 18px;
    border: 1px solid rgba(0, 0, 0, 0.08);
    padding: 14px;
}

/* ===== TEXT ===== */
QLabel {
    color: #14532d;
    font-weight: 600;
}

/* ===== INPUTS ===== */
QLineEdit {
    background-color: rgba(255,255,255,0.9);
    border-radius: 12px;
    padding: 14px;
    border: 1px solid rgba(0,0,0,0.15);
    color: #111827;
    font-size: 15px;
}

QLineEdit:focus {
    border: 1px solid #22c55e;
}

/* ===== BUTTONS ===== */
QPushButton {
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #22c55e,
        stop:1 #16a34a
    );
    border-radius: 14px;
    padding: 14px;
    font-size: 15px;
    font-weight: bold;
    color: white;
}

QPushButton:hover {
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #16a34a,
        stop:1 #15803d
    );
}

/* ===== SECONDARY / LOGOUT BUTTON ===== */
QPushButton#logoutButton {
    background: transparent;
    color: #14532d;
    border: 1px solid #22c55e;
}

QPushButton#logoutButton:hover {
    background-color: rgba(34,197,94,0.18);
}
"""
