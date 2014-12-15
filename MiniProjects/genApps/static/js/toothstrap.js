/* ToothStrap JS Effect Here */
/* This file contsins common JS */
$(document).ready(function() {
 
/* ============== Start of code ============== */

/******** usefull functions here **************/
window.addClass = function(ele,cls){
  console.log('>>> adding calss '+cls+' to element '+ele);
  $(ele).addClass(cls);
 };
window.removeClass = function(ele,cls){
  console.log('>>> removing calss '+cls+' to element '+ele);
  $(ele).removeClass(cls);
 };
window.toggleClass = function(ele,cls){
  console.log('>>> toggleing calss '+cls+' to element '+ele);
  if( $(ele).hasClass(cls))
  {
    $(ele).removeClass(cls);
  }
  else{
    $(ele).addClass(cls);
  }
 };
/******** endusefull functions here **************/





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

/****************** Menu *******************/
window.toggleMenu  = function(elem){
 if($(".menu").hasClass("hide-sidebar"))
 { //show it.. 
 $(".menu").removeClass("hide-sidebar");
 $(".menu .nav span").fadeIn("slow", function(){
   $(".menu .logo").fadeIn("slow");
   });
 }
 else{
 //hide it
 $(".menu .logo").fadeOut("slow",function(){
    $(".menu .nav span").hide();
 });
 $(".menu").addClass("hide-sidebar");
 }
}

/********************Action Hide and Show on Hover and Click ***************/
/* This will add / remove class on hover or click */
 $('.toggle_open_class_on_hover_click').bind({
  mouseenter: function(e) {
  // Hover event handler
  $(this).addClass("open")
  },
  mouseleave: function(e) {
   $(this).removeClass("open")
  },
  click: function(e) {
  if($(this).hasClass("open")){
  $(this).removeClass("open");
  }
  else{
  $(this).addClass("open")
  }
  },
  blur: function(e) {
  $(this).removeClass("open")
  }
 });
/********************** End of this action *********************************/
 
 
/* End of document ready*/ 
/* End of document ready*/ 
})



/*full screen */

