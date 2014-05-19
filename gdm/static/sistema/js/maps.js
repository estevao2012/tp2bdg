function Maps(mapa){

  var map;
  var self = this;

  var defineMap = function(){
    map = new OpenLayers.Map(mapa);

  }

  self.setBaseLayer = function( urlLayer , propriedades){
    var layer = new OpenLayers.Layer.WMS( "OpenLayers WMS", urlLayer , propriedades );
    map.addLayer(layer);
    map.zoomToMaxExtent();
  }

  self.setCenterMap = function(lat,lng,zoom){
    map.setCenter(new OpenLayers.LonLat( lat, lng ), zoom);
  }

  self.novaCamada = function(nomecamada,geojson,propriedades){
    var prop = {externalGraphic: '/static/sistema/img/marker.png', graphicWidth: 20, graphicHeight: 24, graphicYOffset: -24};
    $.extend(prop,propriedades);

    var featurecollection = {
    "type": "FeatureCollection", 
    "features": [{
        "geometry": {
          "type": "GeometryCollection", 
          "geometries": [geojson]
        }, 
        "type": "Feature", 
        "properties": {
          "name": "Coors Field"
        }
      }]
    };
 
    var geojson_format = new OpenLayers.Format.GeoJSON();
    var styleMap = new OpenLayers.StyleMap(prop)
    var vector_layer = new OpenLayers.Layer.Vector(nomecamada,{styleMap: styleMap});  

    map.addLayer(vector_layer); 
    vector_layer.addFeatures(geojson_format.read(featurecollection) );

  } 

  var init = function(){
    defineMap();
  } 

  init();

}