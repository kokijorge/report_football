{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
      <section id="main-content">
        <section class="wrapper">          
          <div class="row">
            <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_piechart"></i> INFORMES ITERACTIVO ENTRENADOR</h3>
            </div>
          </div>
          
          <!-- page start--> 
          <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
              <ul class="nav pull-center top-menu">                    
                  <li id="label_temporada_entrenador_iteractivo_a" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione temporada</label>       
                  </li>
                  <li class="dropdown">
                    <select class="form-control" id="iteractivo_entrenador_temporada_a">
                      <option value="2016">2016/2017</option>
                      <option value="2017">2017/2018</option>
                      <option value="todo">Todas</option>
                    </select>
                  </li>
                </ul>
                <ul class="nav pull-center top-menu">                    
                  <li id="label_temporada_a" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione entrenador</label>       
                  </li>
                  <div class="dropdown">
                    <button class="btn  dropdown-toggle" type="button" data-toggle="dropdown" style="
                    background: white; border: 1px solid #c7c7cc;" id="button_entrenador_a">----------
                    <span class="caret"></span>
                    </button>
                    <ul class="dropdown-menu" id="dropdown_entrenador_a">
                      <input class="form-control" id="Input_entrenador_a" type="text" placeholder="Search..">
                    </ul>
                  </div>
                </ul>               
            </div>
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
              <ul class="nav pull-center top-menu">                    
                  <li id="label_temporada_entrenador_iteractivo_b" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione temporada</label>       
                  </li>
                  <li class="dropdown">
                    <select class="form-control" id="iteractivo_entrenador_temporada_b">
                      <option value="2016">2016/2017</option>
                      <option value="2017">2017/2018</option>
                      <option value="todo">Todas</option>
                    </select>
                  </li>
                </ul>
                <ul class="nav pull-center top-menu">                    
                  <li id="label_temporada_b" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione entrenador</label>       
                  </li>
                  <div class="dropdown">
                    <button class="btn  dropdown-toggle" type="button" data-toggle="dropdown" style="
                    background: white; border: 1px solid #c7c7cc;" id="button_entrenador_b">----------
                    <span class="caret"></span>
                    </button>
                    <ul class="dropdown-menu" id="dropdown_entrenador_b">
                      <input class="form-control" id="Input_entrenador_b" type="text" placeholder="Search..">
                    </ul>
                  </div>
                </ul>              
            </div>         
          </div>  

        <div id="tablas_entrenador_iteractivo" style="display:none"  class="col-md-12">            
          <div class="row"> 
              <h3 id="text_local"> LOCAL </h3>          
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div id="tabla_entrenador_local_a" ></div>         
                </div> 
                <div class="col-lg-6 col-md-46 col-sm-12 col-xs-12">  
                <div id="tabla_entrenador_local_b" ></div>         
                </div>
          </div>   

            <div class="row"> 
              <h3 id="text_local"> VISITANTE </h3>    
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div id="tabla_entrenador_visitante_a" ></div>         
                </div> 
                <div class="col-lg-6 col-md-46 col-sm-12 col-xs-12">  
                <div id="tabla_entrenador_visitante_b" ></div>         
                </div>
            </div>  

            <div class="row"> 
              <h3 id="text_total"> TOTAL </h3>    
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div id="tabla_entrenador_total_a" ></div>         
                </div> 
                <div class="col-lg-6 col-md-46 col-sm-12 col-xs-12">  
                <div id="tabla_entrenador_total_b" ></div>         
                </div>
            </div>  
        </div>
          
          <div class="row">         
            <div class="col-md-12" id="linechart_material" style="width: 900px; height: 300px;"></div>
          </div>            

          <script type="text/javascript" src="/js/charts_google.js"></script>
          <script>
            google.charts.load("current", {packages:["corechart"]});
            var anos_entrenador_select_a = {{anos_entrenador_select_a}};
            var anos_entrenador_select_b = {{anos_entrenador_select_b}};

            var select_temporada_a= $('#iteractivo_entrenador_temporada_a');
            var dropdown_entrenador_a= $('#dropdown_entrenador_a');  
            var select_temporada_b= $('#iteractivo_entrenador_temporada_b');
            var dropdown_entrenador_b= $('#dropdown_entrenador_b'); 

            select_temporada_a.on('change', function() {

              dropdown_entrenador_a.empty();
              var lista_entrenadores_a = anos_entrenador_select_a[select_temporada_a.val()];
              $('<input class="form-control" id="Input_entrenador_a" type="text" placeholder="Search..">').appendTo(dropdown_entrenador_a);
              busquedaEnDropdownEntrenador("a");

                $.each(lista_entrenadores_a, function(index, entrenador) {

                  var li_ent_a = $('<li><a href="#">'+entrenador[0] + '||' + entrenador[1] + '</a></li>').attr('value', entrenador[0] + '||' + entrenador[1]);                    
                  li_ent_a.click(function() {
                    var ent = $(this).attr('value').split('||');

                    $.getJSON("/entrenador_iteractivo", {
                        nombre: ent[0],
                        equipo: ent[1],                        
                        ano: $("#iteractivo_entrenador_temporada_a").val()
                    })

                    .done(function(json) {
                        $("#button_entrenador_a").text(entrenador[0] + '||' + entrenador[1]);
                        $("#button_entrenador_a").append($('<span class="caret"></span>'));
                        entrenador_a = json;
                        printar_si_AB();
                    })

                    .fail(function(jqxhr, textStatus, error) {
                        var err = textStatus + ", " + error;
                        console.log("Request Failed: " + err);
                    });
                  });
                  li_ent_a.appendTo(dropdown_entrenador_a);
                });

            })    

            var entrenador_a = null;
            var entrenador_b = null;  

            function printar_si_AB(){
              if (entrenador_a != null && entrenador_b != null){        
                // tabla inicio
                google.charts.load('current', {'packages':['line']});
                google.charts.setOnLoadCallback(drawChart);

                function drawChart() {

                  var data = google.visualization.arrayToDataTable([
                  ['Quarks', 'Leptons', 'Gauge Bosons', 'Scalar Bosons'],
                  [2/3, -1, 0, 0],
                  [2/3, -1, 0, null],
                  [2/3, -1, 0, null],
                  [-1/3, 0, 1, null],
                  [-1/3, 0, -1, null],
                  [-1/3, 0, null, null],
                  [-1/3, 0, null, null]
                  ]);

                  var options = {
                    title: 'Charges of subatomic particles',
                    legend: { position: 'top', maxLines: 2 },
                    colors: ['#5C3292', '#1A8763', '#871B47', '#999999'],
                    interpolateNulls: false,
                  };
              
                  var chart = new google.visualization.Histogram(document.getElementById('linechart_material'));
                  chart.draw(data, options);        
                }

                $("#tablas_entrenador_iteractivo").show();

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEentrenadorA);
                function drawTableEentrenadorA() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( entrenador_a.puntuaciones_entrenador_global );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_entrenador_total_a'));
                  table_info.draw(data_info,options_info ); 
                }

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEentrenadorB);
                function drawTableEentrenadorB() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( entrenador_b.puntuaciones_entrenador_global );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_entrenador_total_b'));
                  table_info.draw(data_info,options_info ); 
                }

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEntrenadorLocalA);
                function drawTableEntrenadorLocalA() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( entrenador_a.puntuaciones_entrenador_local );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_entrenador_local_a'));
                  table_info.draw(data_info,options_info ); 
                }

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEntrenadorLocalB);
                function drawTableEntrenadorLocalB() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( entrenador_b.puntuaciones_entrenador_local );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_entrenador_local_b'));
                  table_info.draw(data_info,options_info ); 
                }

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEntrenadorVisitanteA);
                function drawTableEntrenadorVisitanteA() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( entrenador_a.puntuaciones_entrenador_visitante );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_entrenador_visitante_a'));
                  table_info.draw(data_info,options_info ); 
                }

                google.charts.load('current', {'packages':['table']});
                google.charts.setOnLoadCallback(drawTableEntrenadorVisitanteB);
                function drawTableEntrenadorVisitanteB() {
                  var data_info = new google.visualization.DataTable();
                  data_info.addColumn('number', 'Empates');
                  data_info.addColumn('number', 'Victorias');
                  data_info.addColumn('number', 'Derrotas');
                  data_info.addColumn('number', 'Goles a favor');
                  data_info.addColumn('number', 'Goles en contra');
                  data_info.addColumn('number', 'Puntos'); 
                  data_info.addRows( entrenador_b.puntuaciones_entrenador_visitante );
                  var options_info = {showRowNumber: true, width: '100%', height: '100%'};
                  var table_info = new google.visualization.Table(document.getElementById('tabla_entrenador_visitante_b'));
                  table_info.draw(data_info,options_info ); 
                }

              }
            }

            select_temporada_b.on('change', function() {

              dropdown_entrenador_b.empty();
              var lista_entrenadores_b = anos_entrenador_select_b[select_temporada_b.val()];
              $('<input class="form-control" id="Input_entrenador_b" type="text" placeholder="Search..">').appendTo(dropdown_entrenador_b);
              busquedaEnDropdownEntrenador("b");

                $.each(lista_entrenadores_b, function(index, entrenador) {

                  var li_ent_b = $('<li><a href="#">'+entrenador[0] + '||' + entrenador[1] + '</a></li>').attr('value', entrenador[0] + '||' + entrenador[1]);                    
                  li_ent_b.click(function() {
                    var ent = $(this).attr('value').split('||');

                    $.getJSON("/entrenador_iteractivo", {
                        nombre: ent[0],
                        equipo: ent[1],                        
                        ano: $("#iteractivo_entrenador_temporada_b").val()
                    })

                    .done(function(json) {
                        $("#button_entrenador_b").text(entrenador[0] + '||' + entrenador[1]);
                        $("#button_entrenador_b").append($('<span class="caret"></span>'));
                        entrenador_b = json;
                        printar_si_AB();
                    })

                    .fail(function(jqxhr, textStatus, error) {
                        var err = textStatus + ", " + error;
                        console.log("Request Failed: " + err);
                    });
                  });
                  li_ent_b.appendTo(dropdown_entrenador_b);
                });

            })   

function busquedaEnDropdownEntrenador(aOb) {
    $("#Input_entrenador_" + aOb).on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".dropdown-menu li").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
}

$( document ).ready(function() {    
    $('#iteractivo_entrenador_temporada_a').trigger("change");    
    $('#iteractivo_entrenador_temporada_b').trigger("change");        
});
          </script>     
          <!-- page end-->
        </section>
      </section>
      <!--main content end-->
{% endblock%}
