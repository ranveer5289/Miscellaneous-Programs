import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import base64
import argparse
import zipfile

zip_filename = "test.zip"
zf = zipfile.ZipFile(zip_filename,  mode='w')

gmail_username = "ranveer.raghu@gmail.com"
#gmail_password = ""

parser = argparse.ArgumentParser(description='Send email', add_help=True)
parser.add_argument("-r", action ="store", dest='toaddr', help="Add recepient address")
parser.add_argument("-m", action ="store", dest='message', help="body of the mail")
parser.add_argument("-a", action ="store", dest='attachment', help="Path/name of attachment")
parser.add_argument("-z", action ="store_true", default=False,  help="zip contents")

output = parser.parse_args()



def messagebody(toaddr, subject, attach):
        msg = MIMEMultipart()
        msg['From'] = gmail_username
        msg['To'] = toaddr
        msg['Subject'] = subject

        msg.attach(MIMEText(output.message))

        part = MIMEBase('application',  'octet-stream')
        part.set_payload(open(attach,  'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 
                        'attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)
        return msg

def sendmail():

        msg = messagebody("ranveer.raghu@gmail.com", "test", output.attachment)
        mailServer = smtplib.SMTP_SSL("smtp.gmail.com",  465)
        mailServer.login(gmail_username,  gmail_password)
        mailServer.sendmail(gmail_username,  output.toaddr,  msg.as_string())
        mailServer.close()

sendmail()




