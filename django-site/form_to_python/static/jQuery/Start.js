// Labels Animations

$(document).ready(function(){
    $(".label").on({
        mouseenter : function(){
            $(this).animate({ backgroundColor: "white", color: "green"});
        },
        mouseleave : function(){
            $(this).animate({ backgroundColor: "#DCDCDC", color: "green"});
        },
        focus : function(){
            $(this).css({"background-color": "white", "color": "white", "outline": "none"});
        },

        blur : function(){
            $(this).css({"background-color": "#DCDCDC"});
        }
    });
});

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

// References

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
