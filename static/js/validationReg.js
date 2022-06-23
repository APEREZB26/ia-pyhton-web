const formulario = document.getElementById("formulario");
const inputs = document.querySelectorAll("#formulario input");

const spinner = document.querySelector(".spinner-container");
const containerReg = document.querySelector(".containerReg");
const msgError = document.querySelector(".error");


const messageError = document.getElementById("message-error");
// Message error in document html register_page
messageError.style.display = "block";
setTimeout(() => {
  messageError.style.display = "none";
}, 3000);

const expresiones = {
  fullname: /^[a-zA-ZÀ-ÿ\s]{1,40}$/,
  password: /^.{4,12}$/,
  email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
  photo: /^/,
  dni: /^/,
  checkbox: /^/,
};

const campos = {
  fullname: false,
  photo: false,
  email: false,
  dni: false,
  password: false,
  checkbox: false,
};

const validarFormulario = (e) => {
  switch (e.target.name) {
    case "fullname":
      validarCampo(expresiones.fullname, e.target, "fullname");
      break;
    case "photo":
      validarCampoPhoto();
      break;
    case "email":
      validarCampo(expresiones.email, e.target, "email");
      break;
    case "dni":
      validarCampo(expresiones.dni, e.target, "dni");
      break;
    case "password":
      validarCampo(expresiones.password, e.target, "password");
      break;
    case "checkbox":
      validarCampo(expresiones.checkbox, e.target, "checkbox");
      console.log(campos["checkbox"]);
      break;
  }
};

const validarCampo = (expresion, input, camp) => {
  if (expresion.test(input.value)) {
    document.getElementById(camp).classList.remove("incorrect");
    document.getElementById(camp).classList.add("correct");
    campos[camp] = true;
  } else {
    document.getElementById(camp).classList.add("incorrect");
    document.getElementById(camp).classList.remove("correct");
  }
};

const validarCampoPhoto = () => {
  photo = document.getElementById("photo");
  if (photo.value !== "") {
    campos["photo"] = true;
    console.log(campos["photo"]);
  } else {
    campos["photo"] = false;
    console.log(campos["photo"]);
  }
};

inputs.forEach((input) => {
  input.addEventListener("blur", validarFormulario);
  input.addEventListener("keyup", validarFormulario);
});

formulario.addEventListener("submit", (e) => {
  if (
    campos.fullname &&
    campos.photo &&
    campos.email &&
    campos.dni &&
    campos.password
  ) {
    spinner.classList.add("active");
    containerReg.classList.add("remove");
  } else {
    e.preventDefault();
    msgError.classList.add("active");
    setTimeout(() => {
      msgError.classList.remove("active");
    }, 2000);
  }
});
