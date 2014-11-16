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
