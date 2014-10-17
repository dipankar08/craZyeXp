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

/* ============== End of code ============== */
})

