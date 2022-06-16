@echo off
set /p nombre= Ingrese su DNI=< dni.txt

echo %nombre%
cd C:\Users\Usuario\Desktop\OficialEXPOTEC\ia-pyhton-web\face_recognition_and_liveness\face_recognition
python encode_faces.py -i dataset\%nombre% -e encoded_faces.pickle -d cnn
exit


