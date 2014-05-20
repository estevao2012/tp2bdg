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
 
 
  
  
  var map = new Maps('map');
  map.setBaseLayer("http://vmap0.tiles.osgeo.org/wms/vmap0",{layers: 'basic'});  
  
  allActivesLayers(map); 
  
  $(".consultas li a").click(function(){
    toggleCamada(map, $(this));
    $(this).closest('li').toggleClass('disabled');
    $(this).toggleClass('disabled');
  })
}) 
 
function allActivesLayers(map){
  i=0
  $('.consultas li:not(.disabled)').each(function(){

    var link = $(this).find('a');
    url = link.data('href');  
    
    $.getJSON(url,function(json){

      todosgeos = [];
      
      $.each(json.resultado, function(i,v){  
        todosgeos.push($.parseJSON(v.geom))
      });  

      map.novaCamada(link.data('name'), todosgeos , $.parseJSON(json.propriedades) , i );

    });
     
    i++
  });

  
}

function toggleCamada(map,name)
{ 

  var mLayers = map.getLayers(); 
  var hideShow = false;
  if(name.hasClass('disabled'))
    hideShow = true;

  for(var a = 0; a < mLayers.length; a++ ){

    if(mLayers[a].name == name.data('name')) 
        map.toggleCamada(mLayers[a],hideShow);

  };
}