$(document).ready(function(){
    $("#CatsForm").validate({
        rules: {
            nombre_cat:{
                required: true,
                minlength: 3

            },
        }
    });
});