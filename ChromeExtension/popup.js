$(document).ready(function(){
        var dot = [$("#dot1"), $("#dot2"), $("#dot3"), $("#dot4")]
        var button = [$("#button1"), $("#button2"), $("#button3"), $("#button4"),]
    button[0].click(function(){
        if (dot[0].css('right') == '2px')
        {
            dot[0].animate({right: "-25px"});
            dot[1].animate({right: "-25px"});
            dot[2].animate({right: "-25px"});
            dot[3].animate({right: "-25px"});
            button[0].animate({backgroundColor: "#90EE90"}, "slow");
            button[1].animate({backgroundColor: "#90EE90"}, "slow");
            button[2].animate({backgroundColor: "#90EE90"}, "slow");
            button[3].animate({backgroundColor: "#90EE90"}, "slow");
        }
        else
        {
            dot[0].animate({right: "2px"});
            dot[1].animate({right: "2px"});
            dot[2].animate({right: "2px"});
            dot[3].animate({right: "2px"});
            button[0].animate({backgroundColor: "white"}, "slow");
            button[1].animate({backgroundColor: "white"}, "slow");
            button[2].animate({backgroundColor: "white"}, "slow");
            button[3].animate({backgroundColor: "white"}, "slow");
        }
    })

    button[1].click(function(){
        if (dot[1].css('right') == '2px')
        {
            dot[1].animate({right: "-25px"});
            button[1].animate({backgroundColor: "#90EE90"}, "slow");
        }
        else
        {
            dot[1].animate({right: "2px"});
            button[1].animate({backgroundColor: "white"}, "slow");
        }
    })

    button[2].click(function(){
        if (dot[2].css('right') == '2px')
        {
            dot[2].animate({right: "-25px"});
            button[2].animate({backgroundColor: "#90EE90"}, "slow");
        }
        else
        {
            dot[2].animate({right: "2px"});
            button[2].animate({backgroundColor: "white"}, "slow");
        }
    })

    button[3].click(function(){
        if (dot[3].css('right') == '2px')
        {
            dot[3].animate({right: "-25px"});
            button[3].animate({backgroundColor: "#90EE90"}, "slow");
        }
        else
        {
            dot[3].animate({right: "2px"});
            button[3].animate({backgroundColor: "white"}, "slow");
        }
    })
})

$(document).ready(function(){
    $(".logButton").on({
        mouseenter: function(){
            $(this).animate({ backgroundColor: "white", color: "black"});
        },
        mouseleave: function(){
            $(this).animate({ backgroundColor: "transparent", color: "gray"});
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