// Initialize the map
var map = L.map('map').setView([21.005315, 105.843036], 17);

// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Add a marker and update the hidden input fields when the user clicks on the map
var marker;
var city;
var fulladdr;
map.on('click', function(e) {
    var locationField = document.getElementById('location')
    var latitudeField = document.getElementById('latitude');
    var longitudeField = document.getElementById('longitude');

    if (!latitudeField || !longitudeField) {
        // Create the hidden input fields if they don't exist
        locationField = document.createElement('input');
        locationField.type = 'hidden';
        locationField.id = 'location';
        locationField.name = 'location';

        latitudeField = document.createElement('input');
        latitudeField.type = 'hidden';
        latitudeField.id = 'latitude';
        latitudeField.name = 'latitude';

        longitudeField = document.createElement('input');
        longitudeField.type = 'hidden';
        longitudeField.id = 'longitude';
        longitudeField.name = 'longitude';

        // Append the fields to the form
        var form = document.getElementById('report-form');
        form.appendChild(locationField);
        form.appendChild(latitudeField);
        form.appendChild(longitudeField);
    }

    // Remove any existing marker and add a new one at the clicked location
    if (marker) {
        map.removeLayer(marker);
    }

    fetch(`https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode?f=pjson&langCode=EN&location=${e.latlng.lng},${e.latlng.lat}`)
        .then(res => res.json())
        .then(myJson => {
            city = myJson.address.City;
            fulladdr = myJson.address.LongLabel;
            locationField.value = city;
            latitudeField.value = e.latlng.lat;
            longitudeField.value = e.latlng.lng;
            var popupContent = "<b>This is your chosen address:<br></b>" + fulladdr;
            var popup = L.popup().setContent(popupContent);
            marker = L.marker(e.latlng).addTo(map).bindPopup(popup).openPopup();
            console.log(myJson.address);
        });
});
