from modules.configs import URL
from modules.send_email import send_email
from modules.mod_date import formatted_date_func
from modules.full_funcs import check_conditions, process_audio, process_image_canva
from modules.file_handler import get_video_path
from modules.video_generator import generate_video
from modules.scrapper import get_gospel


def main():
    print('Inicializando o script...')
    if URL.endswith("None/None/None.html"):
        print('Amanhã é domingo, o evangelho é na missa!.')
        exit()

    passage_text, intro_text, gospel_text = get_gospel(URL)

    print(f'Intro: {intro_text}')
    print(f'Passagem: {passage_text}')
    print(f'Texto: {gospel_text}')
    
    check_conditions()
    
    audio_path = process_audio(intro_text, passage_text, gospel_text)
    image_path = process_image_canva(intro_text, passage_text, gospel_text)

    formatted_date = formatted_date_func()
    video_path = get_video_path(formatted_date)
    generate_video(image_path, audio_path, video_path)

    send_email()



if __name__ == "__main__":
    main()