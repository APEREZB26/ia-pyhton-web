/* PARA ABRIR EL MODAL DELETE*/
const buttonsEdit = document.querySelectorAll(".button-edit");
buttonsEdit.forEach((buttonEdit) => {
  console.log(buttonEdit);
  buttonEdit.addEventListener("click", () => {
    const id = document.getElementById("id-user");
    console.log(id);
    //window.location.href = `/users/edit/${id}`;
  });
});

/* PARA CERRAR EL MODAL DELETE*/
// const closeModalDelete = document.querySelector(".button-cancelar");
// closeModalDelete.addEventListener("click", () => {
//   document.querySelector(".content-modal-delete").classList.toggle("open");
// });

// /* PARA ABRIR EL MODAL GUARDAR EMPLEADO*/
// const modalEdit = document.querySelector(".button-edit");
// modalEdit.addEventListener("click", () => {
//   document.querySelector(".content-modal-edit").classList.toggle("open");
//   document.querySelector(".in-add-email").classList.add("d-none");
//   document.querySelector(".in-add-pass").classList.add("d-none");
// });

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
