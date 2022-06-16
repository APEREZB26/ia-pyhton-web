
/* PARA EMPEZAR EDITAR EL PERFIL DEL ADMIN*/

const openPerfilEdit = document.querySelector(".perfil-edit");
openPerfilEdit.addEventListener("click", (e) =>{
    document.querySelector(".from-button").classList.toggle("open");
    document.querySelector(".from-button-main").classList.toggle("open");
    document.querySelector(".dato-edit-dis").classList.toggle("open");
    document.querySelector(".dato-edit").classList.toggle("open");
})
/* PARA CERRAR EL EDITAR DEL PERFIL DEL ADMIN*/ 
const closePerfilEdit = document.querySelector(".from-button-cancel");
closePerfilEdit.addEventListener("click", () =>{
    document.querySelector(".from-button").classList.toggle("open");
    document.querySelector(".from-button-main").classList.toggle("open");
    document.querySelector(".dato-edit-dis").classList.toggle("open");
    document.querySelector(".dato-edit").classList.toggle("open");
})



