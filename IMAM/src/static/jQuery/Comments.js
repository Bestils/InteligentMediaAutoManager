$(document).ready(function(){

    $("#single_comment").on({
        keypress : function(){
            singleCommentButtonService(single_comment_button, comment)
            submitButtonService(submit_button, comments_to_add)
        },
        blur : function(){
            singleCommentButtonService(single_comment_button, comment)
            submitButtonService(submit_button, comments_to_add)
        }
    });
});

function singleCommentButtonService(button, comment)
{
    var single_comment_button = "single_comment_submit";
    var comment = document.getElementById("comment").value;
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

function submitButtonService()
{
    var submit_button = "submit";
    var comments_to_add = document.getElementById("comments_to_add").value;
    if (comments_to_add.length > 0)
    {
        document.getElementById(submit_button).setAttribute("type", "submit");
        document.getElementById(submit_button).setAttribute("class", "launch");
    }
    else
    {
        document.getElementById(submit_button).setAttribute("type", "text");
        document.getElementById(submit_button).setAttribute("class", "inactive_button");
    }
}