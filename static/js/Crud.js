/* PARA ABRIR EL MODAL DELETE*/
const buttonsEdit = document.querySelectorAll(".button-edit");
buttonsEdit.forEach((buttonEdit) => {
  buttonEdit.addEventListener("click", () => {
    let id = buttonEdit.children[0].value;
    window.location.href = `/admin/manage/getEmpl/${id}`;
  });
});

const modalAdd = document.querySelector(".button-add");
modalAdd.addEventListener("click", () => {
  document.querySelector(".content-modal-edit").classList.toggle("open");
  document.querySelector(".in-add-email").classList.remove("d-none");
  document.querySelector(".in-add-pass").classList.remove("d-none");
});
// /* PARA CERRAR EL MODAL GUARDAR EMPLEADO*/
const closeModalEdit = document.querySelector(".cancel-button");
closeModalEdit.addEventListener("click", (e) => {
  e.preventDefault();
  document.querySelector(".content-modal-edit").classList.toggle("open");
});
