🌱 **Investment Plan Calculator**

A web-based calculation tool developed in Python (Flask) to support agricultural consultants and farmers who submits applications for investment plans under the Greek CAP Strategic Plan 2023–2027.

The application helps users estimate:

•	total investment budget

•	private participation

•	30% private participation threshold

•	eligibility warnings based on official rules
________________________________________
📌 **Overview**

This application supports the pre-publication of the Call for Applications for the following interventions:

•	P3-73-2.1 – Improvement Plans for Agricultural Holdings contributing to Competitiveness

•	P3-73-2.2 – Investments in agricultural holdings contributing to water savings


•	P3-73-2.6 – Circular economy and energy investments in agricultural holdings

The app works as an interactive form.
Once the user fills in all required fields, the system automatically performs the calculations and displays eligibility messages.
________________________________________
⭐ **Features**

•	✔ Automatic calculation of:

o	Total investment budget

o	Private participation


o	30% private participation threshold

•	✔ Eligibility checks based on:

o	Investment type

o	Budget limits


o	Turnover requirements

•	✔ Dynamic expense categories

•	✔ Error and warning messages displayed directly on the form

•	✔ Backend validation using Python (Flask)
________________________________________
🛠** Technologies Used**

•	Python 3.11+

•	Flask

•	HTML

•	CSS

•	JavaScript (Fetch API)
________________________________________
**📂 Repository Structure**

Investment_plan

├── .gitignore              # Git ignored files

├── .vscode/                # VS Code settings

├── Regulatory framework/   # Regulatory documentation

├── __pycache__/            # Python cache files

├── static/                 # Static assets (CSS, JS)

├── templates/              # HTML templates

├── calcs.py                # Main Flask application

├── file_handler.py         # File handling utilities

└── requirements.txt        # Python dependencies

└──README.md        # Project documentation

└──LICENSE        # Project license

________________________________________
🚀 **How to Run the Project Locally**

1️⃣ Clone the repository

Open Visual Studio Code

Then open the Terminal (View → Terminal) and run:

git clone https://github.com/marakik05/Investment_plan

2️⃣ Create and activate a virtual environment

3️⃣ Install required packages

pip install -r requirements.txt

✔ This installs Flask and all required dependencies.

4️⃣ Run the application

Start the Flask server by running:

python calcs.py

You should see a message like:

Running on http://127.0.0.1:5000

5️⃣ Open the application in your browser

Open a browser and go to:

http://127.0.0.1:5000

🎉 The application is now running locally.
________________________________________
⚠️ **Important Notes**

•	The application runs using Flask’s development server

•	All calculations are performed on the backend


•	Input validation is applied on both frontend and backend

•	Internet connection is not required after installation
________________________________________
📬 **Contact**

For questions or feedback, feel free to open an issue in the repository.
________________________________________
📄**License**

This project is licensed under the **MIT License**
________________________________________
⚠️ **Disclaimer**

This tool is intended to assist users during the pre-evaluation stage.
Final eligibility and approval depend exclusively on official public authorities and the final Call for Applications.
________________________________________
📝 **Note**

Although this README is written in English, the web application itself — including regulatory documents — is in Greek.

This is because the tool is intended for Greek agricultural consultants and farmers and follows the official Greek pre-publication of the Call for Applications for the interventions P3-73-2.1, P3-73-2.2 and P3-73-2.6.
