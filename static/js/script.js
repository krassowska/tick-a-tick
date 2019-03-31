var mymap = L.map('mapid').setView([51.505, -0.09], 13);
// Find user location:
// https://ipstack.com/
// https://stackoverflow.com/questions/24906833/get-your-location-through-python

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox.streets',
  //accessToken: 'pk.eyJ1IjoidGlja2l0IiwiYSI6ImNqdGQ5dHd5ODB4ajI0M3BmcGIzd2ozaHAifQ.kcP--rwUzKohsV_AOxMx7Q'
}).addTo(mymap);

//var marker = L.marker([51.5, -0.09]).addTo(mymap);
//var marker = L.marker([51.55, -0.095]).addTo(mymap);


function add_markers(ticks) {
  for (var i = 0; i < ticks.length; i++ ) {
    var tick = ticks[i];
    var marker = L.marker([tick['longitude'], tick['latitude']]).addTo(mymap);
    marker.bindPopup("This tick bit a " + tick['age'] + "-year-old " + tick['sex'] + " on: " + tick['date']);
  }
}


/*
for (var tick_id = 0; tick_id < Tick[id]; tick_id++) {
  var marker = L.marker([Tick[longitude], Tick[latitude]]).addTo(mymap);
}
*/

// popups and markers - START
//var marker = L.marker([longitude, latitude]).addTo(mymap);
/*marker.bindPopup("This is your tick." + date.toString() + e.latlng.toString()).openPopup();
var popup = L.popup();

function onMapClick(e) {
  popup
    .setLatLng(e.latlng)
    .setContent("You clicked the map at " + e.latlng.toString())
    .openOn(mymap);
}

mymap.on('click', onMapClick);
*/
// popups and markers - END

marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();

var popup = L.popup()
  .setLatLng([51.5, -0.07])
  .setContent("I am a standalone popup.")
  .openOn(mymap);

mymap.addControl(new L.Control.Fullscreen());