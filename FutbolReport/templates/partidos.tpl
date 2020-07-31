{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start--> 
    <section id="main-content">
      <section class="wrapper">
        <div class="row">
          <div class="col-lg-4">
            <h3 class="page-header"><i class="fa fa-table"></i>  {{ info_partidos}}</h3>
          </div>
          <div class="col-lg-4">
            <h3 class="page-header"><i class="fa fa-table"></i> PARTIDOS</h3>
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