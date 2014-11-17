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
    $('#debugDiv').html(message);
};
console.error = console.debug = console.info =  console.log


});
