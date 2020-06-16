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
            <div class="ui-widget">
              <label for="tags">Tags: </label>
              <input id="tags_equipo">
            </div>
          </div>

          <script>
          
          var anos_equipos_select = {{anos_equipos_select}};

          var select_temporada= $('#completo_equipo_temporada');
          var select_equipo= $('#completo_equipo_equipo');
          var tag_equipo= $('#tags_equipo');

          select_temporada.on('change', function() {
  
            select_equipo.empty();
            tag_equipo.empty();
            var lista_equipos= anos_equipos_select[select_temporada.val()];
            var availableTags = [];    

            $.each(lista_equipos, function( index, equipo ) {            
              $('<option>')
                .attr('value', equipo[0])
                .text( equipo[0])
                .appendTo(select_equipo);

              availableTags.push(equipo[0]);
              $( "#tags_equipo" ).autocomplete({
                  source: availableTags
              }); 
            });                  
          })

          </script>

          <!-- page end-->
        </section>
      </section>
      <!--main content end-->
{% endblock%}