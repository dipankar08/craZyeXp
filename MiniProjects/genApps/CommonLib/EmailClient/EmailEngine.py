#########################################
#  Email Client To Send Email to some address.
#  Adding prototype which is used to send HTML mail.
#  Schedule Mail on Time.
#########################################
import smtplib
import pdb
class MailEngine:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, SMTP_SERVER='smtp.gmail.com', SMTP_PORT = 587,UNAME="pequenas.mail@gmail.com",PASSWD="dipankar08"):
      self.SMTP_SERVER= SMTP_SERVER ;
      self.SMTP_PORT = SMTP_PORT
      self.UNAME=UNAME
      self.PASSWD =PASSWD
   
   def SendMail(self,sender = 'dipankar@gmail.com',recipient="dutta.dipankar08@gmail.com",subject="test mail",body="Sample Body"):
      headers = ["From: " + sender,
                 "Subject: " + subject,
                 "To: " + recipient,
                 "MIME-Version: 1.0",
                 "Content-Type: text/html"]
      headers = "\r\n".join(headers)    
      pdb.set_trace()      
      session = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
      session.ehlo()
      session.starttls()
      session.ehlo()
      session.login(self.UNAME, self.PASSWD)       
      session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
      session.quit()
      print '>>> Email Send Successfully '
   def SetSchedule(self):
      pass
   def BuildMailTemplate(file,data):
      " Build HTML Email template and fillup with data - Return HTML mail"
      pass
      
#Sampel Test is Here.
m = MailEngine()
m.SendMail()
