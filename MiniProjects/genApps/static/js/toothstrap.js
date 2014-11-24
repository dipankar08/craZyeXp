/* ToothStrap JS Effect Here */
/* This file contsins common JS */
$(document).ready(function() {
 
/* ============== Start of code ============== */


/*== Q2 sliding tabs ========================= */
//$("#div-nav-bar .data>div).hide();
$("#div-nav-bar .menu li").click(function(){
  $("#div-nav-bar .menu li").removeClass("active");
  $(this).addClass("active");  
  
  /* Animation Rule Here*/
  if($("#div-nav-bar").hasClass("use-animation-slide"))
  {
   $("#div-nav-bar .data > div").hide();
   $("#div-nav-bar .data div#"+$(this).attr("target-id")).slideDown("slow"); 
  }
  else{
    $("#div-nav-bar .data > div").hide();
    $("#div-nav-bar .data div#"+$(this).attr("target-id")).fadeIn("slow"); 
  }  
});

$(".onflyout").toggle('click', function(){
var a= $(this).data('flyout');
$("#flyout."+a.cls).css("top",a.top);
$("#flyout."+a.cls).css("left",a.left);
}); 

/* ============== End of code ============== */


/**********************Start Overlay-Popup ******************/
 window.showPopup = function(idname){
        $('html').addClass('overlay');
        $(idname).addClass('animated');
        if($(idname).hasClass('RightSlide')){
        $(idname).removeClass('lightSpeedOut').addClass('lightSpeedIn');
        }
        else{
          $(idname).removeClass('flipOutY').addClass('flipInY');
        }
        $(idname).addClass('visible');
}

$(document).keyup(function (e) {
        if (e.keyCode == 27 && $('html').hasClass('overlay')) {
            clearPopup_box();
        }
});

$('.popup-exit').click(function () {clearPopup_box(); });
$('.popup-overlay').click(function () { clearPopup_box();});

function clearPopup_box() {
  if($('.popup.visible').hasClass('RightSlide')){
  $('.popup.visible').removeClass('lightSpeedIn').addClass('lightSpeedOut');
  }
  else{
  $('.popup.visible').removeClass('flipInY').addClass('flipOutY');
  }
  //$('.popup.visible').removeClass('visible');
  
 // $('html').removeClass('overlay');
  }
  
/**********************Start Overlay-Popup ******************/
 
})

