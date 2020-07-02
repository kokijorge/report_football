{% extends 'base.tpl' %}
{% block body%}    
    <!--main content start-->
    <section id="main-content">
        <section class="wrapper">          
          <div class="row">
            <div class="col-lg-12">
              <h3 class="page-header"><i class="icon_piechart"></i> INFORMES ITERACTIVO ENTRENADOR</h3>
            </div>
          </div>
          
          <!-- page start--> 
          <div class="row"> 
          <ul class="nav pull-center top-menu">                    
              <li id="label_temporada" class="dropdown">
                <label for="labelTemporada" form style="width:100px">Seleccione temporada</label>       
              </li>
              <li class="dropdown">
                <select class="form-control" id="completo_jugador_temporada">
                  <option value="2016">2016/2017</option>
                  <option value="2017">2017/2018</option>
                  <option value="todo">Todas</option>
                </select>
              </li>
            </ul>
            <ul class="nav pull-center top-menu">                    
              <li id="label_jugador" class="dropdown">
                <label for="labelTemporada" form style="width:100px">Seleccione jugador</label>       
              </li>
              <li class="dropdown">
                <select class="form-control" id="completo_jugador_jugador">                                                     
                </select>
              </li>
            </ul>          

<script type="text/javascript" src="/js/charts_google.js"></script>
<script>


});                   
        </script>     
          <!-- page end-->
        </section>
      </section>
      <!--main content end-->
{% endblock%}
