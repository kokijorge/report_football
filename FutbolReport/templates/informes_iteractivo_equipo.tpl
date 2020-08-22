{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
      <section id="main-content">
        <section class="wrapper">          
          <div class="row">
            <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_piechart"></i> INFORMES ITERACTIVO EQUIPO</h3>
            </div>
          </div>
          
          <!-- page start--> 
          <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
              <ul class="nav pull-center top-menu">                    
                  <li id="label_temporada_equipo_iteractivo_a" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione temporada</label>       
                  </li>
                  <li class="dropdown">
                    <select class="form-control" id="iteractivo_equipo_temporada_a">
                      <option value="2016">2016/2017</option>
                      <option value="2017">2017/2018</option>
                      <option value="todo">Todas</option>
                    </select>
                  </li>
                </ul>
                <ul class="nav pull-center top-menu">                    
                  <li id="label_temporada_a" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione equipo</label>       
                  </li>
                  <div class="dropdown">
                    <button class="btn  dropdown-toggle" type="button" data-toggle="dropdown" style="
                    background: white; border: 1px solid #c7c7cc;" id="button_equipo_a">----------
                    <span class="caret"></span>
                    </button>
                    <ul class="dropdown-menu" id="dropdown_equipo_a">
                      <input class="form-control" id="Input_equipo_a" type="text" placeholder="Search..">
                    </ul>
                  </div>
                </ul>               
            </div>
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
              <ul class="nav pull-center top-menu">                    
                  <li id="label_temporada_equipo_iteractivo_b" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione temporada</label>       
                  </li>
                  <li class="dropdown">
                    <select class="form-control" id="iteractivo_equipo_temporada_b">
                      <option value="2016">2016/2017</option>
                      <option value="2017">2017/2018</option>
                      <option value="todo">Todas</option>
                    </select>
                  </li>
                </ul>
                <ul class="nav pull-center top-menu">                    
                  <li id="label_temporada_b" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione equipo</label>       
                  </li>
                  <div class="dropdown">
                    <button class="btn  dropdown-toggle" type="button" data-toggle="dropdown" style="
                    background: white; border: 1px solid #c7c7cc;" id="button_equipo_b">----------
                    <span class="caret"></span>
                    </button>
                    <ul class="dropdown-menu" id="dropdown_equipo_b">
                      <input class="form-control" id="Input_equipo_b" type="text" placeholder="Search..">
                    </ul>
                  </div>
                </ul>              
            </div>         
          </div>  

        <div id="tablas" style="display:none"  class="col-md-12">            
            <div class="row"> 
              <h3 id="text_local"> LOCAL </h3>          
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                  <div id="tabla_equipo_local_a" ></div>         
                </div> 
                <div class="col-lg-6 col-md-46 col-sm-12 col-xs-12">  
                  <div id="tabla_equipo_local_b" ></div>         
                </div>
            </div>   

            <div class="row"> 
              <h3 id="text_local"> VISITANTE </h3>    
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div id="tabla_equipo_visitante_a" ></div>         
                </div> 
                <div class="col-lg-6 col-md-46 col-sm-12 col-xs-12">  
                <div id="tabla_equipo_visitante_b" ></div>         
                </div>
            </div>  

            <div class="row"> 
              <h3 id="text_total"> TOTAL </h3>    
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                  <div id="tabla_equipo_total_a" ></div>         
                </div> 
                <div class="col-lg-6 col-md-46 col-sm-12 col-xs-12">  
                  <div id="tabla_equipo_total_b" ></div>         
                </div>
              </div>  
          </div> 

            
          <div class="row">         
            <div class="col-md-12" id="linechart_material" style="width: 900px; height: 300px;"></div>
          </div>  

          <div class="row">         
            <div class="col-md-12" id="linechart_puntos" style="width: 900px; height: 300px;"></div>
          </div>        

          <script type="text/javascript" src="/js/charts_google.js"></script>
          <script>
            google.charts.load("current", {packages:["corechart"]});
            var anos_equipo_select_a = {{anos_equipo_select_a}};
            var anos_equipo_select_b = {{anos_equipo_select_b}};

            var select_temporada_a= $('#iteractivo_equipo_temporada_a');
            var dropdown_equipo_a= $('#dropdown_equipo_a');  
            var select_temporada_b= $('#iteractivo_equipo_temporada_b');
            var dropdown_equipo_b= $('#dropdown_equipo_b');

            select_temporada_a.on('change', function() {

              dropdown_equipo_a.empty();
              var lista_equipos_a = anos_equipo_select_a[select_temporada_a.val()];
              $('<input class="form-control" id="Input_equipo_a" type="text" placeholder="Search..">').appendTo(dropdown_equipo_a);
              busquedaEnDropdownEquipo("a");

                $.each(lista_equipos_a, function(index, equipo) {

                  var li_equ_a = $('<li><a href="#">' + equipo[0] +  '</a></li>').attr('value', equipo[0]);
                  li_equ_a.click(function() {
                    var equ = $(this).attr('value').split('||');

                    $.getJSON("/equipo_iteractivo", {
                        nombre: equ[0],                        
                        ano: $("#iteractivo_equipo_temporada_a").val()
                    })

                    .done(function(json) {
                        $("#button_equipo_a").text(equipo[0]);
                        $("#button_equipo_a").append($('<span class="caret"></span>'));
                        equipo_a = json;
                        printar_si_AB();
                    })

                    .fail(function(jqxhr, textStatus, error) {
                        var err = textStatus + ", " + error;
                        console.log("Request Failed: " + err);
                    });
                  });
                  li_equ_a.appendTo(dropdown_equipo_a);
                });

            })

            var equipo_a = null;
            var equipo_b = null;

            function printar_si_AB(){
              if (equipo_a != null && equipo_b != null){        
                // tabla inicio
                google.charts.load('current', {'packages':['line']});
                google.charts.load('current', {'packages':['bar']});
                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(drawChart);                

                function drawChart() {
                  var a = equipo_a.puntuaciones_equipo_estacion;
                  var b = equipo_b.puntuaciones_equipo_estacion;

                  console.log("jugadorA: " + a);
                  console.log("jugadorA[0]: " + a[0]);

                  var data = google.visualization.arrayToDataTable([
                    ["Estacion", equipo_a.equipo, equipo_b.equipo],
                    [a[0][0], a[0][1],b[0][1]],
                    [a[1][0], a[1][1],b[1][1]],
                    [a[2][0], a[2][1],b[2][1]],
                    [a[3][0], a[3][1],b[3][1]]
                   ]);

                  var options = {
                    title: 'Rendimiento en función de la estación del año',
                    legend: { position: 'top', maxLines: 2 },
                    colors: ['#5C3292', '#1A8763', '#871B47', '#999999'],
                    interpolateNulls: false,
                  };
              
                  var chart = new google.charts.Bar(document.getElementById('linechart_material'));
                  chart.draw(data, google.charts.Bar.convertOptions(options));      
                }

                $("#tablas").show();
                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(drawChartLine);
                function drawChartLine() {                  
                  var data_line_chart = google.visualization.arrayToDataTable([
                    ['Jornada', equipo_a.equipo, equipo_b.equipo],
                    ['2004',  1000,      400],
                    ['2005',  1170,      460],
                    ['2006',  660,       1120],
                    ['2007',  1030,      540]
                  ]);
                  var options_line_chart = {
                    title: 'Rendimiento del equipo a nivel de jornada',
                    curveType: 'function',
                    legend: { position: 'bottom' }
                  };

                  var chart_line = new google.visualization.LineChart(document.getElementById('linechart_puntos'));

                  chart_line.draw(data_line_chart, options_line_chart);
                }

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEquipoA);
                function drawTableEquipoA() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( equipo_a.puntuaciones_equipo_global );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_equipo_total_a'));
                  table_info.draw(data_info,options_info ); 
                }

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEquipoB);
                function drawTableEquipoB() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( equipo_b.puntuaciones_equipo_global );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_equipo_total_b'));
                  table_info.draw(data_info,options_info ); 
                }

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEquipoLocalA);
                function drawTableEquipoLocalA() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( equipo_a.puntuaciones_equipo_local );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_equipo_local_a'));
                  table_info.draw(data_info,options_info ); 
                }

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEquipoLocalB);
                function drawTableEquipoLocalB() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( equipo_b.puntuaciones_equipo_local );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_equipo_local_b'));
                  table_info.draw(data_info,options_info ); 
                }

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEquipoVisitanteA);
                function drawTableEquipoVisitanteA() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( equipo_a.puntuaciones_equipo_visitante );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_equipo_visitante_a'));
                  table_info.draw(data_info,options_info ); 
                }

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEquipoVisitanteB);
                function drawTableEquipoVisitanteB() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( equipo_b.puntuaciones_equipo_visitante );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_equipo_visitante_b'));
                  table_info.draw(data_info,options_info ); 
                }

              }
            }
            
            select_temporada_b.on('change', function() {

              dropdown_equipo_b.empty();
              var lista_equipos_b = anos_equipo_select_b[select_temporada_a.val()];
              $('<input class="form-control" id="Input_equipo_a" type="text" placeholder="Search..">').appendTo(dropdown_equipo_b);
              busquedaEnDropdownEquipo("b");

              $.each(lista_equipos_b, function(index, equipo) {

                var li_equ_b = $('<li><a href="#">' + equipo[0] +  '</a></li>').attr('value', equipo[0]);
                li_equ_b.click(function() {
                  var equ = $(this).attr('value').split('||');

                    $.getJSON("/equipo_iteractivo", {
                        nombre: equ[0],                        
                        ano: $("#iteractivo_equipo_temporada_b").val()
                    })

                    .done(function(json) {

                        $("#button_equipo_b").text(equipo[0]);
                        $("#button_equipo_b").append($('<span class="caret"></span>'));
                        equipo_b = json;
                        printar_si_AB();
                    })

                    .fail(function(jqxhr, textStatus, error) {
                        var err = textStatus + ", " + error;
                        console.log("Request Failed: " + err);
                    });
                });
                  li_equ_b.appendTo(dropdown_equipo_b);
              });

            })            

function busquedaEnDropdownEquipo(aOb) {
    $("#Input_equipo_" + aOb).on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".dropdown-menu li").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
}

$( document ).ready(function() {    
    $('#iteractivo_equipo_temporada_a').trigger("change");    
    $('#iteractivo_equipo_temporada_b').trigger("change");        
});

          </script>     
          <!-- page end-->
        </section>
      </section>
      <!--main content end-->
{% endblock%}
