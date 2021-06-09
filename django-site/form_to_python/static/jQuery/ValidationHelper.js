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

function valueError(input, error, error_description)
{
    var value = document.getElementById(input).value;
    if(value > 0)
    {
        setCorrect(input, error);
    }
    else if(value < 0)
    {
        setError(input, error, error_description)
    }
    else if(value.length == 0)
    {
        setNeutral(input, error)
    }
    else
    {
        setError(input, error, error_description)
    }
}

function wrongCharsDetector(input, error, error_description, possible_chars)
{
    var value = document.getElementById(input).value;
    var wrong = true;
    if(value.length != 0)
    {
        for(var i = 0; i < value.length; i ++)
        {
            for(var j = 0; j < possible_chars.length; j ++)
            {
                if(value[i] == possible_chars[j])
                {
                    wrong = false;
                }
            }
            if (error == true)
            {
                setError(input, error, error_description);
                return
            }
        }
        setCorrect(input, error);
    }
    else
    {
        setNeutral(input, error);
    }
}

function probabilityError(input, error, error_description){
    var value = document.getElementById(input).value;
    if(value.length == 0)
    {
        setNeutral(input, error)
    }
    else if(!isNaN(value) && value > 0 && value <= 100)
    {
        setCorrect(input, error);
    }
    else
    {
        setError(input, error, error_description);
    }
}

function setError(input, error, error_description)
{
    document.getElementById(input).style.borderColor = "red";
    document.getElementById(input).style.borderWidth = "1px";
    document.getElementById(error).style.color = "red";
    document.getElementById(error).innerHTML = error_description;
}

function setCorrect(input, error)
{
    document.getElementById(input).style.borderColor = "green";
    document.getElementById(input).style.borderWidth = "1px";
    document.getElementById(error).innerHTML = "";
}

function setNeutral(input, error)
{
    document.getElementById(input).style.borderColor = "lightgray";
    document.getElementById(input).style.borderWidth = "0.5px";
    document.getElementById(error).innerHTML = "";
}

function checkBoth(input, input_error, other, other_error)
{
    var value = document.getElementById(input).value;
    var other_element = document.getElementById(other);
    other_style = getComputedStyle(other_element);

    if(value.length == 0 && other_style.borderLeftColor == green)
    {
        setError(input, error_field, "This field can't be empty");
    }
    else
    {
        setNeutral(input,error);
    }
}