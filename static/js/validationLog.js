//VALIDAR FORMULARIO DE LOGIN
const formLog = document.getElementById("formLog");
const logInputs = document.querySelectorAll(".inputLog");
const msgError = document.querySelector(".error");

camposLog = {
  dniLog: false,
  passwordLog: false,
};

const validarFormulario = (e) => {
  switch (e.target.name) {
    case "dni":
      if(document.getElementsByName(e.target.value).length == 0){
        camposLog['dniLog']=true
        console.log(camposLog['dniLog'])
      }
      break;
    case "password":
        if(document.getElementsByName(e.target.value).length == 0){
            camposLog['passwordLog']=true
            console.log(camposLog['passwordLog'])
          }
      break;
  }
};

logInputs.forEach((input) => {
  input.addEventListener("blur", validarFormulario);
});

formLog.addEventListener("submit", (e) => {
  if (camposLog.dniLog && camposLog.passwordLog) {
    
  } else {
    e.preventDefault();
    msgError.classList.add("active");
    setTimeout(() => {
      msgError.classList.remove("active");
    }, 2000);
  }
});
