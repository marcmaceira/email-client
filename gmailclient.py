import getpass
import smtplib
import socket
import sys


def main():
    try:
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        print("Connection to Gmail was successful.")
        print("Connected to Gmail.\n")
        try:
            gmail_user = str(input("Enter your email: ")).lower().strip()
            gmail_pass = getpass.getpass("Enter your password: ").strip()
            smtpObj.login(gmail_user, gmail_pass)
            print("Logged in successfully.\n")
        except smtplib.SMTPResponseException:
            print("Authentication failed.\n")
            smtpObj.close()
            sys.exit(1)

    except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
        print("Connection to Gmail failed.\n")
        print(e)
        sys.exit(1)

    send_to = input("Send mail to: ").lower().strip()
    subject = input("Subject: ")
    body = input("Body: ")

    try:
        print("To: " + send_to)
        print("From: " + gmail_user)
        smtpObj.sendmail(gmail_user, send_to, "Subject:" + str(subject) + "\n" + str(body))
        print("Sending...")
    except:
        print("Email could not be sent.\n")
        smtpObj.close()
        sys.exit(1)

    print("Sent successfully.\n")
    smtpObj.close()
    sys.exit(1)

main()
