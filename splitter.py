import os
from pydub import AudioSegment

def audio_splitter(audio_path="", output_folder="audio_segments"):
    # Ruta del archivo de audio
    audio_path = audio_path
    # Duración de cada segmento en milisegundos (ejemplo: 60000 ms = 1 minuto)
    segment_duration = 60000

    # Cargar el archivo de audio
    audio = AudioSegment.from_file(audio_path)

    # Obtener la duración total del audio en milisegundos
    total_duration = len(audio)

    os.makedirs(output_folder, exist_ok=True)

    # Dividir el audio en segmentos
    for i in range(0, total_duration, segment_duration):
        start_time = i
        end_time = min(i + segment_duration, total_duration)

        segment = audio[start_time:end_time]

        audio_file = f"segment_{i // segment_duration + 1}.mp3"

        if os.path.exists("processed_audio/" + audio_file):
            print(f"{audio_file} already exists")
            continue

        # Guardar cada segmento
        segment_name = os.path.join(output_folder, audio_file)
        segment.export(segment_name, format="mp3")

        print(f"Segmento guardado: {segment_name}")
