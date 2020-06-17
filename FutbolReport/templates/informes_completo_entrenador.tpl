{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
        <section class="wrapper">
          <div class="row">
            <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_piechart"></i> INFORMES COMPLETO ENTRENADOR </h3>
            </div>
          </div>
          <!-- page start-->
          <div class="row"> 
          <ul class="nav pull-center top-menu">                    
              <li id="label_temporada" class="dropdown">
                <label for="labelTemporada" form style="width:100px">Seleccione temporada</label>       
              </li>
              <li class="dropdown">
                <select class="form-control" id="completo_entrenador_temporada">
                  <option value="2016">2016/2017</option>
                  <option value="2017">2017/2018</option>
                  <option value="todo">Todas</option>
                </select>
              </li>
            </ul>
            <ul class="nav pull-center top-menu">                    
              <li id="label_entrenador" class="dropdown">
                <label for="labelTemporada" form style="width:100px">Seleccione entrenador</label>       
              </li>
              <li class="dropdown">
                <select class="form-control" id="completo_entrenador_entrenador">                                                     
                </select>
              </li>
            </ul>            
            <div class="ui-widget">
              <label for="tags">Tags: </label>
              <input id="tags_entrenador">
            </div>
          </div>

          <script>
          
          var anos_entrenadores_select = {{anos_entrenadores_select}};

          var select_temporada= $('#completo_entrenador_temporada');
          var select_entrenador= $('#completo_entrenador_entrenador');
          var tag_entrenador= $('#tags_entrenador');

          select_temporada.on('change', function() {
  
            select_entrenador.empty();
            tag_entrenador.empty();
            var lista_entrenadores= anos_entrenadores_select[select_temporada.val()];
            var availableTags = [];    

            $.each(lista_entrenadores, function( index, entrenador ) {            
              $('<option>')
                .attr('value', entrenador[0])
                .text( entrenador[0])
                .appendTo(select_entrenador);

              availableTags.push(entrenador[0]);
              $( "#tags_entrenador" ).autocomplete({
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