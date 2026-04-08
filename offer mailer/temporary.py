import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("yourgmail@gmail.com", "yourpassword")
print("✅ Login Successful")
server.quit()
