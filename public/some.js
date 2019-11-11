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
                $('#form2').empty();
                for (let i = 1; i < resp.length; i++) {
                    var text = `<div class="form-check">
                    <label class="form-check-label" for="radio1"><input type="radio" class="form-check-input" id="radio1" name="optradio" value="${i-1}">${resp[i]}</label>
                    </div>`
                    $('#form2').append(text)
                }
                $('#form2').append(`<button type="submit" class="btn btn-primary">Submit</button>`)
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
            },
            error: function(jqXHR, textStatus, err){
                console.log('text status '+textStatus+', err '+err)
            }
        })

        
    })

})


