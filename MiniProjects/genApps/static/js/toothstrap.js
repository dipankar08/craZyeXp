/* ToothStrap JS Effect Here */
/* This file contsins common JS */
$(document).ready(function() {
 
/* ============== Start of code ============== */

/**************** usefull functions here **************/
/* 
ele: element to add classm 
cls:which calls to be added
how: up-go up
cur: pass this variable for refer
Example: onclick="toggleClass('.has-sub','opened','up',this)"
*/

window.addClass = function(ele,cls,how,cur){
  console.log('>>> adding calss '+cls+' to element <'+cur+'>on<'+how+'>');
  var x;
  if(how == 'up'){ x=$(cur).closest(ele);}
  else{  x = $(ele) }
  console.log('Effeted Element :')
  console.log(x);
  x.addClass(cls);  
 };
window.removeClass = function(ele,cls,how,cur){
  console.log('>>> removing calss '+cls+' to element '+ele+'on'+how);
  var x;
  if(how == 'up'){ x=$(cur).closest(ele); }
  else{ x = $(ele) }  
  x.removeClass(cls);
 };

window.toggleClass = function(ele,cls,how,cur){
  console.log('>>> toggleing calss '+cls+' to element '+ele+'on'+how);
  var x;
  if(how == 'up'){ x=$(cur).closest(ele); }
  else{  x = $(ele) }
  
  console.log('Effeted Element :')
  console.log(x);
  if( x.hasClass(cls)) {
    x.removeClass(cls);
  }
  else{
    x.addClass(cls);
  }
 };
 
/* serializeFrom: Extract the value of a from  */
window.serializeFrom  = function(ele){
  var a = $(ele).serializeArray();
  var m = {}
  a.forEach(function(entry) {
    if(m.hasOwnProperty(entry.name)){
       m[entry.name]=m[entry.name]+','+entry.value
    }
    else{
       m[entry.name]=entry.value
    }
  });
  return m;
}
/* mergeObj: Merge two Object */
window.mergeObj  = function (obj1,obj2){
    var obj3 = {};
    for (var attrname in obj1) { obj3[attrname] = obj1[attrname]; }
    for (var attrname in obj2) { obj3[attrname] = obj2[attrname]; }
    return obj3;
}

/******** end usefull functions here **************/

/************  table Resize  ************************/
window.tableResize = function(ele){
console.log('tableResize called for '+ele);
// Change the selector if needed
if (ele){
  var $table = $(ele)
}
else{
var $table = $('.table.scroll')
}
var $bodyCells = $table.find('tbody tr:first').children(), colWidth;

// Adjust the width of thead cells when window resizes
    // Get the tbody columns width array
    colWidth = $bodyCells.map(function() {
        return $(this).width();
    }).get();
    
    // Set the width of thead columns
    $table.find('thead tr').children().each(function(i, v) {
        $(v).width(colWidth[i]);
    });    
    
    //Just do a liner distribution
    $table.find('tr').children().each(function(i, v) {
      $(v).width($('.table.scroll').width()/$bodyCells.length -2);
    }); 
}
/************  table Resize End Here ************************/


/*== Q2 sliding tabs ========================= */
//$("#div-nav-bar .data>div).hide();
$(".menu a").click(function(){
  var uid=$(this).attr('targetid')
  tab = $(this).closest('.tab') 

  tab.find('.menu >a').removeClass('active')
  $(this).addClass('active')
  tab.find('.data > div').removeClass('active')
  tab.find('.data > #'+uid).addClass('active')

});

/*******************  fly out **************/
$(".onflyout").toggle('click', function(){
var a= $(this).data('flyout');
$("#flyout."+a.cls).css("top",a.top);
$("#flyout."+a.cls).css("left",a.left);
}); 

/* ============== End of code ============== */


/**********************Start Overlay-Popup ******************/
 window.showPopup = function(idname){
        $('html').addClass('overlay');
        $(idname).addClass('visible');
        $(idname).addClass('animated');
        if($(idname).hasClass('RightSlide')){
        $(idname).removeClass('lightSpeedOut').addClass('lightSpeedIn');
        }
        if($(idname).hasClass('fromTop')){
        $(idname).removeClass('fadeOutUp').addClass('fadeInDown');
        }
        else{
          $(idname).removeClass('flipOutY').addClass('flipInY');
        }
        
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
  $('.popup').removeClass('lightSpeedIn').addClass('lightSpeedOut');
  }
  else if($('.popup.visible').hasClass('fromTop')){
  $('.popup').removeClass('fadeInDown').addClass('fadeOutUp');
  }
  else{
  $('.popup').removeClass('flipInY').addClass('flipOutY'); 
  }
  setTimeout(function(){
    $('.popup.visible').removeClass('visible');
    $('html').removeClass('overlay');
    },1000);
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

/***************************  Mouse Move *********************/

window.addClassOnMouseMoveZone = function(){  
  var mie = (navigator.appName == "Microsoft Internet Explorer") ? true : false;
  if (!mie) {
       document.captureEvents(Event.MOUSEMOVE);
       document.captureEvents(Event.MOUSEDOWN);
  }
  document.onmousemove = function (e) {mousePos(e);};
  document.onmousedown = function (e) {mouseClicked();};
  var mouseClick;
  var keyClicked;
  var mouseX = 0;
  var mouseY = 0;

  function mousePos (e) {
      if (!mie) {
          mouseX = e.pageX; 
          mouseY = e.pageY;
      }
      else {
          mouseX = event.clientX + document.body.scrollLeft;
          mouseY = event.clientY + document.body.scrollTop;
      }
      // Write your action here..
      if (mouseX <15){$('#menu').addClass('show') } 
      if (mouseX >100){$('#menu').removeClass('show') } 
  }
  function mouseClicked()
  {
    console.log(' mouse click is not impelmenbted yet !')
  }
}
addClassOnMouseMoveZone ();
/*************************** End of  Mouse Move *********************/
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


/***************** Change the Body color ***********************************/
window.autoColor= (function(){
	var hexacode = ['#2B60DE', '#6960EC', '#38ACEC', '#ED7839', '#7DFDFE','#FF7D7D','#347C2C','#BCE954','#AF7817','#493D26','#6F4E37','#6F4E37','#800517'],
	el = document.getElementById('autocolor').style,
	counter = -1,
	hexalen = hexacode.length;
	function auto(){
		el.backgroundColor = hexacode[counter = ++counter % hexalen];
	}
	setInterval(auto, 10000);
});
// shoud call this fynction autoColor();
/***************** End Change the Body color ********************************/
 
/* End of document ready*/ 
/* End of document ready*/ 
})

/******************  Generated Ajax Call Back ***************************
* Example : AjaxCommand(MODEL_NAME,[action],{param},function success(a){})
* AjaxCommand('code','getall',{},function(a){alert(a.msg);})
* AjaxCommand('code','get',{'id':1},function(a){alert(a.msg);})
* AjaxCommand('code','create',{'id':1},function(a){alert(a.msg);})
**************************************************************************/
function AjaxCommand(model,action,param,cb_success,cb_error){
  var url =''
  var type='post'
  /* TODO: We can support many more */
  if (action=="getall"){ url = '/api/'+model+'/',type='get' }
  else if (action=="get"){ url = '/api/'+model+'/'+param.id+'/',type='get' }
  else if(action=="create"){ url = '/api/'+model+'/' }
  else if(action=="update"){ url = '/api/'+model+'/'+param.id+'/' }
  else if (action=="delete"){ url = '/api/'+model+'/'+param.id+'/' }
  else{ url = '/api/cleancode/invalid/' }  
  
  /*Ajax call is here */
  $.ajax({ 
    url: url,
    type: type,
    data: param,
    contentType: 'application/x-www-form-urlencoded; charset=utf-8',  
    processData: true,
    success: function( data, textStatus, jQxhr ){
      console.log(data)
      cb_success(data)
    },
    error: function( jqXhr, textStatus, errorThrown ){
      console.log( errorThrown ); 
    } 
  });
}
/******************  Generated Ajax Call Back ****************************/

/****************** Tree Menu Js ************************/
/* It will do action(add/remove/toggle) a class(class/id) on all sibling of ele(id/class) based on a cond(condition -like hasclass cond)

ele- element whose sibling to be effected
cls - class to be added /removed
cond - if that id has this cls
action - either add/remove/toggle
//TODO : Amke it Generalized. Action in Bulk. 
*/

function actionClassOnSiblingButNotThis(ele,cls,cond,action){
 var sib= ele.parentNode.childNodes
 for( i =0;i<sib.length;i++)
 {
   if( sib[i] != ele && $(sib[i]).hasClass(cond)){
     if(action=='toggle'){$(sib[i]).toggleClass(cls)}
     if(action=='add'){$(sib[i]).addClass(cls)}
     if(action=='remove'){$(sib[i]).removeClass(cls)} 
   }
 }
}

function recur(ll,level){
  var h='<ul>'
  ll.forEach(function(e) {
    var has_child = (e.hasOwnProperty('child') && e.child.length != 0)
    if (has_child){
      h+='<li class="has_child"  style="margin-left:'+level*18+'px">'
      h+='<i class="jstree-icon jstree-ocl"></i>'
      h+='<a onclick="actionClassOnSiblingButNotThis(this.parentNode,\'expanded\',\'has_child\',\'remove\');toggleClass(\'li\',\'expanded\',\'up\',this); " ><i class="fa fa-folder-open-o"></i> '+e.name+'</a>'
      h+= recur(e.child,1)
      h+='</li>'
    }
    else{
      h+='<li style="margin-left:'+level*18+'px">'
      h+='<i class="jstree-icon jstree-ocl"></i>'
      h+='<a> <i class="fa fa-file-o"></i>'+e.name+'</a>'
      h+='</li>'
    }    
  });
  h += '</ul>'
  return h;
}

var a=[
  { 'name':'dd1' },
  {'name':'dd2'},
  {'name':'dd3','child':
    [
        { 'name':'dd31' },
        {'name':'dd32'},
        {'name':'dd33','child':
          [
            { 'name':'dd331'}
          ]
        },
        {'name':'dd33','child':
          [
            { 'name':'dd331'}
          ]
        },
        {'name':'dd33','child':
          [
            { 'name':'dd331'}
          ]
        },
        {'name':'dd33','child':
          [
            { 'name':'dd331'}
          ]
        },
        {'name':'dd33','child':
          [
            { 'name':'dd331'},
            {'name':'dd33','child':
              [
                { 'name':'dd331'},
                {'name':'dd33','child':
                  [
                    { 'name':'dd331'},
                    {'name':'dd33','child':
                              [
                                { 'name':'dd331'}
                              ]
                    }
                  ]
                }
              ]
            }
          ]
        }
    ]
  }
  ]



var html = recur(a,0)
$(document).ready(function() {
$("#test").html(html)

});
/******************  End of Tree Menu Js *****************/
