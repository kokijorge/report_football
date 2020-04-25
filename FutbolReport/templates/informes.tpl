{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
        <section class="wrapper">
          <div class="row">
            <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_piechart"></i> INFORMES</h3>
            </div>
          </div>
          <!-- page start-->
          <div class="row">
          <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
            <div class="info-box blue-bg">
              <i class="fa fa-cloud"></i>
              <div class="count">Tiempo</div>              
              <a class="btn btn-default" href="javascript:informe_tiempo();">Temperatura</a>
            </div>            
          </div>          

          <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
            <div class="info-box brown-bg">
              <i class="fa fa-calendar"></i>
              <div class="count">Fecha</div>              
              <a class="btn btn-default" href="javascript:informe_fecha();">Semana del año</a>
            </div>            
          </div>          

          <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
            <div class="info-box dark-bg">
              <i class="fa fa-map-marker"></i>
              <div class="count">Mapa</div>              
              <a class="btn btn-default" href="javascript:informe_mapa();">Estadio</a>
            </div>            
          </div>          

          <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
            <div class="info-box green-bg">
              <i class="fa fa-male"></i>
              <div class="count">Rival</div>              
              <a class="btn btn-default" href="javascript:informe_rival();">Entrenador</a>
            </div>            
          </div>          
        </div>

        
          <!-- page end-->
        </section>
      </section>
      <!--main content end-->
{% endblock%}