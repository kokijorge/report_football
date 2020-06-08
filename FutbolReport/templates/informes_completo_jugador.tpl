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
          <div class="ui-widget">
            <label for="tags">Tags: </label>
            <input id="tags_jugador">
          </div>
          

    <div id="table_div"></div>    
    <div class="col-lg-12">
          <h3 class="page-header">Informe en función del clima</h3>            
          <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
          <div id="columnchart_temperatura" style="width: 300px; height: 200px;"></div>         
          </div> 
          <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">  
          <div id="columnchart_lluvias" style="width: 300px; height: 200px;"></div>         
          </div>
          <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">    
          <div id="columnchart_humedad" style="width: 300px; height: 200px;"></div>         
          </div>               
    </div> 
    <div id="donutchart" style="width: 900px; height: 500px;"></div>
    <div id="columnchart_values" style="width: 900px; height: 300px;"></div> 
    <div id="columnchart_rivales" style="width: 1200px; height: 700px;"></div> 

<script type="text/javascript" src="/js/charts_google.js"></script>
 
<script>

google.charts.load("current", {packages:["corechart"]});
var anos_jugadores_select = {{anos_jugadores_select}};



var select_temporada= $('#completo_jugador_temporada');
var select_jugador= $('#completo_jugador_jugador');
var tag_jugador= $('#tags_jugador');

select_temporada.on('change', function() {
  
  select_jugador.empty();
  tag_jugador.empty();
  var lista_jugadores= anos_jugadores_select[select_temporada.val()];
  var availableTags = [
    ];    

  $.each(lista_jugadores, function( index, jugador ) {
  
  //marcial !!
  $('<option>')
    .attr('value', jugador[0] + '||' + jugador[1])
    .text( jugador[0] + '||' + jugador[1] + '||' + jugador[2])
    .appendTo(select_jugador);

 availableTags.push(jugador[0] + '||' + jugador[1]);
  $( "#tags_jugador" ).autocomplete({
      source: availableTags
    }); 

  });
  
 

})


select_jugador.on('change', function() {
  
  var jug = this.value.split('||');
  
  $.getJSON( "/marcial", { nombre: jug[0], fecha: jug[1], ano: $("#completo_jugador_temporada").val() } )
  
  .done(function( json ) {

    console.log( "JSON Data: " + json.puntuaciones_temperatura );

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
      var table_info = new google.visualization.Table(document.getElementById('table_div'));
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
        width: 600,
        height: 400,
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
        width: 300,
        height: 200,
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
        width: 300,
        height: 200,
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
        width: 300,
        height: 200,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart_humedad = new google.visualization.ColumnChart(document.getElementById("columnchart_humedad"));
      chart_humedad.draw(data_humedad, options_humedad); 

    //<!-- puntuaciones rivales->         
      var data_puntuaciones_rivales = new google.visualization.DataTable();
      data_puntuaciones_rivales.addColumn('string', 'Equipo');
      data_puntuaciones_rivales.addColumn('number', 'Puntuacion');    
      data_puntuaciones_rivales.addRows(json.puntuaciones_rivales); 
      var options_rivales = {
        title: "Equipos contra los que jugó mejor/peor",
        width: 1200,
        height: 700,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart_rivales = new google.visualization.LineChart(document.getElementById("columnchart_rivales"));
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
