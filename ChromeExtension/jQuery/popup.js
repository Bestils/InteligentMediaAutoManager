// Funcionality Buttons Animation
$(document).ready(function(){
        var dot = [$("#dot1"), $("#dot2"), $("#dot3"), $("#dot4")]
        var button = [$("#turnAll"), $("#Follow"), $("#Like"), $("#Comment"),]
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
            dot[2].animate({right: "-25px"});
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
            dot[3].animate({right: "-25px"});
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

// LOG Button Animation
$(document).ready(function(){
    $(".logButton").on({
        mouseenter: function(){
            $(this).animate({ backgroundColor: "gray", color: "white"});
        },
        mouseleave: function(){
            $(this).animate({ backgroundColor: "white", color: "gray"});
        }
    });
})

// LABEL ANIMATIONS
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

// Funcionality example

$document.ready(function(){
    button[1].click(function(){
		var search_topic = $('#keyword').val();

		if (search_topic){
                chrome.runtime.sendMessage(
					{topic: search_topic},
					function(response) {
						result = response.farewell;
						alert(result.summary);

						var notifOptions = {
							type: "basic",
							iconUrl: "icon48.png",
							title: "WikiPedia Summary For Your Result",
							message: result.summary
						};

						chrome.notifications.create('WikiNotif', notifOptions);

					});
		}
		$('#keyword').val('');
    });
});