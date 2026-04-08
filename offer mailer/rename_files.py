import pandas as pd
import os
import shutil

PASSING_YEAR = "26"          # 🔥 sabhi ke liye same
COMPANY_NAME = "Collabera"

df = pd.read_excel("students.xlsx")

old_folder = "offers"
new_folder = "renamed"

os.makedirs(new_folder, exist_ok=True)

files = os.listdir(old_folder)

for _, row in df.iterrows():
    student_name = row["name"].strip().replace(" ", "_")
    offer_no = str(row["offer_no"]).strip()

    # PDF sirf offer number se match
    matching_pdfs = [f for f in files if f"Offer {offer_no}" in f]

    if not matching_pdfs:
        print(f"❌ PDF not found for Offer {offer_no}")
        continue

    old_filename = matching_pdfs[0]
    old_path = os.path.join(old_folder, old_filename)

    new_filename = f"{PASSING_YEAR}_{student_name}_{COMPANY_NAME}.pdf"
    new_path = os.path.join(new_folder, new_filename)

    shutil.copy(old_path, new_path)

    print(f"✅ {old_filename}  →  {new_filename}")

print("🎉 All offer letters renamed successfully!")
