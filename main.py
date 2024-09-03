import os
import re
from datetime import datetime

from audiogetter import get_audio_from_video
from splitter import audio_splitter
from whisper_process import get_text_from_audio

if __name__ == '__main__':
    video_path = "videos/recording.mov"

    if not os.path.exists(video_path):
        get_audio_from_video(
            video_path=video_path,
            audio_output_path="audios/recording.mp3"
        )

    audio_splitter(
        audio_path="audios/recording.mp3",
        output_folder="processed_audio"
    )

    now = str(datetime.now())
    output_file_path = f"transcribe_{now}.txt"

    # Especifica la folder de la que quieres obtener los archivos
    folder = "processed_audio/"

    # Obtén la lista de todos los archivos en la folder
    files_names = [archivo for archivo in os.listdir(folder) if os.path.isfile(os.path.join(folder, archivo))]

    files_names = sorted(files_names, key=lambda file: int(re.search(r'\d+', file).group()))

    for i, file_name in enumerate(files_names):

        if i > 20:
            break

        get_text_from_audio(
            audio_path=folder + file_name,
            output_file_path=output_file_path
        )



