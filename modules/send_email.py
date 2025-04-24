import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
from mod_date import formatted_date_func
from file_handler import get_files_email

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

formatted_date = formatted_date_func()

def send_email_func():
    print('Enviando e-mail...')
    files = get_files_email()

    # Filtra apenas o arquivo de vídeo (.mp4)
    video_file = next((file for file in files if file.endswith(".mp4")), None)

    msg = EmailMessage()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    if video_file:
        msg["Subject"] = f"Evangelho do Dia - {formatted_date}"
        msg.set_content(f"Segue em anexo o vídeo do Evangelho do Dia {formatted_date}.")
        
        with open(video_file, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(video_file)
            msg.add_attachment(file_data, maintype="video", subtype="mp4", filename=file_name)
    else:
        msg["Subject"] = f"Evangelho do Dia - {formatted_date}"
        msg.set_content(f"Segue anexo da IMAGEM apenas do Evangelho do dia - {formatted_date}. Vídeo não foi gerado por falta de créditos na API de geração de áudio.")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    send_email_func()
