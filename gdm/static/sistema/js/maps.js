function Maps(mapa){

  var map;
  var self = this;

  var defineMap = function(){
    map = new OpenLayers.Map(mapa);
  }

  self.removeCamada = function(layer, bolean){
    map.removeLayer(layer,bolean);
  }

  self.toggleCamada = function(layer,hideShow){
    layer.display(hideShow);
  }

  self.setBaseLayer = function( urlLayer , propriedades){
    var layer = new OpenLayers.Layer.WMS( "OpenLayers WMS", urlLayer , propriedades );
    map.addLayer(layer);
    map.zoomToMaxExtent();
  }

  self.setCenterMap = function(lat,lng,zoom){
    map.setCenter(new OpenLayers.LonLat( lat, lng ), zoom);
  }

  self.getLayers = function(){
    return map.layers;
  }
  self.novaCamada = function(nomecamada, geojson, propriedades, ordem){
    var prop = {
                fillColor: '#c9c9c9',
                externalGraphic: '/static/sistema/img/marker.png',
                graphicWidth: 20,
                graphicHeight: 24,
                graphicYOffset: -24,
                'strokeWidth': 1,
                fillOpacity: 0.9
            };
    $.extend(prop,propriedades);

    var featurecollection = {
    "type": "FeatureCollection", 
    "features": [{
        "geometry": {
          "type": "GeometryCollection", 
          "geometries": geojson
        }, 
        "type": "Feature", 
        "properties": {
          "name": "Coors Field"
        }
      }]
    }; 
 
    var geojson_format = new OpenLayers.Format.GeoJSON();
    var styleMap = new OpenLayers.StyleMap(prop);
    var vector_layer = new OpenLayers.Layer.Vector(nomecamada, { styleMap: styleMap , rendererOptions: {yOrdering: true}});  

    map.addLayer(vector_layer); 
    vector_layer.addFeatures(geojson_format.read(featurecollection) );

    map.setLayerIndex(vector_layer, ordem);

    // var highlightCtrl = new OpenLayers.Control.SelectFeature(vector_layer, {
    //     hover: true,
    //     highlightOnly: true,
    //     renderIntent: "temporary", 
    // });

    // var selectCtrl = new OpenLayers.Control.SelectFeature(vector_layer,
    //     {clickout: true}
    // );

    // map.addControl(highlightCtrl);
    // map.addControl(selectCtrl);


  } 

  var init = function(){
    defineMap();
  } 

  init();

}