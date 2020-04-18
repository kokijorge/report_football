/*$('#select_temporada').on('click', function(){
    console.log($(this).val());
});*/

$(document).on('change', '#select_temporada', function(event) {
	$('#id_input').val($("#select_temporada").val());
});