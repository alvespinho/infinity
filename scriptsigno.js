function confirmar(){

    // let msg = window.document.getElementById("res")
    // let img = window.document.getElementById("imagem")    
    /// let hora = data.getHours()  << USAR HORA ATUAL >>
    
    let mes = document.getElementById("nummes")
    let dia = document.getElementById("numdia")
    let res = document.getElementById("res")


    if ((mes.value >= 13) || (mes.value < 1) || (dia.value > 31) || (dia.value < 1)){
        window.alert ("Erro. Data de Nascimento inválida.")
        
    } else if  ((mes.value == 1) && (dia.value <= 22) || (mes.value == 2) && (dia.value >= 22)){
        res.innerHTML = `Você é AQUÁRIO.`



    } else if ((mes.value == 3) && (dia.value <= 22) || (mes.value == 2) && (dia.value >= 22)){
        res.innerHTML = `Você é PEIXES.`



    } else if ((mes.value == 4) && (dia.value <= 22) || (mes.value == 3) && (dia.value >= 22)){
        res.innerHTML = `Você é ÁRIES.`



    } else if ((mes.value == 5) && (dia.value <= 22) || (mes.value == 4) && (dia.value >= 22)){
        res.innerHTML = `Você é TOURO.`



    } else if ((mes.value == 6) && (dia.value <= 22) || (mes.value == 5) && (dia.value >= 22)){
        res.innerHTML = `Você é GÊMEOS.`



    } else if ((mes.value == 7) && (dia.value <= 22) || (mes.value == 6) && (dia.value >= 22)){
        res.innerHTML = `Você é CÂNCER.`



    } else if ((mes.value == 8) && (dia.value <= 22) || (mes.value == 7) && (dia.value >= 22)){
        res.innerHTML = `Você é LEÃO.`



    } else if ((mes.value == 9) && (dia.value <= 22) || (mes.value == 8) && (dia.value >= 22)){
        res.innerHTML = `Você é VIRGEM.`



    } else if ((mes.value == 10) && (dia.value <= 22) || (mes.value == 9) && (dia.value >= 22)){
        res.innerHTML = `Você é LIBRA.`



    } else if ((mes.value == 11) && (dia.value <= 22) || (mes.value == 10) && (dia.value >= 22)){
        res.innerHTML = `Você é ESCORPIÃO.`



    } else if ((mes.value == 12) && (dia.value <= 22) || (mes.value == 11) && (dia.value >= 22)){
        res.innerHTML = `Você é SAGITÁRIO.`



    } else if ((mes.value == 1) && (dia.value <= 22) || (mes.value == 12) && (dia.value >= 22)){
        res.innerHTML = `Você é CAPRICÓRNIO.`
      
    
    }}
