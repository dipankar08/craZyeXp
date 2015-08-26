/**********************************************************************
* Introducing utils.js. The aim is to support all common JS functionality 
* across the all website you developed. 
* Please move all the common lib here only
* date: 9/8/2015 by dipankar dutta
* How to use : Just copy <script src="/media/js/utils.js"></script>
**********************************************************************/

/*******************************  H E L P E R ********************************/
function log(msg,level,color){
    if(level == undefined) level=""
    if(color ==  undefined) color="#980c8b"
    var err = new Error();
    var line = err.stack.split('\n')[1]
    console.log("%c"+ '>>> '+level + '[ '+ line.substring(line.lastIndexOf("/")+1,line.length) +' ]: '+ msg,"color:" + color + ";font-weight:bold;")
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
window.onerror = function(msg, url, linenumber, column, errorObj)  { 
    if(errorObj !== undefined) //so it won't blow up in the rest of the browsers
        log('Error: ' + errorObj.stack,"","red");
    alert('Error In page: '+msg+'\n\nURL: '+url+'\n\nBackTrace: '+errorObj.stack);
    return true;
}

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
/*############################################################################
    Please add common function top of this line 
    Below This line we have all COMMON Cleancode Related HTML Handling JS  

##############################################################################/

/********************* WinStylePopUp *********************************************/
function showWinStylePopup(title, desc, type, yes_txt, no_txt, yes_cb, no_cb){
  var dismiss_me = function(){
     $("#common_pop_up").hide();
     $("#overlay").hide();
  }
  $("#overlay").show()
  $("#common_pop_up .title").html(title);
  $("#common_pop_up .desc").html(desc); 
  $("#common_pop_up button.yes").html(yes_txt)
  $("#common_pop_up button.no").html(no_txt)
  if(yes_cb != undefined){
     $("#common_pop_up button.yes").click(function(){yes_cb();dismiss_me();})
  }
  else{
     $("#common_pop_up button.yes").click(dismiss_me)
  }
  if(no_cb != undefined){
     $("#common_pop_up buttn.no").click(function(){no_cb();dismiss_me();})
  }
  else{
    $("#common_pop_up button.no").click(dismiss_me)
  }    
  if(type != 'confirm'){
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
