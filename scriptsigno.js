function confirmar() {

let msg = window.document.getElementById("res")
let img = window.document.getElementById("imagem")

let data = new Date()

/// let hora = data.getHours()  << USAR HORA ATUAL >>

let fmes = document.getElementById("txtmes")
let fdia = document.getElementById("txtdia")

let mes = number(fmes.value)
let dia = number(fdia.value)


if (mes.value > 12 || mes.value < 1 || dia.value < 1 || dia.value > 31) {
    window.alert ("Erro. Data de Nascimento inválida.")
} else if (mes.value == 2) {
    /// AQUARIO
    img.src = ""
    document.body.style.background = ""
    res.innerHTML = `Você é AQUÁRIO.`
} else if (mes.value == 3){
    /// PEIXES
    img.src = ""
    document.body.style.background = ""
    res.innerHTML = `Você é PEIXES.`
} else if (mes.value == 4){
    /// ARIES
    img.src = ""
    document.body.style.background = ""
    res.innerHTML = `Você é ÁRIES.`  
} else if (mes.value == 5){
    /// TOURO
    img.src = ""
    document.body.style.background = ""
    res.innerHTML = `Você é TOURO.`
} else if (mes.value == 6){
    /// GÊMEOS
    img.src = ""
    document.body.style.background = ""
    res.innerHTML = `Você é GÊMEOS.`
} else if (mes.value == 7){
    /// CÂNCER 
    img.src = ""
    document.body.style.background = ""
    res.innerHTML = `Você é CÂNCER.`
} else if (mes.value == 8){
    /// LEAO
    img.src = ""
    document.body.style.background = ""
    res.innerHTML = `Você é LEÃO.`
} else if (mes.value == 9){
    /// VIRGEM
    img.src = ""
    document.body.style.background = ""
} else if (mes.value == 10){
    /// LIBRA
    img.src = ""
    document.body.style.background = ""
    res.innerHTML = `Você é LIBRA.`
} else if (mes.value == 11){
    /// ESCORPIÃO 
    img.src = ""
    document.body.style.background =""
    res.innerHTML = `Você é ESCORPIÃO.`
} else if (mes.value == 12){
    /// SAGITÁRIO 
    img.src = ""
    document.body.style.background = ""   
    res.innerHTML = `Você é SAGITÁRIO.`
} else (mes.value == 1){
    /// CAPRICÓRNIO
    img.src = ""
    document.body.style.background = ""   
    res.innerHTML = `Você é CAPRICÓRNIO.`
}}