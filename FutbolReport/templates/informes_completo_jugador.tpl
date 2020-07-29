{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
        <section class="wrapper">          
          <div class="row">
            <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_piechart"></i> INFORMES COMPLETO JUGADOR</h3>
            </div>
          </div>
          
          <!-- page start--> 
          <div class="row"> 
          <ul class="nav pull-center top-menu">                    
              <li id="label_temporada" class="dropdown">
                <label for="labelTemporada" form style="width:100px">Seleccione temporada</label>       
              </li>
              <li class="dropdown">
                <select class="form-control" id="completo_jugador_temporada">
                  <option value="2016">2016/2017</option>
                  <option value="2017">2017/2018</option>
                  <option value="todo">Todas</option>
                </select>
              </li>
            </ul>
            <ul class="nav pull-center top-menu">                    
              <li id="label_jugador" class="dropdown">
                <label for="labelTemporada" form style="width:100px">Seleccione jugador</label>       
              </li>
              <li class="dropdown">
                <select class="form-control" id="completo_jugador_jugador">                                                     
                </select>
              </li>
            </ul>            
          </div>
          <!-- MARCIAL -->
          <div class="dropdown">
            <button class="btn  dropdown-toggle" type="button" data-toggle="dropdown" style="
            background: white; border: 1px solid #c7c7cc;">----------
            <span class="caret"></span></button>
            <ul class="dropdown-menu" id="dropdown_jugador">
              <input class="form-control" id="myInput" type="text" placeholder="Search..">
            </ul>
          </div>
          <!-- MARCIAL -->
          
<div class="row"> 
    <div id="table_div_jugador" class="col-md-12"></div>    
</div >   

<div class="row"> 
    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
    <div id="columnchart_temperatura" style="width: 500px; height: 300px;"></div>         
    </div> 
    <div class="col-lg-6 col-md-46 col-sm-12 col-xs-12">  
    <div id="columnchart_lluvias" style="width: 500px; height: 300px;"></div>         
    </div>
</div>    
<div class="row">     
    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">    
    <div id="columnchart_humedad" style="width: 500px; height: 300px;"></div>         
    </div> 
    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">    
    <div id="columnchart_viento" style="width: 500px; height: 300px;"></div>         
    </div>           
</div> 
  
<div class="row">         
    <div class="col-md-12" id="donutchart" style="width: 900px; height: 300px;"></div>
</div>  
<div class="row"> 
    <div class="col-md-12" id="columnchart_values" style="width: 900px; height: 300px;"></div> 
</div>  
<div class="row"> 
    <div class="col-md-12"id="columnchart_rivales" style="width: 900px; height: 300px;"></div> 
</div>  
<div class="row"> 
    <div class="col-md-12"id="columnchart_rivales_media" style="width: 900px; height: 300px;"></div> 
</div>  


<script type="text/javascript" src="/js/charts_google.js"></script>
<script>

google.charts.load("current", {packages:["corechart"]});
var anos_jugadores_select = {{anos_jugadores_select}};

var select_temporada= $('#completo_jugador_temporada');
var select_jugador= $('#completo_jugador_jugador');
var dropdown_jugador = $("#dropdown_jugador");

select_temporada.on('change', function() {
  
  select_jugador.empty();
  var lista_jugadores= anos_jugadores_select[select_temporada.val()];  






  $.each(lista_jugadores, function( index, jugador ) {
    
    $('<option>')
      .attr('value', jugador[0] + '||' + jugador[1] + '||' + jugador[3])
      .text( jugador[0] + '||' + jugador[2] + '||' + jugador[3])
      .appendTo(select_jugador);


      var li = $('<li><a href="#">'+jugador[0] + '||' + jugador[2] + '||' + jugador[3]+'</a></li>').attr('value', jugador[0] + '||' + jugador[1] + '||' + jugador[3]);      
      li.click(function(){
        alert ($(this).attr('value'))
      })
      dropdown_jugador.append(li);

    });       
  
})

$( document ).ready(function() {    
  $('#completo_jugador_temporada').trigger("change");    
});

//<!-- MARCIAL -->
$(document).ready(function(){
  $("#myInput").on("keyup", function() {    
    var value = $(this).val().toLowerCase();
    $(".dropdown-menu li").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
//<!-- MARCIAL -->

select_jugador.on('change', function() {
  
  var jug = this.value.split('||');
  console.log( "select_jugador: " + jug );
  $.getJSON( "/jugador_completo", { nombre: jug[0], fecha: jug[1], equipo: jug[2], ano: $("#completo_jugador_temporada").val() } )
  
  .done(function( json ) {    

    // tabla con toda la informacion
    google.charts.load('current', {'packages':['table']});
    google.charts.setOnLoadCallback(drawTable);
    function drawTable() {
      var data_info = new google.visualization.DataTable();
      data_info.addColumn('string', 'Nombre');
      data_info.addColumn('string', 'Equipo');
      data_info.addColumn('number', 'Puntos');
      data_info.addColumn('number', 'Minutos');
      data_info.addColumn('number', 'Goles');
      data_info.addColumn('number', 'Amarillas');
      data_info.addColumn('number', 'Rojas');
      data_info.addColumn('number', 'Titularidades');        
      data_info.addRows( json.puntuaciones_info_global );
      var options_info = {showRowNumber: true, width: '100%', height: '100%'};
      var table_info = new google.visualization.Table(document.getElementById('table_div_jugador'));
      table_info.draw(data_info,options_info ); 
    }     

    //<!-- puntuaciones hora partido-->          
    var data_hora_partido = new google.visualization.DataTable();
    data_hora_partido.addColumn('string', 'Horas');
    data_hora_partido.addColumn('number', 'Porcentaje');    
    data_hora_partido.addRows(json.puntuaciones_hora_partido); 
    var options_hora_partido = {
      title: 'Informe en función de la hora de partido',
      pieHole: 0.4,
    };
    var chart_hora_partido = new google.visualization.PieChart(document.getElementById('donutchart'));
    chart_hora_partido.draw(data_hora_partido, options_hora_partido);
    
    //<!-- puntuaciones estacion año-->         
      var data_estacion_ano = new google.visualization.DataTable();
      data_estacion_ano.addColumn('string', 'Estacion del año');
      data_estacion_ano.addColumn('number', 'Puntuacion');    
      data_estacion_ano.addRows(json.puntuaciones_estacion_ano); 
      var options_estacion_ano = {
        title: "Informe en función de la estación del año",        
        width: 900,
        height: 300,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart_estacion_ano = new google.visualization.ColumnChart(document.getElementById("columnchart_values"));
      chart_estacion_ano.draw(data_estacion_ano, options_estacion_ano);     

        //<!-- puntuaciones temperatura-->         
      var data_temperatura = new google.visualization.DataTable();
      data_temperatura.addColumn('string', 'Temperatura');
      data_temperatura.addColumn('number', 'Puntuacion');    
      data_temperatura.addRows(json.puntuaciones_temperatura); 
      var options_temperatura = {
        title: "Informe en función de la temperatura",
        width: 500,
        height: 300,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart_temperatura = new google.visualization.ColumnChart(document.getElementById("columnchart_temperatura"));
      chart_temperatura.draw(data_temperatura, options_temperatura);  

    //<!-- puntuaciones lluvias-->         
      var data_lluvias = new google.visualization.DataTable();
      data_lluvias.addColumn('string', 'Temperatura');
      data_lluvias.addColumn('number', 'Puntuacion');    
      data_lluvias.addRows(json.puntuaciones_lluvias); 
      var options_lluvias = {
        title: "Informe en función de las lluvias",
        width: 500,
        height: 300,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart_lluvias = new google.visualization.ColumnChart(document.getElementById("columnchart_lluvias"));
      chart_lluvias.draw(data_lluvias, options_lluvias);  

    //<!-- puntuaciones humedad-->         
      var data_humedad = new google.visualization.DataTable();
      data_humedad.addColumn('string', 'Temperatura');
      data_humedad.addColumn('number', 'Puntuacion');    
      data_humedad.addRows(json.puntuaciones_humedad); 
      var options_humedad = {
        title: "Informe en función de la humedad",
        width: 500,
        height: 300,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart_humedad = new google.visualization.ColumnChart(document.getElementById("columnchart_humedad"));
      chart_humedad.draw(data_humedad, options_humedad);

      //<!-- puntuaciones viento-->         
      var data_viento= new google.visualization.DataTable();
      data_viento.addColumn('string', 'Velocidad Viento');
      data_viento.addColumn('number', 'Puntuacion');    
      data_viento.addRows(json.puntuaciones_viento); 
      var options_viento = {
        title: "Informe en función de la velocidad de viento",
        width: 500,
        height: 300,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart_viento = new google.visualization.ColumnChart(document.getElementById("columnchart_viento"));
      chart_viento.draw(data_viento, options_viento); 

    //<!-- puntuaciones rivales total->         
      var data_puntuaciones_rivales = new google.visualization.DataTable();
      data_puntuaciones_rivales.addColumn('string', 'Equipo');
      data_puntuaciones_rivales.addColumn('number', 'Puntuacion');    
      data_puntuaciones_rivales.addColumn({type: 'string', role: 'tooltip'});
      data_puntuaciones_rivales.addRows(json.puntuaciones_rivales); 
      var options_rivales = {
        title: "Equipos contra los que jugó mejor/peor",
        width: 900,
        height: 300,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
        tooltip: {isHtml: true}
      };
      var chart_rivales = new google.visualization.LineChart(document.getElementById("columnchart_rivales"));
      chart_rivales.draw(data_puntuaciones_rivales, options_rivales);   

    //<!-- puntuaciones rivales media->         
      var data_puntuaciones_rivales = new google.visualization.DataTable();
      data_puntuaciones_rivales.addColumn('string', 'Equipo');
      data_puntuaciones_rivales.addColumn('number', 'Puntuacion');    
      data_puntuaciones_rivales.addColumn({type: 'string', role: 'tooltip'});
      data_puntuaciones_rivales.addRows(json.puntuaciones_rivales_media); 
      var options_rivales = {
        title: "Equipos contra los que jugó mejor/peor de media",
        width: 900,
        height: 300,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
        tooltip: {isHtml: true}
      };
      var chart_rivales = new google.visualization.LineChart(document.getElementById("columnchart_rivales_media"));
      chart_rivales.draw(data_puntuaciones_rivales, options_rivales); 

  })
  
  .fail(function( jqxhr, textStatus, error ) {
    var err = textStatus + ", " + error;
    console.log( "Request Failed: " + err );
  });


});                   
        </script>     
          <!-- page end-->
        </section>
      </section>
      <!--main content end-->
{% endblock%}
