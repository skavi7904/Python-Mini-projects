import smtplib

my_email = "your_email@gmail.com"  # Replace with your email address
password = "your_app_password"  # Replace with your Google account app password

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="recipient_email@gmail.com",  # Replace with recipient's email address
        msg="Subject: Your Subject Here\n\nYour message content here"
    )
connection.close()
