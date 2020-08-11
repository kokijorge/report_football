{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start--> 
    <section id="main-content">
      <section class="wrapper">
        <div class="row">
          <div class="col-lg-4">
            <h3 class="page-header"><i class="fa fa-table"></i>  {{ info_partidos.2}} {{ info_partidos.3}} - {{ info_partidos.4}} {{ info_partidos.1}}</h3> <!-- meter todo-->
          </div>    
          <div class="col-lg-4">
            <h3 class="page-header">  Campo: {{ info_partidos.0}}
          </div>      
          <div class="col-lg-4">
            <h3 class="page-header">  1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
          </div>   
        </div>
       <!-- page start-->
          <div class="row">
          <div class="col-lg-12">
            <section class="panel">
              <header id="tabla_partidos" class="panel-heading">                 
                Entrenador local: {{ info_partidos.5}}
                Entrenador visitante: {{ info_partidos.6}}
                Temperatura: {{ info_partidos.7}}
                LLuvias: {{ info_partidos.8}}
                Humedad: {{ info_partidos.9}}
                Velocidad del viento: {{ info_partidos.10}}
              </header>
              <div class="table-responsive">
                <table id="id_partidos" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%">                
                  <thead>
                    <tr>                      
                      <th>Nombre</th>
                      <th>Posicion</th>
                      <th>Equipo</th>
                      <th>Puntuación</th>
                      <th>Titular</th>                   
                      <th>Tarjeta amarilla</th>                  
                      <th>Tarjeta roja</th>
                      <th>Minutos jugados</th>
                      <th>Goles</th>
                    </tr>
                  </thead>
                  <tbody>                    
                    {% for partido in partidos %}                    
                    <tr>
                      <td> {{ partido.0}} </td>
                      <td> {{ partido.1}} </td>
                      <td> {{ partido.2}} </td>
                      <td> {{ partido.3}} </td>
                      <td> {{ partido.4}} </td>
                      <td> {{ partido.5}} </td>
                      <td> {{ partido.6}} </td>
                      <td> {{ partido.7}} </td>
                      <td> {{ partido.8}} </td>                      
                    </tr>
                    {% endfor%}
                  </tbody>
                </table>
              </div>
            </section>
          </div>       
        <!-- page end-->
      </section>
    </section>
      <!--main content end-->
      <script>
      $(document).ready(function () {
        $('#id_partidos').DataTable({
            "aaSorting": []
          });
          $('.dataTables_length').addClass('bs-select');          
        });                
      </script>
{% endblock%}