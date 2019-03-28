var mymap = L.map('mapid').setView([51.505, -0.09], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox.streets',
  // accessToken: 'pk.eyJ1IjoidGlja2l0IiwiYSI6ImNqdGQ5dHd5ODB4ajI0M3BmcGIzd2ozaHAifQ.kcP--rwUzKohsV_AOxMx7Q'
}).addTo(mymap);

var marker = L.marker([51.5, -0.09]).addTo(mymap);

// popups and markers - START
var marker = L.marker([longitude, latitude]).addTo(mymap);
marker.bindPopup("This is your tick." + date.toString() + e.latlng.toString()).openPopup();
var popup = L.popup();

function onMapClick(e) {
  popup
    .setLatLng(e.latlng)
    .setContent("You clicked the map at " + e.latlng.toString())
    .openOn(mymap);
}

mymap.on('click', onMapClick);

// popups and markers - END

marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();

var popup = L.popup()
  .setLatLng([51.5, -0.07])
  .setContent("I am a standalone popup.")
  .openOn(mymap);

mymap.addControl(new L.Control.Fullscreen());