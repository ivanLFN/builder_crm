$(document).ready(function() {
    $('#keywords-input').on('input', function() {
        var keywords = $(this).val();
        if (keywords.trim() === '') {
            $('#search-results').empty();
        } else {
            $.ajax({
                url: '/crm/search/',
                type: 'GET',
                data: {keywords: keywords},
                success: function(data) {
                    $('#search-results').html(data);
                }
            });
        }
    });
});