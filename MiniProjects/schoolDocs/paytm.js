/* This file contsins common JS */
$(document).ready(function() {
 
/* ============== Start of code ============== */
 
 /*==========Q5 popup ================ */
 
$('[data-popup-target]').click(function () {
        $('html').addClass('overlay');
        var activePopup = $(this).attr('data-popup-target');
        $(activePopup).addClass('visible');
});
$(document).keyup(function (e) {
        if (e.keyCode == 27 && $('html').hasClass('overlay')) {
            clearPopup();
        }
});

$('.popup-exit').click(function () {clearPopup(); });
$('.popup-overlay').click(function () { clearPopup();});

function clearPopup() {
  $('.popup.visible').addClass('transitioning').removeClass('visible');
  $('html').removeClass('overlay');
  setTimeout(function () {
    $('.popup').removeClass('transitioning');
    }, 200);
  }
 
/*Q. 11 youtube bar */
$({property: 0}).animate({property: 105}, {
    duration: 4000,
    step: function() {
        var _percent = Math.round(this.property);
        $('#progress').css('width',  _percent+"%");
        if(_percent == 105) {
            $("#progress").addClass("done");
        }
    },
    complete: function() {
        alert('complete');
    }
});



 
/* ============== End of code ============== */
})