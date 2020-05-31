{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
        <section class="wrapper">
          <div class="row">
            <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_piechart"></i> INFORMES COMPLETOS</h3>
            </div>
          </div>
          <!-- page start-->
          <div class="row">
          <div id="btn_completo_jugador" class="btn_informe col-lg-3 col-md-3 col-sm-12 col-xs-12">
            <div class="info-box blue-bg">
              <i class="fa fa-cloud"></i>
              <div class="count">Jugador</div>              
            </div>            
          </div>          

          <div id="btn_completo_equipo" class="btn_informe col-lg-3 col-md-3 col-sm-12 col-xs-12">
            <div class="info-box brown-bg">
              <i class="fa fa-calendar"></i>
              <div class="count">Equipo</div>              
            </div>            
          </div>          

          <div id="btn_completo_entrenador" class="btn_informe col-lg-3 col-md-3 col-sm-12 col-xs-12">
            <div class="info-box dark-bg">
              <i class="fa fa-map-marker"></i>
              <div class="count">Entrenador</div>              
            </div>            
          </div>          
        </div>

        <div class="row">
        <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_piechart"></i> INFORMES INTERACTIVOS</h3>
            </div>
          <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
            <div class="info-box green-bg">
              <i class="fa fa-male"></i>
              <div class="count">Rival</div>              
              <a class="btn btn-default" href="javascript:informe_rival();">Entrenador</a>
            </div>            
          </div> 
          <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
            <div class="info-box green-bg">
              <i class="fa fa-male"></i>
              <div class="count">Rival</div>              
              <a class="btn btn-default" href="javascript:informe_rival();">Entrenador</a>
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
<script>
  $(".btn_informe").each(function(index,elem){
    $(elem).on("click", function(elem){
      window.location.href="/informes/"+$(this).attr('id').substr(4);
    })
  });
</script>        
          <!-- page end-->
        </section>
      </section>
      <!--main content end-->
{% endblock%}