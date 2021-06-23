console.log("hola")
$(document).ready(function(){
    $("#CatsForm").validate({
        rules: {
            nombre_cat:{
                required: true,
                minlength: 3

            },
        },

        messages:{
            nombre_cat:{
                required: "requerido",
                minlength: "nombre corto"
            }
        }
    });
});