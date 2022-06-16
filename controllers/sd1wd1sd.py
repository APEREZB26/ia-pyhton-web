# from flask import Flask, render_template, redirect, url_for, request, session
# from werkzeug.security import generate_password_hash, check_password_hash

# from face_recognition_and_liveness.face_liveness_detection.face_recognition_liveness_app import recognition_liveness

# import os
# import time

# def login_user(): #Puede ser considerar solo POST
#     if request.method == 'POST':
#         dni = request.form['dni']
#         password = request.form['password']
#         user = Users.query.filter_by(
#             dni=dni).first()

#         # print(user.id)
#         if user and check_password_hash(user.password, password):
#             detected_name, label_name = recognition_liveness('face_recognition_and_liveness/face_liveness_detection/liveness.model',
#                                                              'face_recognition_and_liveness/face_liveness_detection/label_encoder.pickle',
#                                                              'face_recognition_and_liveness/face_liveness_detection/face_detector',
#                                                              'face_recognition_and_liveness/face_recognition/encoded_faces.pickle',
#                                                              confidence=0.5)
#             print("detected_name: ",detected_name)
#             print("label_name: ",label_name)
#             print("user_dni: ", user.dni)
#             if user.dni == detected_name and label_name == 'real' and user.rol == "admin":
#                 session['id'] = user.id
#                 session['fullname'] = user.fullname
#                 return redirect(url_for('admin'))
#             elif user.dni == detected_name and label_name == 'real' and user.rol== "client":
#                 session['id'] = user.id
#                 session['fullname'] = user.fullname
#                 print("session: ", session['id'])
#                 return redirect(url_for('client'))
#             else:
#                 return render_template('login_page.html', invalid_user=True, username=user.fullname)
#         else:
#             return render_template('login_page.html', incorrect=True)
#     return render_template('login_page.html')

# def register_user():
#     if request.method == 'POST':
#         # img = request.files['image']
#         fullname = request.form['fullname']
#         email = request.form["email"]
#         dni = request.form['dni']
#         password = request.form['password']
#         rol = "admin"
#         hashed_password = generate_password_hash(password, method='sha256')
#         new_user = Users(fullname=fullname, email=email,
#                          dni=dni, password=hashed_password,rol=rol)
#         print(new_user)
#         db.session.add(new_user)
#         db.session.commit()
#         print("User registrado")

#         os.mkdir(f'face_recognition_and_liveness/face_recognition/dataset/{dni}')

#         return redirect(url_for('login'))
#     return render_template('register_page.html')