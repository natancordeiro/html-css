function verificar() {
  var date = new Date()
  var year = date.getFullYear()
  var formyear = document.getElementById('txtyear')
  var res = document.querySelector('div#res')
  if (formyear.value.length == 0 || Number(formyear.value) > year) {
    window.alert(' [ERRO] Verifique os dados e tene novamente!')
  } else {
    var formsex = document.getElementsByName('radsex')
    var old = year - Number(formyear.value)
    var genero = ''
    var img = document.createElement ('img')
    img.setAttribute('id', 'foto')
    if (formsex[0].checked) {
      genero = 'Homem'
      if (old >=0 && old <12){
        // CRIANÇA
        img.setAttribute('src', 'imagens/menino.png')
      } else if (old < 21) {
        // JOVEM
        img.setAttribute('src', 'imagens/jovem-homem.png')
      } else if (old < 55) {
        // ADULTO
        img.setAttribute('src', 'imagens/homem.png')
      } else {
        // IDOSO
        img.setAttribute('src', 'imagens/senhor.png')
      }
    } else if (formsex[1].checked) {
      genero = 'Mulher'
      if (old >=0 && old <12){
        // CRIANÇA
        img.setAttribute('src', 'imagens/menina.png')
        } else if (old < 21) {
          // JOVEM
          img.setAttribute('src', 'imagens/jovem-mulher.png')
        } else if (old < 55) {
          // ADULTO
          img.setAttribute('src', 'imagens/mulher.png')
        } else {
          // IDOSO
          img.setAttribute('src', 'imagens/senhora.png')
        }
    }
    res.style.textAlign = 'center'
    res.innerHTML = `Detectamos ${genero} com ${old} anos.`
    res.appendChild(img)
  }
  
}