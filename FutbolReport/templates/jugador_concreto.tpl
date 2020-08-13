{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start--> 
    <section id="main-content">
      <section class="wrapper">
        <div class="row">
          <div class="col-lg-4">
            <h3 class="page-header"><i class="fas fa-running"></i> {{ jugadores.0.0}}</h3>
          </div>
        </div>
       <!-- page start-->
          <div class="row">
          <div class="col-lg-12">
            <section class="panel">
              <header id="tabla_partidos" class="panel-heading">
                1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
              </header>
              <div class="table-responsive">
                <table id="id_jugador" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%">                
                  <thead>
                    <tr>                      
                      <th>Nombre</th>
                      <th>Equipo</th>
                      <th>Equipo Rival</th>
                      <th>Puntuación</th>
                      <th>Titular</th>                   
                      <th>Es Local</th>
                      <th>Tarjeta amarilla</th>                  
                      <th>Tarjeta roja</th>
                      <th>Minutos jugados</th>
                      <th>Goles</th>
                    </tr>
                  </thead>
                  <tbody>                    
                    {% for jugador in jugadores %}                    
                    <tr>
                      <td> {{ jugador.0}} </td>                      
                      <td> <a href="/equipos/{{temporada_seleccionada}}/{{ jugador.1}}"> {{ jugador.1}} </a> </td>                                                   
                      <td> <a href="/equipos/{{temporada_seleccionada}}/{{ jugador.2}}"> {{ jugador.2}} </a> </td>                                                                         
                      <td> {{ jugador.3}} </td>
                      <td> {{ jugador.4}} </td>
                      <td> {{ jugador.5}} </td>
                      <td> {{ jugador.6}} </td>
                      <td> {{ jugador.7}} </td>
                      <td> {{ jugador.8}} </td>                      
                      <td> {{ jugador.9}} </td>
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
        $('#id_jugador').DataTable({
            "aaSorting": []
          });
          $('.dataTables_length').addClass('bs-select');          
        });                  
      </script>
{% endblock%}