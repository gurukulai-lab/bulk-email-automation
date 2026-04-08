import pandas as pd
import smtplib
from email.message import EmailMessage
import os

SENDER_EMAIL = "yourgmail@gmail.com"
SENDER_PASSWORD = "yourpassword"

df = pd.read_excel("students.xlsx")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)


import os

files = os.listdir("offers")
SEND_ONLY = {"140", "141", "146", "147", "148"}

for _, row in df.iterrows():
    offer_no = str(row["offer_no"]).strip()

    # 👉 sirf selected offers ko bhejna
    if offer_no not in SEND_ONLY:
        continue

    student_name = row["name"]
    email = row["email"]

    # 🔍 sirf offer number se PDF dhundo
    matching_pdfs = [f for f in files if f"Offer {offer_no}" in f]

    if not matching_pdfs:
        print(f"❌ No PDF found for Offer {offer_no}")
        continue

    pdf_filename = matching_pdfs[0]
    pdf_path = os.path.join("offers", pdf_filename)

    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = email
    msg["Subject"] = "Offer Letter – Collabera"

    msg.set_content(f"""
Dear {student_name},

Congratulations!

Please find attached your Offer Letter from Collabera.

Regards,
Training & Placement Cell
Quantum University
""")

    with open(pdf_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=pdf_filename
        )

    server.send_message(msg)
    print(f"✅ Sent to {student_name} (Offer {offer_no})")
