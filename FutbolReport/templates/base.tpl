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
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.1/css/fontawesome.min.css" integrity="sha256-80fAXabaQMIQSB79XD5pFt2eVZuI12D3yF6/FAkbO8E=" crossorigin="anonymous" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.1/css/solid.min.css" integrity="sha256-EykeDBUB7g2D5PjMR0Ql9SdPsPNB5ASVQl89hxWRiL0=" crossorigin="anonymous" />
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
          <a href="http://localhost:80/" class="logo">Futbol <span class="lite">Report</span></a>          
          <!--logo end-->            
          
    </header>
    <!--header end-->

    <!--sidebar mroustart-->
    <aside>
      <div id="sidebar" class="nav-collapse " style="overflow: scroll;">
            <!-- sidebar menu start-->
            <ul class="sidebar-menu">
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
                <a href="javascript:escoger_jugador();" class="">
                              <i class="fas fa-running"></i>  
                              <span>Jugadores</span>                          
                          </a>            
              </li>   
                                     
    
              <li class="sub-menu">
                <a href="javascript:escoger_equipo();" class="">
                              <i class="fas fa-user-friends"></i>
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
                              <i class="fas fa-calendar-alt"></i>
                              <span>Jornadas</span>                          
                          </a>
              </li>
              <li class="">
                <a href="javascript:escoger_estadio();" class="">
                              <i class="icon_house_alt"></i>
                              <span>Estadios</span>
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
    <!-- Datatable jquery -->
    <link href="https://cdn.datatables.net/1.10.21/css/jquery.dataTables.min.css" rel="stylesheet">  
    <script type="text/javascript" src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>
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
