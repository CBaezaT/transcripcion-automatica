#los paquetes que necesitaremos seran principalmente speech_recognition para transcribir el audio,
# os para crear los directorios que usaremos y tambien tanto AudioSegment como split_on_silence 
# de pydub para manipular el archivo .wav
import speech_recognition as sr
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence


# reconocedor de habla
r = sr.Recognizer()

def get_large_audio_transcription(path):
    """
    Separaremos el audio largo en trozos para
    aplicar reconocimiento de voz a cada trozo 
    """
    # abrimos el audio con pydub
    sound = AudioSegment.from_wav(path)  
    # separamos el audio donde el silencio dure 700 miliseconds o más por los trozos
    chunks = split_on_silence(sound,
        # estas cantidades pueden variar según tu audio
        min_silence_len = 500,
        # ajustese según se necesite
        silence_thresh = sound.dBFS-14,
        # mantiene el silencio por 1 segundo, tambien ajustable
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # crea un directorio para guardar los trozos del audio 
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # procesamos cada trozo
    for i, audio_chunk in enumerate(chunks, start=1):
        # exportamos el trozo del audio y lo guardamos enumerado
        # en la carpeta de nombre `folder_name`.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # reconocemos el trozo de audio
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # lo intentamos convertir en texto, en este caso establecemos
            # usar el reconocimiento de google en español
            try:
                text = r.recognize_google(audio_listened, language="es-ES")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # entrega el texto por todos los trozos de audio
    return whole_text

#seleccionamos el path de nuestro archivo wav
path = "entrevista.wav"
print("\nFull text:", get_large_audio_transcription(path))