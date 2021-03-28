$(document).ready(function(){
    $('#button1').click(function(){
        if ($("#dot1").css('right') == '2px')
        {
            $("#dot1").animate({right: "-25px"});
            $("#dot2").animate({right: "-25px"});
            $("#dot3").animate({right: "-25px"});
            $("#dot4").animate({right: "-25px"});
            $("#button1").animate({backgroundColor: "#90EE90"}, "slow");
            $("#button2").animate({backgroundColor: "#90EE90"}, "slow");
            $("#button3").animate({backgroundColor: "#90EE90"}, "slow");
            $("#button4").animate({backgroundColor: "#90EE90"}, "slow");
        }
        else
        {
            $("#dot1").animate({right: "2px"});
            $("#dot2").animate({right: "2px"});
            $("#dot3").animate({right: "2px"});
            $("#dot4").animate({right: "2px"});
            $("#button1").animate({backgroundColor: "white"}, "slow");
            $("#button2").animate({backgroundColor: "white"}, "slow");
            $("#button3").animate({backgroundColor: "white"}, "slow");
            $("#button4").animate({backgroundColor: "white"}, "slow");
        }
    })
})

$(document).ready(function(){
    $('#button2').click(function(){
        if ($("#dot2").css('right') == '2px')
        {
            $("#dot2").animate({right: "-25px"});
            $("#button2").animate({backgroundColor: "#90EE90"}, "slow");
        }
        else
        {
            $("#dot2").animate({right: "2px"});
            $("#button2").animate({backgroundColor: "white"}, "slow");
        }
    })
})

$(document).ready(function(){
    $('#button3').click(function(){
        if ($("#dot3").css('right') == '2px')
        {
            $("#dot3").animate({right: "-25px"});
            $("#button3").animate({backgroundColor: "#90EE90"}, "slow");
        }
        else
        {
            $("#dot3").animate({right: "2px"});
            $("#button3").animate({backgroundColor: "white"}, "slow");
        }
    })
})

$(document).ready(function(){
    $('#button4').click(function(){
        if ($("#dot4").css('right') == '2px')
        {
            $("#dot4").animate({right: "-25px"});
            $("#button4").animate({backgroundColor: "#90EE90"}, "slow");
        }
        else
        {
            $("#dot4").animate({right: "2px"});
            $("#button4").animate({backgroundColor: "white"}, "slow");
        }
    })
})

$(document).ready(function(){
    $(".logButton").on({
        mouseenter: function(){
            $(this).animate({ backgroundColor: "#EEE8AA", color: "black", borderColor: "black"});
        },
        mouseleave: function(){
            $(this).animate({ backgroundColor: "transparent", color: "gray", borderColor: "gray"});
        }
    });
})

$(document).ready(function(){
    $(".label").on({
        focus : function(){
            $(this).css({"border-color": "#FFEFD5", "background-color": "#EEE8AA"});
        },

        blur : function(){
            $(this).css({"border-color": "white", "background-color": "white"});
        }
    });
})