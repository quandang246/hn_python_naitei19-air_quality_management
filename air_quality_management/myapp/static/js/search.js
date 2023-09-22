$(document).ready(function () {
    $('#searchInput').on('input', function () {
        // Get the search input value
        var searchValue = $(this).val().toLowerCase();

        // Loop through table rows
        $('table tbody tr').each(function () {
            var row = $(this);
            var rowText = row.text().toLowerCase();

            // Check if the row contains the search value
            if (rowText.includes(searchValue)) {
                row.show();
            } else {
                row.hide();
            }
        });
    });
});
