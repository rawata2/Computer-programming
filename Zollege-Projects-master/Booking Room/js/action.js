$(document).ready(function() {
    $('#book').click(function() {
        $.ajax({
            url: "https://itp-module-x14346081.c9users.io/booking.php"
        }).done(function(data) {
            $('#magicdiv').html(data);
        });
    });
    $('#register').click(function() {
        $.ajax({
            url: "https://itp-module-x14346081.c9users.io/room.php"
        }).done(function(data) {
            $('#magicdiv').html(data);
        });
    });
});

//hide div when clicked again