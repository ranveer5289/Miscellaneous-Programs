#TODO: Send multiple attachments without zipping or without(-z option)
#For eg: pymail -r "send2some1" -m "test mail" -a 1.py,2.py,3.py

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import base64
import argparse
import zipfile


gmail_username = "ranveer.raghu@gmail.com"
gmail_password = "secretpassword"

current_directory = os.getcwd()
path_to_delete_file = os.path.join(current_directory,"test.zip")
print path_to_delete_file

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
        
        if output.z:
                msg = messagebody("ranveer.raghu@gmail.com", "test", "test.zip")
        else:
                msg = messagebody("ranveer.raghu@gmail.com", "test", output.attachment)

        mailServer = smtplib.SMTP_SSL("smtp.gmail.com",  465)
        mailServer.login(gmail_username,  gmail_password)
        mydict = mailServer.sendmail(gmail_username,  output.toaddr,  msg.as_string())

        if mydict:
                print "error sending mail"
        else:
                print "send successfully"
        mailServer.close()


def multiple_attachment():
        zip_filename = "test.zip"
        zf = zipfile.ZipFile(zip_filename,  mode='w')  
        if "," in output.attachment:
                attachment_list = output.attachment.split(",")
                for attach in attachment_list:
                        zf.write(attach)
                zf.close()

if output.z:
        multiple_attachment()

sendmail()

os.system("del "+  path_to_delete_file)

