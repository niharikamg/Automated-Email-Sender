import smtplib
import argparse
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

SMTP_SERVER = "smtp.gmail.com"  # Change for Outlook/Yahoo
SMTP_PORT = 587

def send_email(sender_email, sender_password, recipient, subject, body, attachment=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        if attachment:
            filename = os.path.basename(attachment)
            attachment_file = open(attachment, "rb")
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment_file.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={filename}")
            msg.attach(part)
            attachment_file.close()

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient, text)
        server.quit()

        print(f"✅ Email sent successfully to {recipient}")

    except Exception as e:
        print(f"❌ Error sending email: {e}")

def send_bulk_email(sender_email, sender_password, csv_file, subject, body, attachment=None):
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        recipient = row["Email"]
        send_email(sender_email, sender_password, recipient, subject, body, attachment)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Email Sender CLI")
    parser.add_argument("--to", type=str, help="Recipient email address")
    parser.add_argument("--csv", type=str, help="CSV file with recipient email addresses")
    parser.add_argument("--subject", type=str, required=True, help="Email subject")
    parser.add_argument("--body", type=str, required=True, help="Email body")
    parser.add_argument("--attachment", type=str, help="File to attach")
    parser.add_argument("--email", type=str, required=True, help="Sender email address")
    parser.add_argument("--password", type=str, required=True, help="Sender email password")

    args = parser.parse_args()

    if args.csv:
        send_bulk_email(args.email, args.password, args.csv, args.subject, args.body, args.attachment)
    elif args.to:
        send_email(args.email, args.password, args.to, args.subject, args.body, args.attachment)
    else:
        print("❌ Please provide a recipient email or a CSV file.")
