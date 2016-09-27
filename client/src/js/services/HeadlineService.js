export default function($http) {
	return $http({
      method: 'GET',
      url: 'http://localhost:5000/today'
    }).then(function(response) {
      return response;
    }, function(error) {
      return {
      	data: false
      };
  });
}
