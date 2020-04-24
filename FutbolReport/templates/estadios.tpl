{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
        <section class="wrapper">
          <div class="row">
            <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_house_alt"></i> ESTADIOS</h3>
            </div>
          </div>
          <!-- page start-->   
          <div>          
          <p>Clica en un estadio de españa:</p>
          <img src="/img/mapa_estadios.jpg" alt="Workplace" usemap="#workmap" width="700" height="490" style="float:left">
          <map name="workmap">          
          {% for estadio in estadios %} 
          <area shape="circle" coords="{{estadio.5}},{{ estadio.6}},5" href="javascript:estadio_seleccionado({{estadio.7}});">
          {% endfor%}           
          </map>
          <section class="panel">     
           <div class="table-condensed"   style="float:right" width="700" height="490">
              <table class="table">
                <thead>
                  <tr>                    
                    <th>#</th>
                    <th>Equipo</th> 
                    <th>Estadio</th>
                    <th>Ciudad</th>                     
                    <th>Capacidad</th>                    
                  </tr>
                </thead>
                <tbody>                        
                {% for estadio in estadios %}                                               
                  <tr id="{{estadio.7}}">
                    <td> {{ estadio.0}} </td>
                    <td> {{ estadio.1}} </td>
                    <td> {{ estadio.2}} </td>
                    <td> {{ estadio.3}} </td>              
                    <td> {{ estadio.4}} </td>
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