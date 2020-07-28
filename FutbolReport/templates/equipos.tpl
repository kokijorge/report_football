{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
    <section class="wrapper">
      <div class="row">
        <div class="col-lg-4">
          <h3 class="page-header"><i class="fas fa-user-friends"></i> EQUIPOS</h3>  
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
              <header id="tabla_equipos" class="panel-heading">
                1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
              </header>
              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Nombre</th>
                      <th>Año_fundacion</th>                                 
                      <th>Ciudad</th>                      
                    </tr>
                  </thead>
                  <tbody>                    
                    {% for equipo in equipos %}                    
                    <tr>                      
                      <td> {{ equipo.0}} </td>                      
                      <td> {{ equipo.1}} </td>
                      <td> {{ equipo.2}} </td>
                      <td> {{ equipo.3}} </td>                      
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
{% endblock%}