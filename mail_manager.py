import csv
import os
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 465

class MailManager():
    def __init__(self,finalData):
        self.finalData = finalData

    def sendMails(self):
        fileName = self.getSheet(self.finalData["recipients"])
        
        with open(fileName,"r") as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                toEmail = row["email"]
                toName = row["name"]
                try:
                    #setting up the connection
                    context = ssl.create_default_context()
                    email_conn = smtplib.SMTP_SSL(host,port)
                    email_conn.ehlo()
                    email_conn.login(self.finalData["email"],self.finalData["pass"]) 
                    message=MIMEMultipart()
                    message["Subject"]=self.finalData["subject"]
                    message["From"]=self.finalData["email"]
                    message["To"]=toEmail

                    #creating the mail draft
                    message.attach(MIMEText(self.finalData["body"],"plain"))
                    email_conn.sendmail(self.finalData["email"],toEmail, message.as_string())
                    email_conn.quit()
                    print("sent!")
                except smtplib.SMTPException:
                    print(str(smtplib.SMTPException))

    
    def getSheet(self,filePath):
        filename = os.path.join(os.path.dirname(__file__),filePath)
        return filename   
    
    def userMail(self):
        pass