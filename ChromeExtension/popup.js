$(function(){
    $('#output).keyup(function(){
        $('#greet').text('Hello ' + $('#output').val());
    })
})