function confirmar() {

let msg = window.document.getElementById ("msg")
let img = window.document.getElementById ("imagem")
let data = new Date()

/// let hora = data.getHours()  << USAR HORA ATUAL >>

let mes = data.getMonth()
let dia = data.getDay()

msg.innerHTML = `Agora são ${hora} horas.`

if (mes == 2) {
    /// AQUARIO
    img.src = ""
    document.body.style.background = ""
} else if (mes == 3){
    /// PEIXES
    img.src = ""
    document.body.style.background = ""
} else if (mes == 4){
    /// ARIES
    img.src = ""
    document.body.style.background = ""
} else if (mes == 5){
    /// TOURO
    img.src = ""
    document.body.style.background = ""
} else if (mes == 6){
    /// GÊMEOS
    img.src = ""
    document.body.style.background = ""
} else if (mes == 7){
    /// CÂNCER 
    img.src = ""
    document.body.style.background = ""
} else if (mes == 8){
    /// LEAO
    img.src = ""
    document.body.style.background = ""
} else if (mes == 9){
    /// VIRGEM
    img.src = ""
    document.body.style.background = ""
} else if (mes == 10){
    /// LIBRA
    img.src = ""
    document.body.style.background = ""
} else if (mes == 11){
    /// ESCORPIÃO 
    img.src = ""
    document.body.style.background =""
} else if (mes == 12){
    /// SAGITÁRIO 
    img.src = ""
    document.body.style.background = ""
} else (mes == 1){
    /// CAPRICÓRNIO
    img.src = ""
    document.body.style.background = ""
}}