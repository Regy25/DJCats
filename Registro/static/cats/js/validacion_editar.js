console.log('hola')
$(document).ready(function(){
    $("#add").validate({
        rules: {
            name_cat:{
                required: true,
                minlength: 3

            },
            ascii_cat: {
                required: true,
                minlength: 2
            },
            desc_cat: {
                required: true,
                minlength: 20
            }
        },

        messages:{
            name_cat:{
                required: "Ingrese nombre del gatito",
                minlength: "nombre corto"
            },
            ascii_cat: {
                required: "Ingrese el gatito",
                minlength: "Ingrese minimo 2 caracteres"
            },
            desc_cat: {
                required: "Ingrese la descripcion del gatito",
                minlength: "Ingrese minimo 20 caracteres"
            },
        },
        errorElement: 'div'
    });
});