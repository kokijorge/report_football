{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
        <section class="wrapper">          
          <div class="row">
            <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_piechart"></i> INFORMES ITERACTIVO JUGADOR</h3>
            </div>
          </div>
          
          <!-- page start--> 
          <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
              <ul class="nav pull-center top-menu">                    
                  <li id="label_temporada_jugador_iteractivo_a" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione temporada</label>       
                  </li>
                  <li class="dropdown">
                    <select class="form-control" id="iteractivo_jugador_temporada_a">
                      <option value="2016">2016/2017</option>
                      <option value="2017">2017/2018</option>
                      <option value="todo">Todas</option>
                    </select>
                  </li>
                </ul>
                <ul class="nav pull-center top-menu">                    
                  <li id="label_jugador_a" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione jugador</label>       
                  </li>
                  <div class="dropdown">
                    <button class="btn  dropdown-toggle" type="button" data-toggle="dropdown" style="
                    background: white; border: 1px solid #c7c7cc;" id="button_jugador_a">----------
                    <span class="caret"></span>
                    </button>
                    <ul class="dropdown-menu" id="dropdown_jugador_a">
                      <input class="form-control" id="Input_jugador_a" type="text" placeholder="Search..">
                    </ul>
                  </div>
                </ul>               
            </div>
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
              <ul class="nav pull-center top-menu">                    
                  <li id="label_temporada_jugador_iteractivo_b" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione temporada</label>       
                  </li>
                  <li class="dropdown">
                    <select class="form-control" id="iteractivo_jugador_temporada_b">
                      <option value="2016">2016/2017</option>
                      <option value="2017">2017/2018</option>
                      <option value="todo">Todas</option>
                    </select>
                  </li>
                </ul>
                <ul class="nav pull-center top-menu">                    
                  <li id="label_jugador_b" class="dropdown">
                    <label for="labelTemporada" form style="width:100px">Seleccione jugador</label>       
                  </li>
                  <div class="dropdown">
                    <button class="btn  dropdown-toggle" type="button" data-toggle="dropdown" style="
                    background: white; border: 1px solid #c7c7cc;" id="button_jugador_b">----------
                    <span class="caret"></span>
                    </button>
                    <ul class="dropdown-menu" id="dropdown_jugador_b">
                      <input class="form-control" id="Input_jugador_b" type="text" placeholder="Search..">
                    </ul>
                  </div>
                </ul>              
            </div>         
          </div>  
          
          <div class="row"> 
              <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
              <div id="tabla_jugador_a" style="width: 500px; height: 300px;"></div>         
              </div> 
              <div class="col-lg-6 col-md-46 col-sm-12 col-xs-12">  
              <div id="tabla_jugador_b" style="width: 500px; height: 300px;"></div>         
              </div>
          </div>  
           
          <div class="row">         
            <div class="col-md-12" id="linechart_material" style="width: 900px; height: 300px;"></div>
          </div>        

<script type="text/javascript" src="/js/charts_google.js"></script>
  <script>

    google.charts.load("current", {packages:["corechart"]});
    var anos_jugadores_select_a = {{anos_jugadores_select_a}};
    var anos_jugadores_select_b = {{anos_jugadores_select_b}};

    var select_temporada_a= $('#iteractivo_jugador_temporada_a');
    var dropdown_jugador_a= $('#dropdown_jugador_a');  
    var select_temporada_b= $('#iteractivo_jugador_temporada_b');
    var dropdown_jugador_b= $('#dropdown_jugador_b'); 
    

    select_temporada_a.on('change', function() {

        dropdown_jugador_a.empty();
        var lista_jugadores_a = anos_jugadores_select_a[select_temporada_a.val()];
        $('<input class="form-control" id="Input_jugador_a" type="text" placeholder="Search..">').appendTo(dropdown_jugador_a);
        busquedaEnDropdownJugador("a");

        $.each(lista_jugadores_a, function(index, jugador) {

            var li_jug_a = $('<li><a href="#">' + jugador[0] + '||' + jugador[2] + '||' + jugador[3] + '</a></li>').attr('value', jugador[0] + '||' + jugador[1] + '||' + jugador[3]);
            li_jug_a.click(function() {
                var jug = $(this).attr('value').split('||');

                $.getJSON("/jugador_iteractivo", {
                        nombre: jug[0],
                        fecha: jug[1],
                        equipo: jug[2],
                        ano: $("#iteractivo_jugador_temporada_a").val()
                    })

                    .done(function(json) {
                        $("#button_jugador_a").text(jugador[0] + '||' + jugador[2] + '||' + jugador[3]);
                        $("#button_jugador_a").append($('<span class="caret"></span>'));
                        console.log("JSON Data: " + json.nombre);
                        console.log("JSON Data: " + json);
                        jugador_a = json;
                        printar_si_AB();
                    })

                    .fail(function(jqxhr, textStatus, error) {
                        var err = textStatus + ", " + error;
                        console.log("Request Failed: " + err);
                    });


            });
            li_jug_a.appendTo(dropdown_jugador_a);
        });

    })


    var jugador_a = null;
    var jugador_b = null;

    function printar_si_AB(){
        if (jugador_a != null && jugador_b != null){        
          // marcial -> aqui tendría que meter los datos de los dos jugadores y que se vean bien -> https://developers.google.com/chart/interactive/docs/gallery/histogram
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
          // marcial q se vean bien las dos tablas siguientes
          google.charts.load('current', {'packages':['table']});
          google.charts.setOnLoadCallback(drawTableJugA);
          function drawTableJugA() {
            var data_info = new google.visualization.DataTable();
            data_info.addColumn('string', 'Nombre');
            data_info.addColumn('string', 'Equipo');
            data_info.addColumn('number', 'Puntos');
            data_info.addColumn('number', 'Minutos');
            data_info.addColumn('number', 'Goles');
            data_info.addColumn('number', 'Amarillas');
            data_info.addColumn('number', 'Rojas');
            data_info.addColumn('number', 'Titularidades');        
            data_info.addRows( jugador_a.puntuaciones_info_global );
            var options_info = {showRowNumber: true, width: '100%', height: '100%'};
            var table_info = new google.visualization.Table(document.getElementById('tabla_jugador_a'));
            table_info.draw(data_info,options_info ); 
          } 

          google.charts.setOnLoadCallback(drawTableJugB);
          function drawTableJugB() {
            var data_info = new google.visualization.DataTable();
            data_info.addColumn('string', 'Nombre');
            data_info.addColumn('string', 'Equipo');
            data_info.addColumn('number', 'Puntos');
            data_info.addColumn('number', 'Minutos');
            data_info.addColumn('number', 'Goles');
            data_info.addColumn('number', 'Amarillas');
            data_info.addColumn('number', 'Rojas');
            data_info.addColumn('number', 'Titularidades');        
            data_info.addRows( jugador_b.puntuaciones_info_global );
            var options_info = {showRowNumber: true, width: '100%', height: '100%'};
            var table_info = new google.visualization.Table(document.getElementById('tabla_jugador_b'));
            table_info.draw(data_info,options_info ); 
          } 
        }
    }

  

select_temporada_b.on('change', function() {

    dropdown_jugador_b.empty();
    var lista_jugadores_b = anos_jugadores_select_b[select_temporada_b.val()];
    $('<input class="form-control" id="Input_jugador_b" type="text" placeholder="Search..">').appendTo(dropdown_jugador_b);
    busquedaEnDropdownJugador("b");

    $.each(lista_jugadores_b, function(index, jugador) {

        var li_jug_b = $('<li><a href="#">' + jugador[0] + '||' + jugador[2] + '||' + jugador[3] + '</a></li>').attr('value', jugador[0] + '||' + jugador[1] + '||' + jugador[3]);
        li_jug_b.click(function() {

            var jug = $(this).attr('value').split('||');

            $.getJSON("/jugador_iteractivo", {
                    nombre: jug[0],
                    fecha: jug[1],
                    equipo: jug[2],
                    ano: $("#iteractivo_jugador_temporada_b").val()
                })

                .done(function(json) {
                    $("#button_jugador_b").text(jugador[0] + '||' + jugador[2] + '||' + jugador[3]);
                    $("#button_jugador_b").append($('<span class="caret"></span>'));
                    console.log("JSON Data: " + json.nombre);
                    jugador_b = json;
                    printar_si_AB();
                })

                .fail(function(jqxhr, textStatus, error) {
                    var err = textStatus + ", " + error;
                    console.log("Request Failed: " + err);
                });


        });
        li_jug_b.appendTo(dropdown_jugador_b);

    });

})



function busquedaEnDropdownJugador(aOb) {
    $("#Input_jugador_" + aOb).on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".dropdown-menu li").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
}

$( document ).ready(function() {    
    $('#iteractivo_jugador_temporada_a').trigger("change");    
    $('#iteractivo_jugador_temporada_b').trigger("change");        
});



  </script>     
          <!-- page end-->
        </section>
      </section>
      <!--main content end-->
{% endblock%}
