from moviepy.editor import VideoFileClip

def get_audio_from_video(video_path="", audio_output_path=""):

    # Cargar el videos
    video_clip = VideoFileClip(video_path)

    # Extraer el audio
    audio_clip = video_clip.audio

    # Guardar el audio en un archivo
    audio_clip.write_audiofile(audio_output_path)

    # Cerrar los clips para liberar recursos
    video_clip.close()
    audio_clip.close()