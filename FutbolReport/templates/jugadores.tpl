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
                      <th>Dorsal</th>
                      <th>Nacionalidad</th>
                      <th>Club_actual</th>
                      <th>Altura</th>                   
                      <th>Pie</th>
                      <th>Fichado_desde</th>
                      <th>Club_anterior</th>
                      <th>Contrato_hasta</th>
                      <th>Valor_mercado</th>
                      <th>Fecha_nacimiento</th>                      
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
                      <td> {{ jugador.7}} </td>
                      <td> {{ jugador.8}} </td>
                      <td> {{ jugador.9}} </td>
                      <td> {{ jugador.10}} </td>
                      <td> {{ jugador.11}} </td>
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