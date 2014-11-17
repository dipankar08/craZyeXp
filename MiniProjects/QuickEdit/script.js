    angular.module('dipankar', ['ngSanitize'])
      .controller('ExampleController', ['$scope', '$sce', function($scope, $sce) {
        $scope.html ='';
        $scope.deliberatelyTrustDangerousSnippet = function() {
          return $sce.trustAsHtml($scope.html);
        };
      }]);

$(document).ready(function() {

$('#html').bind('input propertychange', function() {
console.log(this.value);
var html = this.value;
/* Will Do some Majic here */

var content = $("#preview").contents().find("body"); // iframe id is 'preview'
content.html(html);
     
});

$('#html').keypress(function(event){
       
	var keycode = (event.keyCode ? event.keyCode : event.which);
   { /* auto ending closing tag */    
        a = this.value.slice(0,this.selectionStart)
        b = this.value
        //alert('You pressed a "enter" key in textbox'+this.value+"#"+keycode+"#"+this.selectionStart+"#"+this.selectionEnd);	
        if(keycode == 62 && a[a.lastIndexOf('<')+1]!='/')
       {   
           tag = a.substring(a.lastIndexOf('<')+1,this.selectionStart)
           inj = "></"+tag+">"
           this.value = b.substring(0,this.selectionStart)+inj+b.substring(this.selectionStart,b.length)
           this.value = this.value.slice(0,this.value.length -1);

       } 
    }
     
 });

$('#css').bind('input propertychange', function() {

    var csVal = this.value;
    var cssLink = "<style>" + csVal + "</style>"; // cssVal contains css code
    var head = $("#preview").contents().find("head").find("style");
    head.replaceWith(cssLink);
          
});

$('#js').bind('input propertychange', function() {

var jsCode = this.value;
console.log(jsCode);
var js ="<script>"+jsCode+"</script>" ; 
var head = $("#preview").contents().find("head");
head.append(js );


});

if (typeof console  != "undefined") 
    if (typeof console.log != 'undefined')
        console.olog = console.log;
    else
        console.olog = function() {};

console.log = function(message) {
    console.olog(message);
    $('#debugDiv').html(message);
};
console.error = console.debug = console.info =  console.log


});
/*********  end of code ***************/

