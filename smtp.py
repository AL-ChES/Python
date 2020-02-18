import smtplib

class Gmail(object):
    def __init__(email, password):
        email = email
        password = password
        server = 'smtp.gmail.com'
        port = 587
        session = smtplib.SMTP(server,port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        session = session
    def send_message(self, subject, body):
        ''' This must be removed '''
        headers = [
            "From: " + email,
            "Subject: " + subject,
            "To: " + email,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        session.sendmail(
            email,
            email,
            headers + "\r\n\r\n" + body)


gm = Gmail('sumitkumarnagar1993@gmail.com', 'KUMAR@6004')

gm.send_message('Subject', 'Message')
