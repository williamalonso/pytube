from pytubefix import YouTube
from pytubefix.cli import on_progress

def baixar_video(url, caminho_destino='.'):
    try:
        # Cria um objeto YouTube com callback de progresso
        video = YouTube(url, on_progress_callback=on_progress)

        # Pega a melhor resolução com áudio e vídeo juntos
        stream = video.streams.filter(progressive=True, file_extension='mp4') \
                              .order_by('resolution') \
                              .desc() \
                              .first()

        # Verifica se a stream foi encontrada
        if stream:
            print(f'Baixando: {video.title} ({stream.resolution})')
            stream.download(output_path=caminho_destino)
            print('Download concluído com sucesso!')
        else:
            print("Erro: Não foi possível encontrar uma stream com áudio e vídeo.")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    # Insira a URL do vídeo que deseja baixar
    url_do_video = input("Insira a URL do vídeo do YouTube: ")

    # Insira o caminho de destino (pasta) para salvar o vídeo (opcional)
    caminho_destino = input("Insira o caminho de destino (pressione Enter para usar o diretório atual): ") or '.'

    # Chama a função para baixar o vídeo
    baixar_video(url_do_video, caminho_destino)
