angular.module('MatrixApp', [])
.controller('MatrixController', ['$scope', '$http', function($scope, $http) {
    $scope.size = 2;
    $scope.useOpenMP = false;
    $scope.result = null;
    $scope.error = null;
    $scope.loading = false;

    $scope.submit = function() {
        $scope.result = null;
        $scope.error = null;
        $scope.loading = true;

        $http.post('/calculate', {
            size: $scope.size,
            use_openmp: $scope.useOpenMP
        }).then(function(response) {
            $scope.result = response.data;
            $scope.loading = false;
        }, function(error) {
            $scope.error = error.data.error || 'An error occurred';
            $scope.loading = false;
        });
    };
}]);
