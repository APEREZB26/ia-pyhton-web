@echo off

echo Codificando Imagenes...
cd C:\Users\KENNET\Desktop\ia-pyhton-web-1\face_recognition_and_liveness\face_recognition
python encode_faces.py -i dataset -e encoded_faces.pickle -d cnn
exit