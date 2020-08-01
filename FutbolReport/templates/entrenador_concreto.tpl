{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start--> 
    <section id="main-content">
      <section class="wrapper">
        <div class="row">
          <div class="col-lg-4">
            <h3 class="page-header"><i class="icon_documents_alt"></i> ENTRENADOR CONCRETO</h3>
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
                <table id="id_entrenador_concreto" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%">                
                  <thead>
                    <tr>                      
                      <th>Nombre</th>
                      <th>Equipo</th>
                      <th>Entrenador Rival</th>
                      <th>Equipo Rival</th>                                    
                      <th>Goles a favor</th>
                      <th>Goles en contra</th>
                      <th>Es Local</th>
                      <th>Puntuaciones</th>
                      <th>Amarillas</th>                  
                      <th>Rojas</th>                                            
                    </tr>
                  </thead>
                  <tbody>                    
                    {% for entr in entrenador_concreto %}                    
                    <tr>
                      <td> {{ entr.0}} </td>
                      <td> {{ entr.1}} </td>
                      <td> {{ entr.2}} </td>
                      <td> {{ entr.3}} </td>
                      <td> {{ entr.4}} </td>
                      <td> {{ entr.5}} </td>
                      <td> {{ entr.6}} </td>
                      <td> {{ entr.7}} </td>
                      <td> {{ entr.8}} </td>                      
                      <td> {{ entr.9}} </td>
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
        $('#id_entrenador_concreto').DataTable({
            "aaSorting": []
          });
          $('.dataTables_length').addClass('bs-select');          
        });                  
      </script>
{% endblock%}