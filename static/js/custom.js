$(document).ready(function () {
    $("#id_title").change(function () {
        if ($("select option[value='C']").is(':selected')) {
            $("<input type='number' min='0' class='temporary' placeholder='Use nums 0 - 9 to specify the number of Kgs (1.99 per Kg)' name='kgs'>", {
            }).appendTo($('#temp'));
        }
        else {
            $( ".temporary" ).hide();
        }
    });
    if ($("select option[value='C']").is(':selected')) {
            $("<input type='number' min='0' class='temporary' placeholder='Use nums 0 - 9 to specify the number of Kgs (1.99 per Kg)' name='kgs'>", {
            }).appendTo($('#temp'));
        }
});
