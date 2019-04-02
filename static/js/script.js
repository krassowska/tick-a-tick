var mymap = L.map('mapid', {gestureHandling: true}).setView([51.505, -0.09], 13);
// Find user location:
// https://ipstack.com/
// https://stackoverflow.com/questions/24906833/get-your-location-through-python

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  minZoom: 1,
  maxZoom: 18,
  id: 'mapbox.streets',
  accessToken: 'pk.eyJ1IjoidGlja2l0IiwiYSI6ImNqdGQ5dHd5ODB4ajI0M3BmcGIzd2ozaHAifQ.kcP--rwUzKohsV_AOxMx7Q'
}).addTo(mymap);


function add_markers(ticks) {
  for (var i = 0; i < ticks.length; i++ ) {
    var tick = ticks[i];
    var marker = L.marker([tick['latitude'], tick['longitude']]).addTo(mymap);
    marker.bindPopup("This tick bit a " + tick['age'] + "-year-old " + tick['sex'] + " on: " + tick['date']);
  }
}

mymap.addControl(new L.Control.Fullscreen());


/* Search map https://github.com/stefanocudini/leaflet-search */
mymap.addControl(new L.Control.Search({
  url: 'https://nominatim.openstreetmap.org/search?format=json&q={s}',
  jsonpParam: 'json_callback',
  propertyName: 'display_name',
  propertyLoc: ['lat','lon'],
  marker: L.circleMarker([0,0],{radius:30}),
  autoCollapse: true,
  autoType: false,
  minLength: 2
}) );


/* Search map https://github.com/stefanocudini/leaflet-search */
mymap.addControl(new L.Control.Search({
  container: 'place',
  url: 'https://nominatim.openstreetmap.org/search?format=json&q={s}',
  jsonpParam: 'json_callback',
  propertyName: 'display_name',
  propertyLoc: ['lat','lon'],
  marker: L.circleMarker([0,0],{radius:30}),
  autoType: false,
  autoCollapse: false,
  collapsed: false,
  initial: false,
  minLength: 2
}) );
