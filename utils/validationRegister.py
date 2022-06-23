def validRegister(fullname, email, password, dni, image):
    if not (
        valueLen(fullname, password)
        and email
        and validateDNI(dni)
        and validateImage(image)
    ):
        return False
    return True


# Complements
def valueLen(fullname, password):
    if not (len(fullname.strip()) > 6 and len(password.strip()) > 6):
        return False
    return True


def validateImage(image):
    extensionValid = [".jpg", ".jpeg", ".png"]
    if not any(extension in image.filename for extension in extensionValid):
        return False
    return True


def validateDNI(dni):
    if not (len(dni) == 8 and dni.isdigit()):
        return False
    return True
