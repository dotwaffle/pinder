app.controller('PinderController',  function($scope, pinderFactory) {

    $scope.object = {};
    $scope.requests = [];
    $scope.showSuccessMessage = false;
    $scope.getRequest = function(r_id){
         pinderFactory.getRequestByID(r_id)
        .then(function(data){
            $scope.object = data;
        },function(err){
            alert(err);});
    };

    $scope.getRequests = function(){
        pinderFactory.getAllRequests()
        .then(function(data){
            $scope.requests = data.results;
            console.log($scope.requests);
        },function(err){
            alert(err);});
    };
    $scope.handleRequest = function (state,r_id) {
        var data = {
              state: state
            };
        pinderFactory.toggleStatus(data, r_id)
        .then(function(data){
            $scope.showSuccessMessage = true;
        },function(err){
            alert(err);});
        
    };

});
