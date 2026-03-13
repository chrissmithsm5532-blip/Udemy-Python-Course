import smtplib
from email.message import EmailMessage
import imghdr

Image = "image_to_send.png"

def send_email(Image):
   print("sending email")
   email_message = EmailMessage()
   email_message["Subject"] = "A new Customer showed up"
   email_message.set_content("A new Customer showed up")

   with open(Image,'rb') as file:
      content = file.read()
   email_message.add_attachment(content,maintype="image",subtype=imghdr.what(None,content))
   gmail= smtplib.SMTP("smtp.gmail.com",587)
   gmail.ehlo()
   gmail.starttls()
   gmail.login(SENDER,PASSWORD)
   gmail.sendmail(SENDER,RECEIVER,email_message.as_string())
   gmail.quit()
   print("Email sent successfully")

if __name__ == "__main__":
   send_email(image_path="/images/1.png")