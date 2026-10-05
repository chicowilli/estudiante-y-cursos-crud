document.querySelectorAll("form").forEach((formulario) => {
    formulario.addEventListener("submit", (evento) => {
        const boton = formulario.querySelector("button[type='submit']");
        if (boton) {
            boton.disabled = true;
            boton.textContent = "Guardando...";
        }
    });
});
