$(document).ready(function(){
  if(CONECTADO != "True")
    $('#conexao').modal() 

  $("body").on('click','#alterarConexao',function(){
    $('#conexao').modal()     
  })
  
  $("#btnConectar").click(function(){
    $("#formularioConexao").submit();
  })
  
  $("form").ajaxSubmit(function(){

  });


})