from pytube import YouTube

def baixar_video(url, caminho_destino='.'):
    try:
        # Cria um objeto YouTube
        video = YouTube(url)

        # Filtra as streams para incluir vídeo e áudio
        stream = video.streams.filter(res='720p', progressive=True).first()

        # Verifica se a stream foi encontrada
        if stream:
            # Baixa o vídeo
            print(f'Baixando: {video.title} (720p)')
            stream.download(output_path=caminho_destino)
            print('Download concluído com sucesso!')
        else:
            print("Erro: Não foi possível encontrar uma stream com a qualidade 720p para o vídeo.")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    # Insira a URL do vídeo que deseja baixar
    url_do_video = input("Insira a URL do vídeo do YouTube: ")

    # Insira o caminho de destino (pasta) para salvar o vídeo (opcional)
    caminho_destino = input("Insira o caminho de destino (pressione Enter para usar o diretório atual): ") or '.'

    # Chama a função para baixar o vídeo
    baixar_video(url_do_video, caminho_destino)
