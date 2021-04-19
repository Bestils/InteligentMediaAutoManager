// Labels and log button Animations
$(document).ready(function(){
    $(".logButton").on({
        mouseenter: function(){
            $(this).animate({ backgroundColor: "gray", color: "white"});
        },
        mouseleave: function(){
            $(this).animate({ backgroundColor: "green", color: "white"});
        },
    });
})

$(document).ready(function(){
    $(".label").on({
        mouseenter : function(){
            $(this).animate({backgroundColor: "white", color: "green"});
        },
        mouseleave : function(){
            $(this).animate({backgroundColor: "#DCDCDC", color: "green"});
        },
        focus : function(){
            $(this).css({"background-color": "white", "color": "white", "outline": "none"});
        },

        blur : function(){
            $(this).css({"background-color": "#DCDCDC"});
        }
    });
})

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