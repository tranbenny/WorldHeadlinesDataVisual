"use strict";

var MainController = function($scope, $http) {
  $scope.name = "hello world";
  $scope.result = "hi benny";
  getData();

  // get data from flask api
  function getData() {
    $http({
      method: 'GET',
      url: 'http://localhost:5000/headlines'
    }).then(function(response) {
      console.log(response);
      return response;
    }, function(error) {
      console.log("error occured");
      console.log(error);
    });
  }
}

module.exports = MainController;

