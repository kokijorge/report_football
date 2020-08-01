{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
    <section class="wrapper">
      <div class="row">
        <div class="col-lg-4">
          <h3 class="page-header"><i class="icon_documents_alt"></i> ENTRENADORES</h3> 
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
              <header id="tabla_entrenadores" class="panel-heading">
                1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
              </header>
              <div class="table-responsive">
                <table id="id_entrenador" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Equipo</th>
                      <th>Nombre</th>
                      <th>Año debut</th>
                      <th>Fecha nacimiento</th>
                      <th>Nacionalidad</th>                      
                    </tr>
                  </thead>
                  <tbody>                    
                    {% for entrenador in entrenadores %}                    
                    <tr data="{{entrenador.2}}">
                      <td> {{ entrenador.0}} </td>                      
                      <td> {{ entrenador.1}} </td>
                      <td> {{ entrenador.2}} </td>
                      <td> {{ entrenador.3}} </td>
                      <td> {{ entrenador.4}} </td>
                      <td> {{ entrenador.5}} </td>
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
        $('#id_entrenador').DataTable({
            "aaSorting": [],
            columnDefs: [{
            orderable: false,
            targets: 0
            }]
          });
          $('.dataTables_length').addClass('bs-select');          
        });       
      $("#id_entrenador>tbody>tr").click(function(){          
          window.location.href= window.location.href+'/'+$(this).attr("data") ;
          })         
      </script>
{% endblock%}