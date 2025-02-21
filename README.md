# Automated Email Sender CLI

## 📌 Description
A command-line tool to send emails automatically via SMTP. Supports bulk sending, attachments, and email templates.

## 🚀 Features
- Send emails via **Gmail, Outlook, Yahoo, or custom SMTP servers**.
- Support **bulk email sending** from a CSV file.
- Attach **files (PDF, images, docs, etc.)** to emails.
- Use **plain text or HTML email templates**.
- Log sent emails for tracking.

## 🛠 Requirements
Ensure you have **Python 3.6+** installed. Install dependencies with:
```sh
pip install pandas
```

## 📄 Usage
Send an email to a single recipient:
```sh
python email_sender.py --to "recipient@example.com" --subject "Meeting Reminder" --body "Don't forget our meeting at 3 PM." --email "your_email@gmail.com" --password "yourpassword"
```

Send bulk emails from a CSV file:
```sh
python email_sender.py --csv contacts.csv --subject "Newsletter" --body "Check out our latest updates!" --email "your_email@gmail.com" --password "yourpassword"
```

Attach a file:
```sh
python email_sender.py --to "recipient@example.com" --subject "Invoice Attached" --body "Please find the invoice attached." --attachment "invoice.pdf" --email "your_email@gmail.com" --password "yourpassword"
```

## ⚠️ Security Notice
For security reasons, **do not hardcode passwords**. Use **App Passwords** or environment variables.

## 📜 License
This project is open-source and available under the MIT License.
