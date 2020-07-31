{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start--> 
    <section id="main-content">
    <section class="wrapper">
      <div class="row">
        <div class="col-lg-4">
          <h3 class="page-header"><i class="fa fa-table"></i> JORNADAS</h3>
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
          <ul class="nav pull-center top-menu">                    
            <li id="label_jornada" class="dropdown">
              <label for="label_jornada" form style="width:100px">Seleccione jornada</label>       
            </li>
            <li class="dropdown">
              <select class="form-control" id="select_jornada">
                {% for jornada in num_jornadas %} 
                <option id='valor_jornada'> {{ jornada.0}} </option>                                
                {% endfor%}
              </select>
            </li>
          </ul>
          <div class="row">
            <div class="col-lg-12">
              <section class="panel">
                <header id="tabla_jornadas" class="panel-heading">
                  1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
                </header>
                <div class="table-responsive">                  
                  <table id="selectedColumn" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%">
                    <thead>
                      <tr>
                        <th>Más Info</th>
                        <th>Equipo local</th>
                        <th>Resultado local</th>
                        <th>Equipo visitante</th>
                        <th>Resultado visitante</th>
                        <th>Fecha</th>
                        <th>Hora</th>                        
                      </tr>                      
                    </thead>
                    <tbody>                    
                      {% for jornada in jornadas %}                    
                      <tr data="{{jornada.7}}">                        
                        <td> <a class="sort-link" href="www.google.es">#</a> </td>
                        <td> {{ jornada.1}} </td>
                        <td> {{ jornada.2}} </td>
                        <td> {{ jornada.3}} </td>
                        <td> {{ jornada.4}} </td>
                        <td> {{ jornada.5}} </td>
                        <td> {{ jornada.6}} </td>
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
        $('#selectedColumn').DataTable({
            "aaSorting": [],
            columnDefs: [{
            orderable: false,
            targets: 0
            }]
          });
          $('.dataTables_length').addClass('bs-select');          
        });        
        $("#selectedColumn>tbody>tr").click(function(){          
          window.location.href= window.location.href+'/'+$(this).attr("data") ;
          })
      </script>
{% endblock%}