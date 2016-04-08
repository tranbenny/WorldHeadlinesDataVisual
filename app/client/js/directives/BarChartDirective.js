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


function BarChartDirective(d3, worldMap, headlines, countryData) {
	
	// data format: 
	// "USA": 1
	let data = {};
	let palleteScale = {};
	let dataMap = {};

	// populate dataset
	function findCountry(name) {
		let countryName = '';
		for (let i = 0; i < name.length; i++) {
			if (i === 0 || name.charAt(i - 1) === ' ') {
				countryName = countryName + name.charAt(i).toUpperCase();
			} else {
				countryName = countryName + name.charAt(i);

			}
		}
		let result = countryData.lookup.countries({name: countryName})[0];
		try {
			let code = result['alpha3'];
			if (Object.keys(data).indexOf(code) !== -1) {
				data[code] = data[code] + 1;
			} else {
				data[code] = 1;
			}
		} catch(err) {}
	}

	// sets up color gradient scale for headline data
	function setUpGradient() {
		let minValue = data[Object.keys(data)[0]];
		let maxValue = data[Object.keys(data)[0]];
		Object.keys(data).forEach((x) => {
			const value = data[x];
			if (value < minValue) {
				minValue = value;
			}
			if (value > maxValue) {
				maxValue = value;
			}
		});
		palleteScale = d3.scale.linear()
			.domain([minValue, maxValue])
			.range(['#EFEFFF', '#02386F']);
	}

	// create color mapping values for map
	function colorMap() {
		Object.keys(data).forEach((x) => {
			dataMap[x] = { "fillColor": palleteScale(data[x])};
		});
	}



	return {
		restrict: 'E',
		link: function(scope, element, attrs) {
			var map = new worldMap({
				element: document.getElementById('chart'),
				fills: {
					defaultFill: '#b2b2b2'
				}, 
				geographyConfig: {
		            // change this to load the article titles
		            popupTemplate: function(geo, data) {
		                return ['<div class="hoverinfo"><strong>',
		                        'hi ' + geo.properties.name,
		                        '</strong></div>'].join('');
           			}
		        },
				setProjection: function(element, options) {
					var projection = d3.geo.equirectangular()
						.scale(200)
						.translate([element.offsetWidth / 2, element.offsetHeight / 2]);
					var path = d3.geo.path()
						.projection(projection);
					return {path:path, projection: projection};
				}
			});

			headlines.then(function(response) {
				// write function to load the data onto the map
				if (response.data !== false) {
					// make dataset for datamaps to update the color
					response.data.data.forEach(function(value, index, array) {
						let countries = value['countries'];
						countries.forEach((value) => {
							findCountry(value)
						});
					});
				}
				// set up data for gradient
				setUpGradient();
				colorMap();
				map.updateChoropleth(dataMap);
			});
		}, 
		template: "<div id='chart'></div>"
	};
}


export default BarChartDirective;