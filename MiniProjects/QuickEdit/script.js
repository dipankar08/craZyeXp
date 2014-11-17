    angular.module('dipankar', ['ngSanitize'])
      .controller('ExampleController', ['$scope', '$sce', function($scope, $sce) {
        $scope.html =
          '<p style="color:blue">an html\n' +
          '<em onmouseover="this.textContent=\'PWN3D!\'">click here</em>\n' +
          'snippet</p>';
        $scope.deliberatelyTrustDangerousSnippet = function() {
          return $sce.trustAsHtml($scope.html);
        };
      }]);

$(document).ready(function() {


    var html = "<div>Hello from iframe</div>"; // HTML code
    var content = $("#preview").contents().find("body"); // iframe id is 'preview'

    content.html(html);

    var csVal = "div { color: red; font-size: 40px;}";
    var cssLink = "<style>" + csVal + "</style>"; // cssVal contains css code
    var head = $("#preview").contents().find("head");
    head.append(cssLink);

    var jsCode = "alert('you are in the iframe')";

    var js ='<script>'+jsCode+'<\/script>' ; 

    // following part is not working
    var content = $('#preview').contents();
    content.find('head').append('<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"><\/script>' );             
    content.find('body').append(js );

$('#html').bind('input propertychange', function() {
console.log(this.value);
var html = this.value;
var content = $("#preview").contents().find("body"); // iframe id is 'preview'
content.html(html);
     
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
    $('#debugDiv').append('<p>' + message + '</p>');
};
console.error = console.debug = console.info =  console.log


});
