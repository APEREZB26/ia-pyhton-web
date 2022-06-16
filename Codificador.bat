@echo off
set /p nombre=Ingrese su DNI:
echo %nombre%
cd C:\Users\Usuario\Desktop\Nueva carpeta\python-web-ia\face_recognition_and_liveness\face_recognition
python encode_faces.py -i dataset\%nombre% -e encoded_faces.pickle -d cnn
exit


