$(document).ready(function(){
    var comment = $("#single_comment")
    comment.keypress(function(){
        if (comment.val().length > 1)
        {
            $("#single_comment_submit").attr("type" , "Submit");
            $("#single_comment_submit").attr("class" , "launch");
        }
        else
        {
            $("#single_comment_submit").attr("type" , "text");
            $("#single_comment_submit").attr("class" , "inactive_button");
        }
    });
});