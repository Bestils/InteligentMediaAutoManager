// Funcionality Buttons Animation
$(document).ready(function(){
        var dot = [$("#dot1"), $("#dot2"), $("#dot3"), $("#dot4")]
        var button = [$("#turnAll"), $("#Follow"), $("#Like"), $("#Comment"),]
    button[0].click(function(){
        if (dot[0].css('right') == '2px')
        {
            dot[0].animate({right: "-40px"});
            dot[1].animate({right: "-40px"});
            dot[2].animate({right: "-40px"});
            dot[3].animate({right: "-40px"});
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
            dot[1].animate({right: "-40px"});
            button[1].animate({backgroundColor: "#90EE90"}, "slow");
            // HERE SHOULD BE LOGIC - Follow
        }
        else
        {
            dot[1].animate({right: "2px"});
            button[1].animate({backgroundColor: "white"}, "slow");
            // HERE SHOULD BE LOGIC TO Disable Follow
        }
    })

    button[2].click(function(){
        if (dot[2].css('right') == '2px')
        {
            dot[2].animate({right: "-40px"});
            button[2].animate({backgroundColor: "#90EE90"}, "slow");
            // HERE SHOULD BE LOGIC - Like
        }
        else
        {
            dot[2].animate({right: "2px"});
            button[2].animate({backgroundColor: "white"}, "slow");
            // HERE SHOULD BE LOGIC to Disable - Like
        }
    })

    button[3].click(function(){
        if (dot[3].css('right') == '2px')
        {
            dot[3].animate({right: "-40px"});
            button[3].animate({backgroundColor: "#90EE90"}, "slow");
            // HERE SHOULD BE LOGIC - Comment
        }
        else
        {
            dot[3].animate({right: "2px"});
            button[3].animate({backgroundColor: "white"}, "slow");
            // HERE SHOULD BE LOGIC to Disable - Comment
        }
    })
})
