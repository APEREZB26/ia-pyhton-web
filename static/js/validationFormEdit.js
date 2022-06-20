const phone = document.getElementById("inputPhone"),
  errorForm = document.getElementById("errorForm");

document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("formAdd").addEventListener("submit", validForm);
});

phone.addEventListener("change", validPhone);


function validForm(e) {
  e.preventDefault();
  if (validAll() === false) {
    console.log("Hubo algun error");
    return;
  }

  this.submit();
}

function validAll() {
  if ((validPhone()) == false) {
    return false;
  }

  errorForm.style.display = "none";
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

