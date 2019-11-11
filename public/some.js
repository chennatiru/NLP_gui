// const python_s = require('child_process').spawn('python', ['./nlp.py']);
$(document).ready(function(){
    console.log("hii")
    
    

    $('#form1').submit(function(e){
        e.preventDefault();
        var data = $('input[name=qno]').val();
        $.ajax({
            type:'POST',
            url:'http://localhost:3000/ajax11',
            dataType:'json',
            data:{qno:data},
            success:function(resp){
                console.log(resp)
                $('#question_area').text(resp[0]);
                $('#form_row').empty();

                $('#form_row').append(`<div class = "col-sm-1"></div>`)
                $('#btn_id').remove();

                for (let i = 1; i < resp.length; i++) {
                    var text = `<div class = "col-sm-2"><div class="form-check">
                    <label class="form-check-label" for="radio1"><input type="radio" class="form-check-input" id="radio1" name="optradio" value="${i-1}">${resp[i]}</label>
                    </div></div>`
                    $('#form_row').append(text)
                }
                $('#form_row').append(`<div class = "col-sm-1"></div><br><br>`)
                $('#form2').append(`<center><button type="submit" class="btn btn-primary" id="btn_id">Submit</button></center>`)

                $('#ques_div').show()
            },
            error: function(jqXHR, textStatus, err){
                console.log('text status '+textStatus+', err '+err)
            }
        })

        
    })


    $('#form2').submit(function(e){
        e.preventDefault();
        var data = $('input[name=optradio]:checked').parent('label').text();
        $.ajax({
            type:'POST',
            url:'http://localhost:3000/ajax22',
            dataType:'json',
            data:{radio_text:data},
            success:function(resp){
                console.log(resp)
                $('#yra_id').text(resp[0])
                $('#aca_id').text(resp[1])
                $('#mpt_id').text(resp[2])
            },
            error: function(jqXHR, textStatus, err){
                console.log('text status '+textStatus+', err '+err)
            }
        })

        
    })

})


