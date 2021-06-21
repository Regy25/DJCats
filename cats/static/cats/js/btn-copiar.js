$(document).ready(function () {
    $("#btn-copiar").click(function () {
            var gato = document.getElementById(gato).innerHTML;

            function CopiadordeGatos(e) {
                e.clipboardData.setData("text/html", gato);
                e.clipboardData.setData("text/plain", gato);
                e.preventDefault();
            }
            document.addEventListener("copy", CopiadordeGatos);
            document.execCommand("copy");
            document.removeEventListener("copy", CopiadordeGatos);
    });
});