{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
        <section class="wrapper">
          <div class="row">
            <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_desktop"></i> JUGADORES</h3>
              <ol class="breadcrumb">
                <li> {{ nuevo_equipo }} </li>
              </ol>
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
                <table class="table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Nombre</th>
                      <th>Fecha_nacimiento</th>
                      <th>Nacionalidad</th>
                      <th>Pie</th>
                      <th>Posicion</th>                   
                      <th>Valor_mercado</th>                     
                    </tr>
                  </thead>
                  <tbody>                    
                    {% for jugador in jugadores %}                    
                    <tr>
                      <td> {{ jugador.0}} </td>
                      <td> {{ jugador.1}} </td>
                      <td> {{ jugador.2}} </td>
                      <td> {{ jugador.3}} </td>
                      <td> {{ jugador.4}} </td>
                      <td> {{ jugador.5}} </td>
                      <td> {{ jugador.6}} </td>
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