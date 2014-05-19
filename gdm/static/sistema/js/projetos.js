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
 
 
  // var cordenadas = { "type": "Point", "coordinates": [ -60.639283446655206, -13.474461590980399 ] }; 
  var map = new Maps('map');
  map.setBaseLayer("http://vmap0.tiles.osgeo.org/wms/vmap0",{layers: 'basic'});  
  
  // var propriedades = {fillColor: "#ff0000"} 
  // map.novaCamada('Ponto Teste', cordenadas, propriedades);
  getConsultasProntas();
}) 

function getConsultasProntas(){
  url = $('.consultas li:first a').attr('href');
  console.log(url);
  // $.get('')
}
