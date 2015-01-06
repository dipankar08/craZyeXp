/*helper*/
// http://stackoverflow.com/questions/512528/set-cursor-position-in-html-textbox#answer-12518737
function setCaretPosition(elemId, caretPos) {
    var el = elemId;//document.getElementById(elemId);

    el.value = el.value;
    // ^ this is used to not only get "focus", but
    // to make sure we don't have it everything -selected-
    // (it causes an issue in chrome, and having it doesn't hurt any other browser)

    if (el !== null) {

        if (el.createTextRange) {
            var range = el.createTextRange();
            range.move('character', caretPos);
            range.select();
            return true;
        }

        else {
            // (el.selectionStart === 0 added for Firefox bug)
            if (el.selectionStart || el.selectionStart === 0) {
                el.focus();
                el.setSelectionRange(caretPos, caretPos);
                return true;
            }

            else  { // fail city, fortunately this never happens (as far as I've tested) :)
                el.focus();
                return false;
            }
        }
    }
}

var createCookie = function(name, value, days) {
    var expires;
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    }
    else {
        expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) {
                c_end = document.cookie.length;
            }
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}


/*end helper*/

angular.module('dipankar', ['ngSanitize'])
      .controller('ExampleController', ['$scope', '$sce', function($scope, $sce) {
        $scope.html ='';
        $scope.deliberatelyTrustDangerousSnippet = function() {
          return $sce.trustAsHtml($scope.html);
        };
      }]);


/* Jacascript Code for handaing data */
$(document).ready(function() {

showPopup('#example-popup');
/************ strat of autoLoad by cookie**************************/
$("#css").val(getCookie("css"));
$("#js").val(getCookie("js"));
$("#html").val(getCookie("html"));
/************ end of autoLoad by cookie**************************/

/************ start of insert html**************************/
$('#html').bind('input propertychange paste', function() {
var html = this.value;
var content = $("#preview").contents().find("body"); // iframe id is 'preview'
content.html(html);
});

/************ end of insert html**************************/


/************ start of auto complete HTML**************************/
$('#html').keypress(function(event){   
	var keycode = (event.keyCode ? event.keyCode : event.which);
	/* auto ending closing tag */
  {    
        a = this.value.slice(0,this.selectionStart)
        b = this.value
        c = this.selectionStart 
        //alert('You pressed a "enter" key in textbox'+this.value+"#"+keycode+"#"+this.selectionStart+"#"+this.selectionEnd);	
        if(keycode == 62 && a[a.lastIndexOf('<')+1]!='/')
       {   
           tag = a.substring(a.lastIndexOf('<')+1,this.selectionStart)
           inj = "</"+tag+">"
           this.value = b.substring(0,this.selectionStart)+inj+b.substring(this.selectionStart,b.length)
           //this.value = this.value.slice(0,this.value.length -1);
           setCaretPosition(this, c);
       }
}
});

/************ end of auto complete HTML**************************/

/************ start of insert CSSS**************************/
$('#css').bind('input propertychange paste', function() {
    var csVal = this.value;
    var cssLink = "<style>" + csVal + "</style>"; // cssVal contains css code
    var head = $("#preview").contents().find("head").find("style");
    head.replaceWith(cssLink);
});
/************ end of insert CSSS**************************/


/************ insert JS**************************/
$('#js').bind('input propertychange paste', function() {
var jsCode = this.value;
var js =jsCode ; 
  try {
    frames[0].window.eval(js.toString());
    console.log('JS successfuly Injected..');
  } catch(e) {
   // console.log('[Js-Error]'+e);
   // console.error(e.stack);
  }


});

/************ end of insert JS**************************/

/************ start of logging**************************/
if (typeof console  != "undefined") 
    if (typeof console.log != 'undefined')
        console.olog = console.log;
    else
        console.olog = function() {};
console.log = function(message) {
    console.olog(message);
    $('#debugDiv').html(message);
};
//console.error = console.debug = console.info =  console.log

/************ end of logging**************************/

/************ strat of autosave by cookie**************************/
window.setInterval(function(){
    console.log("Auto saving ....");
    createCookie("css",$("#css").val(),1);
    createCookie("js",$("#js").val(),1);
    createCookie("html",$("#html").val(),1);
}, 15000);

/************ strat of autosave by cookie**************************/

});
/*********  end of code ***************/



/************************* start of tidy HTML logic *****************************/

//var a="<div><p>hello1</p><p>hello1</p><p>hello1</p></div>"

function gettab(x){
TAB="  ";aa=''
for(ii=0;ii<x;ii++)
  aa+= TAB
return aa;
}
/* remove White Space */
function rms(dtx){
var ans=''
var fstart=true
for (var j=0;j<dtx.length;j++){
  if(dtx[j] == '>'){fstart=true}
  else if(fstart==true &&(dtx[j] =='\n' || dtx[j] =='\t' || dtx[j] ==' ' )){
  continue;
  }
  else if(fstart==true &&!(dtx[j] =='\n' || dtx[j] =='\t' || dtx[j] ==' ') ){
  fstart=false
  }
  ans+= dtx[j];
}

dtx = ans
ans= ''
var fstart=true
for (var j=dtx.length-1;j>=0;j--){
  if(dtx[j] == '<'){fstart=true}
  else if(fstart==true &&(dtx[j] =='\n' || dtx[j] =='\t' || dtx[j] ==' ' )){continue;}
  else if(fstart==true &&!(dtx[j] =='\n' || dtx[j] =='\t' || dtx[j] ==' ') ){fstart=false}
  ans= dtx[j]+ans;
}
return ans
}

function clearii(){
var r = confirm("Do I clear  all data ?");
if (r == true) {
     $("#css").val('');
     $("#js").val('');
     $("#html").val('');
} else {
    console.log('clear canceled');
}

}

/* Tide Html logic here */
function hp(){
var a = $("#html").val();
console.log('Moving whitespace.....')
a = rms(a)
console.log(a)
  var b=''
  var tp=0;
  var is_new_line = true; // if No next Line is true will doesnt cretat a new line..
  var is_inside_start_tag = 0// Indise_StartTag=1; inside_end_tag =3 ; Inside test: 2

  for(i=0;i<a.length;i++)  {
    if(a[i] != '>' && a[i] != '<'){  
     //Do Nothing...
    }
    else if(a[i] == '<' && a[i+1]!='/'){ //start tag: It will always in new tab and next line..  
       { b += '\n '+ gettab(tp);  tp++;}
       is_inside_start_tag = 1;
    } 
    // End tag Start. Shoud i do it same line or a new line with -- tab ?
    else if(a[i] == '<'&& a[i+1]=='/'){ //endtag: Always tab - and <nocol>
       is_inside_start_tag = 3;
       tp--;
       if(is_new_line){ b += '\n '+ gettab(tp)}
       else{
           is_new_line = true
       }
    }
    // No New line if Start-tag End
    // 1. <div></div>
    // 2. <div>hello</div>
    else if((is_inside_start_tag == 1)&&
           ( (a[i] == '>' && a[i+1] == '<' && a[i+2] == '/')||
             (a[i] == '>' && a[i+1] != '<'))){ // tag doesnt contains tag  but something else..
      is_new_line = false
    }
    else if(1){
     
    }
    b += a[i]   
  }
  $("#html").val(b)
}

/************************* end of tidy HTML logic *****************************/
