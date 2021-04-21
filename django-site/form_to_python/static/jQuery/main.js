$(document).ready(function(){
    $("a").on({
        mouseenter : function(){
            $(this).animate({backgroundColor: "gray", color: "black"});
        },
        mouseleave : function(){
            $(this).animate({backgroundColor: "black", color: "white"});
        },
        click : function(){
            $(this).css({"color": "lightgreen", "background-color": "gray"});
        }
    });
})