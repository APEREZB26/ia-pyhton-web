import cloudinary
import cloudinary.uploader
import cloudinary.api


def upload_image(img, dni):
    upload_result = cloudinary.uploader.upload(img, public_id = dni)
    return upload_result;