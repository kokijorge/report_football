function escoger_equipo(){
    var dir_equipo = "/equipos/"+$("#select_temporada").val();
    window.location.href=dir_equipo; 
}

function escoger_entrenador(){
    var dir_entrenadores = "/entrenadores/"+$("#select_temporada").val();
    window.location.href=dir_entrenadores; 
}

function escoger_jugador(){
    var dir_jugadores = "/jugadores/"+$("#select_temporada").val();
    window.location.href=dir_jugadores; 
}

function escoger_estadio(){
    var dir_estadios = "/estadios/"+$("#select_temporada").val();
    window.location.href=dir_estadios; 
}


function escoger_informe(){
    var dir_informes = "/informes/"+$("#select_temporada").val();
    window.location.href=dir_informes; 
}

function escoger_jornadas(){
    var dir_jornadas = "/jornadas/"+$("#select_jornada").val()+"/"+$("#select_temporada").val();
    window.location.href=dir_jornadas; 
}

function top_menu(){
    var dir_menu = "/top/"+$("#select_temporada").val();
    window.location.href=dir_menu; 
}

function init() {

$('#select_jornada').val({{ jornada_seleccionada }});
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

$(document).on('change', '#select_jornada', function(event) {     
    var pag_jornada = window.location.pathname.slice(0,-5)
    if (pag_jornada.length > 0) {
        var dominio_jornada = pag_jornada+"/"+$("#select_jornada").val()+"/"+$("#select_temporada").val();
            window.location.href=dominio_jornada;
      } else {
        var dominio_jornada = "/"+$("#select_jornada").val()+"/"+$("#select_temporada").val();
            window.location.href=dominio_jornada; 
      }  
});

}

jQuery(document).ready(function(){
    init();
});