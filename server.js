/**
 * Created by DEEPAK.SHARMA on 12/26/2015.
 */
var express = require('express');
var app = express();

var path = require('path');
app.use('/', express.static(__dirname));

console.log('starting web server');
app.listen(3000);

