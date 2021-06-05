$(document).ready(function(){
    var button = "single_comment_submit"
    $("#single_comment").on({
        keypress : function(){
            comment = $("#single_comment").val();
            commentButtonService(button, comment);
        },
        blur : function(){
            comment = $("#single_comment").val();
            commentButtonService(button, comment);
        }
    });
});

function commentButtonService(button, comment)
{
    if (comment.length > 0)
    {
        document.getElementById(button).setAttribute("type", "submit");
        document.getElementById(button).setAttribute("class", "launch");
    }
    else
    {
        document.getElementById(button).setAttribute("type", "text");
        document.getElementById(button).setAttribute("class", "inactive_button");
    }

}