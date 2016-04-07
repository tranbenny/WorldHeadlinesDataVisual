
class MainController {
  
  constructor($http) {
    this.name = "replace me with today's date";
    this.result = "replace me with a router nav-bar";
  }

  // get data from flask api
  getData() {
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

export default MainController;

