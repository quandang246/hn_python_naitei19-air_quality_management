// Initialize the map
var map = L.map('map').setView([21.024, 105.85], 13);

// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Add a marker and update the hidden input fields when the user clicks on the map
var marker;
map.on('click', function(e) {
    var latitudeField = document.getElementById('latitude');
    var longitudeField = document.getElementById('longitude');

    if (!latitudeField || !longitudeField) {
        // Create the hidden input fields if they don't exist
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
        form.appendChild(latitudeField);
        form.appendChild(longitudeField);
    }

    // Update the hidden input fields with the latitude and longitude values
    latitudeField.value = e.latlng.lat;
    longitudeField.value = e.latlng.lng;

    // Remove any existing marker and add a new one at the clicked location
    if (marker) {
        map.removeLayer(marker);
    }
    marker = L.marker(e.latlng).addTo(map)
        .bindPopup('This is your chosen location.<br> LMAO')
        .openPopup();
});