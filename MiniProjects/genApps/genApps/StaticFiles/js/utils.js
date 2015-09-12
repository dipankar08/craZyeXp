/**********************************************************************
* Introducing utils.js. The aim is to support all common JS functionality 
* across the all website you developed. 
* Please move all the common lib here only
* date: 9/8/2015 by dipankar dutta
* How to use : Just copy <script src="/media/js/utils.js"></script>
**********************************************************************/

var DEBUG = true ; //<<<<<<<<<<<<<< MAKE IT TRUE FOR LOGGING


function resetUrl(i){
    window.history.pushState('page2', 'Title', '/cleancode/'+i+'/');
}
/*******************************  H E L P E R ********************************/
function log(msg,color,level){
 // console.log(msg);
    if(level == undefined) level=""
    if(color ==  undefined) color="#980c8b"
    var err = new Error();
    var line = err.stack.split('\n')[1]
 console.log("%c"+ '>>> '+level + '[ '+ line.substring(line.lastIndexOf("/")+1,line.length) +' ]: '+ msg,"color:" + color + ";font-weight:bold;") 
}

/*******************************************************************************************
    Implementation of circle Timer
*******************************************************************************************/
function timer_start(time){
    if (time == undefined ) time = 10    
    time =10
    var initialOffset = '440';
    var i = 1
    $("#svgid").empty();
    $('#svgid').html( '<g><title>Layer 1</title><circle id="circle" class="circle_animation" r="30" cy="34" cx="36" stroke-width="6" stroke="#ff5722" fill="none"/> </g>');
    var interval = setInterval(function() {
        $('.circle_timer .circle_animation').css('stroke-dashoffset', initialOffset-(i*(initialOffset/time)));
        $('.circle_timer span').text(time-i);
        if (i == time) {
            clearInterval(interval);
        }
        i++;  
    }, 1000);
}

/******************************** L O A D J S / C S S **********************************/
function loadJS(file) {
    var jsElm = document.createElement("script");
    jsElm.type = "application/javascript";
    jsElm.src = file;
    document.body.appendChild(jsElm);
    log('Loding js #'+file);
}
function loadCSS(file) {
    var jsElm = document.createElement("link");
    jsElm.rel = 'stylesheet'
    jsElm.type = 'text/css'
    jsElm.href = file;
    document.head.appendChild(jsElm);
    log('Loding js #'+file);
}
function loadCSSInline(data) {
    var style = document.createElement("style");
    style.type = 'text/css';
    style.innerHTML = data
    document.head.appendChild(style);
    log('Applying inline CSS #'+data);
}

/******************************** L O A D J S / C S S V2 with call backs. **************
Example:
lazyScriptLoading(['https://cdn.firebase.com/js/client/2.2.4/firebase.js',
                'https://cdn.firebase.com/libs/firepad/1.1.0/firepad.min.js',
                "https://cdn.firebase.com/libs/firepad/1.1.0/firepad.css"],init)
                
****************************************************************************************/
function _loadJS1(scriptURL, onloadCB) {
    log('Start loading.. : '+scriptURL)
      var scriptEl    = document.createElement("script");
      scriptEl.type   = "text/javascript";
      scriptEl.src    = scriptURL;
      function calltheCBcmn() {
        onloadCB(scriptURL);
        log('Loaded: '+scriptURL)
      }
      if(typeof(scriptEl.addEventListener) != 'undefined') {
        scriptEl.addEventListener('load',calltheCBcmn,false);
      }
      else {
        function handleIeState() {
          if(scriptEl.readyState == 'loaded'){
            calltheCBcmn(scriptURL);
            log('Loaded: '+scriptURL)
          }
        }
        var ret = scriptEl.attachEvent('onreadystatechange',handleIeState);
      }
      document.getElementsByTagName("head")[0].appendChild(scriptEl);
}
/*************************************
    This function Ensure that we perform some action when completion of all load of fileList 
**************************************/
function lazyScriptLoading(fileList,onloadCallback){
    if( fileList.length == 1){ // this is the last script..
        _loadJS1(fileList[0], onloadCallback);
    }
    else{
        now = fileList.shift()
          _loadJS1(now, function(){lazyScriptLoading(fileList,onloadCallback)});
        }
}

/* Example:
<button onclick="loadJS('file1.js');">Load file1.js</button>
<button onclick="loadJS('file2.js');">Load file2.js</button>
*/


/**************************************************************** 
     Mereg Two Javascript Objcet : Second Overwrite first 
****************************************************************/
function merge(obj1,obj2){
    var obj3 = {};
    for (var attrname in obj1) { obj3[attrname] = obj1[attrname]; }
    for (var attrname in obj2) { obj3[attrname] = obj2[attrname]; }
    return obj3;
}


/****************************************************************
    //sleep : You can use the following code to simulate a sleep for short periods of time:
********************************************************************/
function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}


/*****************************************************************
     Cookie Operation 
*****************************************************************/
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires+ "; path=/";
} 
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}
function eraseCookie(cname) {
    setCookie(cname,"",-1);
}


/********************************************************************
  Resolve Unicode: Clear Unicode as backed dent support this 
********************************************************************/
function solveUnicode(str){
   str = str.replace(/’/g, "'");
   str = str.replace(/‘/g, "'");
   str = str.replace(/“/g, '"');
   str = str.replace(/”/g, '"'); 
   
   str = str.replace(/”/g, '"'); 
   str = str.replace(/”/g, '"'); 
   str = str.replace(/”/g, '"'); 
   return str;
}
function RemoveWhiteChar(a){
    return a.replace(/\s+|\s+$/gm,'').trim(); 
}

/********************************************************************
  getRandom() : Will return random of 16 length
********************************************************************/
function genRandomString(length, chars) {
    var result = '';
    for (var i = length; i > 0; --i) result += chars[Math.round(Math.random() * (chars.length - 1))];
    return result;
}
function getRandom(){
    return genRandomString(4, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ');
}


/********************************************************************
  window.onerror: Print Explictly Javascript Error.
********************************************************************/
/*
window.onerror = function(msg, url, linenumber, column, errorObj)  { 
    if(errorObj !== undefined) //so it won't blow up in the rest of the browsers
        log('Error: ' + errorObj.stack,"","red");
    alert('Error In page: '+msg+'\n\nURL: '+url+'\n\nBackTrace: '+errorObj.stack);
    return true;
}
*/
/**********************************************************
    DOM Manipulation Quick Function function 
************************************************************/
function show(id){$(id).show();}
function hide(id){$(id).hide();}
function toggle(id){$(id).toggle();}



/**********************************************************
    ShowHide Tab based on click.
************************************************************/
function autoDetectToggleSilde(menuId,targetId,animation){
    //var menuParent = 
    animation = 'overlap_opicity'
    var targetMenu = $(menuId)
    var targetDiv = $(targetId).children().eq(targetMenu.index())
    var activeMenu = $(menuId).siblings(".active")
    var activeDiv = $(targetId).children().eq(activeMenu.index())
    if(animation == undefined){
        activeDiv.fadeOut(200,function(){
            activeMenu.removeClass('active');
            targetMenu.addClass('active') 
            targetDiv.fadeIn(200, function(){            
                activeDiv.removeClass('active');
                targetDiv.addClass('active')            
            });
        });
    }
    else if(animation == 'overlap_opicity'){ // div operlap just cahnge the opicity..
            activeMenu.removeClass('active');
            targetMenu.addClass('active')            
            activeDiv.removeClass('active');
            targetDiv.addClass('active')            
    } // End of overlap_opicity

    /*
    activeDiv.fadeOut(500);
    targetDiv.fadeIn(500);
                activeMenu.removeClass('active');
            activeDiv.removeClass('active');
            targetDiv.addClass('active')
            targetMenu.addClass('active')
    */
}

function autoDetectToggleSildeNext(menuId,targetId){
    //TODO
    animation = 'overlap_opicity'
    var targetMenu = $(menuId)
    var targetDiv = $(targetId).children().eq(targetMenu.index())
    var activeMenu = $(menuId).siblings(".active")
    var activeDiv = $(targetId).children().eq(activeMenu.index())
    if(animation == undefined){
        activeDiv.fadeOut(200,function(){
            activeMenu.removeClass('active');
            targetMenu.addClass('active') 
            targetDiv.fadeIn(200, function(){            
                activeDiv.removeClass('active');
                targetDiv.addClass('active')            
            });
        });
    }
    else if(animation == 'overlap_opicity'){ // div operlap just cahnge the opicity..
            activeMenu.removeClass('active');
            targetMenu.addClass('active')            
            activeDiv.removeClass('active');
            targetDiv.addClass('active')            
    } // End of overlap_opicity

    /*
    activeDiv.fadeOut(500);
    targetDiv.fadeIn(500);
                activeMenu.removeClass('active');
            activeDiv.removeClass('active');
            targetDiv.addClass('active')
            targetMenu.addClass('active')
    */
}
/**********************************************************
    AJAX API CALL WRAPPER 
************************************************************/
function call_backend_api(type,url,param,before_cb,success_cb,error_cb,complete_cb,contentType){
    if (type == undefined || type == null){ type = 'GET';}
    if (param == undefined || param == null){ param = {}}
    if(url == undefined || url == null ){log('USE: call_backend_api(type,url,param,before_cb,success_cb,error_cb)','green');return;}
    if(contentType == undefined) { contentType =  'application/x-www-form-urlencoded; charset=utf-8'  }
    $.ajax({
        type: type,
        url: url,
        data: param,
        contentType:  contentType,
        processData: true,
        beforeSend: function() {
          log('************************ A J A X Started ******************' )
          if(!jQuery.isFunction(before_cb)){
            log('Suugestion: before_cb not implemented' )
          }else{
            before_cb();
          }
        },
        success: function(data) {
            if(data.status != 'error'){ /* Success or info */
                  if(!jQuery.isFunction(success_cb)){
                    log('Suugestion: success_cb not implemented','gray' )
                  }else{
                    success_cb(data);
                  }
            }
            else{
                if(!jQuery.isFunction(error_cb)){
                    log('Suugestion: error_cb not implemented','gray' )
                  }else{
                    error_cb(data);
                  }
            }   
            
        },
        error: function(xhr) { // if error occured
            if(! jQuery.isFunction(error_cb)){
                log('Suugestion: error_cb not implemented','gray' )
            }else{
                error_cb(xhr);
            }
        },
        complete: function() {
            if(! jQuery.isFunction(complete_cb)){
                log('Suugestion: complete_cb not implemented','gray' )
            }else{
                complete_cb();
            }
           log('************************ A J A X Completed ******************' )
        },
        
        //We might have a Progress bar ..
        xhr: function() {
            var xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener("progress", function(evt) {
                if (evt.lengthComputable) {
                    var percentComplete = evt.loaded / evt.total;
                    //Do something with upload progress here
                }
           }, false);
           xhr.addEventListener("progress", function(evt) {
               if (evt.lengthComputable) {
                   var percentComplete = evt.loaded / evt.total;
                   console.log(percentComplete);
               }
           }, false);
           return xhr;
        },
        
    });
}

/*############################################################################
    Please add common function top of this line 
    Below This line we have all COMMON Cleancode Related HTML Handling JS  

##############################################################################/

/********************* WinStylePopUp *********************************************/
function showWinStylePopup(title, desc, is_cancel_able,yes_txt, yes_cb, no_txt,no_cb){
    var dismiss_me = function(){
        $("#common_pop_up").hide();
        $("#overlay").hide();
    }
    $("#overlay").show()
    $("#common_pop_up .title").html(title);
    $("#common_pop_up .desc").html(desc); 
    $("#common_pop_up button.yes").html((yes_txt==undefined)?'Yes':yes_txt).show().off("click").click(dismiss_me)
    $("#common_pop_up button.no").html((no_txt==undefined)?'Close':no_txt).show().off("click").click(dismiss_me)

    if(jQuery.isFunction(yes_cb)){
        $("#common_pop_up button.yes").click(function(){yes_cb();dismiss_me();})
    }
    if(jQuery.isFunction(no_cb)){
        $("#common_pop_up buttn.no").click(function(){no_cb();dismiss_me();})
    } 
    if(!is_cancel_able ){
        $("#common_pop_up button.no").hide()
    }

    $("#common_pop_up").show()
}
function dismissWinStylePopup(){
    var dismiss_me = function(){
        $("#common_pop_up").hide();
        $("#overlay").hide();
    }
    dismiss_me();
}

/********************* R E C T  P O P U P ********************************************/
function openRectPopUP(id,cb){
   // $("#container").css("opacity",0.15)
    $("#overlay").show()
    $(id).show();
    if(cb != undefined){cb();}
}
function dismissRectPopUP(id,cb){
   $(id).hide();
   $("#overlay").hide();
   if(cb != undefined){cb();}
}
/**********************************************************
    BROWSER PLM STUFF
************************************************************/
window.onbeforeunload= function(){    
    //showWinStylePopup("You are about to leave your page!", "Looks like you are about to close page or navigate outside. Are you sure you want to leave? Your un-save data will be lost!", true,"yes", function(){return 'You have unsaved changes!';;}, "Cancel",function(){return 'You have unsaved changes!';})
    return 'You have unsaved changes!';    
}

/**********************************************************
    E R R O R  P O P U P / T E L E M E T R Y 
************************************************************/
if (!DEBUG){
    window.onerror = function(msg, url, linenumber, column, errorObj)  { 
        var t =''
        if(errorObj !== undefined) //so it won't blow up in the rest of the browsers
            t = errorObj.stack
        log('Error: ' +t ,"","red");
        //showWinStylePopup(title, desc, is_cancel_able,yes_txt, yes_cb, no_txt,no_cb)
        showWinStylePopup("Does that mean I am not mature ?", "I though that I am mature, but I am not :( Here is why ?<br><br><div style='color: #771045; font-family: monospace;font-size: 14px;border-left: 3px solid;padding-left: 16px;margin:10px 0;}>'>"+t+"</div> <br> We have some internal server error and I am working hard to fix that.. Please stay back and relux until I fix it! ",true,'Report me','yes_cb','Close','no_cb')
        //alert('Error In page: '+msg+'\n\nURL: '+url+'\n\nBackTrace: '+errorObj.stack);
        return true;
    }
}

/**********************************************************
    SHORT CUT KEY FOR CTRL + L
************************************************************/
function showKeyCode(e) {
    var keycode;
    if (window.event)
        keycode = window.event.keyCode;
    else if (e)
        keycode = e.which;

    // Mozilla firefox
    if ($.browser.mozilla) {
        if ((e.ctrlKey && keycode == 103)) {
            ctrlG();
            //disable default action 
            if (e.preventDefault) {
                e.preventDefault();
                e.stopPropagation();
            }
        }
    }
    // IE
    else if ($.browser.msie) {
        if ((window.event.ctrlKey && keycode == 103)) {
            ctrlG();
            //disable default action 
            window.event.returnValue = false;
            window.event.keyCode = 0;
            window.status = "Refresh is disabled";
        }
    }
    //chrome..
    else { 
        if(e.ctrlKey && e.keyCode == 103 ){
            ctrlG();
            //disable default action 
            event.returnValue = false;
            event.keyCode = 0;
            window.status = "Refresh is disabled";
            

        }
    }
    
  //if(e.ctrlKey && e.keyCode == 103 ){
  function ctrlG(){  
      var person = prompt("Enter ID:", "2");
      if (person != null) {
          window.location.href = '/cleancode/'+person +'/';
      }
  }

}