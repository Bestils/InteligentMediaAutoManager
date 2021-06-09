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
            $(this).css({backgroundColor: "gray", color: "black"});
        },
        mouseleave : function(){
            $(this).css({backgroundColor: "black", color: "white"});
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
            $(this).css({backgroundColor: "gray", color: "black"});
        },
        mouseleave : function(){
            $(this).css({backgroundColor: "black", color: "white"});
        },
        click : function(){
            $(this).css({"color": "green", "background-color": "gray"});
        }
    });
})