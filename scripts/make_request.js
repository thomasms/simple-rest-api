var request = require('request');

var inputs = [];
process.argv.forEach(function (val, index, array) {
    if(index > 1){
        inputs.push(parseFloat(val));
    }
});

request.post(
    'http://localhost:8080/api/v0.1/add',
    { json: { data: inputs } },
    function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log('result = ' + body['result']);
        }
    }
);
