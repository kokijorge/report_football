{% extends 'base.tpl' %}
{% block body%}    

<!--main content start-->
<section id="main-content">
    <section class="wrapper">
      <div class="row">
        <div class="col-lg-12">
          <h3 class="page-header"><i class="icon_genius"></i> TOP</h3>
        </div>
      </div>
      <!-- page start-->
      <div class="row">
        <div class="col-sm-6">
          <section class="panel">
            <header id="tabla_top" class="panel-heading">
              Máximas puntuacion de 1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
            </header>
            <div class="table-responsive">
              <table class="table">
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Nombre</th>
                    <th>Punt</th>                     
                  </tr>
                </thead>
                <tbody>                    
                  {% for punto in puntos %}                    
                  <tr>
                    <td> {{ punto.2}} </td>
                    <td> {{ punto.0}} </td>
                    <td> {{ punto.1}} </td>
                  </tr>
                  {% endfor%}
                </tbody>
              </table>
            </div>

          </section>
        </div>         
            <div class="col-sm-6">
              <section class="panel">
                <header class="panel-heading">
                    Máximos goleadores de 1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
                </header>
                <table class="table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Nombre</th>
                      <th>Goles</th>                      
                    </tr>
                  </thead>
                  <tbody>
                    {% for goleador in goleadores %}                    
                  <tr>
                    <td> {{ goleador.2}} </td>
                    <td> {{ goleador.0}} </td>
                    <td> {{ goleador.1}} </td>
                  </tr>
                  {% endfor%}
                  </tbody>
                </table>
              </section>
            </div>      
      <!-- page end-->
    </section>
  </section>
  <!--main content end-->

{% endblock%}