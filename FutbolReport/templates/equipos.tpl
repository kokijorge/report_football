{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
      <section class="wrapper">
        <div class="row">
          <div class="col-lg-12">
            <h3 class="page-header"><i class="fa fa-table"></i> EQUIPOS</h3>
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
                      <th>Plantilla</th>
                      <th>Edad</th>
                      <th>Extranjeros</th>
                      <th>Valor_total</th>                      
                    </tr>
                  </thead>
                  <tbody>                    
                    {% for equipo in equipos %}                    
                    <tr>
                      <td> {{ equipo.5}} </td>
                      <td> {{ equipo.0}} </td>
                      <td> {{ equipo.1}} </td>
                      <td> {{ equipo.2}} </td>
                      <td> {{ equipo.3}} </td>
                      <td> {{ equipo.4}} </td>
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