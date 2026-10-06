const validateVolName = (name) => {
    if(!name) return false;
    let lengthValid = name.trim().length >= 3;

    return lengthValid;
};

const validateEmail = (email) => {
    if(!email) return false;
    let lengthValid = email.length > 10;

    //validamos el formato
    let re = /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    let formatValid = re.test(email);

    //devolvemos la lógica AND de las validaciones
    return lengthValid && formatValid;
};

const validateRegion = () => {
    const region = document.getElementById("region-voluntario").value;
    const error = document.getElementById("error-region");

    if(region===""){
        error.classList.add("visible");
        return false;
    }

    error.classList.remove("visible");
    return true;
};

const validateComuna = () => {

    const comuna = document.getElementById("comuna-voluntario").value;
    const error = document.getElementById("error-comuna");

    if (comuna === "") {
        error.classList.add("visible");
        return false;
    }

    error.classList.remove("visible");
    return true;
};

const validateTipo = (tipo) => {
    if(!tipo) return false;
    let lengthValid = tipo.trim().length >= 2;

    return lengthValid;
};

const validateAveName = (name) => {
    if(!name) return false;
    let lengthValid = name.trim().length >= 2;

    return lengthValid;
};

const validateLugar = (lugar) => {
    if(!lugar) return false;

    let lengthValid = lugar.trim().length >= 10;

    return lengthValid;

};

const validateFecha = (fecha) => {

    if(!fecha) return false;

    const fechaIngresada = new Date(fecha + "T00:00:00");

    const hoy = new Date();
    hoy.setHours(0, 0, 0, 0);

    const semanaAtras = new Date(hoy);
    semanaAtras.setDate(hoy.getDate() - 7);

    return fechaIngresada <= hoy && fechaIngresada >= semanaAtras;
};

const validateHora = (fecha, hora) => {
    if(!fecha || !hora) return false;
    const fechaHora = new Date(`${fecha}T${hora}`);

    return fechaHora <= new Date();
};

const validateFiles = (files) => {
    if (!files) return false;

    //validación del nro y tipo de archivos
    let lengthValid = 1 <= files.length && files.length <= 3;
    let typeValid = true;

    for (const file of files) {
        //el tipo de archivo debe ser imagen o video
        let fileFamily = file.type.split("/")[0];
        typeValid &&= (fileFamily == "image" || fileFamily == "video");
    }
    return lengthValid && typeValid
};

const validateSelect = (select) => {
    if(!select) return false;
    return select.value !== ""; //para no dejar que se escoja la opción de ""--seleccione--""
};

const validateForm = () => {

    const nombre = document.getElementById("nombre-voluntario").value;
    const correo = document.getElementById("correo-voluntario").value;
    const region = document.getElementById("region-voluntario");
    const comuna = document.getElementById("comuna-voluntario");

    const tipo = document.getElementById("tipo-ave").value;
    const nombreAve = document.getElementById("nombre-ave").value;
    const lugar = document.getElementById("lugar-ave").value;
    const fecha = document.getElementById("fecha").value;
    const hora = document.getElementById("hora").value;
    const files = document.getElementById("foto-video").files;

    let valid = true;

    const nombreValido = validateVolName(nombre);
    const errorNombre = document.getElementById("error-nombre");

    if (!nombreValido) {
        errorNombre.classList.add("visible");
        valid = false;
    } else {
        errorNombre.classList.remove("visible");
    }


    const correoValido = validateEmail(correo);
    const errorCorreo = document.getElementById("error-correo");

    if (!correoValido) {
        errorCorreo.classList.add("visible");
        valid = false;
    } else {
        errorCorreo.classList.remove("visible");
    }


    const regionValida = validateSelect(region);
    const errorRegion = document.getElementById("error-region");

    if (!regionValida) {
        errorRegion.classList.add("visible");
        valid = false;
    } else {
        errorRegion.classList.remove("visible");
    }


    const comunaValida = validateSelect(comuna);
    const errorComuna = document.getElementById("error-comuna");

    if (!comunaValida) {
        errorComuna.classList.add("visible");
        valid = false;
    } else {
        errorComuna.classList.remove("visible");
    }


    const tipoValido = validateTipo(tipo);
    const errorTipo = document.getElementById("error-tipo");

    if (!tipoValido) {
        errorTipo.classList.add("visible");
        valid = false;
    } else {
        errorTipo.classList.remove("visible");
    }


    const nombreAveValido = validateAveName(nombreAve);
    const errorNombreAve = document.getElementById("error-nombre-ave");

    if (!nombreAveValido) {
        errorNombreAve.classList.add("visible");
        valid = false;
    } else {
        errorNombreAve.classList.remove("visible");
    }


    const lugarValido = validateLugar(lugar);
    const errorLugar = document.getElementById("error-lugar");

    if (!lugarValido) {
        errorLugar.classList.add("visible");
        valid = false;
    } else {
        errorLugar.classList.remove("visible");
    }


    const fechaValida = validateFecha(fecha);
    const errorFecha = document.getElementById("error-fecha");

    if (!fechaValida) {
        errorFecha.classList.add("visible");
        valid = false;
    } else {
        errorFecha.classList.remove("visible");
    }


    const horaValida = validateHora(fecha, hora);
    const errorHora = document.getElementById("error-hora");

    if (!horaValida) {
        errorHora.classList.add("visible");
        valid = false;
    } else {
        errorHora.classList.remove("visible");
    }


    const archivosValidos = validateFiles(files);
    const errorArchivos = document.getElementById("error-foto-video");

    if (!archivosValidos) {
        errorArchivos.classList.add("visible");
        valid = false;
    } else {
        errorArchivos.classList.remove("visible");
    }


    if (valid) {
        alert("Información válida");
    }
};

let sumbitBtn = document.getElementById("submit");
sumbitBtn.addEventListener("click", validateForm);