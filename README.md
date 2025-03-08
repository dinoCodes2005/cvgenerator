CV generator 

Overview :
It is a CV generator website made using Django and Tailwind CSS. It takes user input through forms and formats the text into PDF which the user can download.

✅ Features
User-Friendly interface to add and edit CV details
Resume generation using pdfkit and wkhtmltopdf
Tailwind CSS for responsive design
CRUD operations for managing multiple profiles

🛠️ Tech Stack
Backend: Django, Python
Frontend: HTML, Tailwind CSS, JavaScript
Database: SQLite (or any Django-supported database)
PDF Generation: pdfkit, wkhtmltopdf

📂 Installation & Setup

git clone [https://github.com/dinoCodes2005/cvgenerator.git](https://github.com/dinoCodes2005/cvgenerator.git)
cd cvgenerator
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Download and extract wkhtml from [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)
head to views.py and change the config = pdfkit.configuration(wkhtmltopdf = r"<link-to-wkthmltopdf.exe>")
python manage.py migrate
python manage.py tailwind start
python manage.py runserver
Open 127.0.0.1:8000 on your browser
