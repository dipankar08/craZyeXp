/* This is base.js file */

/* This file contsins common JS */
$(document).ready(function() {
 
/* ============== Start of code ============== */


/*== Q2 sliding tabs ========================= */
$("#hr-tab .tabs li").click(function(){
  console.log("#hr-tab .data div."+$(this).attr("target-id")) 
  $("#hr-tab .tabs li").removeClass("active");
  $(this).addClass("active");
  
  $("#hr-tab .data div").hide();
  $("#hr-tab .data div#"+$(this).attr("id")).fadeIn("slow");  
  
});


/*==========Q5 popup ================ */
 /*
$('[data-popup-target]').click(function () {
        $('html').addClass('overlay');
        var activePopup = $(this).attr('data-popup-target');
        $(activePopup).addClass('visible');
});
$(document).keyup(function (e) {
        if (e.keyCode == 27 && $('html').hasClass('overlay')) {
            clearPopup_box();
        }
});

$('.popup-exit').click(function () {clearPopup_box(); });
$('.popup-overlay').click(function () { clearPopup_box();});

function clearPopup_box() {
  $('.popup.visible').addClass('transitioning').removeClass('visible');
  $('html').removeClass('overlay');
  setTimeout(function () {
    $('.popup').removeClass('transitioning');
    }, 200);
  }
  
 */
/*Q5A -- POPUP-SIDEBAR-- */

$('.popup-sidebar-link').click(function () {
        $('html').addClass('overlay');
        $('.popup-sidebar-data').animate({width:"400px"});
});

$(document).keyup(function (e) {
  if (e.keyCode == 27 && $('html').hasClass('overlay')) {             clear_popup_sidebar() ;
        }
});
$('.popup-exit').click(function () { clear_popup_sidebar() ;});
$('.popup-overlay').click(function () { clear_popup_sidebar();});

function clear_popup_sidebar() {
  //$('.popup-sidebar-data').addClass('hide');
  $('.popup-sidebar-data').animate({width:"0px"});
  $('html').removeClass('overlay');
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
       // alert('complete');
    }
});

/*Q13 Majic line */
/*
 var $el, leftPos, newWidth,
        $mainNav = $("#example-one");
    
    $mainNav.append("<li id='magic-line'></li>");
    var $magicLine = $("#magic-line");
    
    $magicLine
        .width($(".current_page_item").width())
        .css("left", $(".current_page_item a").position().left)
        .data("origLeft", $magicLine.position().left)
        .data("origWidth", $magicLine.width());
        
    $("#example-one li a").hover(function() {
        $el = $(this);
        leftPos = $el.position().left;
        newWidth = $el.parent().width();
        $magicLine.stop().animate({
            left: leftPos,
            width: newWidth
        });
    }, function() {
        $magicLine.stop().animate({
            left: $magicLine.data("origLeft"),
            width: $magicLine.data("origWidth")
        });    
    });
*/
/*Q14 Colupsable List*/
$("#CollapseList .item").click(function(){

  var x = $(this).find(".details").hasClass("hide");
  $("#CollapseList .details").addClass("hide"); //hide all
  
  if(x){
//  $(this).find(".details").slideDown( 'slow')
  $(this).find(".details").removeClass("hide") //show this
  }
});


/* ============== End of code ============== */
})


 
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


/*****************  Start full screen ***********************/
window.toggleFullScreen  = function(elem) {
    if ((document.fullScreenElement && document.fullScreenElement !== null) || (document.msfullscreenElement && document.msfullscreenElement !== null) || (!document.mozFullScreen && !document.webkitIsFullScreen)) {
        if (elem.requestFullScreen) {
            elem.requestFullScreen();
        } else if (elem.mozRequestFullScreen) {
            elem.mozRequestFullScreen();
        } else if (elem.webkitRequestFullScreen) {
            elem.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
        } else if (elem.msRequestFullscreen) {
            elem.msRequestFullscreen();
        }
       $( "body" ).addClass( "fullscreen" )
    } else {
        if (document.cancelFullScreen) {
            document.cancelFullScreen();
        } else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
        } else if (document.webkitCancelFullScreen) {
            document.webkitCancelFullScreen();
        } else if (document.msExitFullscreen) {
            document.msExitFullscreen();
        }
         $( "body" ).removeClass( "fullscreen" )
    }
}
/************** End of fll screen ******************************/


 
})



/*full screen */

