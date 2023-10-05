    google.charts.load('current', { packages: ['corechart'] });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        // Create a DataTable for the Google Chart
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Location');
        data.addColumn('number', 'Air Quality Index');

        // Get a reference to the table
        var table = document.getElementById('dataTable');
        var rows = table.getElementsByTagName('tr');

        // Loop through the table rows (skip the header row)
        for (var i = 1; i < rows.length; i++) {
            var cells = rows[i].getElementsByTagName('td');
            var city = cells[0].textContent; // Extract the city
            var airQualityIndex = parseFloat(cells[1].textContent); // Extract the air quality index as a number

            // Add the data to the DataTable
            data.addRow([city, airQualityIndex]);
        }

        // Set chart options
        var options = {
            title: 'Air Quality Index by City',
            // Other chart options here
        };

        // Create and draw the chart
        var chart = new google.visualization.BarChart(document.getElementById('myChart'));
        chart.draw(data, options);
    }
