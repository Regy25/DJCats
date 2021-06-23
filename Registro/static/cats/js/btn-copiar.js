
const copybtn = [...document.getElementsByClassName('copy-btn')]
console.log(copybtn)


let ultimo = null

copybtn.forEach(btn=> btn.addEventListener('click', ()=>{
    const id = btn.getAttribute('data-id')
    var ascii = document.getElementById(id).innerHTML;
    btn.textContent ='Copiado'

    navigator.clipboard.writeText(ascii)

    if (ultimo) {
        ultimo.textContent = 'Copiar'

    }
    ultimo = btn

}))

