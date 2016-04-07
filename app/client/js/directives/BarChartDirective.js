// directives need:
// - restrict
// - scope? 
// - template
// - link function(scope object, element(jquery object), attrs(array of attributes on the element))
// 		use the link function to perform DOM manipulation

// TODO: 
// - create a GeoJSON for coordinates, DONE
// - change the color of countries with headlines
// - create a blue scale map for the headlines data
// - when a country is clicked, load up a pop up of the headlines


function BarChartDirective(d3, worldMap) {
	return {
		restrict: 'E',
		link: function(scope, element, attrs) {
			console.log("trying something new");
			var map = new worldMap({
				element: document.getElementById('chart'),
				setProjection: function(element, options) {
					var projection = d3.geo.equirectangular()
						.scale(200)
						.translate([element.offsetWidth / 2, element.offsetHeight / 2]);
					var path = d3.geo.path()
						.projection(projection);

					return {path:path, projection: projection};
				}
			});
		}, 
		template: "<div id='chart'></div>"
	};
}


export default BarChartDirective;