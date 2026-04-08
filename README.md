📧 Bulk Email Automation System

A Python-based automation tool to send personalized emails with unique attachments (such as offer letters) to multiple recipients using Gmail.

🚀 Features
📩 Send bulk emails automatically
👤 Personalized emails for each recipient
📎 Attach different files for each user
📊 Reads data from Excel sheet
⚡ Fast and efficient email delivery
🔁 Reduces manual work completely

🛠️ Tech Stack
Python
Pandas
smtplib (Email sending)
openpyxl (Excel handling)
OS & File handling

📂 Project Structure
Bulk_Email_System/
│── rename_files.py
│── send_emails.py
│── students.xlsx
│── offers/
│── renamed/
│── README.md

⚙️ How It Works
Read student data from Excel file
Match each student with their offer letter PDF
Rename files in a structured format
Send personalized emails with correct attachment
Repeat for all students automatically

▶️ Usage
Step 1: Rename files
Run:
python rename_files.py

Step 2: Send emails
Run:
python send_emails.py

📌 Requirements
Install dependencies:
pip install pandas openpyxl

🔐 Security Note
⚠️ Email credentials are not stored in the code.
Use environment variables to store your email and password securely.

⚡ Use Cases
🎓 Sending offer letters to students
📢 Bulk notifications with attachments
🏢 HR onboarding emails
📄 Automated document distribution

⚠️ Disclaimer
This project is for educational and automation purposes only.
Ensure compliance with email policies and avoid spam usage.

👨‍💻 Author
Built by GurukulAI Lab 🚀
