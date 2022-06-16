registar = document.querySelector(".reg-button")
spinner = document.querySelector(".spinner-container")
containerReg = document.querySelector(".containerReg")

registar.addEventListener("click", ()=>{
    spinner.classList.add("active");
    containerReg.classList.add("remove")
})