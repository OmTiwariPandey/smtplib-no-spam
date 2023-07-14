import smtplib
import csv
# Set up the SMTP server
smtp_server = "smtp.gmail.com"
port = 587
sender_email = " Your Email"
password = "Your App Password"

# Create a secure SSL/TLS connection
server = smtplib.SMTP(smtp_server, port)
server.starttls()

# Login to the server
server.login(sender_email, password)

# Read email addresses from CSV file
with open('testing.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            recipient_email = row[0]
            subject = "Subject"
            body = '''Your email body'''
            message = f"Subject: {subject}\n\n{body}"
        
        # Send the email
            server.sendmail(sender_email, recipient_email, message)
            print('Sent')
        except:
            'Not Sent!'

# Close the server connection
server.quit()