$(document).ready(function(){
    var possible_tag_chars = "0123456789abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ_ ";
    var possible_location_chars = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ ";
    var probability_error = "Probability must be a number between 1 and 100";
    var tag_error = "Tags can only contain letters, numbers, and underscores";
    var amount_error = "Amount must be a number greater than 0";
    var delay_error = "Delay must be a number greater than 0";
    var location_error = "Locations can only contain letters";
    var green = "rgb(0, 128, 0)";

    $("#like_photo_probability_field").focusout(function(){
            var value = $(this).val()
            probabilityError("like_photo_probability_field", "like_photo_probability_error_field", probability_error);
            checkOther("like_photo_tags_field", "like_photo_tags_error_field", tag_error, wrongCharsDetector);
    });

    $("#like_video_probability_field").focusout(function(){
            var value = $(this).val()
            checkOther("like_video_tags_field", "like_video_tags_error_field");
            probabilityError("like_video_probability_field", "like_video_probability_error_field", probability_error);
    });

    $("#like_photo_tags_field").focusout(function(){
        var value = $(this).val();
        wrongCharsDetector("like_photo_tags_field", "like_photo_tags_error_field", tag_error, possible_tag_chars);
        checkOther("like_photo_probability_field", "like_photo_probability_error_field");
    });

    $("#like_video_tags_field").focusout(function(){
        var value = $(this).val();
        wrongCharsDetector("like_video_tags_field", "like_video_tags_error_field", tag_error, possible_tag_chars);
        checkOther("like_video_probability_field", "like_video_probability_error_field");
    });

    $("#follow_by_tags_field").focusout(function(){
        var value = $(this).val();
        wrongCharsDetector("follow_by_tags_field", "follow_by_tags_error_field", tag_error, possible_tag_chars);
    });

    $("#locations_field").focusout(function(){
        var value = $(this).val();
        wrongCharsDetector("locations_field", "locations_error_field", location_error, possible_location_chars);
    });

    $("#unfollow_non_followers_amount_field").focusout(function(){
        var value = $(this).val();
        valueError("unfollow_non_followers_amount_field", "unfollow_non_followers_amount_error_field", amount_error)
        checkOther("unfollow_non_follower_time_field", "unfollow_non_follower_time_error_field");
    });

    $("#unfollow_non_followers_time_field").focusout(function(){
        var value = $(this).val();
        valueError("unfollow_non_followers_time_field", "unfollow_non_followers_time_error_field", delay_error);
        checkOther("unfollow_non_follower_amount_field", "unfollow_non_follower_amount_error_field");
    });

    $("#unfollow_new_followers_amount_field").focusout(function(){
        var value = $(this).val();
        var error = "Amount must be a number greater than 0";
        valueError("unfollow_new_followers_amount_field", "unfollow_new_followers_amount_error_field", amount_error)
        checkOther("unfollow_new_follower_time_field", "unfollow_new_follower_time_error_field");
    });

    $("#unfollow_new_followers_time_field").focusout(function(){
        var value = $(this).val();
        valueError("unfollow_new_followers_time_field", "unfollow_new_followers_time_error_field", delay_error);
        checkOther("unfollow_new_follower_amount_field", "unfollow_new_follower_amount_error_field");
    });

    $("input").focusout(function(){
        checkForm(green);
    });
})

function checkForm(green)
{
    var elements = document.getElementsByTagName("input");
    for(var i = 0; i < elements.length;i++)
    {
        style = getComputedStyle(elements[i]);
        console.log(style.borderLeftColor);
        border = style.borderLeftColor;

        if(border == green)
        {
            document.getElementById("launch").style.display="block";
            break;
        }
        else
        {
            document.getElementById("launch").style.display="none";
        }
    }
}

function valueError(input_field, error_field, error_description)
{
    var value = document.getElementById(input_field).value;
    if(value > 0)
    {
        setCorrect(input_field, error_field);
    }
    else if(value < 0)
    {
        setError(input_field, error_field, error_description)
    }
    else if(value.length == 0)
    {
        setNeutral(input_field, error_field)
    }
    else
    {
        setError(input_field, error_field, error_description)
    }
}
function wrongCharsDetector(input_field, error_field, error_description, possible_chars)
{
    var value = document.getElementById(input_field).value;
    var error = true;
    if(value.length != 0)
    {
        for(var i = 0; i < value.length; i ++)
        {
            for(var j = 0; j < possible_chars.length; j ++)
            {
                if(value[i] == possible_chars[j])
                {
                    error = false;
                }
            }
            if (error == true)
            {
                setError(input_field, error_field, error_description);
                return
            }
        }
        setCorrect(input_field, error_field);
    }
    else{
        setNeutral(input_field, error_field);
    }
}

function probabilityError(input_field, error_field, error_description){
    var value = document.getElementById(input_field).value;
    if(value.length == 0)
    {
        setNeutral(input_field, error_field)
    }
    else if(!isNaN(value) && value > 0 && value <= 100)
    {
        setCorrect(input_field, error_field);
    }
    else
    {
        setError(input_field, error_field, error_description);
    }
}

function setError(input_field, error_field, description)
{
    document.getElementById(input_field).style.borderColor = "red";
    document.getElementById(input_field).style.borderWidth = "1px";
    document.getElementById(error_field).style.color = "red";
    document.getElementById(error_field).innerHTML = description;
}

function setCorrect(input_field, error_field)
{
    document.getElementById(input_field).style.borderColor = "green";
    document.getElementById(input_field).style.borderWidth = "1px";
    document.getElementById(error_field).innerHTML = "";
}

function setNeutral(input_field, error_field)
{
    document.getElementById(input_field).style.borderColor = "lightgray";
    document.getElementById(input_field).style.borderWidth = "0.5px";
    document.getElementById(error_field).innerHTML = "";
}

function checkOther(input_field, error_field, error, errorCheckMethod)
{
    var possible_tag_chars = "0123456789abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ_ ";
    var value = document.getElementById(input_field).value;
    console.log(error_field);
    if(value.length == 0)
    {
        setError(input_field, error_field, "This field can't be empty");
    }
    else
    {
        errorCheckMethod(input_field, error_field, error, possible_tag_chars);
    }
}


