$(document).ready(function(){
  $('#conexao').modal() 

  $("#btnConectar").click(function(){
    var dados = []; 
    var formulario = $("#formularioConexao");
    $.each(formulario.find('input'),function(index , elem){
      ele = $(elem)
      dados[ele.attr('name')] = ele.val();
    });
    console.log(dados)
    $.post( formulario.attr('action'),dados ,function(data){
      console.log(data);
    });

  })
})