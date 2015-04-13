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
    try:
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
    except Exceception ,e:
      print '>>> ERROR: ',e
  def SetSchedule(self):
      pass
  def BuildMailTemplate(self,file,data={'name':'Dipankar'}):
      " Build HTML Email template and fillup with data - Return HTML mail"
      try:
        from jinja2 import Template
        f = open(file);
        template = Template(f.read())
        res = template.render(data)
        pdb.set_trace()
        return res;
      except Exceception ,e:
        print '>>> ERROR: ',e      
      
#Sampel Test is Here.
m = MailEngine()
x = m.BuildMailTemplate('Template.html',{'q':'My Question','a':'Ans','link':'http://google.com'});
m.SendMail(body=x)
