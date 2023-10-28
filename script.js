function carregar() {

var msg = window.document.getElementById ("msg")
var img = window.document.getElementById ("imagem")
var data = new Date()
/// var hora = data.getHours()  << USAR HORA ATUAL >>
var hora = 1
msg.innerHTML = `Agora são ${hora} horas.`

if (hora >= 0 && hora <= 12) {
    /// BOM DIA!!!
    img.src = "morning_pic.png"
    document.body.style.background = "#f1f15d"
} else if (hora >= 12 && hora < 18){
    /// BOA TARDE
    img.src = "noon_pic.png"
    document.body.style.background = "#ff5e00"
} else {
    /// BOA NOITE
    img.src = "nite_pic.png"
    document.body.style.background = "#378dc2"
}}