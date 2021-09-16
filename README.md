# Transcripción de audios automática  v1
_Por Cristian Baeza T_  
Transcribir audios largos en español en texto escrito en Python.  
_Basado_ _en_ _el_ _trabajo_ _de_ _Adbou_ _Rockikz_ _en_ _[PythonCode](thepythoncode.com)_

Esta solución fue pensada para agilizar la transcripción de entrevistas, no es una automatización _perfecta_, sobre todo en casos en que el hablante posee un acento marcado, aún así la revisión de la transcripción se hace sencilla.  
Su funcionamiento de basa en utilizar el reconocimiento de voz de Google para transcribir audios en formato .wav,uno de los problemas del reconocimiento de voz es que no es practico para transcribir audios largos, por lo que se usa pydub para recortar estos audios en los silencios e interrupciones, guardando cada archivo enumerado. 
Se aplicará el reconocimiento de voz a cada trozo de audio y la consola entregara la transcripción de cada uno, así luego se podrá hacer la revisión por cada una de estas partes. Como resultado final, la consola entregará el texto completo.  
  
___
  
### Tutorial
Este proyecto fue llevado a cabo en Python 3.8.5 en Conda, VScode como IDE en Mac OS.   

Lo primero es asegurarse de tener instalados los paquetes necesarios SpeechRecognition y pydub:  
```
pip install SpeechRecognition pydud   
```  

Lo siguiente es tener preparado nuestra carpeta o directorio en donde tendremos nuestro archivo de audio en formato **wav**. En este mismo directorio, ya dentro de Visual Studio Code, creamos nuestro archivo **transcripcion.py** o simplemente descargar  de mi [repositorio](https://github.com/CBaezaT/transcripcion-automatica) el archivo __transcrip.py__  o hacer un fork de este repositorio.  

---  
Luego, ya con nuestro archivo python importamos los paquetes y funciones que usaremos.  

```python  
import speech_recognition as sr
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence  
```
Establecemos el reconocedor de habla como __r__  
```python  
r = sr.Recognizer()
``` 
Ahora, creamos una función que separará nuestro audio en trozos donde hayan silencios de minimo 700 milisegundos o más, luego guardara estos trozos en una carpeta, para luego analizar y transcribir cada uno de ellos con el reconocimiento de voz de Google y finalmente unir todo el texto.  

```python  
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
    folder_name = "audio-chunks" # nombre para la carpeta de los trozos de audio
    # crea un directorio para guardar los trozos del audio 
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # procesamos cada trozo
    for i, audio_chunk in enumerate(chunks, start=1):
        # exportamos el trozo del audio y lo guardamos enumerado
        # en la carpeta de nombre `audio-chunks`.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # reconocemos el trozo de audio
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # lo intentamos convertir en texto, en este caso establecemos
            # usar el reconocimiento de google en español y entrega en la consola el nombre del trozo y su texto en el formato "chunk1: Hola mundo"
            try:
                text = r.recognize_google(audio_listened, language="es-ES")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # entrega el texto completo de  todos los trozos de audio que se transcribieron
    return whole_text
```

Ahora, ya teniendo lista la función en nuestro script solo debemos seleccionar el audio que usaremos y que imprima el texto completo en la consola, si esta en la carpeta como se indico antes solo debes escribir el nombre del archivo.  
```python
#seleccionamos el path de nuestro archivo wav
path = "audio.wav"
print("\nFull text:", get_large_audio_transcription(path))  
````

---  
Espero que les sea utíl!  
 Agradecimientos a Adbou Rockikz de PythonCode.
___  
[Repositorio de transcripción automatica](https://github.com/CBaezaT/transcripcion-automatica)  
[Proyecto Original de pythoncode](https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python)  
[Documentación de pydub](https://pypi.org/project/pydub/)  
[Documentación de SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
