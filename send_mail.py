import smtplib

# Email details
sender = 'enter email here'
receivers = ['enter reciver mail here']
subject = 'Test Email'
message = """
This is a test email sent from Python.
Trying to type with multiple line.
Done.
"""

# Email server details
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(sender, "enter password here")

# Compose and send the email
email_text = f"Subject: {subject}\n\n{message}"
server.sendmail(sender, receivers, email_text)

# Close the server connection
server.quit()
