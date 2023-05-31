import requests
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = 'nicolas.aira@hotmail.com'
receiver_email = 'naira@uic.es'
password = '4484215Nicoaira'

# SMTP server settings
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587

url = "https://icp.administracionelectronica.gob.es/icpplustieb/citar?p=8&locale=es"
text_to_check = "En este mmento no hay citas disponibles en esta sede"

response = requests.get(url,headers={
   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}, verify=False)

while True:
    if text_to_check not in response.text:
        print("El texto desaparecio!")

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'CITA TIE DISPONIBLE'

        # Add email body
        body = 'Cita TIE disponible\n\n'
        body += 'Acceder al link:\n'
        body += 'https://icp.administracionelectronica.gob.es/icpplustieb/citar?p=8&locale=es\n\n\n\n\n'
        body +=  response.text

        message.attach(MIMEText(body, 'plain'))

        # Establish a secure connection with the SMTP server
        
        print("Estableciendo conexion con el servidor	")
        smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.ehlo()
        smtp.starttls()
        
        print("Logueando al hotmail...")

        # Login to your Hotmail/Outlook account
        smtp.login(sender_email, password)
        
        print("Enviando email de alerta...")

        # Send the email
        smtp.send_message(message)

        # Close the connection
        smtp.quit()
        print("Se ha enviado el email correctamente!")

        break

    else:
        print("Sin cambios, chequeando nuevamente en 10 segundos...")
        time.sleep(10)
