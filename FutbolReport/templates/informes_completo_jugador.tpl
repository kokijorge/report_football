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
              <li id="label_temporada" class="dropdown">
                <label for="labelTemporada" form style="width:100px">Seleccione jugador</label>       
              </li>
              <li class="dropdown">
                <select class="form-control" id="completo_jugador_jugador">                                                     

                </select>
              </li>
            </ul>  
          </div>


    <div id="chart_div" style="width: 900px; height: 500px;"></div>
       <div id="donutchart" style="width: 900px; height: 500px;"></div>
    <div id="columnchart_values" style="width: 900px; height: 300px;"></div>


<script type="text/javascript" src="/js/charts_google.js"></script>
 
<script>

      google.charts.load("current", {packages:["corechart"]});
var anos_jugadores_select = {{anos_jugadores_select}};



var select_temporada= $('#completo_jugador_temporada');
var select_jugador= $('#completo_jugador_jugador');

select_temporada.on('change', function() {
  
  select_jugador.empty();
  var lista_jugadores= anos_jugadores_select[select_temporada.val()];

  $.each(lista_jugadores, function( index, jugador ) {
  
  
  $('<option>')
    .attr('value', jugador[0] + '||' + jugador[1])
    .text( jugador[0] + '||' + jugador[1] + '||' + jugador[2])
    .appendTo(select_jugador);

  });


})


select_jugador.on('change', function() {
  
  var jug = this.value.split('||');
  
  $.getJSON( "/marcial", { nombre: jug[0], fecha: jug[1], ano: $("#completo_jugador_temporada").val() } )
  
  .done(function( json ) {

    console.log( "JSON Data: " + json.puntuaciones );

var data = new google.visualization.DataTable();

data.addColumn('string', 'Rivales');
data.addColumn('number', 'Puntos');

data.addRows(json.puntuaciones);

        var options = {
          title: 'Informe de los rivales contra los que jugó mejor y peor',
          legend: { position: 'none' },
        };

        var chart = new google.visualization.Histogram(document.getElementById('chart_div'));
        chart.draw(data, options);

  })
  
  .fail(function( jqxhr, textStatus, error ) {
    var err = textStatus + ", " + error;
    console.log( "Request Failed: " + err );
  });


});

//<!-- puntuaciones rivales--> 



//<!-- puntuaciones hora partido-->        

      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Porcentaje', 'Horas'],
          {{ puntuaciones_hora_partido }}]);        

        var options = {
          title: 'Informe en función de la hora de partido',
          pieHole: 0.4,
        };

        var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
        chart.draw(data, options);
      }

    

    //<!-- puntuaciones estacion año-->        

    google.charts.load("current", {packages:['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var data = google.visualization.arrayToDataTable([
        ["Estación del año", "Puntuación"], 
        {{ puntuaciones_estacion_ano }}]);   
      var view = new google.visualization.DataView(data);

      var options = {
        title: "Informe en función de la estación del año",
        width: 600,
        height: 400,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart = new google.visualization.ColumnChart(document.getElementById("columnchart_values"));
      chart.draw(view, options);
    } 
    </script>

<!-- tabla con toda la informacion-->       

          <!-- page end-->
        </section>
      </section>
      <!--main content end-->
{% endblock%}
