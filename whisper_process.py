import os
import whisper


def get_text_from_audio(audio_path="", output_file_path=""):
    model = whisper.load_model("large")
    result = model.transcribe(audio_path)

    print(audio_path)
    print(result["text"])

    file_name = output_file_path

    if not os.path.exists(file_name):
        with open(file_name, "w") as archivo:
            archivo.write("Transcription.\n")

    # Hacer un append para agregar más texto al archivo
    with open(file_name, "a") as archivo:
        archivo.write(result["text"] + "\n")
