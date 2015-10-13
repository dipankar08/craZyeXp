/**********  MOVING ALL JS IN A SINGLE FILE FROM CLEANCODE ******/

 
/************ G L O B A L V E R I A B L E ******************************************/
var gEditors = undefined; // This need to populated in the implementation html
var editor_type = "ACE"
var BASE_URL = ''              
var IS_SHELL_OPEN = false;



/*************** G L O B A L C O N S T  S T R I N G *********************************/
const NO_SOLUTION_MSG = "Looks like you didn't white any solution yet! Let's start writing about your code.";

const NEW_COLABOATION_POPUP_HEADER = "You are about to share your code !"
const NEW_COLABOATION_POPUP_HTML = "Code colaboration is a great thing when you are working as a group. It allow your friend to edit the same document the one you are editing right now."

const EXIST_COLABOATION_POPUP_HEADER = "Yupp! Your friend need your help !"
const EXIST_COLABOATION_POPUP_HTML = "Congrts! You received a colaboration request, where both of you can edit the same document simultaniouly. It will help you to understand the code in a better way."

const ENTER_LICENSE_POPUP_HEADER = "Wait a min! Do you have a license ?"
const ENTER_LICENSE_POPUP_HTML = "This is something where you need to have a licence to browse 1000+ practical coding questions, create your own save and delete. <input class='f1' id ='lic' style='padding-left: 10px; font-size:19px; width:400px;border:0; border-bottom:1px solid white;background:transparent;color:white;' placeholder='Enter your license' >"


/*######################### COMMON HELPER FUNC #######################################*/

/*********************** A L E R T ******************************/
function custom_alert(str){
  alert(str);
}
function custom_confirm(str) {
    x = confirm(str);
    return x;
}

/***********************  O P E N   P O P U P ********************************/
    
function openOpopup(url) {
    window.open(url, "PartySearch", "width=400,height=500");
    return false;
}
        
        
/***********************  G E T  / L O A D  I D******************************/
function getID(){
   var id = 0;
   if ($("#id").html() != "0"){
     id = $("#id").html();
   }
   else{
        var url
        try {
             url= window.location.href
            var myRegexp = /.*\/cleancode\/(.*?)\/.*/g;
            id = myRegexp.exec(url)[1];
        }
        catch(err) {
            log('Id can bnot be retrived from url: '+url)
            id = '0'
        }

   }
   return id
}
function LoadID(id){
   getAnItem(id);
}
function reLoadId(){
   var id = getID();
   if (id != '0'){
     getAnItem(id);
   }
}

/******************************************************************************
        C O D E   E D I T O R   J S    C L A S S  
*******************************************************************************/
var CODE_EDITOR = function (id_list) { // ['main','hello',]
        this.editors={};
        for (i=0;i<id_list.length ;i++) { this.editors[id_list[i]] = undefined;}
        this.editor_type = 'ACE'
        this.language = 'c'
        this.init()
}
CODE_EDITOR.prototype.addEditor = function(id) { this.editors[id]=undefined;};
CODE_EDITOR.prototype.setEditorType = function(type) { this.editor_type = type}; // 'ACE'or 'CODEMIRROR'
CODE_EDITOR.prototype.setLanguage = function(language) { this.language = language}; // c cpp java or py
CODE_EDITOR.prototype.init = function() { if(this.editor_type == 'ACE'){ this._initACE();} else{this._initCodeMirror();}}; // c cpp java or py
CODE_EDITOR.prototype._initCodeMirror = function(){
                    var init = function(){
                         /**** Wrapper on code mirror ***/
                        function autoFormat(editor) {
                            var totalLines = editor.lineCount();
                            var totalChars = editor.getTextArea().value.length;
                            editor.autoFormatRange({line:0, ch:0}, {line:totalLines, ch:totalChars});
                        }
                        for (var key in gEditors.editors) {
                            if (gEditors.editors.hasOwnProperty(key)) {
                               gEditors.editors[key] = CodeMirror.fromTextArea(document.getElementById(key), {
                                    theme: "default",
                                    lineNumbers: true,
                                    matchBrackets: true,
                                    mode: "text/x-c++src",
                                    styleActiveLine: true,
                                    autoCloseBrackets: true 
                                });
                                autoFormat(gEditors.editors[key]);
                                 /***** Correct indentation  on Paste */
                                gEditors.editors[key].on("change", function(cm, change) {
                                  if (change.origin != "paste" || change.text.length < 2) return;
                                  cm.operation(function() {
                                    for (var line = change.from.line, end = CodeMirror.changeEnd(change).line; line <= end; ++line)
                                      cm.indentLine(line, "smart");
                                  });
                                });
                          }
                        } // end for
                        loadCSSInline('.CodeMirror {height: 100%;}.CodeMirror-code > div{line-height: 1.8;}.CodeMirror-gutters {min-height:100% !important;z-index: 0;}');
                        log('SUCCESS: Code Mirror Initilized properly......','',"Green")
                    } //end init
                    
                    lazyScriptLoading(["/media/js/codemirror.js","/media/js/clike.js","/media/js/python.js","/media/js/matchbrackets.js","/media/js/formatting.js","/media/js/closebrackets.js","/media/js/javascript.js","/media/js//foldcode.js"],init)
                    loadCSS("/media/css/codemirror.css")
            
                    var cssList=["http://codemirror.net/theme/3024-day.css",  "http://codemirror.net/theme/3024-night.css",  "http://codemirror.net/theme/ambiance.css",  "http://codemirror.net/theme/base16-dark.css",  "http://codemirror.net/theme/base16-light.css",  "http://codemirror.net/theme/blackboard.css",  "http://codemirror.net/theme/cobalt.css",  "http://codemirror.net/theme/eclipse.css",  "http://codemirror.net/theme/elegant.css",  "http://codemirror.net/theme/erlang-dark.css",  "http://codemirror.net/theme/lesser-dark.css",  "http://codemirror.net/theme/mbo.css",  "http://codemirror.net/theme/mdn-like.css",  "http://codemirror.net/theme/midnight.css",  "http://codemirror.net/theme/monokai.css",  "http://codemirror.net/theme/neat.css",  "http://codemirror.net/theme/neo.css",  "http://codemirror.net/theme/night.css",  "http://codemirror.net/theme/paraiso-dark.css",  "http://codemirror.net/theme/paraiso-light.css",  "http://codemirror.net/theme/pastel-on-dark.css",  "http://codemirror.net/theme/rubyblue.css",  "http://codemirror.net/theme/solarized.css",  "http://codemirror.net/theme/the-matrix.css",  "http://codemirror.net/theme/tomorrow-night-bright.css",  "http://codemirror.net/theme/tomorrow-night-eighties.css",  "http://codemirror.net/theme/twilight.css",  "http://codemirror.net/theme/vibrant-ink.css",  "http://codemirror.net/theme/xq-dark.css",  "http://codemirror.net/theme/xq-light.css",  "http://codemirror.net/theme/zenburn.css"]
                    for (i = 0; i < cssList.length; i++) {
                       loadCSS(cssList[i]);
                    }
            } //End of initCodeMirror
CODE_EDITOR.prototype._initACE = function(){
            var init = function(){
                for (var key in gEditors.editors) {
                   if (gEditors.editors.hasOwnProperty(key)) {
                    gEditors.editors[key] = ace.edit(key)
                    gEditors.editors[key].setTheme("ace/theme/eclipse");
                    var session = gEditors.editors[key].getSession() 
                    session.setMode("ace/mode/c_cpp");
                    session.setUseWrapMode(true);
                    session.setUseWorker(false);
                    gEditors.editors[key].container.style.lineHeight=1.5
                    gEditors.editors[key].setOptions({fontSize:"11pt"}); 
                  }
                }
                loadCSSInline('#main,#func,#input {height: 100%;width:100%;} .ace_gutter, .ace_gutter-cell {background: white !important;border-right: 0 !important;color: #87cefa!important;}.ace_active-line{background:#fff !important;}');
                log('SUCCESS: ACE Editor Initilized properly......',"Green")
            } // end init
            lazyScriptLoading(["https://cdnjs.cloudflare.com/ajax/libs/ace/1.2.0/ace.js"],init) 
        } // end of initACE
CODE_EDITOR.prototype.addEditor = function(key){
    if (gEditors.editors.hasOwnProperty(key)) {
        console.log('Already have'); return;
    }
    if(this.editor_type == 'ACE'){
                    gEditors.editors[key] = ace.edit(key)
                    gEditors.editors[key].setTheme("ace/theme/eclipse");
                    var session = gEditors.editors[key].getSession() 
                    session.setMode("ace/mode/c_cpp");
                    session.setUseWrapMode(true);
                    session.setUseWorker(false);
                    gEditors.editors[key].container.style.lineHeight=1.5
                    gEditors.editors[key].setOptions({fontSize:"11pt"}); 
    } else {
     console.log('Not yet Imaplemented ')
    }
}

CODE_EDITOR.prototype.getEditor = function(id){
                return this.editors[id]
        } // end getEditorData 
        
CODE_EDITOR.prototype.getEditorData = function(id){
            if(this.editor_type == 'ACE'){
                return this.editors[id].getValue()
            }
            else{
                return this.editors[id].getValue ; // code mirror
            }
        } // end getEditorData        
CODE_EDITOR.prototype.setEditorData = function(id,data){
            if(this.editor_type == 'ACE'){
                return this.editors[id].setValue(data)
            }
            else{
                return this.editors[id].setValue(data) // code moirror
            }
        }// end getEditorData       
CODE_EDITOR.prototype.setEditorMode = function(){
            for (var key in this.editors) {
                if (this.editors.hasOwnProperty(key)) {
                    x = this.editors[key]
                    if(this.editor_type == 'ACE'){               
                            switch (this.language) { 
                              case 'c': x.getSession().setMode("ace/mode/c_cpp");break;
                              case 'cpp':x.getSession().setMode("ace/mode/c_cpp");break;
                              case 'java':x.getSession().setMode("ace/mode/java");break;
                              case 'py':x.getSession().setMode("ace/mode/python");break;
                            }
                   } else{
                           switch (this.language) { 
                              case 'c':x.setOption("mode", "text/x-c++src");break;
                              case 'cpp': x.setOption("mode", "text/x-c++src"); break;
                              case 'java': x.setOption("mode", "text/x-c++src");break;
                              case 'py':x.setOption("mode", "text/x-cython"); break;
                            }
                   }
                }
            }
        } // end setEditorMode
CODE_EDITOR.prototype.setEditorTheme = function(d1){
            for (var key in this.editors) {
                if (this.editors.hasOwnProperty(key)) {
                    x = editors[key]
                    if(this.editor_type == 'ACE'){
                       x.setTheme(d1);
                   } else{
                        x.setOption("theme", d1); // oce mirror
                   }
                }
            }
        } //end setEditorTheme
/** How to User:
    c  = CODE_EDITOR()
    
/******************************************************************************
       E N D  O F  C O D E   E D I T O R   J S    C L A S S  
*******************************************************************************/


/******************************************************************************
       S T A R T   O F   C O D E   P L A Y E R  
*******************************************************************************/



/******************************************************************************
       E N D   O F   C O D E   P L A Y E R 
*******************************************************************************/



/*********************** L I C E N C E ******************************/
function setLicense() {    
    function initLic(){
        var lic = $("#lic").val();
        if (lic != '') {
        eraseCookie('token');
        setCookie('token',lic,30);
        if(lic == getCookie('token')){
          autohideMsgPopUp('success',"Your License Set Successfully !"); 
          reLoadId();
          }
        else{
          autohideMsgPopUp('error',"Not able to set the license! Ensure that your browser is cookie enabled!");
        }
       }
    }
    showWinStylePopup(ENTER_LICENSE_POPUP_HEADER, ENTER_LICENSE_POPUP_HTML, true,'Allow Access', initLic);
}
/*********************** E X P L A I N  E D I T O R ******************************/
function showExplain(){
  toggleClass('#tut','show');
  toggleClass('.editor-btn','hide');
  toggleClass('.tut-btn','show');
  if($("#tut").hasClass('show')){
  }
}

/*********************** A U T O H I D E  P O P U P ******************************/
var autohideMsgPopUpTimeOut;
function autohideMsgPopUp(type,html,sec) {
  if (sec == undefined){ sec = 2;}
  if (type == undefined){ type = 'success';}
  if(type == 'error'){sec = 20;}
  else{sec= 4;}
  
  $(".autohideMsgPopUp ul").html('<li class="'+type+'"><b>'+type+'!</b>'+html+'</li>');
  if($(".autohideMsgPopUp").hasClass('active')){
    //already pop is dr.
    $(".autohideMsgPopUp").removeClass('active success error').addClass('active '+type);
    clearTimeout(autohideMsgPopUpTimeOut);
  }
  else{
    $(".autohideMsgPopUp").removeClass('active success error').addClass('active '+type);
  }
  autohideMsgPopUpTimeOut = setTimeout(function(){ $(".autohideMsgPopUp").removeClass('active');
  $(".autohideMsgPopUp").html('<ul></ul>') }, sec *1000);
}

/*********************** L O O K  P R E V I E W  ******************************/
function eye_init(){
 $("#eyef").attr('src', '/cleancode/'+getUnifiedParams().id+"/look/");
}
/*********************** G D B  ******************************/
function gdb_init(){
 if(IS_SHELL_OPEN == false){
    $("#gdb").attr('src', "http://shell.dipankar.ngrok.io");
    IS_SHELL_OPEN = true;
 }
}
function startDebugging() {
    if($("#gdbf").attr("src") != ''){
     document.domain = 'ngrok.io'
     butterfly = document.getElementById('gdbf').contentWindow.butterfly;
     butterfly.send('cd /tmp/ \r');
     butterfly.send('clear\r');     
     butterfly.send('gdb ./'+getUnifiedParams().fname+'.exe \r');
    }      
}
/*********************** B U I L D  B O O K  ******************************/
function buildBook(){
  var config = $("#book").val();
 // console.log(config);
  $("#progress").show();
  $.get( "/api/cleancode/buildBooklet/", { config: config} )
      .done(function( data ) {
        $("#progress").hide();
        if(data.status =='success'){
        $('a#dlink').attr('href','/media/tmp/'+ data.fname);
        $('a#dlink i').css("color","green"); 
        $('#dlink').show();
        }
        else{
        alert( "ERROR # " + data.status +'::'+ data.fname  );      
        $('a#dlink').attr('href','javascript:void(0)')
        $('a#dlink i').css("color","red"); 
        }
      }
  );
}


/*********************** R E S I Z E   E D I T O R  ******************************/
//$( "#resizable" ).resizable({ handles: 'e, w'});

 
/*********************** C O L A B O R A T I O N  ******************************/

function ColaborationUtil(hash){
    furl = 'https://cleancode.firebaseio.com/firepads/'+hash 
    datapoint = { 'hash':hash,'furl':furl}
    function init(){            
        log('Script ready! Staring colaboration..','pink');
        var furl = datapoint.furl;
        log('Colaboration Backend ID: '+furl)
        var firepadRef  = new Firebase(furl);
        if (editor_type=='CODEMIRROR'){
                var firepad  = Firepad.fromCodeMirror(firepadRef, editors['main'], {});
        }
        if (editor_type == 'ACE'){
                var firepad  = Firepad.fromACE(firepadRef, editors['main'], {});
        }
           
    }
    loadCSS("https://cdn.firebase.com/libs/firepad/1.1.0/firepad.css");
    lazyScriptLoading(['https://cdn.firebase.com/js/client/2.2.4/firebase.js', 'https://cdn.firebase.com/libs/firepad/1.1.0/firepad.min.js' ] ,init)
} //<!-- end of ColaborationUtil -->

function joinAColaboration(hash){
    if(hash != undefined){
        ColaborationUtil(hash);return;
    }
    if(window.location.href.indexOf('#') != -1){
        var hash = window.location.hash.replace(/#/g, '');
        //showWinStylePopup(title, desc, is_cancel_able,yes_txt, yes_cb, no_txt,no_cb)
        showWinStylePopup(EXIST_COLABOATION_POPUP_HEADER,EXIST_COLABOATION_POPUP_HTML, true, 'Join Colaboration',function(){ColaborationUtil(hash);})
    }
}

// Start a new collaboration with a fresh Hash Tag ..
function startNewColaboration(){
    var hash ;
    if(window.location.href.indexOf('#') != -1){  
       hash = window.location.hash.replace(/#/g, '');
    } else {
    // build a new hash,,
       hash  = getRandom();
    }    
    var newurl = window.location + '#' + hash;
    //showWinStylePopup(title, desc, is_cancel_able,yes_txt, yes_cb, no_txt,no_cb)
showWinStylePopup(NEW_COLABOATION_POPUP_HEADER, NEW_COLABOATION_POPUP_HTML+"<br>1. Copy this url:<span class='f1' style='border:1px solid white;font-size:13px; padding: 2px 14px;vertical-align: middle;margin:0 5px;'>"+newurl+"</span> and share with your friends.<br>2. <input style='\"width\": 500px;' id='user_q' placeholder='Enter your friends mail ID' ></input><button onclick=\"call_backend_api('get','/api/email/',{recipient:$('#user_q').val(), subject:'[PeerReview] Hello, Your friend Share a link to Join!',template:'cleancode_colaboration_invite.html',url:'"+newurl+"'});\">Send Invitation</button>", true, 'Share', function(){ColaborationUtil(hash);  window.location = window.location + '#' + hash;})
}
/***********  S O C I A L A U T H  P O P U P ****************/
function showSocialLoginPopup(){
    //showWinStylePopup(title, desc, is_cancel_able,yes_txt, yes_cb, no_txt,no_cb)
    if (! CLEANCODE_IS_INTERVIEW_MODE){
        showWinStylePopup('Personalize your experience! You just need a click. ','By signing in, you can do a lot more other than coding. Your code got save automatically in fly. You can see your history and many more ...<br> So, what are you waiting for ? Just click your social icon ! <br><div class="social_auth" style="margin-top: 50px;text-align: center;"><a  class="facebook" onclick="openOpopup(\'/login/facebook\')"><i class="fa fa-facebook"></i></a><a class="google"  onclick="openOpopup(\'/login/google\')"><i class="fa fa-google"></i></a><a class="linkedin" onclick="openOpopup(\'/login/linkedin\')"><i class="fa fa-linkedin"></i></a><a class="github"  onclick="openOpopup(\'/login/github\')"><i class="fa fa-github"></i></a></div>',false,'skip for now');
    }
    else{
        showWinStylePopup('Authetication Required for Interview!','Please login using your social account. Please make sure, <b><i>you are using your own account</i></b> as we will send the feedback in your mail id. <br> So, what are you waiting for ? Just click your social icon ! <br><div class="social_auth" style="margin-top: 50px;text-align: center;"><a class="google"  onclick="openOpopup(\'/login/google\')"><i class="fa fa-google"></i></a><a class="linkedin" onclick="openOpopup(\'/login/linkedin\')"><i class="fa fa-linkedin"></i></a><a class="github"  onclick="openOpopup(\'/login/github\')"><i class="fa fa-github"></i></a></div>',false,'skip for now');
    }
}
function login_callback(id,name,email,pic){
    dismissWinStylePopup();    
    console.log(id+name+email+pic);
    if (CLEANCODE_IS_INTERVIEW_MODE){
        show_interview_panel();  
        INTERVIEW_DATA['candidate'] ={id:id,name:name,email:email,pic:pic}
    }
    else{
    }
}



/*************END COMMON HELPER FUNC************************************************/
  
/*------ Object getter and Setter : Unified ---------*/
function extractMetaInfo(data){
  meta={}
  meta.main=''
  meta.depends=''
  temp = data.split('\n')
  var h_flag = 1;
  for (i = 0; i < temp.length; i++) {
    if( h_flag ==1 ){  // if it is a meta tag
       if(temp[i].indexOf("$DEPENDS") == 0){
      meta.depends += temp[i].replace("$DEPENDS",'')+' '
     }
     else if(temp[i].indexOf("$NEW") == 0 ){
     }
     else{
     h_flag = 0; //stop processing the meta tag
     meta.main += temp[i] +'\n'
     }
  }
  else {
    meta.main += temp[i] +'\n'
  }
  }
  // Replace space by commma
  meta.depends = meta.depends.replace(/\s\s+/g, ' ').trim().split(" ").join(",");
  return meta;
}

function getUnifiedParams(){
  return {   
    'func':gEditors.getEditorData ('func'),
    'main':gEditors.getEditorData ('main'),  
    'input':gEditors.getEditorData ('input'),  
    'id':$("#id").html(),
    'name': $("#name").html(),
    'fname': $("#name").html().replace(/[^A-Z0-9]+/ig, ""), //basically a file name created at server side 
    'short_desc': $("#short_desc").html(),    
    'topic': $('#topic').val(), //  we can pass the arry by commna seperated string
    'language':$('#language').val(),
    //'solution':$('#solution').val(), We don't want to undate this everytime..
    'token': getCookie('token'),
    //Inheritance ..
    'compilation':(gEditors.getEditorData ('main').trim()=='')?'NO_CODE':'NO_SOLUTION',     
  }
}

function setUnifiedParams(o){
  if (o != undefined){
      //Normalised.
      o.func = (o.func==null)? '':o.func;
      o.main = (o.main==null)? '':o.main;
      o.input = (o.input==null)? '':o.input;
      o.id = (o.id==null)?'0':o.id;
      o.name = (o.name==null)?'':o.name;
      o.short_desc = (o.short_desc==null)?'':o.short_desc; 
      o.topic = (o.topic == null )?'':o.topic[0] // this is a Array.. take the first Elements
      o.language =(o.language == null )?'c':o.language;
      o.solution =(o.solution == null || o.solution.length < 20 )? STR_SOLUTION :o.solution;
      //Population...
      gEditors.setEditorData('func',o.func)
      gEditors.setEditorData('main',o.main)
      gEditors.setEditorData('input',o.input)
      
      $("#id").html(o.id); 
      $("#name").html(o.name); 
      $("#short_desc").html(o.short_desc);     
      $('#topic').val(o.topic)
      $('#language').val(o.language)
      $('#solution').val(o.solution)
      $("#iname").val(o.name); 
      $("#ishort_desc").val(o.short_desc);             
      autohideMsgPopUp('success',' Cloning the code..');
  }
  else{
      gEditors.setEditorData('func','')
      gEditors.setEditorData('main','')
      gEditors.setEditorData('input','')
      $("#id").html('0'); 
      $("#name").html('Sample99'); 
      $("#short_desc").html('Sample Program');
      $("#iname").val('Sample99'); 
      $("#ishort_desc").val('Sample Program');   
      $("#language").val('c')      
      $('#solution').val(STR_SOLUTION)
      autohideMsgPopUp('success',' Cleaning the editor..');
  }
}

function cleanCodeObj(){
  o = getUnifiedParams();
  if(o.main =='' && o.func =='')
  {
    setUnifiedParams();return;
  }
  var r = confirm("Are You Sure to clear the code ?");
  if (r == true) {
    setUnifiedParams();
  }
  autohideMsgPopUp('success',' Code Editor cleaned');
}

/*------ END Object getter and Setter ---------*/

/*--- start Editor releted styling ----*/
function heighlightErrorInEditor(data){
   $( ".main .CodeMirror-code > div").css('background','white');   
   for ( i = 0;i<data.length;i++){
     // test if the error in main file.
     //if( data[i][0].indexOf($("#name").html()) == -1)
     //  continue;
     // test if this is a waring..
     target = $( ".main .CodeMirror-code > div:nth-child("+(parseInt(data[i][1])-1)+")" )
     if( data[i][3].indexOf("warning") > -1) {
       $( ".main .CodeMirror-code > div:nth-child("+(parseInt(data[i][1])-1)+")" ).css('background','#FAFAD2')
     }
     else if( data[i][3].indexOf("error") > -1) {
     // test this is an error
      $( ".main .CodeMirror-code > div:nth-child("+(parseInt(data[i][1])-1)+")" ).css('background','#FF8C00')
     }
     //$( ".main .CodeMirror-code > div:nth-child("+(parseInt(data[i][1])-1)+")::after").css('content',data[i][4]);
      target.attr('data-content',data[i][4]);
   }
}
function removeHeighlightErrorInEditor(){
  $( ".main .CodeMirror-code > div").css('background','white');
  $( ".main .CodeMirror-code > div").attr('data-content','');
}
/* End of Editot related styling ---*/


/*************************************************
    C O D E   C O M M A N D 
*************************************************/
var CAN_RUN = false;
function codeExecution(action,input, callback){ 
    var o = input;
    var meta = extractMetaInfo(o.main);
    o.main = meta.main; o.depends =meta.depends
    o.fname = o.id;
    if(o.language =='java') o.name = 'Solution'
    function pre_cb(){
        if(action == 'compile'){$('#output').html(''); $("#run_state").html('Compiling...');}
        else{  $("#run_state").html('Running...');}
        $(".top-progress-bar").addClass("progress") 
        $("#process-icon").show()
        $("#no_network").hide()
    }
    function success_cb(data){
        if(action == 'compile'){
            removeHeighlightErrorInEditor();
            $('#output').append('<pre style="padding-left: 35px;">'+data['output']+'</pre>');
            if( data['formated_error'] != undefined){
              heighlightErrorInEditor(data['formated_error']); // alwas show any waring or error.
            }
            if( data["can_run"]=="yes"){
                log('compiled successfully');
                CAN_RUN=true;
            }
            if(callback != undefined){
                callback();
            }

        } else { //run
            $('#output').append('<pre style="padding-left: 35px;">'+data['output']+'</pre>');
            $('#output').append('<br><pre style="padding-left: 35px;">Unexpected Output? <span onclick="showGdb();"><b><i>Debug now!</i></b></span>  </pre>');
            CAN_RUN= false;           
        }
        $("#process-icon").hide()
    }
    function complete_cb(){
        $(".top-progress-bar").addClass("complete");
        $("#process-icon").hide()
        setTimeout(function(){$(".top-progress-bar").removeClass("progress complete done");   },1000); 
    }
    function error_cb(XMLHttpRequest, textStatus, errorThrown){
         console.log('We have a network issue while compilation'); 
         $("#no_network").show();
         CAN_RUN=false;
    }
    var url = (action == 'compile')?'/api/cleancode/compile/':'/api/cleancode/run/';
    // CALL TO UNIFIED API
    call_backend_api('post',url,o,pre_cb,success_cb,error_cb,complete_cb);
}

function runProg(){
    hide_interview_panel();
    input = getUnifiedParams();
    codeExecution('compile',input, function(){if(CAN_RUN){codeExecution('run',input);}});
} 
/************  E N D    O F   C O D E   C O M M A N D ****************/

function cancelAllSideBar(){ /* remove all side bar */
  $(".sidebar-popup").removeClass("show");
}

/*************************************************
          D A T A B A S E   C O M M A N D 
*************************************************/
function createOrUpdate(){
    var param = getUnifiedParams();
    if(param.id == 0){ 
        url = '/api/code/' 
        function success_cb(d){setUnifiedParams(d.res); autohideMsgPopUp('success','New Entry created!');}        
    } else { 
        url = '/api/code/'+param.id+'/'
        function success_cb(d){setUnifiedParams(d.res); autohideMsgPopUp('success','Entry Updated!');}
    }
    function error_cb(d){autohideMsgPopUp('error',d.msg,5);}   
    call_backend_api('post',url,param,'pre_cb',success_cb,error_cb,'complete_cb');
}

function getAnItem(id,is_confirm){
    if(is_confirm != false ) is_confirm = true;
    if(is_confirm){
        var r = confirm("Confrim Reset!");
        if (r == true){
            console.log('Restiing the solution...')
        } else {
            console.log('Cancel Reset the solution...')
            return;
        }
    }
    url = '/api/code/'+id+'/'
    function success_cb(d){setUnifiedParams(d.res);autohideMsgPopUp('success',' Code is copied to editor.');resetUrl(id)}
    function error_cb(d){autohideMsgPopUp('error',d.msg,5);}   
    
    call_backend_api('get',url,getUnifiedParams(),'pre_cb',success_cb,error_cb,'complete_cb');
}

function deleteAnItem(id,is_confirm){
    if(is_confirm != false ) is_confirm = true;
    if(is_confirm){
        var r = confirm("Confrim Delete!");
        if (r == true){
            console.log('Restiing the solution...')
        } else {
            console.log('Cancel Reset the solution...')
            return;
        }
    }
    url = '/api/code/'+id+'/'
    function success_cb(d){autohideMsgPopUp('success',' Code is deleted');}
    function error_cb(d){autohideMsgPopUp('error',d.msg,5);}   
    
    call_backend_api('delete',url,getUnifiedParams(),'pre_cb',success_cb,error_cb,'complete_cb');
}

var browsePaginationPageID = 1;
var browseList = function(page){  
    function success_cb(d){$('#ListTable').html(buildListHTML(d.res.data));}
    function error_cb(d){autohideMsgPopUp('error',d.msg,5);}  
    param = {}; param.token = getUnifiedParams().token; param.page=1;param.limit=10;
    call_backend_api('get','/api/code/',param,'pre_cb',success_cb,error_cb,'complete_cb');
}
NextBrowseList= function(){browseList(browsePaginationPageID + 1);browsePaginationPageID++;}
PrevBrowseList= function(){browseList(browsePaginationPageID - 1);browsePaginationPageID--;}
var browseTree = function(){
    function error_cb(d){autohideMsgPopUp('error',d.msg,5);} 
    function success_cb(d){vv = List2TagTree(d.res.data,'topic');var html = recur(vv,0);$("#browseTree").html(html); isbrowseCodeBaseExist = true;autohideMsgPopUp('success',' Refreshed!! ');  }
    param = {}; param.token = getUnifiedParams().token; param.page=1;param.limit=100;    
    call_backend_api('get','/api/code/',param,'pre_cb',success_cb,error_cb,'complete_cb');
}
var isbrowseCodeBaseExist = false;
function browseCodeBase(force){
    if(!isbrowseCodeBaseExist || force == true ){
        browseTree();
        browseList(1);              
    }
}

function submitSolution(){
    if( $('#solution').val().trim().length < 10  ||  $('#solution').val().trim() == STR_SOLUTION.trim()) { autohideMsgPopUp('error','Please write something to submit! Please use this template !'); return;}
    
    function error_cb(d){autohideMsgPopUp('error',d.msg,5);} 
    function success_cb(d){autohideMsgPopUp('success',' Solution saved.');}
    o = getUnifiedParams()
    param = {'id':o.id,'solution':solveUnicode($('#solution').val())}  
    call_backend_api('get','/api/code/'+o.id+'/',param,'pre_cb',success_cb,error_cb,'complete_cb');
}

/*************************************************
          G E N E R A T E  H T M L 
*************************************************/

function buildActionbtnHTML(i){
    return '<div class="group-btn horz text-only" style="margin: 0px; position: absolute; right:0;"><button title="Download" onclick="window.location.href=\'/api/cleancode/'+i.id+'/download/\'"><i class="fa fa-download"></i></button><button title="Edit" onclick="getAnItem('+i.id+');"><i class="fa fa-chain-broken fa-fw"></i></button><button title="Love it" onclick="Love('+i.id+')"><i class="fa fa-heart-o"></i></button><button title="Add to fev" onclick="Feb('+i.id+')"><i class="fa fa-star-o"></i></button><button title="Delete" class="del" onclick="Delete('+i.id+')"><i class=" fa fa-trash"></i></button></div>'
}
function buildListHTML(l){
    t =''
    for (i = 0; i < l.length; i++) {
        t+= '<tr >'
        t+= '   <td> <span>#'+l[i].id+' <i>'+l[i].name+'</i></span>'
        t+= buildActionbtnHTML(l[i])
        t+= '</td></tr>'
    }
    return t;
}  
    
/****************** Tree Menu Js ************************/
var SORT_FLAG = 0; //sort flag can be 0,1,2,3
function sortList(li){
    ul = li.lastChild; // this is a ul
    var new_ul = ul.cloneNode(false);
    var lis = [];
    for(var i = ul.childNodes.length; i>=0;i-- ){
        if(ul.childNodes[i].nodeName === 'LI')
            lis.push(ul.childNodes[i]);
    }
    
    lis.sort(function(a, b){
       if (SORT_FLAG == 0){
         return parseInt(a.getElementsByClassName('id')[0].innerHTML , 10) - parseInt(b.getElementsByClassName('id')[0].innerHTML , 10);
         }
       else if (SORT_FLAG == 1){
         return parseInt(b.getElementsByClassName('id')[0].innerHTML , 10) - parseInt(a.getElementsByClassName('id')[0].innerHTML , 10);
         }
       else if (SORT_FLAG == 2){
         return b.getElementsByClassName('name')[0].innerHTML.localeCompare(a.getElementsByClassName('name')[0].innerHTML)
         }
       else if (SORT_FLAG == 3){
         return a.getElementsByClassName('name')[0].innerHTML.localeCompare(b.getElementsByClassName('name')[0].innerHTML)
         }
              
    });
    for(var i = 0; i < lis.length; i++)
        new_ul.appendChild(lis[i]);
    ul.parentNode.replaceChild(new_ul, ul);
    SORT_FLAG = (SORT_FLAG+1)%4;
}

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
      h+='<li class="has_child"  style="margin-left:'+level*18+'px;position:relative;">'
      h+='<i class="jstree-icon jstree-ocl"></i>'
      h+='<a onclick="actionClassOnSiblingButNotThis(this.parentNode,\'expanded\',\'has_child\',\'remove\');toggleClass(\'li\',\'expanded\',\'up\',this); " ><i class="fa fa-folder-open-o"></i> '+e.name+'</a>'
      h+='<div> <button class="sort" onclick="sortList(this.parentNode.parentNode)" style="position:absolute;right: 0; top:0;">4 way Sort</button></div>'
      h+= recur(e.child,1)
      h+='</li>'
    }
    else{
      h+='<li style="margin-left:'+level*18+'px">'
      h+='<i class="jstree-icon jstree-ocl"></i>'
      h+='<a> <i class="fa fa-file-o '+e.compilation+'"></i><span class="id">'+e.id+'</span><span class="name">-'+e.name+'</span></a>'
      h+='<div class="group-btn horz text-only" style="margin: 0px; position: absolute; right:0;"><button  title="Download" onclick="window.location.href=\'/api/cleancode/'+e.id+'/download/\'"><i class="fa fa-download"></i></button><button title="Edit" onclick="getAnItem('+e.id+');"><i class="fa fa-chain-broken fa-fw"></i></button><button title="Love it" onclick="Love('+e.id+')"><i class="fa fa-heart-o"></i></button><button title="Add to fev" onclick="deleteItem('+e.id+')"><i class="fa fa-star-o"></i></button><button title="Delete" class="del" onclick="Delete('+e.id+');$(this).closest(\'li\').addClass(\'hide\');"><i class="fa fa-trash"></i></button></div>' 
      h+='</li>' 
    }    
  });
  h += '</ul>'
  return h;
}
function List2TagTree(ll,target_field_name){
  temp={}
  ll.forEach(function(e) {
    fl =eval(e[target_field_name])
    if(fl.length ==0){ fl=['zUnKnown'] }
    fl.forEach(function(f) {
      if(temp.hasOwnProperty(f)){
        temp[f].unshift(e)
      }
      else{
      temp[f] =[]
      temp[f].unshift(e)
      }
    });
  });
  
  out=[]
  for( p in temp) {
  out.push({'name':p,'child':temp[p]})
  }
  out.sort(function(a, b){
      if(a.name < b.name) return -1;
      if(a.name > b.name) return 1;
      return 0;
  });
  return out;
} 
function serach(ID, data){ // Search on Tree Menu.
  jQuery(ID).each(function () {
        if (jQuery(this).text().search(new RegExp(data, "i")) < 0) {
            jQuery(this).hide();
        } else {
            jQuery(this).show()
        }
    });
}
jQuery("#treesearch").keyup(function () {
    var filter = jQuery(this).val();
    serach("#browseTree ul li",filter)
});
function TreeViewtoggle(ele){
  var icon = $($(ele).find('i')[0])
  if($(ele).hasClass('treeview')){
    
    icon.removeClass('fa-list-ul').addClass("fa-sitemap")
    $(ele).removeClass('treeview')    
    $('.treemenu').hide()
    $('.browseList').show()    
  }
  else{
    icon.removeClass('fa-sitemap').addClass("fa-list-ul")
    $(ele).addClass('treeview')
    $('.browseList').hide()
    $('.treemenu').show()    
  }
}/* End of Tree Menu Js */

/*************  E N D  G E N E R A T E  H T M L *************************/

/*************  Some On Click Event call of Menu Button****************************/
function Love(i){
    var win = window.open('/cleancode/'+i+'/iview/', '_blank');
    win.focus();
}    
function quickSave(){
    if($("#id").html() =='0'){
      toggleClass('#savebox','show');
    }
    else{
      createOrUpdate();
    }
}
function Fork(){
    if($("#id").html() =='0'){
      autohideMsgPopUp('error',' Cant fork , Please save it before',5);
    }
    else{
      o = getUnifiedParams()
      t={'id':0,'name':o.name+'-Forked!', 'main':o.main,'func':o.func,'input':o.input,'topic':o.topic,'short_desc':o.short_desc  }
      setUnifiedParams(t)
      autohideMsgPopUp('success',' Fork Done! Please Save.');
    }
}
function Download(id) {
  $.get('/api/cleancode/'+id+'/download/'); 
  autohideMsgPopUp('success','<b>succes!</b>'+'Download done!');
}
/*************  End of On Click Event call ****************************/

/*************************************************
          I N T E R V I E W  C O M M A N D 
*************************************************/
var CLEANCODE_IS_INTERVIEW_MODE = false; // Make it false otherwiese.
var CURRENT_QUESTION_ID = -1;
function show_interview_panel(){$('#interview_panel').addClass('active');$('#output_panel').removeClass('active');}
function hide_interview_panel(){$('#interview_panel').removeClass('active');$('#output_panel').addClass('active');} 
function enterInterviewMode(){
  $('.editor-btn').hide();
  $('.tut-btn').hide();
  $('.editor-btn-left').hide();
  //editors.main.setReadOnly(true);//ACE  
}
function initInterview(){
    enterInterviewMode();
    function getInterviewData(){
        return INTERVIEW_DATA;//TODO  
    }
    INTERVIEW_DATA = getInterviewData();
    ColaborationUtil(INTERVIEW_DATA.hash)
    $('.org_name').html(INTERVIEW_DATA.organizar)
}
function showInstraction(){    
    function TnC_pass(){
        initInterview();
        $('.lunchpage').hide();$('.instraction_page').show()
        $('.instraction_page .qhead').html('Interview Instractions')
        $('.instraction_page .qbody').html(INTERVIEW_DATA.instraction)
        CURRENT_QUESTION_ID = -1;    
    }
    showWinStylePopup("Terms and conditions!", "Welcome to our PeerReview. If you continue to browse and use this service, you are agreeing to comply with and be bound by the <a href='#'>following</a> terms and conditions of use. Please go though and click 'Agree' button as below.", true, "Agree", TnC_pass) 
}
function showNextQuestion(){
    if( CURRENT_QUESTION_ID == INTERVIEW_DATA.question_set.length -2 ){ //last to last qn..
        $('#next_prob_btn').html('Finish')
    }
    function save_sol(){
        INTERVIEW_DATA.question_set[CURRENT_QUESTION_ID].candidate_solution = editors.main.getValue()
    }
    
    function go_next(){
        if( CURRENT_QUESTION_ID == INTERVIEW_DATA.question_set.length -1 ){ //ends..
            showInterViewEndMsg();
            return;
        }
        CURRENT_QUESTION_ID++;
        var cur_q = INTERVIEW_DATA.question_set[CURRENT_QUESTION_ID]
        $('.question_page .qhead').html('Q'+(CURRENT_QUESTION_ID+1)+'.  '+cur_q.name)
        $('.question_page .qbody').html(cur_q.desc) 
        gEditors.setEditorData('main','');
        //editors.main.setReadOnly(true)
    }    
    if(CURRENT_QUESTION_ID == -1){ //We will add first Question..
        //sent a mail to organizar
        call_backend_api('get','/api/email/',{recipient:INTERVIEW_DATA.organizar_email, subject:'[ PeerReview ] Starting interview with '+INTERVIEW_DATA.candidate.name,template:'cleancode_interviewstart_invite.html',name:INTERVIEW_DATA.candidate.name,email:INTERVIEW_DATA.candidate.email,id:INTERVIEW_DATA.candidate.id })
        $('.instraction_page').hide();$('.question_page').show();
        $('#interview_panel').addClass('sidebar')
        go_next();
    }
    else{
        //showWinStylePopup(title, desc, is_cancel_able,yes_txt, yes_cb, no_txt,no_cb)
    showWinStylePopup("The solution of this problem will be Locked!", "Looks like you have answered this question. If you move to next question, you can't come back again to previus question and the solution will be locked! DO you want to proceed to next question ?", true, "Yes", function(){save_sol();go_next();}) 
    }
}

function CopyCodeToEditor(){
    //editors.main.setReadOnly(false)
    if( editors.main.getValue() != "" ){
       return;
       log('Dont copy as we have something ...')
    } 
    if( CURRENT_QUESTION_ID == INTERVIEW_DATA.question_set.length-1){return;}
    gEditors.setEditorData('main',INTERVIEW_DATA.question_set[CURRENT_QUESTION_ID].sol);
    
}
function saveCurrentAnswer( ){
    if( CURRENT_QUESTION_ID == INTERVIEW_DATA.question_set.length -1 ){return;}
    //SOME API CALL
}
function showInterViewEndMsg(){
    $('#interview_panel').removeClass('sidebar');$('.question_page').hide();$('.exit_page').show();
    //Send the ans to organizar    
    INTERVIEW_DATA.subject = '[ PeerReview ] Interview status for '+INTERVIEW_DATA.candidate.name
    INTERVIEW_DATA.template = 'cleancode_interviewans.html'
    INTERVIEW_DATA.recipient = INTERVIEW_DATA.organizar_email +','+ INTERVIEW_DATA.candidate.email
    //call_backend_api(type,url,param,before_cb,success_cb,error_cb,complete_cb,contentType){
    call_backend_api('post','/api/email/',JSON.stringify(INTERVIEW_DATA),'','','','',"application/json; charset=utf-8")
}

/******************  END of Interview Command *********************/




/*###################  E N D OF ACTUAL C O D E ##########################*/




  

/***********************************************************************************
                    START OF TEMPALTE
************************************************************************************/
  var TEMPLATE = function () {
    this.codeTemplateMapList={}
  };
  
  TEMPLATE.prototype.addTemplate = function (language,name,main,func,input) {
    var t = {language:language,name:name, func:func, main:main, input:input};
    if (this.codeTemplateMapList.hasOwnProperty(language)){
      this.codeTemplateMapList[language].push(t)      
    }
    else{
    this.codeTemplateMapList[language]=[]
    this.codeTemplateMapList[language].push(t)
    }
  };

  TEMPLATE.prototype.select_temp  = function (language,id) {
    var _t = this.codeTemplateMapList[language][id]
    _t.id =0
    setUnifiedParams(_t);
  };
  

  /*********************  Add Your Template Here ************************/
  var T = new TEMPLATE();

  T.addTemplate('c','hello1',
    '#include<stdio.h>\nint main(){\n    printf("Hello cleanCode!!! \\n");\n    return 0;\n}\n',
    '',
    ''); 
    
  T.addTemplate('c','hello2',
    '#include<stdio.h>\nint main(){\n printf("fact of %d is %d\\n",10,fact(10));\n return 0;\n}',
    'int fact(int a){\n    //Write your code here..\n}',
    '');

  T.addTemplate('c','input1',
    '#include<stdio.h>\nint main(){\n    int i;\n    float f;\n    char c[10];\n    \n    scanf("%d",&i);\n    scanf("%f",&f);\n    scanf("%s",c);\n    \n    printf("We read i= %d ;f= %f ;c= %s;",i,f,c);\n    return 0;\n}\n',
    '',
    '10\n10.55\nhello10');

    
  T.addTemplate('c','input2',
    '#include<stdio.h>\nint main(){\n    int i,n; char s[100]; \n    scanf("%d",&n);\n    for(i=0;i<n;i++){\n        fgets( s, 100, stdin );\n        puts(s);    \n    }\n    return 0;\n}\n',
    '',
    '3\nhello1 hello1\nhello2\nhello3');

    
  T.addTemplate('c','input3',
    '#include<stdio.h>\nint main(){\n  int n;\n  int *a =READ_INT_ARR(&n);\n  PRINT_INT_ARR(a,n); \n  return 0;\n}',
    '',
    '1 2 3 4 5 6 7  ');

  T.addTemplate('c','input4',
    '#include<stdio.h>\nint main(){\n  int **mat = READ_INT_2DARR(4,4);\n  PRINT_INT_2DARR(mat,4,4);\n  return 0;\n}',
    '',
    '10 20 30 40\n0   0  0  0\n10 10 10 10\n1   2  3  4');
    
  T.addTemplate('py','factorial',
    'def fact(i):\n  if(i==0):\n    return 1;\n  else:\n    return i*fact(i-1)\n\nprint fact(3)',
    '',
    '');
  T.addTemplate('py','trangle',
    '"Draw a Trangle"\ndef trangle(x):\n  for i in range(x/2+1):\n    print \' \'*(x/2-i),\n    print \'*\'*(2*i+1)\n\ntrangle(20)',
    '',
    '');
    
  T.addTemplate('py','Love',
    '"Draw a Trangle"\ndef love(x):\n  for i in range(x-1):\n     print \' \'*(x-i-1),\'*\'*(i*2+1),\' \'*(2*(x-i-2)+1),\'*\'*(i*2+1)\n  print \' \', \'*\'*((x*2-2)*2+1)\n  print \' \', \'*\'*((x*2-2)*2+1)\n  for i in range(((x*2-2)*2+1)): \n    print \'\', \' \'*i,\'*\'*((x*2-2)*2+1-2*i)\nlove(10)',
    '',
    '');

  T.addTemplate('cpp','hello World',
    '#include<iostream>\nusing namespace std;\nint main(){\n    cout<<"hello World";\n}',
    '',
    '');  
 T.addTemplate('java','HelloWorld',
    'public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, World");\n    }\n}\n',
    '',
    '');
 T.addTemplate('c','Custom:Single Linkedlist',
'#include "dlinkedlist.h"\nint main(){\n  int a[]={1,2,3,4,5,6,7,8,9,0};\n  snode *s = buildLinkedList(a,10);\n  print(s);\n}',
    '',
    '');
 T.addTemplate('c','Custom:Bits ops',
'#include "dbit.h"\nint main(){\n  show_bit(1023);\n}',
    '',
    '');
 T.addTemplate('c','Custom: dtest Example',
 '#include "dtest.h"\nint add(int n){\n  int sum=0;\n  for (int i=0;i<=n;i++)\n    sum+= i;\n  return sum;\n}\nint main(){\n  TEST_INT_TO_INT(add);\n}',
 '',
  '4\n1 1\n2 3\n10 55\n10 100');
  /*********  End of Temp Add ***********/
  // Event on Change Editor Language //
  function onChangeLang(language){
    if( language == undefined) language = 'c'
    language= $("#language").val() ;
    
    // Populate correct Template
    if(T.codeTemplateMapList[language] == undefined) { $("#template").html('<option selected disabled>No template</option>');cleanCodeObj();return;}
    html='<option selected disabled>Select template</option>'
    for( i =0;i<T.codeTemplateMapList[language].length;i++)
    {
      html+= '<option value="'+i+'">'+T.codeTemplateMapList[language][i].name+'</option>'
    }
    $("#template").html(html)
    // Set the correct language in Editor Mode.. 
    setEditorMode(language);    
  }
  

  function onChangeTemplate(){
      language=$("#language").val()
      temp=$("#template").val()
      T.select_temp(language,temp);
      autohideMsgPopUp('success','<b>succes!</b>'+'Templete Code got copied');
  }

/***********************************************************************************
                    E N D  of  TEMPALTE
************************************************************************************/



/***********************************************************************************
                    SHORTCUTS
************************************************************************************/

$(document).ready(function () {
    jQuery(document).bind('keydown', function (event){
            if (event.keyCode == 120) { runProg(); }  //press F9 to Run....
            if (event.keyCode == 113) { quickSave(); } //Press F2 for save...
            if (event.keyCode == 27) { cancelAllSideBar();dismissWinStylePopup(); } //Press ESC , hide all windows..
            if (event.keyCode == 119) { changemode(); } //Press F8  ,Change Mode
  });
});  
/***********************************************************************************
                    E N D  of  M A I N  S C R E P T 
************************************************************************************/



/***********************************************************************************
                    DATA BINDINGS
************************************************************************************/

RegisterDataBindingOnEvent('keyup',"input[name='name']",function(){$("#name").html($("input[name='name']").val());})
RegisterDataBindingOnEvent('keyup',"input[name='short_desc']",function(){$("#short_desc").html($("input[name='short_desc']").val());})

/***********************************************************************************
                    E N D  of  BINDING
************************************************************************************/

/***********************************************************************************
                    CHAT FRAMEWORK 
************************************************************************************/
function log(x){
    //document.getElementById("a").innerHTML += x+'<br>'
    console.log(x);
}
var ChatEngine = function(fref, rid){
    self = this
    self._rid = rid
    self._fref = fref
    self._audio = new Audio('/media/sound/pling.ogg');
    //Auto fill
    self._uid = undefined
    self._unane = undefined
    self._fireBaseRef = undefined
   
    self._initOrCreate = function(){ //
      self._fireBaseRef =  new Firebase(fref+rid+'/chat/');
      //self._fireBaseRef.set({users: [], messages: [] });
      nw = self._fireBaseRef.child('users').push({name: 'Dipankar', id: "hrello"});
      log(nw.key())
    }
    self._initOrCreate();
}
ChatEngine.prototype.joinChatRoom = function(uid,uname,pic){
     self = this
    nw = self._fireBaseRef.child('users').push({name: uname, id: uid,pic: pic, 'isTyping':false});
    self._uid = uid
    self._uname = uname;
    self._pic = pic;
    log('User Joined');
}
ChatEngine.prototype.leaveChatRoom = function(){
     self = this
    self._fireBaseRef.child('users').child(self._uid).remove()
  
}
ChatEngine.prototype.getPreviousConversation = function(){
  
}
ChatEngine.prototype.getID = function(){
  return self._rid;
}
ChatEngine.prototype.registerRecvMsgHandalar = function(func){
   self = this
   self._fireBaseRef.child('messages').on('child_added', function(snapshot) {
      func(snapshot.val());
      
      self._audio.play();
   });
}
ChatEngine.prototype.registerRecvNotificationHandalar = function(func){
     self = this
   self._fireBaseRef.child('users').on('child_added', function(snapshot) {
      func('user_added', snapshot.val(),'outside');
   });
   self._fireBaseRef.child('users').on('child_removed', function(snapshot) {
      func('user_removed', snapshot.val());
   });
   // It will cover typing...
   self._fireBaseRef.child('users').on('value', function(snapshot) {
      func('user_changed', snapshot.val());
    });

}
ChatEngine.prototype.sendMessage= function(msg,pic){
   self = this
   self._fireBaseRef.child('messages').push({uid:self._uid, name: self._uname, pic:pic, msg:msg,time:timeStamp()});
   self._fireBaseRef.child('users').child(self._uid).set({'isTyping':false});
}
ChatEngine.prototype.sendNotification= function(type){
     self = this
   if(type == 'typing'){
       self._fireBaseRef.child('users').child(self._uid).set({'isTyping':true});
   }
   if(type == 'stop_typing'){
       self._fireBaseRef.child('users').child(self._uid).set({'isTyping':false});
   }
}
/* test
c = new ChatEngine('https://cleancode.firebaseio.com/','hcc');
c.joinChatRoom('1','Dipankar')
c.registerRecvMsgHandalar(function (a){ log(a.msg)})
c.registerRecvNotificationHandalar(function (a,b){ log(a+'==>'+b)})
c.sendMessage('Hello How r u doing...')
c.sendNotification('typing')
c.leaveChatRoom()
*/
/***********************************************************************************
                    End of CHAT FRAMEWORK 
************************************************************************************/

/***********************************************************************************
                    ACE EDITOR FRAMEWORK 
************************************************************************************/
var MyEditor = function(eid){
    self = this
    self._editors = {}
    self._d_lang= 'javascript'
    self._d_theme= 'twilight'
    self._now_mode_preferences = 'c'    
    self._editors[eid] ={}
    self._editors[eid].ace = self.initEditor(eid);
    self._editors[eid].lang = 'c'
    self._editors[eid].theme = 'twilight'
    
    //Static data
    self._template = {
        c: '#include <stdio.h>\n#include <string.h>\n#include <math.h>\n#include <stdlib.h>\n\nint main() {\n\n    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    \n    return 0;\n}\n',
        cpp :'#include <cmath>\n#include <cstdio>\n#include <vector>\n#include <iostream>\n#include <algorithm>\nusing namespace std;\n\n\nint main() {\n    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   \n    return 0;\n}\n',
        py:"def test():\n    print 'Hello World'\n    # Write your code here\ntest()\n",
        java:'import java.io.*;\nimport java.util.*;\nimport java.text.*;\nimport java.math.*;\nimport java.util.regex.*;\n\npublic class Solution {\n\n    public static void main(String[] args) {\n        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */\n    }\n}',
        js:"function sayHello(){\n    log('Hello World');\n}\nsayHello();"           
    }
    
}
MyEditor.prototype.initEditor = function(eid){
        self = this
        var editor = ace.edit(eid);
        editor.setTheme("ace/theme/"+self._d_theme);
        var session = editor.getSession();
        session.setUseWrapMode(true);
        session.setUseWorker(false);
        session.setMode("ace/mode/"+self._d_lang);
        // set other option,
        editor.setFontSize(17);
        return editor;
}
MyEditor.prototype.addEditor = function(eid){
    this._editors[eid]={}
    this._editors[eid].ace = this.initEditor(eid)
    this._editors[eid].lang = 'c'
    this._editors[eid].theme = 'twilight'
}
MyEditor.prototype.getEditor = function(eid){
    return this._editors[eid].ace;  
}
MyEditor.prototype.get = function(eid){
    return this._editors[eid];   // We get all the deyails here.
}
MyEditor.prototype.getEditorData = function(eid){
  return this._editors[eid].ace.getValue();
}
MyEditor.prototype.setEditorData = function(eid,val){
    this._editors[eid].ace.setValue(val);
}
MyEditor.prototype.setEditorTheme = function(eid,theme){
    this._editors[eid].ace.setTheme("ace/theme/"+theme);
    this._editors[eid].theme = theme
}
MyEditor.prototype.setEditorMode  = function(eid,lang){
    self = this
    self._now_mode_preferences = lang
    this._editors[eid].lang = lang
    if (lang =='c' || lang =='cpp') lang ='c_cpp'
    if(lang == 'py') lang ='python'
    if(lang == 'js') lang ='javascript'
    
    this._editors[eid].ace.getSession().setMode("ace/mode/"+lang);    
}
MyEditor.prototype.setColaboration  = function(eid,colaboration_url){
    var furl = 'https://cleancode.firebaseio.com/firepads/'+colaboration_url
    var firepadRef  = new Firebase(furl);
    var editor = this._editors[eid].ace
    editor.setValue('');
    var firePad = Firepad.fromACE(firepadRef, editor, {});
    console.log(' This ediot i now on shared...')
}
MyEditor.prototype.setEditorWithTemplate= function(eid,language){
    self = this
    if( language == undefined) language = 'c'
    switch(language){
        case 'c': 
            data = self._template['c']
            mode ='c';
            break;
        case 'cpp': 
            data = self._template['cpp']
            mode ='cpp';
            break;
        case 'py':
            data = self._template['py']
            mode ='py'
            break;
        case 'java':
            data = self._template['java']
            mode ='java'
            break;
        case 'js': 
            data = self._template['js']
            mode ='js'
            break;
    }    
    if( this.getEditorData(selected_tab).length <= 10 || 
            self._template[this._editors[eid].lang] == this.getEditorData(selected_tab)){
            this.setEditorData (selected_tab,data)
    } else{
           console.log('canot reset data')
    }
    this.setEditorMode(eid,mode)
}
/***********************************************************************************
                    DATA BINDING FRAMEWORK
************************************************************************************/
var MyDataBind = function(ids){
    self = this
    self._ids = {}
    for (i = 0; i < ids.length; i++) {
        if ($('#'+ids[i]).length == 0){ console.log('No such id: '+ids[i]);continue;}
        self._ids[ids[i]] = self.getValueByID(ids[i])
    }    
}

MyDataBind.prototype._is_input_type = function(jq){
    jq =$('#'+jq)
       return (jq.is('input') || jq.is('textarea') || jq.is('select') || jq.is('checkbox') || jq.is('radio'))
}

MyDataBind.prototype.addID  = function(eid){
    this._ids[eid] = self.getValueByID(eid);
}

MyDataBind.prototype.setValueByID  = function(eeid,val){
    eid = $('#'+eeid)
    if(this._is_input_type(eeid)){
        eid.val(val); this._ids[eeid]= val;
    } else {
        eid.html(val); this._ids[eeid]= val;
    }
}

MyDataBind.prototype.getValueByID  = function(eid){
    if(this._is_input_type(eid)){
        return $('#'+eid).val()
    } else {
        return $('#'+eid).html();
    }
}

MyDataBind.prototype.getData  = function(){
    var obj ={}
    for (var key in this._ids) {
      if (this._ids.hasOwnProperty(key)) {
        obj[key]=this.getValueByID(key)
      }
    }
    return obj
}

MyDataBind.prototype.setData  = function(obj){   
    for (var key in obj) {
      if (this._ids.hasOwnProperty(key)) {
        this.setValueByID(key,obj[key])
      }
    }
    return obj
}
/* Test:
    var m = new MyDataBind(['id','name'])
    m.getData()
    m.setData({'id':'jjhjh','name':'hghghg'})
    m.getValueByID('id')
    m.setValueByID('id','55555')
*/

/***********************************************************************************
                    JA EXECUTION FRAMEWORK
************************************************************************************/
var MyJSExecution= function(code,dependency_l){
    self = this
    self._code = code
    self.dependencies = dependency_l
    
    // build continer
    this.clean = function clean(){
        var oldScript = document.getElementById('scriptContainer');
        if (oldScript) {
          oldScript.parentNode.removeChild(oldScript);
        }
        newScript = document.createElement('script');newScript.id = 'scriptContainer';
        document.body.appendChild(newScript);
    }
    this.clean();
    this.log = function(a){ console.log('>>> '+ a)}
}

MyJSExecution.prototype.addLogAction = function(func){
    this.log = func.toString()
   // window.prototype.log = func
}
MyJSExecution.prototype.run = function(){
    this.clean();
    var scriptText = this.log + this._code
    var ele = document.getElementById('scriptContainer');
    ele.text = scriptText;
    document.body.appendChild(newScript);
}
MyJSExecution.prototype.setAndRun = function(code,dependency_l){
    this.clean();
    this._code = code
    this.dependencies = dependency_l
    this.run();
}

/*********************************************************
    C O D E   P L A Y E R   F R A M E W O R K
**********************************************************/
var CodePlayer = function(ace_instance,autoStart){
    if(ace_instance == undefined){
    console.log('Canot initilized as ace_instance is null ');return;}
    self = this;
    self._ace = ace_instance;
    self._isrecording = false;
    self._isplaying = false;
    self._changelist=[];
    self._play_speed = 1; // 1x means .1 sec .
    self._playoffset = 0;
    self._init_data = undefined;
    
    self._vlength = 0; // ms
    self._seek_break_length  = 100; // 100ms 
    self.seek_partition = []
    self.seek_partition_len = 0;
    self._auto_start = autoStart;
    if(self._auto_start){
        console.log('Automatic started the recoder ..')
        self.start_recording();
    }
    console.log('Code Player Intilized');
    self.start_t =0;
    self.end_t =0;
}
 CodePlayer.prototype.clean = function(){
    self._isrecording = false;
    self._isplaying = false;
    self._changelist=[];
    self._play_speed = 1; // 1x means .1 sec .
    self._playoffset = 0;
    self._init_data = undefined;
    
    self._vlength = 0; // ms
    self._seek_break_length  = 100; // 100ms 
    self.seek_partition = []
    self.seek_partition_len = 0;
    self._auto_start = false;
    self.start_t =0;
    self.end_t =0;
 }
 CodePlayer.prototype.attachProgressCallBack = function(func){
    self._progress_cb = func
 }
 CodePlayer.prototype.setSpeed = function(x){
    self = this;
     if( x <= 1 ){ // if x ==0 , tat means we reset it.
         self._play_speed = 1; return true;
    }
     self._play_speed = self._play_speed /x;
     return true;
 }

CodePlayer.prototype.start_recording = function(){
   self = this;
   if(self._isrecording == true) {
     console.log("can't start, already started..."); return false;
   }
   this.clean();
   console.log('start_recording...')
   self._isrecording = true
   self._init_data = self._ace.getValue();
   self._ace.setReadOnly(false);
   self._ace.on("change", function(e){
        var keyevent = {
            'data': e.data,
            'timestamp': new Date().getTime()
        };
        if (self._isrecording){
            self._changelist.push(keyevent);
            console.log(e,keyevent);
        }
    });
    return true;
}

CodePlayer.prototype.stop_recording = function(){
   self = this;
   if(self._isrecording == false) {
     console.log("can't stop, already stopd..."); return false;
   }
   console.log('stop_recording')
   self._isrecording = false;
   self._ace.off();
   self.start_t = self._changelist[0].timestamp;
   self.end_t = self._changelist[self._changelist.length-1].timestamp;
   self._vlength = self.end_t - self.start_t;
   
   self.build_seek_partition();
   return true;
}
CodePlayer.prototype.build_seek_partition = function(){
    self = this;
    var idx = 1;
    var start_t = self._changelist[0].timestamp    
    n = self._changelist.length
    var loc =[]
    for( var i = 0 ; i < n;){        
        while((i < n) && (self._changelist[i].timestamp < start_t + idx * self._seek_break_length )){
          loc.push(i);
          i++;
        }
        self.seek_partition.push(loc);idx++;loc =[]
    }
    self.seek_partition_len = self.seek_partition.length 
    return true;
}

CodePlayer.prototype.seekTo = function (pos){
    self = this;
    if(pos >= self.seek_partition_len ) {console.log('Seek cross the max limit'); return false;}
    self._ace.setValue(self._init_data); 
    for(var i =0;i< pos;i++){
      for( var j =0;j < self.seek_partition[i].length; j++){
          self.applyChanges(self.seek_partition[i][j])
      }
    }
 
    if(((pos+1) < self.seek_partition_len) && (self.seek_partition[pos+1].length > 0)){
        self._playoffset = self.seek_partition[pos+1][0]
        if(self._isplaying == true)
           self.playOff();
    }
    return true;
}

//playing part
CodePlayer.prototype.start_playing = function(e){
    self = this;
    if(self._isrecording == true) {
     console.log('Can not play.. we are in recodring stage'); return false;
   }
    if(self._isplaying == true) {
     console.log('Can not play playing ...'); return false;
   }
   if(self._changelist.length == 0){
        console.log('Can not play playing you need to record something'); return false;
   }
    
   self._isplaying = true;
   if( self._playoffset  == 0){ // we are strating from begging...
       self._ace.setValue(self._init_data); 
       self._ace.clearSelection();
       self._ace.setReadOnly(true);
       self._startTime=self._changelist[0].timestamp;
       console.log("start_playing")
   }
   else{ // we are moving from pause to play..
       console.log("resumeing ...")
   }
   self.playOff();
   return true;
}

CodePlayer.prototype.playOff = function() {
    self = this;
    if(self._playoffset > self._changelist.length -1){
        console.log('invalid offset');return false;
    }
    var percentage =  (self._changelist[self._playoffset].timestamp - self.start_t)/(self.end_t - self.start_t)*100;
    if ( self._progress_cb != undefined) {    self._progress_cb(percentage);}
    
    if (self._playoffset == (self._changelist.length -1)) { //last elemner
        self.applyChanges(self._playoffset);
        self.stop_playing(); 
        console.log('end video');return false; 
    }
    
    if(self._isplaying == true) {
        self.applyChanges(self._playoffset);
        self._playoffset = self._playoffset + 1;
        setTimeout(function(){
              self.playOff();
        }, self._play_speed*(self._changelist[self._playoffset].timestamp - self._changelist[self._playoffset- 1].timestamp));
    }
}
 CodePlayer.prototype.stop_playing = function() {
     self = this;
     if(self._isrecording == true) {
      console.log('Can not stop.. we are in recodring stage'); return false;
    }
    if(self._isplaying == false) {
      console.log('Already stop'); return false;
    }
    console.log("stop_playing")
    self._isplaying  = false;
    self._playoffset = 0;
    self._ace.setReadOnly(false);
    return true;
 }
 CodePlayer.prototype.reply_playing = function() {
    self = this;
    self.start_playing();
    self.stop_playing();
    return true;
 }
 CodePlayer.prototype.pause_playing = function() {
    self = this;
    if(self._isrecording == true) {
       console.log('Can not pause.. we are in recodring stage'); return false;
    }
    if(self._isplaying == false) {
      console.log('Can not pause playing ...'); return false;
    }
    self._isplaying  = false; // we are not reset the offset..
    return true;
 }

CodePlayer.prototype.applyChanges = function (i) {
        self = this;
        var k = self._changelist[i];
        self._ace.clearSelection();
        switch (k.data.action) {
                case 'insertText':
                    if (k.data.range) {
                        self._ace.moveCursorTo(k.data.range.start.row, k.data.range.start.column);
                    } 
                    else {
                        self._ace.moveCursorTo(0, 0);
                    }
                    self._ace.insert(k.data.text);
                    break;
                case 'removeText':
                    if(i == self._changelist.length - 1)
                     {   break;

                     }   
                    else
                    {
                        self._ace.remove(k.data.range);
                        break;
                    }
                    break;
                case 'removeLines':
                    if(i == self._changelist.length - 1)
                     {   break;

                     }   
                    else
                    {
                        self._ace.remove(k.data.range);
                        break;
                    }

                default:
                    console.log('unknown action: ' + k.data.action);
        }
}  //end of apply changes

/* Test:
    var editor = ace.edit("main_1");
    editor.setTheme("ace/theme/twilight");
    editor.session.setMode("ace/mode/javascript");
    editor.$blockScrolling = Infinity;
    var a = new CodePlayer(editor);


*/

/***********************************************************************************
                C O M M O N   U X   F R A M E W O R K
************************************************************************************/
var CommonUx= function(){
    self = this
    self._all_componenet={} 
}

CommonUx.prototype.addComponenet = function(type,id){ // it must be an id 
    this._all_componenet[id] = {}
    this._all_componenet[id].type = type
    jid = $('#'+id);
    this._all_componenet[id].jid = jid
    this._all_componenet[id]._func = undefined
    selfe = this
    switch(type){
      case 'star_btn':/*
              html='<fieldset class="rate">';
              var arr =["1/2 star","1 star","1 1/2 stars","2 stars","2 1/2 stars","3 stars","3 1/2 stars","4 stars","4 1/2 stars","5 stars"];
              for (var i = 10; i > 0; i--) {
                  if(i%2==0)
                  html+='<input type="radio" id="'+id+i+'" name="'+id+'"  value="'+i+'" /><label for="'+id+i+'" title="'+arr[i-1]+'"></label>';              
                  else 
                  html+='<input type="radio" id="'+id+i+'"  name="'+id+'" value="'+i+'" /><label class="half" for="'+id+i+'" title="'+arr[i]+'"></label>';             
                   
             };
             html+=' </fieldset>';
            

             jid.html(html);  
             $(document).on('click','.rate > input', function (e){ gCom.getData('star_btn',this);})
      */
             break;
    

            //todo
      case 'popup':
            if( !($('.overlay').length )){ $('body').append('<div class="overlay"></div>')}
            
            jid.addClass("animated bounceOut")
            //Event attach  : use selfe .
            $(document).on('keyup', function(e) { if(e.which == 27){ selfe.hideComponent(id); }});
            $(document).on("click", '.overlay', function(){ selfe.hideComponent(id);});
            break;
      case 'social_auth':
            html = '\
            <p class="social_auth_list" style="padding-top: 15px;">\
                    <a data-id="google" onclick="openOpopup(\'/login/google\')"style="border-radius: 50%; margin: 5px; border: 1px solid #ccc; padding: 10px 12px;"><i class="fa fa-google" style="padding-left: 3px;"></i></a>\
                    <a data-id="facebook" onclick="openOpopup(\'/login/facebook\')"  style="border-radius: 50%; margin: 5px; border: 1px solid #ccc; padding: 10px 12px;"><i class="fa fa-facebook" style="padding-left: 3px;"></i></a>\
                    <a data-id="github" onclick="openOpopup(\'/login/github\')" style="border-radius: 50%; margin: 5px; border: 1px solid #ccc; padding: 10px 12px;"><i class="fa fa-github" style="padding-left: 3px;"></i></a>\
                    <a data-id="linkedin" onclick="openOpopup(\'/login/linkedin\')" style="border-radius: 50%; margin: 5px; border: 1px solid #ccc; padding: 10px 12px;"><i class="fa fa-linkedin" style="padding-left: 3px;"></i></a>\
                </p>'
            jid.html(html);            
            jid.addClass("animated bounceIn")            
            break;
      default:
            console.log('All ')
    }
}
CommonUx.prototype.getComponent = function(id){
    return this._all_componenet[id];
}
CommonUx.prototype.registerCompleteHandaler = function(id,func){
    switch(this._all_componenet[id].type){
      case 'social_auth':
            window.login_callback = function(id,name,email,pic){
                func({id:id,name:name,email:email,pic_url:pic})
            }
            break;
      case 'popup':
             break;
      default:
    }
}

CommonUx.prototype.getData = function(type,id){
    switch(type){
      case 'star_btn':
              
            //  console.log(id.name+'  > ' +id.value);
              break;
            //todo
      case 'popup':
             break;
      default:           
    }
}

CommonUx.prototype.setData = function(id,typr,val){
    switch(id){
      case 'star_btn':
            //todo
            /*
            var r=typr+val;
              $('#'+typr+' .rate input:radio[id="'+r+'"]').prop('checked', true);
              console.log('setting '+typr +' to >'+val);
            */
              break;
      case 'popup':
             break;
      default:           
    }
}

CommonUx.prototype.showComponent = function(id){
    this._all_componenet[id].jid.addClass('active')
    jid = this._all_componenet[id].jid
    switch(this._all_componenet[id].type){
      case 'star_btn':
            //todo
            break;
      case 'popup':
            $('.overlay').addClass('active'); jid.removeClass('bounceOut').addClass('bounceIn'); break;
      default:
            this._all_componenet[id].jid.show();
    }
}

CommonUx.prototype.hideComponent = function(id){
    jid = this._all_componenet[id].jid
    jid.removeClass('active')
    switch(this._all_componenet[id].type){
      case 'star_btn':
            //todo
            break;
      case 'popup':
            jid.removeClass('bounceIn').addClass('bounceOut'); 
            $('.overlay').removeClass('active');
            break;            
      default: 
            this._all_componenet[id].jid.hide();
    }
}

/*********************************************************
    G R O U P   A U D I O   C H A T  F R A M E W O R K
*************z*********************************************/
var GroupAudioVideoChat= function(){
    self = this
    self._all_componenet={} 
}

GroupAudioVideoChat.prototype.joinGroup = function(type,cb){ // type might be audio, video or both
    self = this
    return true;
}
GroupAudioVideoChat.prototype.leaveGroup = function(type){
    self = this
    return true;
}

/*********************************************************
    U S E R   P R O F I L E   F R A M E W O R K
**********************************************************/
var UserProfiles= function(id){
    self = this
    this._owner_id = undefined  //This is the owneer
    this._owner_data = undefined  //This is the owneer
}

UserProfiles.prototype.getData = function(cb){ // type might be audio, video or both
    return this._owner_data;
}
UserProfiles.prototype.setData = function(data){
     this._owner_data = data;
     return true;
}
UserProfiles.prototype.getID = function(_id,data){
    return this._owner_data.id
}
/*********************************************************
    T E L E M E T R Y   F R A M E W O R K
**********************************************************/
var Telmetry= function(){
    self = this
    self._endurl = '/api/ks/telemetry/'
    self._session_id = genRandomString(10);
    self._is_enable = true
}
UserProfiles.prototype.enable = function(){
    self._is_enable = true
}
UserProfiles.prototype.disable = function(){
    self._is_enable = false
}
Telmetry.prototype.log = function(tag, type, msg,obj){ // type might be audio, video or both
    if (['debug', 'info', 'error'].indexOf(type) < 0) {
        console.log('We have only debug/info/error');
    }
    if( tag == undefined ) { console.log("lag can't be null");return;}
    var lobj={}
    lobj.type = type
    lobj.tag = tag
    lobj.msg = msg
    lobj.time = timeStamp()
    lobj.data = obj
    lobj.session = self._session_id
    if(self._is_enable){
        call_backend_api('POST',self._endurl,lobj,'before_cb','success_cb','error_cb','complete_cb','json')
    }
}

/*************************************************
    C O M P I L A T I O N   F R A M E W O R K 
*************************************************/
var CAN_RUN = false;
var CompilationEnv = function(){
    self  = this
    self._endpoint = '/api/cleancode/compile/'
    self._endpoint_c ='/api/cleancode/compile/'
    self._endpoint_r ='/api/cleancode/run/'
    self._endpoint_p ='/api/cleancode/run/'
    // COMPILED_SUCCESSFULLY COMPILED_WITH_WARN
    self._compile_state = undefined 
    
    //handlar
    self._callback_compile_before = undefined
    self._callback_compile_success = undefined
    self._callback_compile_error = undefined
    
    self._callback_run_before = undefined
    self._callback_run_success = undefined
    self._callback_run_error = undefined
    
    this._obj = undefined
    this._is_previous_compilation_succeed  = false
    
    this._is_run_after_compilation_succeed  = false
    
}
CompilationEnv.prototype.verifyObject = function(obj){
    self = this
    if( obj.name == undefined || 
        obj.id == undefined || obj.language == undefined || 
        obj.main == undefined || obj.input == undefined){
        return false
        }
    return true;
}
CompilationEnv.prototype.compile = function(obj){
    self = this
    this._obj = obj
    if(!this.verifyObject(obj)){
        console.log('Object Verification failed;')
        return ;
    }
    call_backend_api('post',self._endpoint_c,obj,self._callback_compile_before,self._callback_compile_success,self._callback_compile_error,'complete_cb');
}
CompilationEnv.prototype.run = function(obj){
    self = this
    if(!this.verifyObject(obj)){
        console.log('Object Verification failed;')
        return ;
    }
    call_backend_api('post',self._endpoint_r,obj,self._callback_run_before,self._callback_run_success,self._callback_run_error,'complete_cb');
}
CompilationEnv.prototype.runIfCompileSucceed = function(obj){ 
    self = this
    this._obj = obj
    this._is_run_after_compilation_succeed = true
    this.compile(obj);
}
CompilationEnv.prototype.attachCompileBeforeHandaler= function(func){
    self = this
    self._callback_compile_before = func
}
CompilationEnv.prototype.attachCompileSuccessHandaler= function(func){
    self = this
    self._callback_compile_success = function(data){
        func(data);
        if( data["can_run"]=="yes"){
                self._is_previous_compilation_succeed = true;
                if(self._is_run_after_compilation_succeed){
                   self.run(self._obj);
                   self._is_run_after_compilation_succeed =false
                }
        }     
    };
}
CompilationEnv.prototype.attachCompileErrorHandaler= function(func){
    this._callback_compile_error = func
}

CompilationEnv.prototype.attachRunBeforeHandaler= function(func){
    this._callback_run_before = func
}
CompilationEnv.prototype.attachRunSuccessHandaler= function(func){
    this._callback_run_success = func
}
CompilationEnv.prototype.attachRunErrorHandaler= function(func){
    this._callback_run_error = undefined
}
