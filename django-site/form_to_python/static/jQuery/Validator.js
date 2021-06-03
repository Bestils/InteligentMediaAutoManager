$(document).ready(function(){
    $("#like_photo_prob").focusout(function(){
            var value = $("#like_photo_prob").val()
            probabilityError("like_photo_prob", value, "photo_prob_error");
        });
})

function probabilityError(input_id, value, error_field, error_description){
    if(isNaN(value) && value > 0 && value <= 100)
    {
                setCorrectAction(input_id, error_field_id);
    }
    else
    {
                setError(input_id, error_field_id, error_description);
    }
}

function setError(input_id, error_field, description)
{
    document.getElementById(id).style.borderColor = "red";
                document.getElementById(id).style.borderWidth = "2px";
                document.getElementById(error_field).style.color = "red";
                document.getElementById(error_field).innerHTML = description;
                document.getElementById("launch").setAttribute("type", "text");
}

function setCorrectAction(id)
{
    document.getElementById(id).style.borderColor = "green";
                document.getElementById(id).style.borderWidth = "2px";
                document.getElementById(error_field).innerHTML = "";
                document.getElementById("launch").setAttribute("type", "submit");
}