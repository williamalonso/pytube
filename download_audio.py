from pytube import YouTube

def download_audio(video_urls, output_path='.'):
    try:
        for video_url in video_urls:
            # Cria um objeto YouTube
            yt = YouTube(video_url)

            # Obtém a melhor stream disponível apenas para áudio
            audio_stream = yt.streams.filter(only_audio=True).first()

            # Baixa o áudio para o caminho de saída especificado
            audio_stream.download(output_path)

            # Renomeia o arquivo para ter a extensão .mp3
            new_file_path = f"{output_path}/{yt.title}.mp3"
            audio_stream.download(new_file_path)

            print(f"Download de áudio para {yt.title}.mp3 concluído!")

    except Exception as e:
        print(f"Erro durante o download: {e}")

# Exemplo de uso
video_urls = [
    "https://youtu.be/I2jLdYovW-c",
]

download_audio(video_urls)
