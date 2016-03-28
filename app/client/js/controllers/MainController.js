"use strict";

app.controller('MainCtrl',
  function MainController($scope, $http) {
    $scope.name = "hello world";
    $scope.result = getData();


    // use http service to get data
    function getData() {
      $http({
        method: 'GET',
        url: 'http:localhost:5000/headlines'
      }).then(function(response) {
        // success callback
        console.log(response);
        return response;
      }, function(response) {
        // error callback
        console.log("error occured ");
        console.log(response);
        return {};
      })
    }


  }
);
