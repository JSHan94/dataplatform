const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const path = require('path');
const cors = require('cors');
const corsOptions = {
    origin: 'http://localhost:8080', 
    credentials: true, 
};

app.use(cors(corsOptions));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')))
//app.use(require('connect-history-api-fallback')());

app.use('/', require('./router'))


app.get('*', function (req, res) {
    res.sendFile(path.join(__dirname, 'public/', 'index.html'))
});

app.set('port', process.env.PORT || 3000);

app.listen(app.get('port'), () => {
    console.log('Connected');
})
