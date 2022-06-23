from flask import request, redirect, url_for, render_template, session
from werkzeug.security import check_password_hash
from face_recognition_and_liveness.face_liveness_detection.face_recognition_liveness_app import (
    recognition_liveness,
)
from services.auth.loginUser import login_userDB


def user_login(mysql):
    session.clear()
    dni = request.form["dni"]
    password = request.form["password"]

    if dni.isdigit():
        user = login_userDB(mysql, dni)
        if user == None:
            return render_template("login_page.html", incorrect=True)

        if user and check_password_hash(user[3], password):
            detected_name, label_name = recognition_liveness(
                "face_recognition_and_liveness/face_liveness_detection/liveness.model",
                "face_recognition_and_liveness/face_liveness_detection/label_encoder.pickle",
                "face_recognition_and_liveness/face_liveness_detection/face_detector",
                "face_recognition_and_liveness/face_recognition/encoded_faces.pickle",
                confidence=0.5,
            )
            if user[4] == detected_name and label_name == "real" and user[5] == 1:
                session["id"] = user[0]
                session["fullname"] = user[1]
                return redirect(url_for("admin"))
            elif user[4] == detected_name and label_name == "real" and user[5] == 0:
                session["id"] = user[0]
                session["fullname"] = user[1]
                print("session: ", session["id"])
                return redirect(url_for("client"))
            else:
                return render_template(
                    "login_page.html", invalid_user=True, username=user[1]
                )
        else:
            return render_template("login_page.html", incorrect=True)
    else:
        return render_template("login_page.html", incorrect=True)
