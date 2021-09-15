# Transcripción de audios automática 
Script de python para transcribir audios largos en español en texto escrito.  
_Basado_ _en_ _el_ _trabajo_ _de_ _Adbou_ _Rockikz_ _en_ _[PythonCode](thepythoncode.com)_

Esta solución fue pensada para agilizar la transcripción de entrevistas, no es una automatización _perfecta_,  
sobre todo en casos en que el hablante posee un acento marcado, aún así la revisión de la transcripción se hace sencilla.  
Su funcionamiento de basa en utilizar el reconocimiento de voz de Google para transcribir audios en formato .wav,  
uno de los problemas del reconocimiento de voz es que no es practico para transcribir audios largos, por lo que se  
usa pydub para recortar estos audios en los silencios e interrupciones, guardando cada archivo enumerado. Se aplicará  
el reconocimiento de voz a cada trozo de audio y la consola entregara la transcripción de cada uno, así luego se podrá  
hacer la revisión por cada una de estas partes. Como resultado final, la consola entregará el texto completo.
___
### Inicio del tutorial
Este proyecto fue llevado a cabo en Python 3.8.5 en Conda, VScode como IDE en Mac OS.  
Lo primero es asegurarse de tener instalados los paquetes necesarios SpeechRecognition y pydub:  
```
pip install SpeechRecognition pydud   
```


___  
[Proyecto Original de pythoncode](https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python)  
[Documentación de pydub](https://pypi.org/project/pydub/)  
[Documentación de SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
