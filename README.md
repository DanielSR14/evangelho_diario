# Evangelho do Dia - Automação Pascom

Este projeto tem como objetivo automatizar o processo de criação e envio diário do Evangelho do Dia para a Paróquia de minha cidade, utilizando uma imagem com o versículo do dia e um áudio narrando a passagem bíblica.

O sistema é composto por um conjunto de scripts Python que buscam o Evangelho do Dia em uma página específica, geram uma imagem no Canva com a passagem e o texto, e criam um áudio narrado, além de enviar essas informações por e-mail para os responsáveis pela comunicação da paróquia. A automação é realizada em ambiente local, com interações via teclado e navegação no navegador.

## Funcionalidades

- **Criação da Imagem:** Utiliza o **Canva** para gerar uma imagem com o versículo e o texto do Evangelho do Dia. Como o Canva não oferece uma API para automação, usamos a biblioteca **PyAutoGUI** para simular a interação com o navegador, inserindo o texto diretamente no template pronto do Canva.
- **Geração de Áudio:** Converte o texto do Evangelho para áudio utilizando a API do **Eleven Labs**.
- **Envio de E-mail:** Envia automaticamente o arquivo de imagem e áudio para um endereço de e-mail configurado.
- **Verificações** O script verifica se há conexão com a internet e se o Caps Lock está ativado, garantindo que o processo ocorra sem erros.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação usada para desenvolver o script.
- **BeautifulSoup**: Usado para fazer scraping da página do Evangelho.
- **PyAutoGUI**: Para automação do Canva, uma vez que o Canva não oferece uma API. Simulamos as interações no navegador.
- **Eleven Labs**: API para gerar áudio a partir do texto.
- **SMTP**: Envio de e-mails com anexos (imagem e áudio gerados).

## Instalação

### Requisitos

- **Python 3.x**: Certifique-se de ter o Python 3.x instalado em seu ambiente.
- **Bibliotecas Python**: Instale as dependências com o comando:

# Utilize o comando no terminal/cmd na pasta raiz do projeto

- pip install -r requirements.txt

Este comando instala as bibliotecas necessárias, como requests, pyautogui, beautifulsoup4, dotenv, elevenlabs, entre outras.

# Configuração

- **Arquivo .env**:

Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis de ambiente:

ELEVENLABS_KEYS=<suas-chaves-API>
SMTP_SERVER=<servidor-smtp>
SMTP_PORT=<porta-smtp>
EMAIL_SENDER=<seu-email>
EMAIL_PASSWORD=<senha-do-seu-email>
EMAIL_RECEIVER=<email-do-destinatário>

# Configuração do Canva:

No arquivo config.py, a URL do template do Canva é configurada. Alterar para o template utilizado pela paróquia.

# Configuração do Evangelho do Dia:

A URL para buscar o Evangelho do Dia está configurada em config.py. Certifique-se de que a URL corresponda ao formato correto do site da qual o Evangelho será extraído.

## Como Usar

Executar o Script: Para rodar o script principal que faz todo o processo de automação, basta executar o seguinte comando:

- python main.py

Isso irá:

# Buscar o Evangelho do Dia na URL configurada.

# Abrir o navegador, acessar o Canva e gerar a imagem.

# Criar o áudio com a passagem.

# Enviar a imagem e o áudio por e-mail para o destinatário configurado.

**Agendar a Execução com o Task Scheduler**: Como o script deve ser executado todos os dias pela manhã, recomendamos usar o Task Scheduler do Windows para automatizar a execução do script.

1. Abra o Agendador de Tarefas no Windows.
2. Vá em Criar tarefa
3. Dê um nome a tarefa, como "Evangelho Diário"
4. Vá na aba "Gatilhos", clique em **novo** e selecione **diariamente**
5. Selecione um horario fixo para a execuçãp da tarefa
6. Na aba "Ações", selecione o arquivo "main.py", coloque para executar
   com o interpretador python
7. Clique em concluir.

# Estrutura do Projeto

**main.py**: Script principal que controla o fluxo de execução (busca do Evangelho, geração da imagem, áudio e envio de e-mail).
**verifications.py**: Funções para verificar o Caps Lock e a conexão com a internet.
**scrapper.py**: Funções para fazer o scraping do site e extrair o Evangelho do Dia.
**file_manager.py**: Gerenciamento de arquivos (movimentação e salvamento).
**dates.py**: Funções para lidar com data e formatação.
**automation.py**: Automação de navegação e inserção de texto no Canva utilizando PyAutoGUI.
**audio_generator.py**: Geração do áudio a partir do texto do Evangelho.
**send_email.py**: Função para enviar os arquivos gerados por e-mail.
**config.py**: Configurações do projeto, como URLs e caminhos.

# Logs e Monitoramento

Os logs de execução, como as tentativas de conectar à internet e o horário de envio dos e-mails, são armazenados em um arquivo JSON (evangelho_logs.json). O script pode ser consultado para ver o histórico de execuções.

# Visualizar os Logs

Você pode visualizar os logs através do script json_viewer.py para acompanhar o status diário.

- python json_viewer.py

# Contribuições

Se desejar contribuir para o projeto, sinta-se à vontade para fazer um fork e submeter pull requests. Toda contribuição é bem-vinda!

# Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

---

# Gospel of the Day - Pascom Automation

This project aims to automate the process of creating and sending the Gospel of the Day daily to the Parish of my city, using an image with the verse of the day and an audio narrating the biblical passage.

The system consists of a set of Python scripts that fetch the Gospel of the Day from a specific page, generate an image in Canva with the passage and text, create a narrated audio, and send this information by email to the people responsible for communication at the parish. The automation is performed in a local environment, with keyboard interactions and browser navigation.

## Features

- **Image Creation:** Uses **Canva** to generate an image with the verse and text of the Gospel of the Day. Since Canva does not offer an API for automation, we use the **PyAutoGUI** library to simulate interaction with the browser, inserting the text directly into Canva's pre-made template.
- **Audio Generation:** Converts the text of the Gospel to audio using the **Eleven Labs** API.
- **Email Sending:** Automatically sends the image and audio files to a configured email address.
- **Checks:** The script checks for an internet connection and if Caps Lock is enabled, ensuring the process runs without errors.

## Technologies Used

- **Python 3.x**: Programming language used to develop the script.
- **BeautifulSoup**: Used to scrape the Gospel page.
- **PyAutoGUI**: For Canva automation, since Canva doesn’t provide an API. We simulate browser interactions.
- **Eleven Labs**: API to generate audio from text.
- **SMTP**: Sending emails with attachments (image and generated audio).

## Installation

### Requirements

- **Python 3.x**: Make sure Python 3.x is installed on your environment.
- **Python Libraries**: Install the dependencies by running the following command:

# Use the command in the terminal/cmd in the project's root folder

- pip install -r requirements.txt

This command installs the required libraries like requests, pyautogui, beautifulsoup4, dotenv, elevenlabs, among others.

# Configuration

- **.env File**:

Create a `.env` file in the root of the project and add the following environment variables:

ELEVENLABS_KEYS=<your-api-keys>
SMTP_SERVER=<smtp-server>
SMTP_PORT=<smtp-port>
EMAIL_SENDER=<your-email>
EMAIL_PASSWORD=<your-email-password>
EMAIL_RECEIVER=<recipient-email>

# Canva Configuration:

In the `config.py` file, the URL of the Canva template is configured. Change it to the template used by the parish.

# Gospel of the Day Configuration:

The URL to fetch the Gospel of the Day is configured in `config.py`. Make sure the URL matches the correct format of the website from which the Gospel will be extracted.

## How to Use

Run the Script: To run the main script that automates the whole process, simply execute the following command:

- python main.py

This will:

# Fetch the Gospel of the Day from the configured URL.

# Open the browser, access Canva, and generate the image.

# Create the audio with the passage.

# Send the image and audio via email to the configured recipient.

**Schedule Execution with Task Scheduler**: Since the script needs to run every morning, we recommend using Windows Task Scheduler to automate its execution.

1. Open Task Scheduler in Windows.
2. Click on "Create Task".
3. Give the task a name, like "Daily Gospel".
4. Go to the "Triggers" tab, click on **New**, and select **Daily**.
5. Choose a fixed time for the task execution.
6. In the "Actions" tab, select the "main.py" file and configure it to run with the Python interpreter.
7. Click "Finish".

# Project Structure

**main.py**: Main script controlling the execution flow (fetching the Gospel, generating the image, audio, and sending email).
**verifications.py**: Functions to check Caps Lock and internet connection.
**scrapper.py**: Functions to scrape the website and extract the Gospel of the Day.
**file_manager.py**: File management (moving and saving).
**dates.py**: Functions to handle date and formatting.
**automation.py**: Browser automation and text insertion into Canva using PyAutoGUI.
**audio_generator.py**: Audio generation from the Gospel text.
**send_email.py**: Function to send the generated files via email.
**config.py**: Project configurations, such as URLs and paths.

# Logs and Monitoring

Execution logs, such as connection attempts and email send times, are stored in a JSON file (`evangelho_logs.json`). The script can be checked to view the execution history.

# View the Logs

You can view the logs using the `json_viewer.py` script to track the daily status.

- python json_viewer.py

# Contributions

If you would like to contribute to the project, feel free to fork and submit pull requests. All contributions are welcome!

# License

This project is licensed under the MIT License - see the LICENSE file for more details.
