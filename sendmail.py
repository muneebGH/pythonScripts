import os
import smtplib
from email.message import EmailMessage

# add name and email of recievers in this dict
recievers={"muneebmain":"muneebch798@gmail.com"}

reciever=input("Enter reciever : ")

for i,j in recievers.items():
    if i==reciever:
        reciever=j
        break;



msg=EmailMessage()
msg['subject']=input("Enter subject : ")
msg['from']="bcsf17m-17@pucit.edu.pk"
msg['to']=reciever
msg.set_content(input("Enter body: "))
filename=input("Enter filename or path : ")
file=open(filename,"rb");
fileData=file.read()
msg.add_attachment(fileData, maintype="application", subtype="octet-stream", filename=file.name)

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login("bcsf17m017@pucit.edu.pk",'yddclyxepnfyovsx')
    smtp.send_message(msg)
    print("Send kardi hy g apky gulam ny ")



