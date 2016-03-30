"use strict";
var $ = require('jquery');
var angular = require('angular');
var MainController = require('./controllers/MainController.js');

var app = angular.module('app', []);
app.controller('MainCtrl', MainController);