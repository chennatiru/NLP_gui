const express = require('express')
const app = express();
const path = require('path');
const morgan = require('morgan');
const bodyParser = require('body-parser');



//support parsing of application/x-www-form-urlencoded post data
app.use(bodyParser.urlencoded({ extended: false }));
app.use(morgan('short'))

app.set('view engine', 'ejs');

app.use('/public',express.static(path.join(__dirname,'/public')));


var pred_act;


var output_dat;
const python_s = require('child_process').spawn('python', ['./cmsqa_sample.py']);
python_s.stdout.once('data',function(output_data){
    
    var ans = JSON.parse(output_data.toString('utf8'));
    output_dat = ans
    // console.log(ans)
        
   
    });

let g_ans;
const python_sss = require('child_process').spawn('python', ['./cmsqa_main.py']);
python_sss.stdout.once('data',function(output_data){
    // console.log("hii")
    var ans = JSON.parse(output_data.toString('utf8'));
    g_ans = ans
    // console.log(ans)
        
    
    });






app.get('/',(req,res) => {
    console.log(output_dat["key_f"][0])
    
    res.render('home',{"hey":output_dat})

})

app.post('/ajax11',(req,res) => {

    const python_ss = require('child_process').spawn('python', ['./cmsqa_final.py',Number(req.body.qno)]);

    python_ss.stdout.once('data',function(output_data){
    
        var ans = JSON.parse(output_data.toString('utf8'));
        pred_act = ans
        console.log(ans)
            
       
        });
    

    console.log("hii")
    console.log(req.body)
    res.json(g_ans["asd"][Number(req.body.qno)-1])

})

app.post('/ajax22',(req,res) => {

    console.log(req.body)
    res.json([req.body.radio_text,pred_act["ans"][0],pred_act["ans"][1]])

})

app.listen(3000,()=>{
    console.log("I am running on port 3000");
})



