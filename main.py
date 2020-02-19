# from email.mime.image import MIMEImage
# The import statement above is for adding an image to the email.
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import smtplib
import Info


def send_email(to, subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(Info.Email, Info.Passowrd)

        # message = 'Subject: {}\n\n{}'.format(subject, msg)
        # message = (message.encode('ascii', 'ignore')).decode("utf-8")
        # server.sendmail(Info.Email, to, message)

        # The message, subject, from, and to.
        new_message = MIMEMultipart()
        new_message['From'] = Info.Email
        new_message['To'] = to
        new_message['Subject'] = subject
        msg = MIMEText(msg)
        new_message.attach(msg)

        # Part to put an attachment. Here it simple puts two images as an attachment.
        '''
        part1 = MIMEBase('application', "octet-stream")
        part1.set_payload(open("inapp.png", "rb").read())
        encoders.encode_base64(part1)
        part1.add_header('Content-Disposition', 'attachment; filename="inapp.png"')
        new_message.attach(part1)

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("onbike.HEIC", "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="onbike.HEIC"')
        new_message.attach(part)
        '''

        server.send_message(new_message)
        server.quit()
        print("Email sent to {}".format(to))
    except:
        print("Failed!")


i = 0
size = len(Info.emails)

while i < size:
    address = Info.emails[i]
    sub = Info.subject[i]
    send_email(address, sub, Info.msg[i])
    i += 1

# You gotta turn this on before you send (https://myaccount.google.com/u/1/lesssecureapps?pageId=none).

