app.controller('MainController',  function($scope, peeringdbFactory) {
 
    $scope.ixps = [];
    $scope.selectedIXP = "";
    $scope.scrASN = "";
    $scope.dstASN = "";
    $scope.loading = false;

    
    $scope.getInfo = function(){
        peeringdbFactory.getByASN($scope.asn)
            .then(function(data){
                console.log(data);
            
        },function(err){
            alert(err);
        })
    };
    
    $scope.loadIXPpeers = function(ixp){
        console.log(ixp);
        $scope.selectedIXP = ixp;
    }
    
    $scope.findIX = function(){
        $scope.loading = true;
        setTimeout(function(){
            peeringdbFactory.getIXPS()
            .then(function(data){
                $scope.ixps = data.data;
            },function(err){
                alert(err);
            });
            $scope.loading = false;
        }, 1000);
        console.log($scope.scrASN,$scope.dstASN)
        
    }
    
});
