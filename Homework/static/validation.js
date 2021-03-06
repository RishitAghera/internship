$(document).ready(function(){
    function contact_validation(){
        len=$('#id_contact').val()
        var con= /^[0-9]*$/
        $('#error_id_contact').remove()
        if((len.length>10 || len.length<10) || (!con.test(len))){
            $('#id_contact').after("<p id='error_id_contact' class='text-danger'>* Numbers only Length Must be 10 digit.</p>")
            return false
        }else{
        $('#error_id_first_name').remove()
        return true
        }
    }

    function first_name_validation(){
        len=$('#id_first_name').val()
        var con= /^[a-zA-Z_]*$/
        $('#error_id_first_name').remove()
        if(!con.test(len)){
            $('#id_first_name').after("<p id='error_id_first_name' class='text-danger'>*Contains only alphabets and '_'</p>")
            return false
        }else{
        $('#error_id_first_name').remove()
        return true
        }
    }

    function last_name_validation(){
        len=$('#id_last_name').val()
        var con= /^[a-zA-Z_]*$/
        $('#error_id_last_name').remove()
        if(!con.test(len)){
            $('#id_last_name').after("<p id='error_id_last_name' class='text-danger'>*Contains only alphabets and '_'</p>")
            return false
        }else{
        $('#error_id_last_name').remove()
        return true
        }
    }

    function email_validation(){
        len=$('#id_email').val()
        var con= /^[a-zA-Z_.0-9]+@[a-zA-Z]+[.]{1}[a-zA-Z]+$/
        $('#error_id_email').remove()

        if(!con.test(len)){
            $('#id_email').after("<p id='error_id_email' class='text-danger'>*Email should contains '.' after '@'</p>")
            return false
        }else{
        $('#error_id_email').remove()
        return true
        }
    }

    function password_validation()
    {
        $('#error_password').remove()
        pass1=$('#id_password1').val()
        pass2=$('#id_password2').val()
        $('#error_password2').remove()
        if(pass2.length<=0){
            $('#id_password2').after("<p id='error_password' class='text-danger'>* Confirm Password should not be blank !</span>")
            return false
        }

        if(pass1!=pass2){
            $('#id_password2').after("<p id='error_password' class='text-danger'>* Password not match with Confirm Password !</span>")
            return false
        }else{
            return true
        }
    }

//registration form validation


        $('#id_contact').blur(function(){
            contact_validation()
        });

        $('#id_first_name').blur(function(){
           first_name_validation()
        });

        $('#id_last_name').blur(function(){
           last_name_validation()
        });

        $('#id_email').blur(function(){
            email_validation()
        });

        $('#id_password2').blur(function(){
           password_validation()
        });

        $('#registration').submit(function(e) {
            if(!(contact_validation() && first_name_validation() && last_name_validation() && email_validation() && password_validation()))
            {
                e.preventDefault()

            }
        });

        //book cleaner form
function city_validation()
    {
        cityval=$('#id_city').val()
        $("#error_city").remove()
        if(cityval.length<=0){
             $("#id_city").after("<span style='color:red' id='error_city'>*  Select City !</span>")
             return false
         }else{
             return true
        }
    }

    function timeslot_validation()
    {
        timeslotval=$('#id_timeslot').val()
        $("#error_timeslot").remove()
        if(timeslotval== 0){
            $("#id_timeslot").after("<span style='color:red' id='error_city'>*  Select Time Slot !</span>")
            return false
        }else{
            return true
        }
    }

    function date_validation()
    {
        dateval=$('#id_date').val()
        select_date=new Date(dateval) //selected date
        syear=select_date.getFullYear()
        smonth=select_date.getMonth()
        sdate=select_date.getDate()
        today_date=new Date() // today date
        tyear=today_date.getFullYear()
        tmonth=today_date.getMonth()
        tdate=today_date.getDate()
        $("#error_date").remove()
        if(syear>tyear){
            return true;
        }else if(syear==tyear){
            if(smonth>tmonth){
                return true;
            }else if(smonth==tmonth){
                if(sdate>tdate){
                    return true;
                }else if(sdate==tdate){
                    return true;
                }else{
                    $("#id_date").after("<span style='color:red' id='error_date'>*  Select Valid Date Not Past Date !</span>");
                    return false;
                }
            }
        }else{
            $("#id_date").after("<span style='color:red' id='error_date'>*  Select Valid Date Not Past Date !</span>");
            return false;
        }
    }

    $('#id_city').change(function(){
        city_validation()
    });

    $('#id_timeslot').change(function(){
        timeslot_validation()
    });

    $('#id_date').change(function(){
        date_validation()
    });

    $("#searchcleaner").submit(function(e){

        if(!(city_validation() && timeslot_validation() && date_validation()))
        {
            e.preventDefault()
        }
    });



    $("#searchcleaner").submit(function(e){
        if(!(city_validation() && timeslot_validation() && date_validation()))
        {
            e.preventDefault();
        }
    });



});