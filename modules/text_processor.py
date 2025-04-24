import re

EVANGELISTAS = {
    "Mateus":"mt",
    "Marcos":"mc",
    "Lucas":"lc",
    "João":"jo"
}

def process_gospel_to_audio(intro, passage, gospel_text):
    audio_text = intro + "\n"

    # Ajuste para capturar múltiplos intervalos de versículos
    matches = re.findall(r"(\d+),(\d+)-(\d+)", passage)
    additional_matches = re.findall(r"\.(\d+)-(\d+)", passage)  # Para casos como ".45-46"

    if matches:
        formatted_text = f"Capítulo {matches[0][0]}, versículos de {matches[0][1]} a {matches[0][2]}"
        
        if additional_matches:
            formatted_text += f", e de {additional_matches[0][0]} a {additional_matches[0][1]}"
        
        formatted_text += "\n"

        # Adiciona a passagem formatada ao texto do áudio
        audio_text += formatted_text

    # Adiciona o texto do evangelho
    audio_text += gospel_text

    # Adiciona o encerramento do texto
    if gospel_text.endswith("Palavra da Salvação."):
        audio_text = audio_text.replace("Palavra da Salvação.", "")
    else:
        audio_text += "\nPalavra da Salvação. \n"
        audio_text += "Glória a vós, Senhor."

    return audio_text


def process_gospel_to_canva(intro, passage, gospel_text,max_length=956):
    # Pega apenas o nome do evangelista
    evangelist = intro.replace("Proclamação do Evangelho de Jesus Cristo segundo ", "").strip()
    
    # Pega a sigla do evangelista
    evangelist_sigla = EVANGELISTAS.get(evangelist, evangelist)  # Fallback para evitar erro
    
    # Formata a passagem completa
    passage_complete = f"{evangelist_sigla} {passage}"
    passage_complete.capitalize() # Capitaliza a primeira letra da sigla do evangelista

    # Remove múltiplas quebras de linha e espaços desnecessários
    passage_text = re.sub(r'\s+', ' ', gospel_text).strip()

    # Se o texto for muito grande, insere uma quebra de linha em um ponto próximo do meio
    if len(passage_text) > max_length:
        middle = len(passage_text) // 2
        closest_space = passage_text.rfind(" ", 0, middle)  # Encontrar espaço mais próximo do meio
        if closest_space != -1:
            passage_text = passage_text[:closest_space] + "\n" + passage_text[closest_space + 1:]

    return passage_complete, passage_text


