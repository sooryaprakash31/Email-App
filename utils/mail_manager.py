import csv
import os
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

host = "smtp.gmail.com"
port = 465

class MailManager():
    def __init__(self,finalData):   
        self.finalData = finalData

    def sendMails(self):
        fileName = self.getPath(self.finalData["recipients"])
        folderName = ""
        if self.finalData["attachment"] != "":
            folderName = self.getPath(self.finalData["attachment"])

        with open(fileName,"r") as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                toEmail = row["email"]
                toName = row["name"]
                try:
                    #setting up the connection
                    context = ssl.create_default_context()
                    email_con = smtplib.SMTP_SSL(host,port,context=context)
                    email_con.ehlo()
                    email_con.login(self.finalData["email"],self.finalData["pass"]) 
                    message=MIMEMultipart()
                    message["Subject"]=self.finalData["subject"]
                    message["From"]=self.finalData["email"]
                    message["To"]=toEmail

                    #creating the mail draft
                    message.attach(MIMEText(self.finalData["body"],"plain"))
                    if folderName!="":
                        attachmentName = toName.lower()+".jpg"                        
                        filePath = folderName+"/"+attachmentName
                        filePath = os.path.join(os.path.dirname(__file__),filePath)
                        with open(filePath,"rb") as attachment:
                            part = MIMEBase("application", "octet-stream")
                            part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        # Add header as key/value pair to attachment part
                        part.add_header(
                            "Content-Disposition",
                            f"attachment; filename= {attachmentName}",
                        )   
                        message.attach(part)
                    email_con.sendmail(self.finalData["email"],toEmail, message.as_string())
                    email_con.quit()
                except smtplib.SMTPException:
                    print(str(smtplib.SMTPException))

    
    def getPath(self,path):
        return os.path.join(os.path.dirname(__file__),path)   
    
    def userMail(self):
        pass