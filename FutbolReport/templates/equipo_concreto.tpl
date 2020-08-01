{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start--> 
    <section id="main-content">
      <section class="wrapper">
        <div class="row">
          <div class="col-lg-4">
            <h3 class="page-header"><i class="fas fa-user-friends"></i> EQUIPO CONCRETO</h3>
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
                      <th>Puntuación total</th>
                      <th>Titularidades</th>
                      <th>Tarjetas amarillas</th>
                      <th>Tarjetas rojas</th>                   
                      <th>Minutos jugados</th>
                      <th>Goles</th>                                        
                    </tr>
                  </thead>
                  <tbody>                    
                    {% for equ in equipo_concreto %}                    
                    <tr>                      
                      <td> {{ equ.1}} </td>
                      <td> {{ equ.2}} </td>
                      <td> {{ equ.3}} </td>
                      <td> {{ equ.4}} </td>
                      <td> {{ equ.5}} </td>
                      <td> {{ equ.6}} </td>
                      <td> {{ equ.7}} </td>
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