{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
        <section class="wrapper">
          <div class="row">
            <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_piechart"></i> INFORMES COMPLETO EQUIPO </h3>
            </div>
          </div>
          <!-- page start-->
          <div class="row"> 
          <ul class="nav pull-center top-menu">                    
              <li id="label_temporada" class="dropdown">
                <label for="labelTemporada" form style="width:100px">Seleccione temporada</label>       
              </li>
              <li class="dropdown">
                <select class="form-control" id="completo_equipo_temporada">
                  <option value="2016">2016/2017</option>
                  <option value="2017">2017/2018</option>
                  <option value="todo">Todas</option>
                </select>
              </li>
            </ul>
            <ul class="nav pull-center top-menu">                    
              <li id="label_equipo" class="dropdown">
                <label for="labelTemporada" form style="width:100px">Seleccione equipo</label>       
              </li>
              <li class="dropdown">
                <select class="form-control" id="completo_equipo_equipo">                                                     
                </select>
              </li>
            </ul>            
          </div>
          
        <div id="row_todo" style="display:none"  class="col-md-12">  
          <div class="row"> 
            <h3 id="text_total"> TOTAL </h3>    
          </div>
          <div class="row"> 
            <div id="table_div_equipo" class="col-md-12"></div>    
          </div >

          <div class="row"> 
            <h3 id="text_local"> LOCAL </h3>    
          </div>
          <div class="row"> 
            <div id="table_div_local" class="col-md-12"></div>   
          </div >

          <div class="row"> 
            <h3 id="text_visitante"> VISITANTE </h3>    
          </div>
          <div class="row"> 
            <div id="table_div_visitante" class="col-md-12"></div>  
          </div > 
        </div>
          <div class="row"> 
            <div class="col-md-12" id="columnchart_values_equipo" style="width: 900px; height: 300px;"></div> 
          </div>  

          <div class="row">     
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">    
            <div id="columnchart_mejor" style="width: 500px; height: 300px;"></div>         
            </div> 
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">    
            <div id="columnchart_peor" style="width: 500px; height: 300px;"></div>         
            </div>           
          </div> 

          <script type="text/javascript" src="/js/charts_google.js"></script>
          <script>
          
          google.charts.load("current", {packages:["corechart"]});
          var anos_equipos_select = {{anos_equipos_select}};

          var select_temporada= $('#completo_equipo_temporada');
          var select_equipo= $('#completo_equipo_equipo');

          select_temporada.on('change', function() {
  
            select_equipo.empty();            
            var lista_equipos= anos_equipos_select[select_temporada.val()];


            $.each(lista_equipos, function( index, equipo ) {            
              $('<option>')
                .attr('value', equipo[0])
                .text( equipo[0])
                .appendTo(select_equipo);              
            });                  
          })

$( document ).ready(function() {    
  $('#completo_equipo_temporada').trigger("change");    
});

    select_equipo.on('change', function() {
    
    $.getJSON( "/equipo_completo", { nombre: this.value,  ano: $("#completo_equipo_temporada").val() })
  
      .done(function( json ) {

        console.log( "JSON Data: " + json.equipo + json.ano );
        // tabla con toda la informacion
        google.charts.load('current', {'packages':['table']});
        google.charts.setOnLoadCallback(drawTable);
        function drawTable() {
          var data_info = new google.visualization.DataTable();
          data_info.addColumn('number', 'Empates');
          data_info.addColumn('number', 'Victorias');
          data_info.addColumn('number', 'Derrotas');
          data_info.addColumn('number', 'Goles a favor');
          data_info.addColumn('number', 'Goles en contra');
          data_info.addColumn('number', 'Puntos'); 
          data_info.addRows( json.puntuaciones_equipo_global );
          var options_info = {showRowNumber: true, width: '100%', height: '100%'};
          var table_info = new google.visualization.Table(document.getElementById('table_div_equipo'));
          table_info.draw(data_info,options_info ); 
        }

        $("#row_todo").show(); //mostrar todo lo oculta una vez que seleccionamos la temporada y el equipo

        // tabla local        
        google.charts.load('current', {'packages':['table']});
        google.charts.setOnLoadCallback(drawTableLocal);
        function drawTableLocal() {
          var data_info_local = new google.visualization.DataTable();
          data_info_local.addColumn('number', 'Empates');
          data_info_local.addColumn('number', 'Victorias');
          data_info_local.addColumn('number', 'Derrotas');
          data_info_local.addColumn('number', 'Goles a favor');
          data_info_local.addColumn('number', 'Goles en contra');
          data_info_local.addColumn('number', 'Puntos'); 
          data_info_local.addRows( json.puntuaciones_equipo_local );
          var options_info_local = {showRowNumber: true, width: '100%', height: '100%'};
          var table_info_local = new google.visualization.Table(document.getElementById('table_div_local'));
          table_info_local.draw(data_info_local,options_info_local ); 
        }

        // tabla visitante        
        google.charts.load('current', {'packages':['table']});
        google.charts.setOnLoadCallback(drawTableVisitante);
        function drawTableVisitante() {
          var data_info_visitante = new google.visualization.DataTable();
          data_info_visitante.addColumn('number', 'Empates');
          data_info_visitante.addColumn('number', 'Victorias');
          data_info_visitante.addColumn('number', 'Derrotas');
          data_info_visitante.addColumn('number', 'Goles a favor');
          data_info_visitante.addColumn('number', 'Goles en contra');
          data_info_visitante.addColumn('number', 'Puntos'); 
          data_info_visitante.addRows( json.puntuaciones_equipo_visitante );
          var options_info_visitante = {showRowNumber: true, width: '100%', height: '100%'};
          var table_info_visitante = new google.visualization.Table(document.getElementById('table_div_visitante'));
          table_info_visitante.draw(data_info_visitante,options_info_visitante ); 
        }

        //<!-- puntuaciones estacion año-->              
        var data_estacion_ano = new google.visualization.DataTable();
        data_estacion_ano.addColumn('string', 'Estacion del año');
        data_estacion_ano.addColumn('number', 'Puntos');    
        data_estacion_ano.addRows(json.puntuaciones_equipo_estacion); 
        var options_estacion_ano = {
          title: "Informe en función de la estación del año",
          width: 900,
          height: 300,
          bar: {groupWidth: "95%"},
          legend: { position: "none" },
        };
        var chart_estacion_ano = new google.visualization.ColumnChart(document.getElementById("columnchart_values_equipo"));
        chart_estacion_ano.draw(data_estacion_ano, options_estacion_ano);

        //<!-- goles favor-->         
        var data_mejor= new google.visualization.DataTable();
        data_mejor.addColumn('string', 'Equipo');
        data_mejor.addColumn('number', 'Goles');    
        data_mejor.addRows(json.puntuaciones_equipo_mejor); 
        var options_mejor = {
          title: "Equipos a los que más goles se le encajó",
          width: 500,
          height: 300,
          bar: {groupWidth: "95%"},
          legend: { position: "none" },
        };
        var chart_viento = new google.visualization.ColumnChart(document.getElementById("columnchart_mejor"));
        chart_viento.draw(data_mejor, options_mejor);

        //<!-- goles contra-->         
        var data_peor= new google.visualization.DataTable();
        data_peor.addColumn('string', 'Equipo');
        data_peor.addColumn('number', 'Goles');    
        data_peor.addRows(json.puntuaciones_equipo_peor); 
        var options_peor = {
          title: "Equipos que más goles le metieron",
          width: 500,
          height: 300,
          bar: {groupWidth: "95%"},
          legend: { position: "none" },
        };
        var chart_viento = new google.visualization.ColumnChart(document.getElementById("columnchart_peor"));
        chart_viento.draw(data_peor, options_peor); 

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