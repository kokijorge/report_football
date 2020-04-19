function escoger_equipo(){
    var dominio = "/equipos/"+$("#select_temporada").val();
    window.location.href=dominio; 
}

function init() {

$('#id_input').val($("#select_temporada").val());
$('#select_temporada').val({{ temporada_seleccionada }});
$(document).on('change', '#select_temporada', function(event) {
    $('#id_input').val($("#select_temporada").val());    
    var pag = window.location.pathname.slice(0,-5)
    if (pag.length > 0) {
        var dominio = pag+"/"+$("#select_temporada").val();
            window.location.href=dominio;
      } else {
        var dominio = "/"+$("#select_temporada").val();
            window.location.href=dominio; 
      }
       
});

}

jQuery(document).ready(function(){
    init();
});