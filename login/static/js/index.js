$('.toggle').on('click', function() {
  $('.container').stop().addClass('active');
});

$('.close').on('click', function() {
  $('.container').stop().removeClass('active');
});

function countdown() {
    seconds = $('.count-down').text();
    if (seconds == 1) {
//        $('.growl-container').toggle( 'bounce', { times: 5 }, "slow" );
//        return;
        $('.growl-container').fadeTo(0, 500).slideUp(500, function(){
            $('.growl-container').slideUp(500);
        });
    }
    seconds--;
    $(".count-down").html(seconds);
    var timeoutMyOswego = setTimeout(countdown, 1000);
}

$("#Register_Username").change(function () {
    var username = $(this).val();
    $(".count-down").html(5);
    $.ajax({
        url: '/ajax/validate_username/',
        data: {
          'username': username
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                $(".growl-container").show();
                countdown();
                $('#register_button').addClass('button-notdisplay');
            }
            else{
                $('#register_button').removeClass('button-notdisplay');
            }
        }
    });

});

