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
             <table class="table" id="tabla_partidos" >
                  <thead>
                    <tr>
                      <th>Entrenador local</th>
                      <th>Entrenador visitante</th>                      
                      <th>Temperatura</th>                  
                      <th>LLuvias</th>
                      <th>Humedad</th>                  
                      <th>Velocidad del viento</th>   
                    </tr>
                  </thead>
                  <tbody>                                      
                  <tr>                    
                    <td> <a href="/entrenadores/{{temporada_seleccionada}}/{{ info_partidos.5}}"> {{ info_partidos.5}} </a> </td> 
                    <td> <a href="/entrenadores/{{temporada_seleccionada}}/{{ info_partidos.6}}"> {{ info_partidos.6}} </a> </td>                     
                    <td> {{ info_partidos.7}} </td>
                    <td> {{ info_partidos.8}} </td>
                    <td> {{ info_partidos.9}} </td>
                    <td> {{ info_partidos.10}} </td>
                  </tr>                  
                  </tbody>
              </table>
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
                      <td> <a href="/jugadores/{{temporada_seleccionada}}/{{ partido.9}}"> {{ partido.0}} </a> </td>                                    
                      <td> {{ partido.1}} </td>                      
                      <td> <a href="/equipos/{{temporada_seleccionada}}/{{ partido.2}}"> {{ partido.2}} </a> </td>                                                   
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