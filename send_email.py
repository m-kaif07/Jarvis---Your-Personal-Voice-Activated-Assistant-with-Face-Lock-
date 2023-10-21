import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# CHANGE THE email, passwor TO YOUR EMAIL AND PASSWORD, ONLY THEN EMAIL CAN BE SENT
email = "your_email"
password = "your_password"

# Dictionary of names and email addresses of recipients
recipient_dict = {
    "kaif": "mohammadkaif5849@gmail.com",
    "abuzar": "abuzarsk399@gmail.com",
    "lambda": "lambda.z@yahoo.com"
}

# SMTP server settings (for Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Creating a connection to the SMTP server
def connect_to_smtp():
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email, password)
        return server
    except smtplib.SMTPAuthenticationError:
        print("Login failed. Check your email and password.")
        return None

# Function to send an email to a recipient
def sendEmail(recipient_name, content):
    if recipient_name in recipient_dict:
        recipient_email = recipient_dict[recipient_name]

        server = connect_to_smtp()
        if server is not None:
            message = MIMEMultipart()
            message['From'] = email
            message['To'] = recipient_email
            message['Subject'] = "Hello, " + recipient_name

            # what content to send the recipient
            message.attach(MIMEText(content, 'plain'))

            text = message.as_string()
            server.sendmail(email, recipient_email, text)
            print(f"Email sent to {recipient_name} ({recipient_email})")
            server.quit()
    else:
        print(f"Recipient with the name '{recipient_name}' not found in the dictionary.")
    
