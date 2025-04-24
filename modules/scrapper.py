import requests
from bs4 import BeautifulSoup

def get_gospel(url):
    print(f'\nBuscando o Evangelho do dia em {url}...')
    response = requests.get(url)
    
    if response.status_code != 200:
        print('\nErro ao acessar o site.')
        return None, None, None
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todas as seções
    sections = soup.find_all('section', class_='section--evidence')

    # Identificar a seção correta (que contém "Evangelho do Dia")
    gospel_section = None
    for section in sections:
        title = section.find('h2')
        if title and "Evangelho do Dia" in title.get_text():
            gospel_section = section
            break

    if not gospel_section:
        print('\nErro: Não foi possível encontrar a seção do Evangelho.')
        return None, None, None
    
    # Capturar os parágrafos dentro da seção
    paragraphs = gospel_section.find_all('p')

    if len(paragraphs) < 2:
        print("\nErro: Estrutura inesperada da página.")
        return None, None, None

    # Pegando os elementos corretamente
    intro_text = paragraphs[0].get_text(strip=True)  # Primeiro <p> é a introdução
    passage_text = paragraphs[1].get_text(strip=True)  # Segundo <p> é a passagem
    
    passage_text = ' '.join(passage_text.split())
    
    gospel_text = '\n\n'.join(p.get_text() for p in paragraphs[2:])  

    return passage_text, intro_text, gospel_text

