{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start--> 
  <section id="main-content">
    <section class="wrapper">
      <div class="row">
        <div class="col-lg-4">
          <h3 class="page-header"><i class="fas fa-running"></i> JUGADORES</h3>
        </div>
        <div class="pull-right">
          <ul class="nav pull-right top-menu">                    
              <li id="label_temporada" class="dropdown">
                <label for="labelTemporada" form style="width:100px">Seleccione temporada</label>       
              </li>
              <li class="dropdown">
                <select class="form-control" id="select_temporada">
                  <option value="2016">2016/2017</option>
                  <option value="2017">2017/2018</option>
                </select>
              </li>
          </ul>
        </div>
      </div>
          <!-- page start-->
          <div class="row">
          <div class="col-lg-12">
            <section class="panel">
              <header id="tabla_jugadores" class="panel-heading">
                1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
              </header>
              <div class="table-responsive">                
                <table id="id_jugadores" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%">                
                  <thead>
                    <tr>                      
                      <th>Nombre</th>
                      <th>Fecha nacimiento</th>
                      <th>Nacionalidad</th>
                      <th>Pie</th>
                      <th>Posición</th>                   
                      <th>Altura</th>                  
                      <th>Inicio contrato</th>
                      <th>Fin contrato</th>
                      <th>Equipo</th>
                    </tr>
                  </thead>
                  <tbody>                    
                    {% for jugador in jugadores %}                    
                    <tr data="{{jugador.10}}"> 
                      <td> <a href="/jugadores/{{temporada_seleccionada}}/{{ jugador.10}}"> {{ jugador.1}} </a> </td>                                           
                      <td> {{ jugador.2}} </td>
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
        $('#id_jugadores').DataTable({
            "aaSorting": [],
            columnDefs: [{                        
            }]
          });
          $('.dataTables_length').addClass('bs-select');          
        });       
      $(".mas_info_button").click(function(){                        
              window.location.href= window.location.href+'/'+$(this).parent().parent().attr("data") ;
            });       
      </script>
{% endblock%}