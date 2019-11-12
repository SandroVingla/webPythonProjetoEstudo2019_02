$("#produto").on("change", function(){
    if($(this).val() != ""){
        $.ajax({
            method:'GET',
            url:'/pedido/selecionaProdutoAjax/' + $(this).val()
        }).done(function(data) {
            $('#valor').val(data.valor)
            calculaTotal()
        })
    }
})

function calculaTotal(){
    var preco =  $('#valor').val();
    var quantidade = $('#quantidade').val();
    var total = 0
    if(quantidade >= 1 && quantidade != ''){

        total = preco * quantidade;
        total = total.toFixed(2);
        $('#total').val(total);

    }else{
        $('#quantidade').val("1");
    }
}

$('#quantidade').on('keyup', function(){
    calculaTotal()
})