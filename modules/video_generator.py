import os
from moviepy.editor import ImageClip, AudioFileClip

def generate_video(image_path, audio_path, output_path):
    """Gera um vídeo a partir da imagem e do áudio fornecidos."""
    print("Gerando vídeo...")
    if not os.path.exists(image_path):
        print(f"Erro: Imagem {image_path} não encontrada!")
        return False

    if not os.path.exists(audio_path):
        print(f"Erro: Áudio {audio_path} não encontrado!")
        return False

    try:
        audio = AudioFileClip(audio_path)
        imagem = ImageClip(image_path).set_duration(audio.duration)
        video = imagem.set_audio(audio)

        video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")

        print(f"Vídeo gerado com sucesso: {output_path}")
        return True
    except Exception as e:
        print(f"Erro ao gerar vídeo: {e}")
        return False


if __name__ == "__main__":
    base_path = r"C:\Users\Daniel\Desktop\Pascom\16-04-2025"

    generate_video(f"{base_path}\\Pascom, evangelho do dia .png", f"{base_path}\\Evangelho-16-04-2025.mp3", f"{base_path}\\Evangelho 16-04-2025.mp4")