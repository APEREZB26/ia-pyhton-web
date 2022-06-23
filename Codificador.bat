@echo off

echo Codificando Imagenes...
cd C:\Users\Usuario\Desktop\finalexpotec\ia-pyhton-web\face_recognition_and_liveness\face_recognition
python encode_faces.py -i dataset -e encoded_faces.pickle -d cnn
exit