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
    if(chars == undefined)
        chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
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
    AJAX API CALL WRAPPER  :
    param : is a JavaScript object  
************************************************************/
function call_backend_api(type,url,param,before_cb,success_cb,error_cb,complete_cb,options){
    if (type == undefined || type == null){ type = 'GET';}
    if (param == undefined || param == null){ param = {}}
    if(url == undefined || url == null ){log('USE: call_backend_api(type,url,param,before_cb,success_cb,error_cb)','green');return;}
    
    opt = options || {'contentType':'form'}    
    opt.contentType = (opt.contentType == 'json') ? 'application/json': 'application/x-www-form-urlencoded; charset=utf-8' 
    var lPageLoadIndicator;
    if(opt.load_animation){
        lPageLoadIndicator = new PageLoadIndicator();
    }
    
    if(opt.contentType == 'application/json') { 
        param = JSON.stringify(param);
    }
    $.ajax({
        type: type,
        url: url,
        data: param,
        contentType:  opt.contentType,
        processData: true,
        beforeSend: function() {
          log('************************ A J A X Started ******************' )          
          if(!jQuery.isFunction(before_cb)){
            log('Suugestion: before_cb not implemented' )
          }else{
            before_cb();
          }
        if(opt.load_animation){lPageLoadIndicator.show()}
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
            if(opt.load_animation){lPageLoadIndicator.hide()}
            
            if(!jQuery.isFunction(complete_cb)){
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

/**********************************************************
    Get The document URL
************************************************************/
function getMyURL(){
    res={}
    res.fullurl= location.href
    res.baseurl= location.origin
    res.path = location.path
    return res
}

/**********************************************************
    add HTTP if not 
************************************************************/
function addhttp(url) {
   if (!/^(f|ht)tps?:\/\//i.test(url)) {
      url = "http://" + url;
   }
   return url;
}
/**********************************************************
    Validate Email
************************************************************/
function validateEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
}

/**********************************************************
    Move a div With Mouse Move.
************************************************************/
var mousemove = false;
var mousePosition;
var offset = [0,0];
function linkMouseMoveEvent(id, event) {
        var line = $('#'+$(id).attr('id')+'-line')
        var originX = parseInt(line.css('left'))+line.width;
        var originY = parseInt(line.css('top'))+2;
        
        var length = Math.sqrt((event.pageX - originX) * (event.pageX - originX) 
            + (event.pageY - originY) * (event.pageY - originY));
    
        var angle = 180 / 3.1415 * Math.acos((event.pageY - originY) / length);
        if(event.pageX > originX)
            angle *= -1;
    
        $('#'+$(id).attr('id')+'-line')
            .css('height', length)
            .css('-webkit-transform', 'rotate(' + angle + 'deg)')
            .css('-moz-transform', 'rotate(' + angle + 'deg)')
            .css('-o-transform', 'rotate(' + angle + 'deg)')
            .css('-ms-transform', 'rotate(' + angle + 'deg)')
            .css('transform', 'rotate(' + angle + 'deg)');
}
function REGISTER_DIV_MOVE(){    
    $('body').on('mousedown', '.mousemove', function(event) {
        mousemove = true;
        offset = [
        this.offsetLeft - event.clientX,
        this.offsetTop - event.clientY
        ];
        console.log('Move start...')
        $(this).css('border-color', "#06a")
    });
    
    $('body').on('mouseup', '.mousemove', function(event) {
       $(this).css('border-color', "#ddd")
        mousemove = false;
    });

    $(document).mouseup(function(event){
        mousemove = false;
        console.log('Move done...')
    });
    
    $('body').on('mousemove', '.mousemove', function(event) {
        if(mousemove === false) return;
        mousePosition = {  
            x : event.clientX,
            y : event.clientY    
        };
        this.style.left = (mousePosition.x + offset[0]) + 'px';
        this.style.top  = (mousePosition.y + offset[1]) + 'px';
        linkMouseMoveEvent(this,event);
    });
    // Click Operation..
    $('body').on('click', '.mousemove .close', function() {
        id = $(this).closest('.mousemove').attr('id');
        $('#'+id).hide(); $('#'+id+'-line').hide()
    });
    $('body').on('click', '.mousemove .submit', function() {
        ele = $(this).closest('.mousemove')
        ele.find('.sections').append('<div class="section"><p> '+$(ele).find('textarea').val()+'</p>\
                <div class="action"> <i class="fa fa-thumbs-o-up"></i> <i class="fa fa-reply"></i><i class="fa fa-pencil"></i></div>\
            </div>')
            //Server call.
    });
}
  
$( document ).ready(function() { // Must be enclosed by ready..
    REGISTER_DIV_MOVE();
});

// Adding a New Command Box
function addNewComment(){
    var  range = editors.main.selection.getRange()
    if( JSON.stringify(range.start) === JSON.stringify(range.end) )
    { 
        console.log('No slection '); return;
    }
    id=getRandom()
    comment_html = '\
    <div id="'+id+'" class="mousemove">\
        <div class="comment">\
            <div class="head"> <i class="fa fa-reply-all"></i> <i class="fa fa-minus"></i><i class="fa fa-times close"></i></div>\
            <div class="sections"></div>\
            <div class="editbox"><textarea type="text" ></textarea><div class="action">    <button class="submit"> submit </button><select name="state"><option value="close">Close</option><option value="Wont Fix"> Wornt Fix</option><option value="Resolve">Resolve</option> <option value="active">active</option></select></div></div>\
            <div class="tail"></div>\
        </div>\
    </div>'
    $(document.body).append(comment_html)
    off = addMarkerToTheSelection(id); 
   //adding line.
   setTimeout(function(){ 
         var top1 = $("."+id).offset().top 
         var left1 = $("."+id).offset().left
         $(document.body).append('<div id="'+id+'-line" style="top:'+top1+'px;left:'+left1+'px;" class="line_to_mousemove"></div>');
       }, 3000);   
}
/**********************************************************
   Some ACE Editor related Utility
************************************************************/
function addMarkerToTheSelection(marker_id){
    var  range = editors.main.selection.getRange()
    editors.main.getSession().addMarker(range, "custom_marker "+ marker_id, "line", true);
    return $("."+marker_id).offset(); 
}
/**********************************************************
   Context Menu: To be re factored
************************************************************/
function buildContextMenu(){
    // Trigger action when the contexmenu is about to be shown
    $(document).bind("contextmenu", function (event) {
        event.preventDefault();
        $(".custom-menu").finish().toggle(100).
        css({
            top: event.pageY + "px",
            left: event.pageX + "px"
        });
    });

    // If the document is clicked somewhere
    $(document).bind("mousedown", function (e) {
        if (!$(e.target).parents(".custom-menu").length > 0) { // If the clicked element is not the menu
            $(".custom-menu").hide(100);
        }
    });

    // If the menu element is clicked
    $('body').on('click', '.custom-menu li', function() {
        switch($(this).attr("data-action")) {            
            case "first": addNewComment(); break;
            case "second": alert("second"); break;
            case "third": alert("third"); break;
        }
        $(".custom-menu").hide(100);
      });
    
    // build the Menu and Inject it
    menu_html='\
    <ul class="custom-menu">\
      <li data-action = "first" data-handaler = "first">Add Commnet</li>\
      <li data-action = "second">Second thing</li>\
      <li data-action = "third">Third thing</li>\
    </ul>\
    '
    $(document.body).append(menu_html)
}//buildContextMenu(); << Call this when you want to use it.


/**********************************************************
   DataBindingOnEvent: Dynamic Allocate Elements
   Example: 
    RegisterDataBindingOnEvent('click','div',function(){alert('hello');})
    DeRegisterEvent('click','div')
    DeRegisterDataBindingOnEvent('dblclick','div',function(){alert('hello'); this.contentEditable = true;})
************************************************************/
function RegisterDataBindingOnEvent(ev,ele,clb){
  $(ele).on(ev, clb );
}
function DeRegisterDataBindingOnEvent(ev,ele){
  $(ele).off(ev);
}

/**********************************************************
   get Cuurent time Stamp
************************************************************/
function timeStamp() { 
  var now = new Date();
  var date = [ now.getMonth() + 1, now.getDate(), now.getFullYear() ];
  var time = [ now.getHours(), now.getMinutes(), now.getSeconds() ];
  var suffix = ( time[0] < 12 ) ? "AM" : "PM";
  time[0] = ( time[0] < 12 ) ? time[0] : time[0] - 12;
  time[0] = time[0] || 12;
  for ( var i = 1; i < 3; i++ ) {
    if ( time[i] < 10 ) {
      time[i] = "0" + time[i];
    }
  }
  return date.join("/") + " " + time.join(":") + " " + suffix;
}
/**********************************************************
   AutoRemove Class  : Jquery Extension.
************************************************************/
jQuery.fn.extend({
  addClassVolatile: function(cls,time) {
        var self = this
        self.addClass(cls)
        setTimeout(function() {
            self.removeClass(cls);
        }, 5000);
    },
  switchClass: function(cls1,cls2,target) {
        if (!(target == undefined)){self = $(target);}else{self = this}        
        if(self.hasClass(cls1)){
            self.removeClass(cls1).addClass(cls2);
        }
        else{
            self.removeClass(cls2).addClass(cls1);
        }
    },
  addClassToMeOnlyInMySibling: function(cls) { 
        $(this).parent().children().removeClass(cls);
        $(this).addClass(cls);
    },
  addClassToSibling: function(cls,target) { 
        $(this).parent().children().removeClass(cls);
        $(target).addClass(cls);
    }
});
//delay
jQuery.fn.delay = function(time,func){
    this.each(function(){
    	setTimeout(func,time);
    });
    return this;
};
//return outer html
jQuery.fn.outerHTML = function(s) {
    return s
        ? this.before(s).remove()
        : jQuery("<p>").append(this.eq(0).clone()).html();
};
/**********************************************************
    ScrollButtom:
************************************************************/
function ScrollButtom(id){
    var objDiv = document.getElementById(id);
    objDiv.scrollTop = objDiv.scrollHeight;
}

/**********************************************************
    openAutoHideMsgPopUp: openAutoHideMsgPopUp('<b>Write your message</b>')
************************************************************/
function openAutoHideMsgPopUp(msg,type){
    //setup
    if( !($('.autohide').length )){ $('body').append('<div class="autohide box animated bounceOut"></div>')}
    
    self = $('.autohide')
    self.html(msg).addClass(type)
    self.switchClass('bounceOut','bounceIn');
    setTimeout(function() {
            jQuery.fn.switchClass('bounceOut','bounceIn');
    }, 5000);    
}
/*******************************************************
     Add resize event 
********************************************************/
function REGISTER_RESIZE(func){
    $(window).resize(function() {
      windowWidth = $(window).width(); //retrieve current window width
      windowHeight = $(window).height(); 
      console.log('Width'+windowWidth +' Height:' + windowHeight );
      if(func != undefined)
        func(windowWidth,windowHeight);
    });
}
/************  ************************************
    Adding new Feature in string class 
***************************************************/
String.prototype.ellipsis= function(n){
          return this.substr(0,n-1)+(this.length>n?'&hellip;':'');
    };
Array.prototype.last = function() {
    if( 0 == this.length) {return null;}
    return this[this.length-1];
}
Array.prototype.first = function() {
    if( 0 == this.length) {return null;}
    return this[0];
}
Array.prototype.nth = function(n) {
    if( n > this.length-1) {return null;}
    return this[n];
}
/*************************************************
    D O W N L O A D   S O R C E C O D E
*************************************************/
 function download() {
                                  var element = document.createElement('a');
                                  var filename="prog."+gEditors.get(selected_tab).lang;
                                  var data;
                                  data=gEditors.getEditorData(selected_tab);
                                  element.setAttribute('href', 'data:'+gEditors.get(selected_tab).lang+'/plain;charset=utf-8,' + encodeURIComponent(data));
                                  element.setAttribute('download', filename);

                                  element.style.display = 'none';
                                  document.body.appendChild(element);

                                  element.click();

                                  document.body.removeChild(element);
                                }



/*******************************************************
     escape-html-tags: uses: escape_html_tags("<b>Hello</b>")
********************************************************/
var tagsToReplace = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;'
};

function replaceTag(tag) {
    return tagsToReplace[tag] || tag;
} 

function escape_html_tags(str) {
    return str.replace(/[&<>]/g, replaceTag);
}
/*******************************************************
     getNamedObjs('#hello') => return all named child value as object
********************************************************/
function getNamedObjs(ele){
    res = {}
    tt = $(ele).find('[name]')
    for( var t=0; t< tt.length;t++){
     res[$(tt[t]).attr('name')] = $(tt[t]).val()
    }
    //console.log(res)
    return res;
}
/*******************************************************
     syntaxHighlight({1:1}) => return html version for js object with syntax sightedly. 
********************************************************/
function syntaxHighlight(json) {
    if (typeof json != 'string') {
         json = JSON.stringify(json, undefined, 4);
    }
    json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
        var cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
                cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
    });
}