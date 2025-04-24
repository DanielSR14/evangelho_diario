import os
from mod_date import formatted_date_func

formatted_date = formatted_date_func()

DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
MAIN_FOLDER = os.path.join(DESKTOP, "Pascom")
DATE_FOLDER = os.path.join(MAIN_FOLDER, formatted_date)

os.makedirs(DATE_FOLDER, exist_ok=True)

def move_file(source, destination_folder, new_filename=None):
    """Move um arquivo para uma pasta específica e renomeia se necessário."""
    if not os.path.exists(source):
        print(f"Erro: Arquivo {source} não encontrado!")
        return False

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder, exist_ok=True)

    filename = new_filename if new_filename else os.path.basename(source)
    destination = os.path.join(destination_folder, filename)

    try:
        os.rename(source, destination)
        print(f"Arquivo movido para {destination}")
        return True
    except Exception as e:
        print(f"Erro ao mover arquivo: {e}")
        return False

def get_image_path(formatted_date):
    """Retorna o caminho da imagem do evangelho do dia."""
    return os.path.join(DATE_FOLDER, f"Evangelho-{formatted_date}.png")

def get_audio_path(formatted_date):
    """Retorna o caminho do áudio do evangelho do dia."""
    return os.path.join(DATE_FOLDER, f"Evangelho-{formatted_date}.mp3")

def get_video_path(formatted_date):
    """Retorna o caminho do vídeo do evangelho do dia."""
    return os.path.join(DATE_FOLDER, f"Evangelho-{formatted_date}.mp4")

def process_image(formatted_date):
    """Moves the downloaded image to the correct folder"""
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    image_filename = "Pascom, evangelho do dia .png"
    image_path = os.path.join(downloads_folder, image_filename)

    if os.path.exists(image_path):
        move_file(image_path, DATE_FOLDER, f"Evangelho-{formatted_date}.png")
    else:
        print("\nErro: Imagem não encontrada na pasta de downloads!")

def get_files_email():
    if not os.path.exists(DATE_FOLDER):
        print(f"Erro: Pasta {DATE_FOLDER} não encontrada!")
        return []

    files = []
    for file in os.listdir(DATE_FOLDER):
        if file.endswith(".mp4"):
            files.append(os.path.join(DATE_FOLDER, file))

    return files