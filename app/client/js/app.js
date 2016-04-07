"use strict";
/*
TODO: 
- set up a basic router with ui-router
- move http service into its own service
- set up directive to use with D3
*/


// libraries
import jQuery from 'jquery';
import angular from 'angular';

// angular components
import MainController from './controllers/MainController.js';
import BarChartDirective from './directives/BarChartDirective.js';
import d3Service from './services/d3Service.js';
import dataMapService from './services/dataMapService.js';



let app = angular.module('app', []);


// controllers
angular.module('app')
	.controller('MainCtrl', MainController);

// services
angular.module('app')
	.factory('dataMap', dataMapService)
	.factory('d3', d3Service);


// directives
angular.module('app')
	.directive('barChart', ['d3', 'dataMap',  BarChartDirective]);

