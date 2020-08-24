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
                      <!-- <option value="todo">Todas</option> --> 
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
                      <!-- <option value="todo">Todas</option> --> 
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
                google.charts.load('current', {'packages':['bar']});              
                google.charts.setOnLoadCallback(drawChart);                

                function drawChart() {
                  var a = equipo_a.puntuaciones_equipo_estacion;
                  var b = equipo_b.puntuaciones_equipo_estacion;
                  array = [];
                  array.push(["Estacion", equipo_a.equipo, equipo_b.equipo])            
                  for (var i = 0; i < 4; i++) {                                                   
                     array.push([a[i][0],a[i][1],b[i][1]])
                  }                                    

                  var data = google.visualization.arrayToDataTable(
                    array                  
                    );

                  var options = {
                    title: 'Rendimiento en función de la estación del año',
                    width: 900,
                    height: 300,
                    legend: { position: 'top', maxLines: 2 },
                    colors: ['#5C3292', '#1A8763', '#871B47', '#999999'],
                    interpolateNulls: false,
                    hAxis: {
                      title: 'Estación del año'                    
                    },
                    vAxis: {
                        title: 'Puntos'                        
                    }
                  };
              
                  var chart = new google.charts.Bar(document.getElementById('linechart_material'));
                  chart.draw(data, google.charts.Bar.convertOptions(options));      
                }

                $("#tablas").show();
                //<!-- line chart->                                     
                google.charts.load('current', {'packages':['corechart']}); 
                google.charts.setOnLoadCallback(tt);
                function tt() {     
                  var a = equipo_a.carrera_equipo;
                  var b= equipo_b.carrera_equipo;  
                  var data_puntuaciones_rivales = new google.visualization.DataTable();
                  data_puntuaciones_rivales.addColumn('number', 'Jornada');
                  data_puntuaciones_rivales.addColumn('number', equipo_a.equipo);
                  data_puntuaciones_rivales.addColumn({type: 'string', role: 'tooltip'});
                  data_puntuaciones_rivales.addColumn('number', equipo_b.equipo);              
                  data_puntuaciones_rivales.addColumn({type: 'string', role: 'tooltip'});
                  array_line_chart = []
                  for (var i = 0; i < 38; i++) {                                                   
                        array_line_chart.push([a[i][0],a[i][1],a[i][2],b[i][1],b[i][2]])
                  } ;              
                  eje_x = [];
                  for (var i = 1; i < 39; i++) {                                                   
                     eje_x.push(i)
                  };
                  data_puntuaciones_rivales.addRows(array_line_chart); 
                  var options_rivales = {
                    title: "Puntos en función de la jornada",
                    width: 900,
                    height: 300,
                    bar: {groupWidth: "95%"},
                    hAxis: {
                      title: 'Jornada',
                      ticks: eje_x
                    },
                    vAxis: {
                        title: 'Puntos Acumulados'                        
                    },                                        
                    tooltip: {isHtml: true}
                  };
                  var chart_rivales = new google.visualization.LineChart(document.getElementById("linechart_puntos"));
                  chart_rivales.draw(data_puntuaciones_rivales, options_rivales);          
                }       
                //fin  line_chart

 
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
              $('<input class="form-control" id="Input_equipo_b" type="text" placeholder="Search..">').appendTo(dropdown_equipo_b);
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
