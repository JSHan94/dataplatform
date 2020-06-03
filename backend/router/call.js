exports.sendTransaction = (req,res) =>{
        console.log("called!")
        const buyer = "0x78658C9AaD8523BB283029C43135CF87339ADC21"
        const uploader = "0x7161a4eCE5dD841756ee38cBEa7da055F29302c9"
        
        // url query examples 
        // getFileInformation - dataHash
        // http://localhost:3000/send?method=getFileInformation&dataHash=123
  
        // buyFile - dataHash
        // http://localhost:3000/send?method=buyFile&dataHash=123
  
        // getToken  -  user, token
        // http://localhost:3000/send?method=getToken&user=0x78658C9AaD8523BB283029C43135CF87339ADC21&token=20
  
        // uploadFile - category, fileName, dataHash, price
        // http://localhost:3000/send?method=uploadFile&category=science&fileName=network&dataHash=123&price=10
  
        // checkEvent - blocknum
        // http://localhost:3000/send?method=checkEvent&blocknum=7909041
  
        // read url query 
        var scriptName = "trading.py"
        var query = [scriptName]
        for (var i in req.query){
            query.push(req.query[i])
        }
        
        console.log(query)

        // make child process   
        var spawn = require('child_process').spawn 
        var process = spawn('python',query) 
  
        // query result 
        process.stdout.on('data',function(data){
            var str = data.toJSON() // buffer to JSON
            var json =JSON.stringify(str) // JSON to string
            var origin = Buffer.from(JSON.parse(json).data).toString('utf-8') // buffer string to origin buffer
            //console.log(origin.toString('utf-8')) // origin buffer decoding
            //var obj = JSON.parse(origin.toString('utf-8'))
            
            var lines = origin.split(/\n/g)
            console.log("event length : "+ lines.length)
            try{
                for (var i in lines){
                    obj = JSON.parse(lines[i])
                    console.log(obj)

                }
            }catch(error){
                //console.log(error)
            }
        })
}