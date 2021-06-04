// Show Password
$(document).ready(function(){
 $(".checkbox").change(function(){
  if($(this).is(':checked')){
   $("#pass").attr("type","text");
  }
  else
  {
   $("#pass").attr("type","password");
  }
 });
});

// References a
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

// SUBMIT BUTTON
$(document).ready(function(){
    $(".launch").on({
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