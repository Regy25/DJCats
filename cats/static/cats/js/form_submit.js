$(document).ready(function () {
  $("#contact-form").validate({
    rules: {
      nombre_gato: {
        required: true,
        minlength: 3
      },
      historia_gato: {
        required: true,
        minlength: 6
      },
      category: {
        required: true,
      },
      gato: {
        required: true,
        minlength: 2
      }
    },
    messages: {
      nombre_gato: {
        required: "Ingrese Nombre",
        minlength: "Largo minimo 3 caracteres"
      },
      historia_gato: {
        required: "Ingrese Historia",
        minlength: "Largo minimo 6 caracteres"
      },
      category: {
        required: "Escoja una categoria",
      },
      gato: {
        required: "Ingresa el gatito",
        minlength: "Largo min 2 caracteres"
      }
    },
      errorElement: 'div'
    
  });
});