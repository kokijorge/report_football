<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Creative - Bootstrap 3 Responsive Admin Template">
  <meta name="author" content="GeeksLabs">
  <meta name="keyword" content="Creative, Dashboard, Admin, Template, Theme, Bootstrap, Responsive, Retina, Minimal">

  <title>Creative - Bootstrap Admin Template</title>

  <!-- Bootstrap CSS -->
  <link href="/css/bootstrap.min.css" rel="stylesheet">
  <!-- bootstrap theme -->
  <link href="/css/bootstrap-theme.css" rel="stylesheet">
  <!--external css-->
  <!-- font icon -->
  <link href="/css/elegant-icons-style.css" rel="stylesheet" />
  <link href="/css/font-awesome.min.css" rel="stylesheet" />
  <!-- full calendar css-->
  <link href="/assets/fullcalendar/fullcalendar/bootstrap-fullcalendar.css" rel="stylesheet" />
  <link href="/assets/fullcalendar/fullcalendar/fullcalendar.css" rel="stylesheet" />
  <!-- easy pie chart-->
  <link href="/assets/jquery-easy-pie-chart/jquery.easy-pie-chart.css" rel="stylesheet" type="text/css" media="screen" />
  <!-- owl carousel -->
  <link rel="stylesheet" href="/css/owl.carousel.css" type="text/css">
  <link href="/css/jquery-jvectormap-1.2.2.css" rel="stylesheet">
  <!-- Custom styles -->
  <link rel="stylesheet" href="/css/fullcalendar.css">
  <link href="/css/widgets.css" rel="stylesheet">
  <link href="/css/style.css" rel="stylesheet">
  <link href="/css/style-responsive.css" rel="stylesheet" />
  <link href="/css/xcharts.min.css" rel=" stylesheet">
  <link href="/css/jquery-ui-1.10.4.min.css" rel="stylesheet">
  <!-- =======================================================
    Theme Name: NiceAdmin
    Theme URL: https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/
    Author: BootstrapMade
    Author URL: https://bootstrapmade.com
  ======================================================= -->
  <script src="/js/jquery.js"></script> 1.10.2
  
  <!--script src="/js/jquery-1.8.3.min.js"></script-->

  <!--script src="/js/jquery-ui-1.10.4.min.js"></script-->

  <script type="text/javascript" src="/js/jquery-ui-1.9.2.custom.min.js"></script>

</head>

<body>
  <!-- container section start -->
  <section id="container" class="">
    <header class="header dark-bg">
        <div class="toggle-nav">
            <div class="icon-reorder tooltips" data-original-title="Toggle Navigation" data-placement="bottom"><i class="icon_menu"></i></div>
          </div>
    
          <!--logo start-->
          <a href="http://localhost:8000/" class="logo">Futbol <span class="lite">Report</span></a>          
          <!--logo end-->            
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
    </header>
    <!--header end-->

    <!--sidebar mroustart-->
    <aside>
      <div id="sidebar" class="nav-collapse " style="overflow: scroll;">
            <!-- sidebar menu start-->
            <ul class="sidebar-menu">
              <li class="">
                <a href="javascript:escoger_estadio();" class="">
                              <i class="icon_house_alt"></i>
                              <span>Estadios</span>
                          </a>
              </li>
              <li class="sub-menu">
                <a  class="">
                              <i class="icon_desktop"></i>
                              <span>Jugadores</span>
                              <span class="menu-arrow arrow_carrot-right"></span>
                          </a>
                <ul id="ul_equipo" class="sub">
                {% for equipo in equipos_jugadores %}                    
                  <li><a  class="" href="javascript:escoger_jugador('{{equipo.0}}');">{{ equipo.0}} </a></li>                
                {% endfor%}
                </ul>                
              </li>
              <li class="sub-menu">               
                <a href="javascript:top_menu();" class="">
                              <i class="icon_genius"></i>
                              <span>Top</span>
                          </a>
              </li>
              <li class="sub-menu">
                <a href="javascript:escoger_informe();" class="">
                              <i class="icon_piechart"></i>
                              <span>Informes</span>
                          </a>
              </li>
    
              <li class="sub-menu">
                <a href="javascript:escoger_equipo();" class="">
                              <i class="icon_table"></i>
                              <span>Equipos</span>                          
                          </a>            
              </li>
    
              <li class="sub-menu">
                <a href="javascript:escoger_entrenador();" class="">
                              <i class="icon_documents_alt"></i>
                              <span>Entrenadores</span>                          
                          </a>
              </li>
    
              <li class="sub-menu">
                <a href="javascript:escoger_jornadas();" class="">
                              <i class="icon_table"></i>
                              <span>Jornadas</span>                          
                          </a>
              </li>
    
            </ul>
            <!-- sidebar menu end-->
          </div>
    </aside>
    <!--sidebar end-->

    <!--main content start-->
    {% block body%}
	{% endblock%}
    <!--main content end-->
  </section>
  <!-- container section start -->

  <!-- javascripts -->

  <script>
    {% include 'main.js' %} 
  </script>
 
  <!-- bootstrap -->
  <script src="/js/bootstrap.min.js"></script>
  <!-- nice scroll -->
  <script src="/js/jquery.scrollTo.min.js"></script>
  <!--<script src="/js/jquery.nicescroll.js" type="text/javascript"></script>-->
  <!-- charts scripts -->
  <script src="/assets/jquery-knob/js/jquery.knob.js"></script>
  <script src="/js/jquery.sparkline.js" type="text/javascript"></script>
  <script src="/assets/jquery-easy-pie-chart/jquery.easy-pie-chart.js"></script>
  <script src="/js/owl.carousel.js"></script>
  <!-- jQuery full calendar -->
  <<script src="/js/fullcalendar.min.js"></script>
    <!-- Full Google Calendar - Calendar -->
    <script src="/assets/fullcalendar/fullcalendar/fullcalendar.js"></script>
    <!--script for this page only-->
    <script src="/js/calendar-custom.js"></script>
    <script src="/js/jquery.rateit.min.js"></script>
    <!-- custom select -->
    <script src="/js/jquery.customSelect.min.js"></script>
    <script src="/assets/chart-master/Chart.js"></script>

    <!--custome script for all page-->
    <script src="/js/scripts.js"></script>
    <!-- custom script for this page-->
    <script src="/js/sparkline-chart.js"></script>
    <script src="/js/easy-pie-chart.js"></script>
    <script src="/js/jquery-jvectormap-1.2.2.min.js"></script>
    <script src="/js/jquery-jvectormap-world-mill-en.js"></script>
    <script src="/js/xcharts.min.js"></script>
    <script src="/js/jquery.autosize.min.js"></script>
    <script src="/js/jquery.placeholder.min.js"></script>
    <script src="/js/gdp-data.js"></script>
    <script src="/js/morris.min.js"></script>
    <script src="/js/sparklines.js"></script>
    <script src="/js/charts.js"></script>
    <script src="/js/jquery.slimscroll.min.js"></script>
    <script>
      //knob
      $(function() {
        $(".knob").knob({
          'draw': function() {
            $(this.i).val(this.cv + '%')
          }
        })
      });

      //carousel
      $(document).ready(function() {
        $("#owl-slider").owlCarousel({
          navigation: true,
          slideSpeed: 300,
          paginationSpeed: 400,
          singleItem: true

        });
      });

      //custom select box

      $(function() {
        $('select.styled').customSelect();
      });

      /* ---------- Map ---------- */
      $(function() {
        $('#map').vectorMap({
          map: 'world_mill_en',
          series: {
            regions: [{
              values: gdpData,
              scale: ['#000', '#000'],
              normalizeFunction: 'polynomial'
            }]
          },
          backgroundColor: '#eef3f7',
          onLabelShow: function(e, el, code) {
            el.html(el.html() + ' (GDP - ' + gdpData[code] + ')');
          }
        });
      });
    </script>

</body>

</html>
