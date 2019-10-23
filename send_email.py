import smtplib
import time


def send_email(sender,sender_password, receivers, message, domain):
   smtpObj = smtplib.SMTP(domain, 587)
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.login(sender, sender_password)
   smtpObj.sendmail(sender, receivers, message)
   smtpObj.quit()
   print ("Successfully sent email")

print("Welcome you can send Email throw this Program")
r = True
while r:
    sender = input('Email:\n')
    if "@" not in sender:
        print("invalid E- mail")
        time.sleep(3)
        continue
    else:
        r = False

sender_password = input("password\n")
receivers = input("Reciver Email:\n")
subject = input("Subject\n")
message0 = input("Type massage here\n")
message1 = f"""Subject: {subject}

{message0}"""

service_provider = sender.split("@")
service_provider = service_provider[1]

if service_provider == 'gmail.com':
    domain = 'smtp.gmail.com'
elif service_provider == 'yahoo.com':
    domain = 'smtp.mail.yahoo.com'
elif service_provider == 'hotmail.com' or 'live.com':
    domain = 'smtp.live.com'
else:
    print("Please enter email of gmail, yahoo or hotmail")

try:
    send_email(sender, sender_password, receivers, message1, domain)

except aa:
    print( 'Error Occupy while send email its may due to\n'
           '    1) Wrong Email or Password\n'
           '    2) permission denied by Gmail \n'
           '    you can allow by gmail throw this link\n'
           '    https://myaccount.google.com/lesssecureapps?pli=1 ', aa)
