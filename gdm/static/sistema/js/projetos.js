$(document).ready(function(){
  if(CONECTADO != "True")
    $('#conexao').modal() 

  $("body").on('click','#alterarConexao',function(){
    $('#conexao').modal()     
  }) 
  
  $("#btnConectar").click(function(){
    $("#formularioConexao").submit();
  })

  $("#btnConsulta, #btnSalvaConsulta").click(function(){
    $("#formularioConsulta").submit(); 
  })

  var lon = 5;
  var lat = 40;
  var zoom = 5;
  var map, layer;

  function init(){
      map = new OpenLayers.Map( 'map' );
      layer = new OpenLayers.Layer.WMS( "OpenLayers WMS", 
              "http://vmap0.tiles.osgeo.org/wms/vmap0",
              {layers: 'basic'} );
      map.addLayer(layer);
      map.setCenter(new OpenLayers.LonLat(lon, lat), zoom);
      var featurecollection = {
        "type": "FeatureCollection", 
        "features": [
          {"geometry": {
              "type": "GeometryCollection", 
              "geometries": [
                { "type": "MultiLineString", "coordinates": [ [ [ -35.761562145697539, -9.685616866222389 ], [ -35.728406203288401, -9.668030414314194 ] ] ] },
                { "type": "MultiLineString", "coordinates": [ [ [ -35.767054173534255, -9.670691771999367 ], [ -35.759181294528936, -9.632356205211362 ] ] ] },
                { "type": "MultiLineString", "coordinates": [ [ [ -35.726289866598478, -9.66697778481895 ], [ -35.747604052158358, -9.69752794967591 ] ] ] }
              ]
          }, 
          "type": "Feature", 
          "properties": {}}
        ]
     };
     var geojson_format = new OpenLayers.Format.GeoJSON();
     var vector_layer = new OpenLayers.Layer.Vector(); 
     map.addLayer(vector_layer);
     vector_layer.addFeatures(geojson_format.read(featurecollection));

  }

  init();

})