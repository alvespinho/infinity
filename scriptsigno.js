function carregar() {

let msg = window.document.getElementById ("msg")
let img = window.document.getElementById ("imagem")
let data = new Date()

/// let hora = data.getHours()  << USAR HORA ATUAL >>

let mes = data.getMonth()
let dia = data.getDay()

msg.innerHTML = `Agora são ${hora} horas.`

if (hora >= 0 && hora <= 12) {
    /// AQUARIO
    img.src = "morning_pic.png"
    document.body.style.background = "#f1f15d"
} else if (hora >= 12 && hora < 18){
    /// PEIXES
    img.src = "noon_pic.png"
    document.body.style.background = "#ff5e00"
} else if (hora >= 12 && hora < 18){
    /// ARIES
    img.src = "noon_pic.png"
    document.body.style.background = "#ff5e00"
} else if (hora >= 12 && hora < 18){
    /// TOURO
    img.src = "noon_pic.png"
    document.body.style.background = "#ff5e00"
} else if (hora >= 12 && hora < 18){
    /// CANCER
    img.src = "noon_pic.png"
    document.body.style.background = "#ff5e00"}
} else if (hora >= 12 && hora < 18){
    /// LEAO
    img.src = "noon_pic.png"
    document.body.style.background ="#ff5e00"
} else if (hora >= 12 && hora < 18){
    /// VIRGEM
    img.src = "noon_pic.png"
    document.body.style.background = "#ff5e00"
} else if (hora >= 12 && hora < 18){
    /// LIBRA
    img.src = "noon_pic.png"
    document.body.style.background = "#ff5e00"
} else if (hora >= 12 && hora < 18){
    /// ESCORPIÃO 
    img.src = "noon_pic.png"
    document.body.style.background ="#ff5e00"
} else if (hora >= 12 && hora < 18){
    /// SAGITÁRIO 
    img.src = "noon_pic.png"
    document.body.style.background = "#ff5e00"

} else if (hora >= 12 && hora < 18){
    /// CAPRICORNIO
    img.src = "noon_pic.png"
    document.body.style.background = "#ff5e00"


} else if (hora >= 12 && hora < 18){
    /// BOA TARDE
    img.src = "noon_pic.png"
    document.body.style.background = "#ff5e00"




else {
    /// BOA NOITE
    img.src = "nite_pic.png"
    document.body.style.background = "#378dc2"
}}