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
  
  registraBotaoConsultas(map);

  criaNovaConsulta(map);

}) 
 
function allActivesLayers(map){
  var i=0;

  $('.consultas li:not(.disabled)').each(function(){
 
    var url = $(this).find('a').data('href');  
    
    $.getJSON(url,function(json){
      insereNovaCamada(map, json, 0);
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
function registraBotaoConsultas(map){ 
  $("body").on('click',".consultas li a",function(){
    toggleCamada(map, $(this));
    $(this).closest('li').toggleClass('disabled');
    $(this).toggleClass('disabled');
  });
}

function criaNovaConsulta(map){
  $('#formularioConsulta').ajaxForm({
    success: callbackNovaConsulta,
    error: function(){
      $("#formularioConsulta").resetForm();
      alert('Essa consulta já foi inserida nesse projeto. \n Evite duplicar as consultas ;)');
    }
  }); 
}

function callbackNovaConsulta(data, statusText, xhr){   
    insereNovaCamada(map, data, 10);

    html = "<li>"
    html += "<a data-href='/consulta/"+data.id+"' class='active' data-name='"+data.consulta+"'>"+data.consulta+"</a>";
    html += "</li>"
    $(".consultas li:last-child").after(html)
    $("#formularioConsulta").resetForm();
    $('#consulta').modal('hide');
}

function insereNovaCamada(map, json, ordem){
  todosgeos = []; 
  $.each(json.resultado, function(i,v){  
    todosgeos.push($.parseJSON(v.geom))
  });  

  map.novaCamada(json.consulta, todosgeos , $.parseJSON(json.propriedades), ordem ); 
}