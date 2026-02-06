# Chemical Equipment Parameter Visualizer

- A full-stack analytics platform for visualizing, analyzing, and reporting chemical equipment data using CSV files.
The project includes a web application, a desktop application, and a Django REST backend, all sharing the same analytical logic and visual theme.
- The system allows users to upload CSV files containing equipment data, automatically compute statistical summaries, generate charts, maintain upload history, and export professional PDF reports.

# Project Overview

1. The Chemical Equipment Parameter Visualizer is designed to solve the problem of manual analysis of chemical equipment datasets by providing:
    - Automated data parsing and validation
    - Real-time analytics and statistics
    - Interactive charts and dashboards
    - Upload history tracking
    - PDF report generation
    - Secure login and user management
    - Consistent UI/UX across web and desktop platforms
2. The project is suitable for academic use, internal lab analytics, and educational demonstrations.

# Supported Platforms

- Web Application (React)
- Desktop Application (PyQt5)
- Backend API (Django REST Framework)

# Key Features

1. Authentication
    - User registration and login
    - Secure password handling via Django authentication
    - Login support for both web and desktop clients
2. CSV Upload & Processing
    - Upload CSV files containing chemical equipment data
    - Automatic parsing using pandas
    - Validation of required columns
    - Backend-driven processing for consistency
3. Analytics & Statistics
    - Total equipment count
    - Average flowrate
    - Average pressure
    - Average temperature
    - Equipment type distribution
4. Visualizations
    - Line chart for flowrate trends
    - Bar chart for pressure distribution
    - Pie chart for equipment type distribution
    - Charts rendered using Matplotlib (desktop) and Chart.js (web)
5. Upload History
    - Stores last 5 uploads
    - Displays:
        - File name
        - Total equipment
        - Average flowrate
        - Average pressure
        - Average temperature
        - Upload timestamp
6. PDF Report Export
    - Generates professional PDF reports
    - Includes all charts and analytics
    - Implemented using ReportLab
7. Cross-Platform UI Consistency
    - Glassmorphism-inspired green theme
    - Identical color palette across web and desktop
    - Clean, readable typography

# Project Structure
```
CHEMICAL-EQUIPMENT-PARAMETER-VISUALIZER/
│
├── .git/
│
├── backend/
│   │
│   ├── accounts/
│   │   ├── __pycache__/
│   │   ├── migrations/
│   │   │   ├── __pycache__/
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── backend/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── equipment/
│   │   ├── __pycache__/
│   │   ├── migrations/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── views.py
│   │
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt
│
├── desktop-frontend/
│   │
│   ├── __pycache__/
│   ├── analytics_dashboard.py
│   ├── api.py
│   ├── charts.py
│   ├── dashboard.py
│   ├── login.py
│   ├── main.py
│   ├── theme.py
│   ├── upload.py
│   └── requirements.txt
│
├── web-frontend/
│   │
│   ├── node_modules/
│   │
│   ├── public/
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── logo.png
│   │   ├── logo192.png
│   │   ├── logo512.png
│   │   ├── manifest.json
│   │   ├── robots.txt
│   │   └── Screenshot 2026-01-28 223551.png
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── Charts.js
│   │   │   ├── Header.js
│   │   │   ├── HistoryTable.js
│   │   │   └── UploadCSV.js
│   │   │
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Profile.jsx
│   │   │   └── Signup.jsx
│   │   │
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── App.test.js
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── logo.svg
│   │   ├── reportWebVitals.js
│   │   └── setupTests.js
│   │
│   ├── .gitignore
│   ├── package.json
│   ├── package-lock.json
│   ├── README.md
│   └── LICENSE
│
├── README.md
└── LICENSE

```
# Technologies Used

1. Backend
    - Python
    - Django 4.2.7
    - Django REST Framework
    - pandas
    - ReportLab
    - SQLite
2. Web Frontend
    - React
    - JavaScript
    - HTML5 / CSS3
    - Chart.js
3. Desktop Frontend
    - Python
    - PyQt5
    - Matplotlib
    - Requests

# System Requirements

1. Minimum Requirements:
    - Python: 3.10 – 3.12
    - Node.js: 18+
    - RAM: 8 GB
    - OS: Windows / Linux / macOS
    - Internet connection
2. Python 3.13 is not recommended due to compatibility issues with some libraries.

# Backend Installation (Django)

1. Navigate to Backend Folder
```
cd backend
```
2. Create Virtual Environment (Recommended)
```
python -m venv venv
```
- Activate it:
- Windows:
```
venv\Scripts\activate
```
- macOS / Linux:
```
source venv/bin/activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
- Backend requirements.txt:
```
Django==4.2.7
djangorestframework
pandas
reportlab
djangorestframework-simplejwt
```
4. Run Migrations
```
python manage.py migrate
```
5. Start Backend Server
```
python manage.py runserver
```
- Backend will run at:
```
http://127.0.0.1:8000/
```

# Web Frontend Installation (React)

1. Navigate to Web Frontend
```
cd web-frontend
```
2. Install Dependencies
```
npm install
```
3. Start Development Server
```
npm start
```
- Web app will run at:
```
http://localhost:3000/
```

# Desktop Application Installation (PyQt5)

1. Navigate to Desktop Frontend
```
cd desktop-frontend
```
2. Create Virtual Environment (Recommended)
```
python -m venv desktop_env
```
- Activate it and install dependencies:
```
pip install -r requirements.txt
```
- Desktop requirements.txt:
```
PyQt5
requests
matplotlib
```
3. Run Desktop Application
```
python main.py
```

# CSV File Format

The uploaded CSV file should contain columns such as:
    - Equipment Name
    - Equipment Type
    - Flowrate
    - Pressure
    - Temperature
The backend automatically calculates statistics based on these fields.

# PDF Report Content

Generated PDF reports include:
    - Flowrate trend chart
    - Pressure distribution chart
    - Equipment type distribution pie chart
    - Clean, printable layout

# Known Limitations

- CSV column names must match expected format
- Large datasets may take longer to render charts
- Desktop and web sessions are independent
- Authentication tokens are session-based

# Troubleshooting

1. Backend Not Responding
    - Ensure Django server is running
    - Check API URLs in web and desktop clients
2. CSV Upload Fails
    - Verify CSV format
    - Ensure required columns exist
    - Check backend logs
3. Charts Not Updating
    - Confirm data returned from API
    - Check browser console or terminal output

# License

This project is intended for educational and academic use.

# Author

Developed as a full-stack academic project combining:
- Django REST APIs
- React web application
- PyQt5 desktop application
