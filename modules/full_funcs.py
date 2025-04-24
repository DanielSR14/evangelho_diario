from modules.verifications import check_capslock, check_internet, verify_gospel_text_length
from modules.text_processor import process_gospel_to_audio, process_gospel_to_canva
from modules.mod_date import formatted_date_func
from modules.file_handler import get_audio_path, get_image_path, process_image
from modules.audio_generator import generate_audio
from modules.automation import open_browser, insert_text, download_image, change_font_size
from modules.configs import CANVA_URL
import time

def check_conditions():
    check_internet()
    check_capslock()

def process_audio(intro_text, passage_text, gospel_text):
    audio_text = process_gospel_to_audio(intro_text, passage_text, gospel_text)
    formatted_date = formatted_date_func()
    audio_path = get_audio_path(formatted_date)
    print("Gerando áudio...")
    success = generate_audio(audio_text, audio_path)
    return audio_path if success else None

def process_image_canva(intro_text, passage_text, gospel_text):
    img_passage, img_text = process_gospel_to_canva(intro_text, passage_text, gospel_text)
    open_browser(CANVA_URL)
    insert_text(img_text, x=1010, y=519)
    time.sleep(1)
    change_font_size(verify_gospel_text_length(img_text))
    time.sleep(1)
    insert_text(img_passage, x=1149, y=366)
    insert_text(img_passage, x=1022, y=935)
    download_image()
    formatted_date = formatted_date_func()
    process_image(formatted_date)
    return get_image_path(formatted_date)