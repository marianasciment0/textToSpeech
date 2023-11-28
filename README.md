
<div align="center">

  ## Text to Speech (Conversor de Texto para Fala) 🔊

</div>

## 💬 Sobre
Este é um script em Python que converte texto em fala usando a biblioteca gTTS (Google Text-to-Speech) e reproduz o áudio usando a biblioteca playsound.

## ⚙️ Instruções de Uso
Para executar este projeto, você precisará ter o [Python](https://www.python.org/downloads/) instalado. Com isso, você pode clonar este repositório e instalar as dependências.
```sh
  # Clone este repositório
  git clone https://github.com/marianasciment0/textToSpeech
```
A biblioteca gTTS é utilizada para a conversão de texto em fala usando a API da Google. Para instalá-la, execute o seguinte comando no terminal:
```sh
  # Instalando a biblioteca gTTs
  pip install gtts
```
A biblioteca playsound é utilizada para a reprodução de áudio. Para instalá-la, execute o seguinte comando no terminal:

```sh
  # Instalando a biblioteca playsound
 pip install playsound
```
Abra um terminal e navegue até o diretório do projeto e execute o script usando o seguinte comando:
```sh
python textoparafala.py
```
O script solicitará que você insira o texto que deseja converter em fala. Digite o texto e pressione Enter. O áudio será reproduzido automaticamente. 
O arquivo de áudio gerado será salvo como audio.mp3 no mesmo diretório. Opcionalmente, você pode remover o arquivo após o uso.
```sh
# Remova o arquivo de áudio (opcional)
os.remove("audio.mp3")
```

