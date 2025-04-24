import os
import time
import dotenv
from elevenlabs import ElevenLabs, VoiceSettings

# Carrega variáveis do .env
dotenv.load_dotenv()
API_KEYS = os.getenv("ELEVENLABS_KEYS").split(",")

# Configurações da voz
VOICE_ID = "nPczCjzI2devNBz1zQrb"  # Brian
VOICE_SETTINGS = VoiceSettings(
    stability=0.7,
    similarity_boost=0.9,
    style=0.5,
    use_speaker_boost=True,
)

def generate_audio(audio_text, filename, retries=1, timeout=120):
    for api_key in API_KEYS:
        attempt = 0
        while attempt < retries:
            try:
                client = ElevenLabs(api_key=api_key.strip())

                # Timeout explícito para evitar operações demoradas
                audio_stream = client.text_to_speech.convert(
                    voice_id=VOICE_ID,
                    optimize_streaming_latency="1", 
                    output_format="mp3_22050_32",
                    text=audio_text,
                    model_id="eleven_multilingual_v2",
                    voice_settings=VOICE_SETTINGS,
                )

                with open(filename, "wb") as f:
                    for chunk in audio_stream:
                        f.write(chunk)

                print(f"Áudio gerado com sucesso: {filename}")
                return True

            except Exception as e:
                print(f"Tentativa {attempt + 1} falhou com chave {api_key.strip()}: {e}")
                attempt += 1
                time.sleep(5)  # Espera 5 segundos antes de tentar novamente

        print(f"Falha ao gerar áudio com chave {api_key.strip()} após {retries} tentativas.")

    print("Falha ao gerar áudio com todas as chaves disponíveis.")
    return False


if __name__ == '__main__':
    audio_text = '''Proclamação do Evangelho de Jesus Cristo segundo João.

Capítulo 7, Versículos de 1 á 2, 10 á 25 á 30
Naquele tempo,
Jesus andava percorrendo a Galileia.
Evitava andar pela Judeia,
porque os judeus procuravam matá-lo.

Entretanto, aproximava-se a festa judaica das Tendas.

Quando seus irmãos já tinham subido,
então também ele subiu para a festa,
não publicamente mas sim, como que às escondidas.

Alguns habitantes de Jerusalém disseram então:
"Não é este a quem procuram matar?

Eis que fala em público e nada lhe dizem.
Será que, na verdade, as autoridades reconheceram
que ele é o Messias?

Mas este, nós sabemos donde é.
O Cristo, quando vier, ninguém saberá donde ele é".

Em alta voz, Jesus ensinava no Templo, dizendo:
"Vós me conheceis e sabeis de onde sou;
eu não vim por mim mesmo,
mas o que me enviou é fidedigno.
A esse, não o conheceis,

mas eu o conheço,
porque venho da parte dele,
e ele foi quem me enviou".

Então, queriam prendê-lo,
mas ninguém pôs a mão nele,
porque ainda não tinha chegado a sua hora.

Palavra da Salvação.
Gloria a vós, Senhor.
    
    '''
    generate_audio(audio_text=audio_text, filename='audio.mp3')