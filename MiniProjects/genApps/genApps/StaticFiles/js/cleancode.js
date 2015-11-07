/*#################################################################
    Clean code FRAMEWORK
    - This js file will contains all the framework we need to build  for our codimg platform
    - All framework must respect OOP patterns
    - Please list down the framewrok with a single line desc here
    
    1. ChatEngine - to support custom chat engine with fire base back-end
    2. 
####################################################################*/

/* List of global config : set it False for production.*/
DEBUG = true

function log(x){ if (DEBUG){  console.log(x);}}


/***********************************************************************************
                    CHAT FRAMEWORK 
************************************************************************************/

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
ChatEngine.prototype.joinChatRoom = function(uid,uname,pic,email){
     self = this
    nw = self._fireBaseRef.child('users').push({name: uname, id: uid,pic: pic, 'isTyping':false,email:email});
    self._uid = uid
    self._uname = uname;
    self._pic = pic;
    self._email = email;
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
        js:"var a = 'dipankar'\n print('Use print to print anything:'+a);"           
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
    log(' This ediot i now on shared...')
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
           log('canot reset data')
    }
    this.setEditorMode(eid,mode)
}
MyEditor.prototype.reFormat= function(eid){
    this._editors[eid].ace.setValue(this._editors[eid].ace.getValue())
}
MyEditor.prototype.addInlineCompilationMsg= function(eid,type,line,msg){ 
    line = parseInt(line) - this._editors[eid].ace.getFirstVisibleRow();
    _t =  $('#'+eid+' .ace_line_group:nth-child('+line+')');
    if(!(_t.hasClass('error'))){
        _t.removeClass("error warning")
        $('#'+eid+' .ace_line_group:nth-child('+line+')').addClass(type).attr('data-content',msg)
        $('#'+eid+' .ace_gutter-cell:nth-child('+line+')').addClass(type).attr('data-content','!')
    }
}
MyEditor.prototype.clearInlineCompilationMsg= function(eid){ 
    $('#'+eid+' .ace_line_group').removeClass("error warning")
    $('#'+eid+' .ace_gutter-cell').removeClass("error warning")
}

/***********************************************************************************
                    DATA BINDING FRAMEWORK
************************************************************************************/
var MyDataBind = function(ids){
    self = this
    self._ids = {}
    for (i = 0; i < ids.length; i++) {
        if ($('#'+ids[i]).length == 0){ log('No such id: '+ids[i]);continue;}
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
    this.log = function(a){ log('>>> '+ a)}
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
    log('Canot initilized as ace_instance is null ');return;}
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
        log('Automatic started the recoder ..')
        self.start_recording();
    }
    log('Code Player Intilized');
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
     log("can't start, already started..."); return false;
   }
   this.clean();
   log('start_recording...')
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
            log(e,keyevent);
        }
    });
    return true;
}

CodePlayer.prototype.stop_recording = function(){
   self = this;
   if(self._isrecording == false) {
     log("can't stop, already stopd..."); return false;
   }
   log('stop_recording')
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
    if(pos >= self.seek_partition_len ) {log('Seek cross the max limit'); return false;}
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
     log('Can not play.. we are in recodring stage'); return false;
   }
    if(self._isplaying == true) {
     log('Can not play playing ...'); return false;
   }
   if(self._changelist.length == 0){
        log('Can not play playing you need to record something'); return false;
   }
    
   self._isplaying = true;
   if( self._playoffset  == 0){ // we are strating from begging...
       self._ace.setValue(self._init_data); 
       self._ace.clearSelection();
       self._ace.setReadOnly(true);
       self._startTime=self._changelist[0].timestamp;
       log("start_playing")
   }
   else{ // we are moving from pause to play..
       log("resumeing ...")
   }
   self.playOff();
   return true;
}

CodePlayer.prototype.playOff = function() {
    self = this;
    if(self._playoffset > self._changelist.length -1){
        log('invalid offset');return false;
    }
    var percentage =  (self._changelist[self._playoffset].timestamp - self.start_t)/(self.end_t - self.start_t)*100;
    if ( self._progress_cb != undefined) {    self._progress_cb(percentage);}
    
    if (self._playoffset == (self._changelist.length -1)) { //last elemner
        self.applyChanges(self._playoffset);
        self.stop_playing(); 
        log('end video');return false; 
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
      log('Can not stop.. we are in recodring stage'); return false;
    }
    if(self._isplaying == false) {
      log('Already stop'); return false;
    }
    log("stop_playing")
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
       log('Can not pause.. we are in recodring stage'); return false;
    }
    if(self._isplaying == false) {
      log('Can not pause playing ...'); return false;
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
                    log('unknown action: ' + k.data.action);
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
      case 'star_btn':
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
             $(document).on('click','.rate > input', function (e){ gCommonUx.getData('star_btn',this);})
      
             break;
    

            //todo
      case 'popup':
            if( !($('.overlay').length )){ $('body').append('<div class="overlay"></div>')}
            jid.hide();
            jid.addClass("animated")
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
            log('All ')
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
              
              log(id.name+'  > ' +id.value);
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
            
            var r=typr+val;
              $('#'+typr+' .rate input:radio[id="'+r+'"]').prop('checked', true);
              log('setting '+typr +' to >'+val);
            
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
            $('.overlay').addClass('active'); jid.show().removeClass('bounceOut').addClass('bounceIn'); break;
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

/********************************************************
    G R O U P   A U D I O   C H A T  F R A M E W O R K
*********************************************************/
var GroupAudioVideoChat= function(){
    this._getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia;    
    if (this._getUserMedia) {
        // Good to go!
    } else {
      log('getUserMedia() is not supported in your browser');
      return;
    }
    this._localStream;
    this._localPeerConnection;
    this._remotePeerConnection;
    this._buildUI();
    this._getDeviceStream();
}
GroupAudioVideoChat.prototype._getDeviceStream = function(){
    self = this // this required.
    log('Initilization of Stream......');
    navigator.getUserMedia  = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia;  
    navigator.getUserMedia (
        {video:true, audio:true},
        function(stream){
            log('Received local stream');
            localVideo.src = URL.createObjectURL(stream);
            self._localStream = stream;
        },
        function(error) {
          log('navigator.getUserMedia error: ', error);
        }
    );
}
GroupAudioVideoChat.prototype._getScreenStream = function(){
    self = this // this required.
    log('Initilization of Stream......');
    navigator.getUserMedia  = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia;  
    navigator.getUserMedia (
        {
            audio: false,
            video: {
                mandatory: {
                    chromeMediaSource: 'screen',
                    maxWidth: 1280,
                    maxHeight: 720
                },
                optional: []
            }
        },
        function(stream){
            log('Received local stream...');
            localVideo.src = URL.createObjectURL(stream);
            self._localStream = stream;
        },
        function(error) {
          log('navigator.getUserMedia error: ', error);
        }
    );
}
GroupAudioVideoChat.prototype._buildUI = function(){
    var _html='\
    <div class="group_audio_video_chat" style="height: 400px; width: 400px; overflow: hidden; left: inherit;  bottom: 1px; top: inherit;right: 1px;"><div class="rel fw">\
        <video id="localVideo" autoplay="" muted=""></video>\
        <div class="mini_list">\
            <video id="remoteVideo" autoplay=""></video>\
        </div>\
        <div class="btn">\
          <span class="b1" id="call"><i class="fa fa-phone"></i></span>\
          <span class="b2" id="mic" disabled=""><i class="fa fa-microphone-slash"></i></span>\
          <span class="b3" id="cam" disabled=""><i class="fa fa-video-camera"></i></span>\
          <span class="b4" id="screen" disabled=""><i class="fa fa-tv"></i></span>\
        </div>\
    </div></div>\
    '
    $('body').append(_html);
    this._group_audio_video_chat = new BuildDraggable('.group_audio_video_chat')
    this._localVideo = document.getElementById('localVideo');
    this._remoteVideo = document.getElementById('remoteVideo');
    this._call_btn = document.getElementById('call');
    this._mic_btn = document.getElementById('mic');
    this._cam_btn = document.getElementById('cam');
    this._screen_btn = document.getElementById('screen');
    
    this._localVideo.addEventListener('loadedmetadata', function(){
        log('Local video currentSrc: ' + this.currentSrc + ', videoWidth: ' + this.videoWidth +'px,  videoHeight: ' + this.videoHeight + 'px');
    });
    this._remoteVideo.addEventListener('loadedmetadata', function(){
        log('Remote video currentSrc: ' + this.currentSrc +', videoWidth: ' + this.videoWidth + 'px,  videoHeight: ' + this.videoHeight + 'px');
    });
    
    $('#call').removeClass('on_call')
    $('#mic').addClass('on_mic')
    $('#cam').addClass('on_cam')
    $('#screen').addClass('on_screen')
    self = this; // thsi is requiured to privent
    
    this._call_btn.onclick = function(){
        if($('#call').hasClass('on_call')){
            self.leave();
        }
        else{
            self.join(12,'dipankar')
        }        
    };
    
    this._mic_btn.onclick = function(){
        if($('#mic').hasClass('on_mic')){
            self.disable_mic();
        }
        else{
            self.enable_mic();
        }        
    };
    this._cam_btn.onclick = function(){
        if($('#cam').hasClass('on_cam')){
            self.disable_cam();
        }
        else{
            self.enable_cam();
        }        
    };
    this._screen_btn.onclick = function(){
        if($('#screen').hasClass('on_screen')){
            self.disable_screen();
        }
        else{
            self.enable_screen();
        }        
    };
}
GroupAudioVideoChat.prototype._messageFromPeer = function(message) {
    // we are getting a message for peers
    self = this
    log('Received a message from server as sdp or ice. let"s set it and give ans')
    var signal = JSON.parse(message.data);
    if(signal.sdp) {
            if(signal.type =='offer'){/*
                self._remotePeerConnection.setRemoteDescription(new RTCSessionDescription(signal.sdp), function() {
                self._remotePeerConnection.createAnswer(setAndSendAns, self._errorHandler);
                }, self._errorHandler);
                
                function setAndSendOffer(description,function(){
                    log('Local Peer Offer a description, lets set it and send it to remote:\n'+ description.sdp)
                    localPeerConnection.setLocalDescription(description, function () {
                        self._sendToPeer(JSON.stringify({'type':'offer','sdp': description}));
                    }, function() {console.log('set description error')}); 
            }*/
            }
    } else if(signal.ice) {
        self._remotePeerConnection.addIceCandidate(new RTCIceCandidate(signal.ice));
    }
}
GroupAudioVideoChat.prototype._sendToPeer = function(message) {
    // Message is send to all peers
    log('Sending message')
    nw = self._fireBaseRef.child('messages').push({'from':self._email,'data':message});
    // deleete immediately
    nw.remove()
}

GroupAudioVideoChat.prototype._initFireBase = function(){
    self = this
    self._fireBaseRef =  new Firebase('https://cleancode.firebaseio.com/'+self._id+'/vchat/');
    nw = self._fireBaseRef.child('users').push({id: self._id, email: self._email});
    this._key = nw.key()
    
    self._fireBaseRef.child('messages').on('child_added', function(snapshot) {
        self._messageFromPeer(snapshot.val())
    });
}
GroupAudioVideoChat.prototype._errorHandler= function(a){log(a)}


GroupAudioVideoChat.prototype.join = function(id,email){
    self = this
    this._id = id
    this._email = email
    

    
    log('Starting call...');
    self._initFireBase()
    //var servers = {'iceServers': [{'url': 'stun:stun.services.mozilla.com'}, {'url': 'stun:stun.l.google.com:19302'}]};
    var servers = null;
    log('Created local peer connection object localPeerConnection');
    webkitRTCPeerConnection = webkitRTCPeerConnection || mozRTCPeerConnection
    var localPeerConnection = new webkitRTCPeerConnection(servers); 
    localPeerConnection.addStream(this._localStream);
    localPeerConnection.onicecandidate = sendAndSetIceCandidate;
    localPeerConnection.createOffer(setAndSendOffer,self._errorHandler)
    

    log('Created remote peer connection object remotePeerConnection');
    var remotePeerConnection = new webkitRTCPeerConnection(servers);    
    remotePeerConnection.onaddstream = function(event){
        self._remoteVideo.src = URL.createObjectURL(event.stream);
        log('Received remote stream');
    };  
    
    function setAndSendOffer(description){
        log('Local Peer Offer a description, lets set it and send it to remote:\n'+ description.sdp)
        localPeerConnection.setLocalDescription(description, function () {
            self._sendToPeer(JSON.stringify({'type':'offer','sdp': description}));
        }, function() {console.log('set description error')});
    }
    
    
    function sendAndSetIceCandidate(event) {
        if(event.candidate != null) {
            self._sendToPeer(JSON.stringify({'ice': event.candidate}));
        }
    }

    this._remotePeerConnection = remotePeerConnection
    this._localPeerConnection = localPeerConnection;    
    $('#call').addClass('on_call')
}

GroupAudioVideoChat.prototype.leave = function(){
  log('Ending call');
  this._localPeerConnection.close();
  this._remotePeerConnection.close();
  this._localPeerConnection = null;
  this._remotePeerConnection = null;
  $('#call').removeClass('on_call')
}

GroupAudioVideoChat.prototype.enable_mic = function(){
     self = this
    $('#mic').addClass('on_mic')
    var audioTracks = self._localStream.getAudioTracks();
    for (var i = 0, l = audioTracks.length; i < l; i++) {
        audioTracks[i].enabled = true
    }
}
GroupAudioVideoChat.prototype.disable_mic = function(){
     self = this
    $('#mic').removeClass('on_mic')
    var audioTracks = self._localStream.getAudioTracks();
    for (var i = 0, l = audioTracks.length; i < l; i++) {
        audioTracks[i].enabled = false
    }
}

GroupAudioVideoChat.prototype.enable_cam = function(){
    self = this
    $('#cam').addClass('on_cam')
    var audioTracks = self._localStream.getVideoTracks();
    for (var i = 0, l = audioTracks.length; i < l; i++) {
        audioTracks[i].enabled = true
    }
}
GroupAudioVideoChat.prototype.disable_cam = function(){
     self = this
    $('#cam').removeClass('on_cam')
    var audioTracks = self._localStream.getVideoTracks();
    for (var i = 0, l = audioTracks.length; i < l; i++) {
        audioTracks[i].enabled = false
    }
}

GroupAudioVideoChat.prototype.enable_screen = function(){
    $('#screen').addClass('on_screen')
}
GroupAudioVideoChat.prototype.disable_screen = function(){
    $('#screen').removeClass('on_screen')
}

GroupAudioVideoChat.prototype.changeVolume = function(level){ 
    // level chnage from 0 to 100.
}


/* Test
    <div class="audio"> ... </div>
    gGroupAudioVideoChat = new GroupAudioVideoChat(".audio");
    gGroupAudioVideoChat.join(id)
    gGroupAudioVideoChat.mute()
    gGroupAudioVideoChat.unmute()
    gGroupAudioVideoChat.chnageVolume(id)
    gGroupAudioVideoChat.leave(id)
*/

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
       // log('We have only debug/info/error');
    }
    if( tag == undefined ) { log("lag can't be null");return;}
    var lobj={}
    lobj.type = type
    lobj.tag = tag
    lobj.msg = msg
    lobj.time = timeStamp()
    lobj.data = obj
    lobj.session = self._session_id
    if(self._is_enable){
        call_backend_api('POST',self._endurl,lobj,'before_cb','success_cb','error_cb','complete_cb',{contentType:'json'})
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
    
    this._is_run_complete = false;
    this._is_compile_complete = false;
    
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
    this._is_compile_complete = false
    this._obj = obj
    if(!this.verifyObject(obj)){
        log('Object Verification failed;')
        return ;
    }
    call_backend_api('post',self._endpoint_c,obj,self._callback_compile_before,self._callback_compile_success,self._callback_compile_error,function(){this._is_compile_complete = true;});
}
CompilationEnv.prototype.run = function(obj){
    self = this
    this._is_run_complete = false
    if(!this.verifyObject(obj)){
        log('Object Verification failed;')
        return ;
    }
call_backend_api('post',self._endpoint_r,obj,self._callback_run_before,self._callback_run_success,self._callback_run_error,function(){this._is_run_complete = true;});
}
CompilationEnv.prototype.runIfCompileSucceed = function(obj){ 
    self = this
    this._is_run_complete = false;
    this._is_compile_complete = false;
    this._obj = obj
    this._is_run_after_compilation_succeed = true
    this.compile(obj);
}
CompilationEnv.prototype.attachCompileBeforeHandaler= function(func){
    self = this
    self._callback_compile_before = func
}
CompilationEnv.prototype.isPreviousCompiledSuccess= function(func){
    return this._is_run_after_compilation_succeed
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
        else{
            log('Compilation error!')
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
    this._callback_run_error = func
}


/*******************************************************************
    P R O B L E M  U N I T  T E S T   F R A M E W  O R K
********************************************************************/
var  ProblemUnitTest = function(){
    this._problem_set = {};
}

ProblemUnitTest.prototype.addProblem = function(data){
    if(data.id == undefined) return false
    this._problem_set[data.id] = data
    this._problem_set[data.id].testcases = []
}
    
ProblemUnitTest.prototype.getProblem = function(id){
    return this._problem_set[id];
}

ProblemUnitTest.prototype.setProblem= function(id,data){
    for (var key in data) {
        if (data.hasOwnProperty(key)) {
            this._problem_set[id].key = data.key;
        }
    }
}

ProblemUnitTest.prototype.addTestCase = function(id,data){
    this._problem_set[id].testcases.push(data)
}

ProblemUnitTest.prototype.getTestCase = function(id){
    return this._problem_set[id].testcases;
}
ProblemUnitTest.prototype.buildUX = function(pid,ele){
    var p = this._problem_set[pid];
    t =''
    for (i =0;i<p.testcases.length;i++){
       t += '<div>'
       t += '<div>'       
    }
    html = '<div class="problem">'
    html += '<div class="id">'+p.id+'</div>'
    html += '<div class="name">'+p.name+'</div>'
    html += '<div class="desc">'+p.desc+'</div>'
    html += '<div class="tc">'+t+'</div>'
    html += '</div>' 
    $(ele).html(html)
}

/*test 
    p =  new ProblemUnitTest()
    p.addProblem({id:0, name:'bit puzzle',desc:'something'})
    p.getProblem(0)
    p.addTestCase(0,{input:'in',output:'out',explanation:'some exp'})
    p.getTestCase(0)
*/
    
/*******************************************************************
    P R O B L E M  U N I T  T E S T   F R A M E W  O R K
********************************************************************/
var  ProblemUnitTest = function(){
    this._problem_set = {};
}

ProblemUnitTest.prototype.addProblem = function(data){
    if(data.id == undefined) return false
    this._problem_set[data.id] = data
    this._problem_set[data.id].testcases = []
}
    
ProblemUnitTest.prototype.getProblem = function(id){
    return this._problem_set[id];
}

ProblemUnitTest.prototype.setProblem= function(id,data){
    for (var key in data) {
        if (data.hasOwnProperty(key)) {
            this._problem_set[id].key = data.key;
        }
    }
}

ProblemUnitTest.prototype.addTestCase = function(id,data){
    this._problem_set[id].testcases.push(data)
}

ProblemUnitTest.prototype.getTestCase = function(id){
    return this._problem_set[id].testcases;
}
/* This will return sample HTML . Please write yur own CSS*/
ProblemUnitTest.prototype.buildUX = function(pid,ele){
    var p = this._problem_set[pid];
    t =''
    for (i =0;i<p.testcases.length;i++){
       t += '<div class="tc" id="tc'+i+'">'
       t += '<div class="title"><span>TestCase#'+(i+1)+'</span><span class="status"><i class="fa fa-question"></i></span></div>'
       t += '<div class="body"><div><span>Input:</span><span>'+p.testcases[i].input+'</span></div><div><span>Output:</span><span>'+p.testcases[i].output+'</span></div></div>'                
       t += '</div>'        
    }
    html = '<div class="problem">'
    html += '<div class="id">'+p.id+'</div>'
    html += '<div class="name">'+p.name+'</div>'
    html += '<div class="desc">'+p.desc+'</div>'
    html += '<div class="btns"><span class="btn_1" onclick="gProblemUnitTest.runAllTestCase('+pid+',getRunData())">Run Test Cases</span></div>' 
    html += '<div class="all_tc">'+t+'</div>'
    html += '</div>' 
    $(ele).html(html)
}

ProblemUnitTest.prototype.setSolution = function(id,sol){
    this._problem_set[id].solution= sol
}
ProblemUnitTest.prototype.runAllTestCase = function(pid,obj){    //take solution object
    $('.tc').removeClass('success error process unknown')
    $('.status >i').removeClass();
    var p = this._problem_set[pid];
    //inner function to run a test
    function _runAtest(i){
        obj.input = p.testcases[i].input
        var output = p.testcases[i].output
        var tl_CompilationEnv = new CompilationEnv()
        tl_CompilationEnv.attachRunSuccessHandaler(
        function(data){             
            if(data.output == output){
                $('#tc'+i).addClass('success').removeClass('process');
                $('#tc'+i+' .status >i').removeClass().addClass('fa fa-check');
            }      
            else {
                $('#tc'+i).addClass('error').removeClass('process');
                $('#tc'+i+' .status >i').removeClass().addClass('fa fa-close');
            }
        });
        tl_CompilationEnv.attachRunErrorHandaler(function(){
            $('#tc'+i).addClass('unknown').removeClass('process');            
        });
        $('#tc'+i).addClass('process');
        $('#tc'+i+' .status >i').removeClass().addClass('fa fa-circle-o-notch fa-spin');
        tl_CompilationEnv.run(obj);
    } // end of inner func
    var tCompilationEnv = new CompilationEnv()
    tCompilationEnv.attachCompileSuccessHandaler(function(data){
        if(data.can_run == 'yes'){
            for (i =0;i< p.testcases.length;i++){
                _runAtest(i);
            }                
        }
        else{
            alert('Compilation failed!, please first fix the compilation issue')
        }
    })
    tCompilationEnv.attachCompileErrorHandaler(function(data){
        log('Compilation Not happened');
    })
    tCompilationEnv.compile(obj)
}
/*test 
    p =  new ProblemUnitTest()
    p.addProblem({id:0, name:'bit puzzle',desc:'something'})
    p.getProblem(0)
    p.addTestCase(0,{input:'in',output:'out',explanation:'some exp'})
    p.addTestCase(0,{input:'in',output:'out',explanation:'some exp'})
    p.getTestCase(0)
*/

/*****************************************************
    FTX MANAGER FRAMEWORK( FIRST TIME EXPERIENCE)
******************************************************/
var  FTXManager = function(){
    this._ftx_items = {};
}
FTXManager.prototype.add = function(name,func){
    this._ftx_items[name] ={}
    this._ftx_items[name].func = func
    
}
FTXManager.prototype.setComplete = function(name){
    setCookie('FTX_'+name,'COMPLETE')
}
FTXManager.prototype.saveState = function(name){
    setCookie('FTX_'+name,'SAVE_STATE')
}
FTXManager.prototype.execute = function(){
    for (var key in this._ftx_items) {
        if (this._ftx_items.hasOwnProperty(key) && getCookie('FTX_'+key) != 'COMPLETE'){
            setCookie('FTX_'+key,'BEGIN')
            this._ftx_items[key].func()
            setCookie('FTX_'+key,'COMPLETE')
        }
    }
}

/* test
    gFTXManager = new FTXManager()
    gFTXManager.add('welcome',function(){
    alert('Welcome to peer review!');
    }) 
    gFTXManager.execute()
*/

/***********************************************
    FLEX SHEET FRAMEWORK
***********************************************/
var FlexSheet = function (row_list,count_col){
    this._col_list = [] // this list contains a list of objs like {name:id,type:input}
    this._count_col = col_size;
}

FlexSheet.prototype.buildUI=function(ele){
    
}
FlexSheet.prototype.addRow=function(count){ // adding row to the sheet
    if(count == undefined) count = 1; 
    
}
FlexSheet.prototype.addColumn=function(count){ // count column to the sheet 
    if(count == undefined) count = 1; 
}
FlexSheet.prototype.getData=function(){
    // will retunn data store in that sheet in a list of object.
}
FlexSheet.prototype.loadData=function(objs){
    // will populate list of objects data into sheet
    
}
FlexSheet.prototype.changeColumnType=function(col_id,types,data){
    // will change type of colum like we can make a column as select .and we have pass the option of select as data.
}
FlexSheet.prototype.setColumnReadOnly=function(col_id,flag){
    // will make a column as read only..
}
FlexSheet.prototype.setRowDirty=function(row_id){
    // make a row durty if a yser change something.
}
FlexSheet.prototype.getDirtyRows=function(){
    // will return all dirty rows as we need to update something in case of bulk push.
}


/* Test 
    
*/

/***********************************************************
    G I T H U B   P R O X Y   F R A M E W O R K 
*************************************************************/
var GitHubProxy = function (){
    this._uname=''
    this._upass =''
    this._url=''
    this._repo=''
    this._cb_get_file_success = function(){log('file retrive')}
    this._cb_get_file_error = function(){log('file retrive failed')}
    this._cb_save_file_success = function(){log('_cb_save_file_success not registered')}
    this._cb_save_file_error = function(){log('_cb_save_file_error not registered')}
}
GitHubProxy.prototype.setInfo = function (d){
    this._uname=d.uname
    this._upass =d.upass
    this._url=d.url
    this._repo = this._getNormUrl(d.url).repo
}

GitHubProxy.prototype._getNormUrl = function (url){
    res= {}
    idx  = url.indexOf('.com'); if (idx == -1) {alert('invalid url');return ;}
    path = url.substring(idx+5,url.length)    
    path = path.split('/')    
    res.repo = path.slice(0,2).join('/')
    res.path = path.slice(4).join('/') 
    return res 
}
GitHubProxy.prototype.get=function(d){
    //normalize url
    url = d.url
    this._url=url
    param= {action:'pull', uname:this._uname ,passwd:this._upass,repo:this._getNormUrl(url).repo,path:this._getNormUrl(url).path}
    call_backend_api('POST','/api/github/',param,'before_cb',this._cb_get_file_success,this._cb_get_file_error,'complete_cb',{load_animation:true}) 
}
GitHubProxy.prototype.save=function(d){
    this._uname = d.uname
    this._upass = d.upass
    url = this._url
    if(!(this._uname && this._upass && this._url && d.cmsg && d.data)) {alert('some info missing');return;}
    param= {action:'push', uname:this._uname ,passwd:this._upass,repo:this._getNormUrl(url).repo,path:this._getNormUrl(url).path,cname:this._uname ,cemail:'peerreviewbot@gmail.com',cmsg:d.cmsg,data:d.data}
    call_backend_api('POST','/api/github/',param,'before_cb',this._cb_save_file_success,this._cb_save_file_error,'complete_cb',{load_animation:true}) 
}
GitHubProxy.prototype.registerGetFileSuccess=function(func){this._cb_get_file_success = func}
GitHubProxy.prototype.registerGetFileError=function(func){this._cb_get_file_error = func}
GitHubProxy.prototype.registerSaveFileSuccess=function(func){this._cb_save_file_success = func}
GitHubProxy.prototype.registerSaveFileError=function(func){this._cb_save_file_error = func}



/***********************************************
    P O P O V E R   F R A M N E W O R K  (Please fix issues)
*************************************************/
var PopOver = function (){
    this._list={}
    this._default_animation={
            'top':['fadeInDown','fadeOutUp'],
            'left':['fadeInLeft','fadeOutRight'],
            'bottom':['fadeInUp','fadeOutDown'],
            'right':['fadeInRight','fadeOutLeft']
        }
}
PopOver.prototype._buildUI=function(id){
    ele = $('#'+id);opt = this._list[id].options  
    ele.hide();
    ele.addClass('PopOver animated').addClass(opt.location).addClass(this._default_animation[opt.location][1]); // setting default animation.
    if(opt.width != undefined){ele.css('width',opt.width);}
    if(opt.height != undefined){ele.css('width',opt.height);}
    
    ele.append('<div class="close" onclick="$(this).closest(\'.PopOver\').removeClass(\''+opt.animation[0]+'\').addClass(\''+opt.animation[1]+'\')" >X</div>');
    //show or hide 
    $('body').on('animationend webkitAnimationEnd oAnimationEnd', '#'+id, function () {
        if($(ele).hasClass(opt.animation[1])){$(ele).hide();}
    });

}
PopOver.prototype.add=function(id,options){
    var options = options || {'location':'top','animation':this._default_animation['top']}
    options.animation = options.animation || this._default_animation[options.location]
    this._list[id]={'options':options}
    this._buildUI(id);    
}
PopOver.prototype.hide=function(id){
    ele = $('#'+id);opt = this._list[id].options 
    ele.show().removeClass(opt.animation[0]).addClass(opt.animation[1]) 
}
PopOver.prototype.show=function(id){
    ele = $('#'+id);opt = this._list[id].options
    ele.show().removeClass(opt.animation[1]).addClass(opt.animation[0]) 
}
/*
    gPopOver = new PopOver()
    gPopOver.add('dipankar',{'location':'left'})
    gPopOver.show('dipankar')
    gPopOver.hide('dipankar')
*/

/****************************************************************
    P A G E   L  O A D   I N D I C  A T O R   F R A M E W O R  K
*****************************************************************/
var PageLoadIndicator = function(){
    this._buildUI();
    $('.uil-ring-css').hide()
}
PageLoadIndicator.prototype._buildUI= function(){
   if( !($('.load_overlay').length )){ $('body').append('<div class="load_overlay"></div>')}
   if( !($('.uil-ring-css').length )){ $('body').append('<div class="uil-ring-css" style="-webkit-transform:scale(0.6)"><div></div></div>')}
}
PageLoadIndicator.prototype.show= function(){
    $('.load_overlay').addClass('active'); $('.uil-ring-css').show();
}

PageLoadIndicator.prototype.hide= function(){
    $('.load_overlay').removeClass('active'); $('.uil-ring-css').hide();
}
PageLoadIndicator.prototype.registerLoadPage= function(){
    self = this
    $(window).load(function() { $('.load_overlay').removeClass('active'); $('.uil-ring-css').hide();}); 
}

/****************************************************************
    D R A G A B B  L E   D I V  
*****************************************************************/
var BuildDraggable = function(ele,options){
    self = this
    self._ele = ele
    self._options = options
    self._buildUI();
}
BuildDraggable.prototype._buildUI = function(){
    ele = $(this._ele)
    ele.addClass('draggable')
    ele.prepend ('<div class="header"><span class="drag_btn"><i class="fa fa-ellipsis-h"></i></span><span style="float:right"><i class="fa fa-expand" onclick="$(this).closest(\'.draggable\').removeClass(\'minimized\').toggleClass(\'fullscreen\')"></i><i class="fa fa-chevron-down" onclick="$(this).closest(\'.draggable\').removeClass(\'fullscreen\').toggleClass(\'minimized\')"></i> <i class="fa fa-remove" onclick="$(this).closest(\'.draggable\').hide()"></i> </span></div>')
    // Note: We need this overlay as we move it try to select other text..
    $('body').append('<div class="drag_overlay" style="z-index:10;width:100%;height:100%;background: transparent;;left:0;top:0;    position: fixed;display:none;"></div>')

    $('body').on('mousedown', '.draggable .drag_btn', function() {
        $('.drag_overlay').show();
        $(this).closest('.draggable').addClass('active').parents().on('mousemove', function(e) {
            $('.draggable.active').offset({
                top: e.pageY-10,
                left: e.pageX - $('.draggable.active').outerWidth() / 2
            }).on('mouseup', function() {
                $(this).removeClass('active');$('.drag_overlay').hide();
            });
        });
    }).on('mouseup', function() {
        $('.draggable').removeClass('active');
        $('.drag_overlay').hide();
    });
}
BuildDraggable.prototype.addOnCloseHadaler= function(){
    
}
BuildDraggable.prototype.show= function(){
    $(this._ele).show()
}
BuildDraggable.prototype.hide= function(){
    $(this._ele).hide()
}
/* test 
    <div class="dipankar"></div>
    a = new BuildDraggable('.dipankar1')
    
*/

/****************************************************************
    D A T A   S O U R C E  P R O X Y    F R A M E W O R K   
    
    ds::<id> -> datamodel attribure
    dsg::<id> -> is a list iteams
    dsh::<id> -> This is just a holder to contains the list of data
    
    Feature: 
    1. Nested object Supported like : ds::name::fname == {name:{fname:val}}
    2. 
*****************************************************************/
var DataSourceProxy =function(model,options){
    self = this
    self._model = model; // this is the table name
    self._url = '/api/ks/'+model+'/'
    self._id = null;
    self._options = options || {}
    self._options.root_ele = options.root_ele || false //
    if(self._options.root_ele != false){
       log('>>> DataSourceProxy:auto detect datamodel...') 
       log('>>> DataSourceProxy: Currently We support only 2nd level dataModel auto detection.') 
       self._bindings = {}
       var ele = $(self._options.root_ele)
       //1. Find direct child.
       lst = ele.find('[name^="ds::"]')
       for (i =0;i<lst.length;i++){
            x = $(lst[i]).attr('name')
            //make sure it is not under dsg:: or dsh::
            if($(lst[i]).closest('[name^="dsg::"]').length == 0 && $(lst[i]).closest('[name^="dsh::"]').length == 0) { 
                self._bindings[x.replace("ds::","")]={ele:'[name="'+x+'"]','type':'text'}
            }
        }
        //2. Find List..
       lst = ele.find('[name^="dsg::"]')
       for (i =0;i<lst.length;i++){
            x = $(lst[i]).attr('name')
            self._bindings[x.replace("dsg::","")]={ele:'[name="'+x+'"]',child:{},'type':'list'}       
            //now find ds under dsg.
            lst1 = $(lst[i]).find('[name^="ds::"]')
            for (i =0;i<lst1.length;i++){
                y = $(lst1[i]).attr('name')
                self._bindings[x.replace("dsg::","")].child[y.replace("ds::","")]={ele:'[name="'+y+'"]'}
            }
        }
    } else {
        self._bindings = options.bindings
    }
    if(! self._bindings){
        log('>>> Not able initite DataModel Proxy as not able find this._bindings' )
    } else{
        log('>>> Binding for this model is as below: Please verify...')
        log(this._bindings)
    }
    self._success_cb = function (data){ log('registerSuccessHandalar is not called:'+data)}
    
    self._error_cb = function (e){ log('registerErrorHandalar is not called:'+e)}
    
    self._success_cb_wrap = function(res){
        if(res.status == "success" && res.res._id != undefined){ // keep track for last id, which will be used for update
            self._id = res.res._id;
            log('saving last id, so you can call save() to update ')
        }            
        self._success_cb(res);
    }
    
}
//getting the elements 
DataSourceProxy.prototype._get= function(){
    
    function _setDataFromDomElement(_res,key,val_ele){ // will set data from DOM element 
        //we have some config to read data in case of editor...
        var _val = null
        var tag = $(val_ele).prop("tagName")
        if( tag == 'INPUT' || tag == 'SELECT' || tag == 'TEXTAREA' ){
            _val = $(val_ele).val();
        } else {
            _val = $(val_ele).html(); // do some unicode here todo
        }
        keys = key.split('::')
        for (var i=0; i < keys.length; i++) {
            var key = keys[i];
            if (i < keys.length -1) {
                if (_res[key] === undefined) {
                    _res[key] = {};
                }
                _res = _res[key] 
            } else {
                _res[key] =_val;
            }
        }
    }
    
    function _recursive_get(dict){
        // we have iterative to support upto level 2. we will have to recursive if you want to support more.
        var _res ={}
        for (var key in dict) {
            if(dict[key].child){ // nested list
                _res[key] = []
                _l = $(dict[key].ele)                
                for(i=0;i<_l.length;i++){
                    _r2 ={}
                    for ( k in dict[key].child ){
                        //_r2[k] = $(_l).find(dict[key].child[k].ele).val()
                        _setDataFromDomElement(_r2,k,$(_l).find(dict[key].child[k].ele))
                    }
                    _res[key].push(_r2)
                }
                //todo
            } else {
                _setDataFromDomElement(_res,key,$(dict[key].ele))
            }            
        }
        return _res;
    }
    
    return _recursive_get(this._bindings);
}

DataSourceProxy.prototype._buildListItem= function(_data){
    // here we need to support custom template for list.
    _h = ''
    for (var k in _data){
        _h += '<div name="ds::'+k+'">' + _data[k]+ '</div>'
    }
    return _h
}

//not working for list.. need to debug more
DataSourceProxy.prototype._set= function(data){
    self = this
    log('For seeting the data, the attribyte must be mattched to [name="ds::xyz"]')
    ele = $(self._options.root_ele)
    function _recursive_set(ele,prefix,data){        
        for ( var k in data){
            if($.isPlainObject(data[k])){
                _recursive_set(prefix+k+'\\:\\:',data[k]); // we support nested object..
            }
            else if($.isArray(data[k])){
                var _arr_ele = ele.find('[name="dsh\\:\\:'+k+'"]')
                var templete = _arr_ele.children().first();
                if(templete == null){log('>>> ERROR: No teplate found. ignoring this data ...');continue;}
                //todo: second call should replace all the previous diff
                for (var i =0;i<data[k].length;i++){
                    _now = _arr_ele.children().eq(i+1)
                    if(_now.length == 0){
                        _arr_ele.append(templete);
                        _now = $(_arr_ele.children().last());
                        _now.removeClass('hide')
                    }                    
                    _recursive_set($(_now),prefix,data[k][i])
                }
            }
            else {
                //setting end object..
                var val_ele = ele.find('[name="'+prefix+k+'"]')
                var tag = $(val_ele).prop("tagName")
                if( tag == 'INPUT' || tag == 'SELECT' || tag == 'TEXTAREA' ){
                    _val = $(val_ele).val(data[k]);
                } else {
                    _val = $(val_ele).html(data[k]); // do some unicode here todo
                }
                //ele.find('[name="'+prefix+k+'"]').val(data[k]);
            }            
        }
    }
    _recursive_set(ele,'ds\\:\\:',data)
}
DataSourceProxy.prototype.get= function(id){
    id = id || this._id
    if(!id){log('You must have an Id to pull data from database or use getall() to pull all data');return;}
    self = this
    function _cb(d){
        if(d.status == 'success' && d.res){
            self._set(d.res)
        }
        self._success_cb_wrap(d);
    }
    call_backend_api('get',self._url+id+'/',{},'before_cb',_cb,self._error_cb,'complete_cb',{load_animation:true});
}
DataSourceProxy.prototype.save= function(){ //update and crete if not exist
    self = this
    param = self._get()
    log('saving....')
    if(self._id){
        log('updaing....');log(param)
        call_backend_api('post',self._url+self._id+'/',param,'before_cb',self._success_cb_wrap,self._error_cb,'complete_cb',{contentType:'json',load_animation:true});
    } else{
        self.create();
    }
}
DataSourceProxy.prototype.create= function(){  // create every time.
    self = this
    param = self._get()
    log('creating....');log(param)
    call_backend_api('post',self._url,param,'before_cb',self._success_cb_wrap,self._error_cb,'complete_cb',{contentType:'json',load_animation:true});
}
DataSourceProxy.prototype.registerSuccessHandalar= function(func){
    this._success_cb = func
}
DataSourceProxy.prototype.registerErrorHandalar= function(func){
    this._error_cb = func
}

/* Test
<div class="dipankar">
    <input name="ds::uname"></input>
    <input name="ds::passwd"></input>
    <select name="ds::gender"> <option value="volvo">Volvo</option><option value="saab">Saab</option></select>
    <input type="checkbox" name="ds::vehicle" value="Bike">bike<br><input type="ds::checkbox" name="vehicle" value="Car" checked> car<br>
    <input type="radio" name="ds::sex" value="male" checked> Male <br><input type="radio" name="ds::sex" value="female"> Female<br>
    <p name="ds::html">1</p>
    <div class="list">
        <div class="list1" name="dsg::list"><input name="ds::sname"></input> <input name="ds::spass"></input></div>
        <div class="list1" name="dsg::list"><input name="ds::sname"></input> <input name="ds::spass"></input></div>
    </div>
    <p name="dsh::list">    We will populate here,, </p>
</div>

d = new DataSourceProxy('aa',{root_ele:'.dipankar'})
d.save() << Create or update

    
*/

/****************************************************************
    J A V A S C R I P T    C O M P I L  A T I O N 
*****************************************************************/
var JavaScriptCompilar  = function(){ 
    self = this
    self._registerInputDataSource = null
    self._registerOutputDataDestination = null;
    self._registerErrorDataDestination = null;
    self._log = function(a){console.log('_registerOutputDataDestination not done! Please do that');console.log(a)}
    self._error_log = function(a){console.log('_registerOutputDataDestination not done! Please do that');console.log(a);}
}
JavaScriptCompilar.prototype.registerInputDataSource = function(func){ 
    self = this
    this._registerInputDataSource = func
}
JavaScriptCompilar.prototype.registerOutputDataDestination = function(ele){
    self = this
    self._registerOutputDataDestination  = ele
    self._log = function(a){
        $(ele).append(a+'\n');
    }
}
JavaScriptCompilar.prototype.registerErrorDataDestination = function(ele){
    self = this
    self._registerErrorDataDestination  = ele
    self._error_log = function(a){
        $(ele).append(a+'\n');
    }
}
JavaScriptCompilar.prototype.run=function(){
    self = this
    //Creating Holders...
    $(self._registerOutputDataDestination).html('');// clean the output.
    if ($('#JavaScriptCompilarHTMLHolder').length == 0) {$(self._registerOutputDataDestination).append('<div id="JavaScriptCompilarHTMLHolder" style="display:block;"></div>')}
    if ($('#JavaScriptCompilarOutputHolder').length == 0) {$(self._registerOutputDataDestination).append('<div id="JavaScriptCompilarOutputHolder" style="display:block;"></div>')}
    //run is little tricky we are making a div and inject this code..
    if ($('#JavaScriptCompilar').length == 0) {$('body').append('<div id="JavaScriptCompilar" style="display:none;"></div>')}
    
    
    
    $('#JavaScriptCompilarOutputHolder').html('>>> Running...<br>')
    code = self._registerInputDataSource() // will get the data
    html_code = ''
    var code_normalized = code.toLowerCase();
    if (code_normalized.indexOf('<script') == -1) {
        code = '<script>\n' + code + '\n</'+'script>\n';
    }
    else {
        //we have html code as well.
            start_of_script = code.indexOf('<script')
            end_of_script =  code.indexOf('</script>') + 9
            html_code = code.slice(0,start_of_script) + code.slice(end_of_script,code.length)
            code = code.slice(start_of_script,end_of_script)            
    }
    if (code_normalized.indexOf('onerror') == -1) { // code is without its own error handling, then add one
        code = '<script>\n'+
        'window.onerror = function(message, url, linenumber) {'+
        '_error_log("<p style=\'color:red\' class=\'animated fadeInUp\'><b>JSError:</b>Line #"+linenumber+":" + message+"</p>");'+
        '};\n</'+'script>\n' + code;
    } 
    //define the log function.
    code = '<style>pre {outline: 1px solid #ccc; padding: 5px; margin: 5px; }\
    .string { color: green; }\
    .number { color: darkorange; }\
    .boolean { color: blue; }\
    .null { color: magenta; }\
    .key { color: red; }</style>\
    <script>\n\
    \nvar _registerOutputDataDestination  ="'+self._registerOutputDataDestination+'"\
    \nvar _registerErrorDataDestination  = "'+ self._registerErrorDataDestination+'"\
    \nvar print = function(message) { $(\'#JavaScriptCompilarOutputHolder\').append(syntaxHighlight(message));}\
    \nvar _error_log = function(message) { $(\'#JavaScriptCompilarOutputHolder\').append(message);}\
    \n</script>\n' + code; 
    
    
    
    //First add the HTML and then put Javascript code..
    $('#JavaScriptCompilarHTMLHolder').html(html_code); 
    $('#JavaScriptCompilar').html(code);    
       
}
/* test
    gJavaScriptCompilar = new JavaScriptCompilar();
    gJavaScriptCompilar.registerInputDataSource(function(){return gEditors.getEditorData(selected_tab);})
    gJavaScriptCompilar.registerOutputDataDestination('#output')
    gJavaScriptCompilar.registerErrorDataDestination('#output') 
*/  
/*******************************************************
    readSingleFile() => read single file from file input form.
    document.getElementById('fileinput').addEventListener('change', readSingleFile, false);
********************************************************/
var FileUploader = function(ele){
    self = this
    self._callback = function(){log('_callback not registered');}
    $(ele).on('change',self._readSingleFile);
}
FileUploader.prototype.registerCallback = function(func) {
    self._callback = func;
}    
FileUploader.prototype._readSingleFile = function(evt) {
    var f = evt.target.files[0];
    if (f) {
        var r = new FileReader();
        r.onload = function(e) { 
            var contents = e.target.result;
            res = {}
            res.name = f.name
            res.type = f.type
            res.size = f.size
            res.data = contents
            log(res); 
            self._callback(res);
        }
        r.readAsText(f);
    } else { 
      log("Failed to load file");
    }
}
/* Test:
    <input type="file"id="f">
    x = new FileUploader('#f')
    x.registerCallback(function(a){print(a);})
    print(x)
*/