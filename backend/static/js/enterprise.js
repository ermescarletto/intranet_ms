$(document).ready(function () {
    // Get the modal element
    var modal = $('#logoutModal');

    // Get the button that opens the modal
    var logoutButton = $('#logoutButton');

    // Get the <span> element that closes the modal
    var span = $('.close', modal);

    // When the user clicks the button, open the modal
    logoutButton.on('click', function () {
        modal.css('display', 'block');
    });

    // When the user clicks on <span> (x), close the modal
    span.on('click', function () {
        modal.css('display', 'none');
    });

    // When the user clicks anywhere outside of the modal, close it
    $(window).on('click', function (event) {
        if (event.target === modal[0]) {
            modal.css('display', 'none');
        }
    });

    // Confirm logout

});