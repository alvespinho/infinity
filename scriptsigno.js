function confirmar(){

    let mes = document.getElementById("nummes")
    let dia = document.getElementById("numdia")
    let res = document.getElementById("res")
    let img = document.getElementById ("imagem")

    if ((mes.value >= 13) || (mes.value < 1) || (dia.value > 31) || (dia.value < 1) || (mes.value == 2 && dia.value > 29)){
        window.alert ("Ops! Data de Nascimento inválida!\nConfira seus dados e tente novamente.")
        
    } else if  ((mes.value == 1) && (dia.value >= 21) || (mes.value == 2) && (dia.value <= 18)){
        res.innerHTML = `Você é AQUÁRIO.`
        // img.src = "aquario_pic.png"
        document.body.style.background = "#fc8484"

    } else if ((mes.value == 2) && (dia.value >= 19) || (mes.value == 3) && (dia.value <= 20)){
        res.innerHTML = `Você é PEIXES.`
        // img.src = "peixes_pic.png"
        document.body.style.background = "#db7ff7"

    } else if ((mes.value == 3) && (dia.value >= 21) || (mes.value == 4) && (dia.value <= 20)){
        res.innerHTML = `Você é ÁRIES.`
        // img.src = "aries_pic.png"
        document.body.style.background = "#bd7ff7"

    } else if ((mes.value == 4) && (dia.value >= 21) || (mes.value == 5) && (dia.value <= 20)){
        res.innerHTML = `Você é TOURO.`
        // img.src = "touro_pic.png"
        document.body.style.background = "#a37ff7"

    } else if ((mes.value == 5) && (dia.value >= 21) || (mes.value == 6) && (dia.value <= 20)){
        res.innerHTML = `Você é GÊMEOS.`
        // img.src = "gemeos_pic.png"
        document.body.style.background = "#7f9bf7"

    } else if ((mes.value == 6) && (dia.value >= 21) || (mes.value == 7) && (dia.value <= 22)){
        res.innerHTML = `Você é CÂNCER.`
        // img.src = "cancer_pic.png"
        document.body.style.background = "#db7ff7"

    } else if ((mes.value == 7) && (dia.value >= 23) || (mes.value == 8) && (dia.value <= 22)){
        res.innerHTML = `Você é LEÃO.`
        // img.src = "leao_pic.png"
        document.body.style.background = "#7fc7f7"

    } else if ((mes.value == 8) && (dia.value >= 23) || (mes.value == 9) && (dia.value <= 22)){
        res.innerHTML = `Você é VIRGEM.`
        // img.src = "virgo_pic.png"
        document.body.style.background = "#7feff7"

    } else if ((mes.value == 9) && (dia.value >= 23) || (mes.value == 10) && (dia.value <= 22)){
        res.innerHTML = `Você é LIBRA.`
        // img.src = "libra_pic.png"
        document.body.style.background = "#7ff7b5"

    } else if ((mes.value == 10) && (dia.value >= 23) || (mes.value == 11) && (dia.value <= 21)){
        res.innerHTML = `Você é ESCORPIÃO.`
        // img.src = "escorp_pic.png"
        document.body.style.background = "#7ff77f"

    } else if ((mes.value == 11) && (dia.value >= 22) || (mes.value == 12) && (dia.value <= 21)){
        res.innerHTML = `Você é SAGITÁRIO.`
        // img.src = "sagit_pic.png"
        document.body.style.background = "#f7f57f"

    } else if ((mes.value == 12) && (dia.value >= 22) || (mes.value == 1) && (dia.value <= 20)){
        res.innerHTML = `Você é CAPRICÓRNIO.`
        // img.src = "capri_pic.png"
        document.body.style.background = "#f7a17f"
    }}