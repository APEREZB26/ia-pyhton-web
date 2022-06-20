const fullname = document.getElementById("inputFullname"),
  dni = document.getElementById("inputDNI"),
  phone = document.getElementById("inputPhone"),
  email = document.getElementById("inputEmail"),
  password = document.getElementById("inputPassword"),
  image = document.getElementById("inputImage"),
  errorForm = document.getElementById("errorForm");

const emailRegex = new RegExp(
  /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
);

document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("formAdd").addEventListener("submit", validForm);
});

image.addEventListener("click", validImage);
fullname.addEventListener("change", validFullname);
dni.addEventListener("change", validDNI);
phone.addEventListener("change", validPhone);
email.addEventListener("change", validEmail);
password.addEventListener("change", validPassword);

function validForm(e) {
  e.preventDefault();
  if (validAll() === false) {
    console.log("Hubo algun error");
    return;
  }

  this.submit();
}

function validAll() {
  if ((validImage() && validFullname() && validDNI() && validPhone() && validEmail() && validPassword()) == false) {
    return false;
  }

  errorForm.style.display = "none";
  email.style.borderBottom = "2px solid green";
  return true;
}

function validImage() {
  console.log(image.src);
  console.log(image);
  console.log(image.value);
  if (image.value === "" || !image.value || image.value === null) {
    errorForm.style.display = "flex";
    errorForm.innerHTML = "Debe seleccionar una imagen";
    return false;
  }

  errorForm.style.display = "none";
  return true;
}

function validFullname() {
  if (fullname.value.trim().length < 6) {
    fullname.style.borderBottom = "2px solid red";
    errorForm.style.display = "flex";
    errorForm.innerHTML = "El nombre debe tener al menos 6 caracteres";
    return false;
  }

  errorForm.style.display = "none";
  fullname.style.borderBottom = "2px solid green";
  return true;
}

function validDNI() {
  if (dni.value.length !== 8) {
    dni.style.borderBottom = "2px solid red";
    errorForm.style.display = "flex";
    errorForm.innerHTML = "El DNI debe tener 8 caracteres";
    return false;
  }

  errorForm.style.display = "none";
  dni.style.borderBottom = "2px solid green";
  return true;
}

function validPhone() {
  if (phone.value.length !== 9) {
    phone.style.borderBottom = "2px solid red";
    errorForm.style.display = "flex";
    errorForm.innerHTML = "El telefono debe tener 9 digitos";
    return false;
  }

  errorForm.style.display = "none";
  phone.style.borderBottom = "2px solid green";
  return true;
}

function validEmail() {
  if (!emailRegex.test(email.value)) {
    email.style.borderBottom = "2px solid red";
    errorForm.style.display = "flex";
    errorForm.innerHTML = "El email no es valido";
    return false;
  }

  errorForm.style.display = "none";
  email.style.borderBottom = "2px solid green";
  return true;
}

function validPassword() {
  if (password.value.length < 6) {
    password.style.borderBottom = "2px solid red";
    errorForm.style.display = "flex";
    errorForm.innerHTML = "La contraseña debe tener almenos 6 caracteres";
    return false;
  }

  errorForm.style.display = "none";
  password.style.borderBottom = "2px solid green";
  return true;
}
