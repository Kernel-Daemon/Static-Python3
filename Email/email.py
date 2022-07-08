import smtplib
from email.mime.text import MIMEText


def send_mail(recipient, subject, message, sender):
    message = MIMEText(message)
    message['Subject - '] = subject
    message['From - '] = sender
    message['To - '] = recipient

    # Create SMTP connection object to localhost
    smtp_conn = smtplib.SMTP('localhost')

    # Send the email
    smtp_conn.sendmail(sender, recipient, message.as_string())

    # Close SMTP connection
    smtp_conn.quit()

    return True