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
          <h2>Image Maps</h2>
          <p>Clica en la taza de tee para ir a la jornada 1 del 2016:</p>
            <img src="/img/mapa_espana.jpg" alt="Workplace" usemap="#workmap" width="830" height="582">
          <map name="workmap">
            <area shape="circle" coords="3,3,44" alt="Cup of coffee" href="http://localhost:8000/jornadas/1/2016">
          </map>
          <!-- page end-->
        </section>
      </section>
      <!--main content end-->
{% endblock%}