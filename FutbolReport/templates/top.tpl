{% extends 'base.tpl' %}
{% block body%}    

<!--main content start-->
<section id="main-content">
    <section class="wrapper">
      <div class="row">
        <div class="col-lg-4">
          <h3 class="page-header"><i class="icon_genius"></i> TOP</h3>
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
                    <th>Nacionalidad</th>                  
                    <th>Posición</th>
                    <th>Puntuación</th>
                  </tr>
                </thead>
                <tbody>                    
                  {% for punto in puntos %}                    
                  <tr>
                    <td> {{ punto.5}} </td>                    
                    <td> {{ punto.0}} </td>                                           
                    <td> {{ punto.1}} </td>
                    <td> {{ punto.2}} </td>
                    <td> {{ punto.3}} </td>
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
                      <th>Nacionalidad</th>                  
                      <th>Posición</th>
                      <th>Goles</th>                  
                    </tr>
                  </thead>
                  <tbody>
                    {% for goleador in goleadores %}                    
                  <tr>
                    <td> {{ goleador.5}} </td>
                    <td> {{ goleador.0}} </td>
                    <td> {{ goleador.1}} </td>
                    <td> {{ goleador.2}} </td>
                    <td> {{ goleador.3}} </td>
                  </tr>
                  {% endfor%}
                  </tbody>
                </table>
              </section>
            </div>  
            <div class="col-sm-6">
              <section class="panel">
                <header class="panel-heading">
                    Jugadores con más amarillas de 1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
                </header>
                <table class="table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Nombre</th>                      
                      <th>Nacionalidad</th>                  
                      <th>Posicion</th>
                      <th>Tarjetas amarillas</th>                  
                    </tr>
                  </thead>
                  <tbody>
                    {% for amarilla in amarillas %}                    
                  <tr>
                    <td> {{ amarilla.5}} </td>
                    <td> {{ amarilla.0}} </td>
                    <td> {{ amarilla.1}} </td>
                    <td> {{ amarilla.2}} </td>
                    <td> {{ amarilla.3}} </td>
                  </tr>
                  {% endfor%}
                  </tbody>
                </table>
              </section>
            </div>
            <div class="col-sm-6">
              <section class="panel">
                <header class="panel-heading">
                    Jugadores con más rojas de 1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
                </header>
                <table class="table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Nombre</th>                      
                      <th>Nacionalidad</th>                  
                      <th>Posición</th>
                      <th>Tarjetas rojas</th>                  
                    </tr>
                  </thead>
                  <tbody>
                    {% for roja in rojas %}                    
                  <tr>
                    <td> {{ roja.5}} </td>
                    <td> {{ roja.0}} </td>
                    <td> {{ roja.1}} </td>
                    <td> {{ roja.2}} </td>
                    <td> {{ roja.3}} </td>
                  </tr>
                  {% endfor%}
                  </tbody>
                </table>
              </section>
            </div>
            <div class="col-sm-6">
              <section class="panel">
                <header class="panel-heading">
                    Jugadores con más minutos de 1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
                </header>
                <table class="table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Nombre</th>                      
                      <th>Nacionalidad</th>                  
                      <th>Posición</th>
                      <th>Minutos</th>                  
                    </tr>
                  </thead>
                  <tbody>
                    {% for minuto in minutos %}                    
                  <tr>
                    <td> {{ minuto.5}} </td>
                    <td> {{ minuto.0}} </td>
                    <td> {{ minuto.1}} </td>
                    <td> {{ minuto.2}} </td>
                    <td> {{ minuto.3}} </td>
                  </tr>
                  {% endfor%}
                  </tbody>
                </table>
              </section>
            </div>
            <div class="col-sm-6">
              <section class="panel">
                <header class="panel-heading">
                    Jugadores con más titularidades de 1ª División Temporada {{ temporada_seleccionada }}/{{ temp }} 
                </header>
                <table class="table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Nombre</th>                      
                      <th>Nacionalidad</th>                  
                      <th>Posición</th>
                      <th>Titularidades</th>                  
                    </tr>
                  </thead>
                  <tbody>
                    {% for titular in titularidades %}                    
                  <tr>
                    <td> {{ titular.5}} </td>
                    <td> {{ titular.0}} </td>
                    <td> {{ titular.1}} </td>
                    <td> {{ titular.2}} </td>
                    <td> {{ titular.3}} </td>
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