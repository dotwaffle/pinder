app.controller('MainController',  function($scope, peeringdbFactory, pinderFactory) {

    $scope.ixps = [];
    $scope.ixpsl = [];
    $scope.ixpsr = [];
    $scope.selectedIXP = "";
    $scope.scrASN = "";
    $scope.dstASN = "";
    $scope.loading = false;
    $scope.showSuccessMessage = false;

    $scope.findIX = function(){
        $scope.showSuccessMessage = false;
        $scope.loading = true;
        $scope.ixps = [];
        $scope.ixpsl = [];
        $scope.ixpsr = [];
        setTimeout(function(){
            peeringdbFactory.getIXPS()
            .then(function(data){
                $scope.ixps = data.data;
                var len = $scope.ixps.length,
                    mid = len / 2;
              $scope.ixpsl  = $scope.ixps.slice(0, mid);
              $scope.ixpsr = $scope.ixps.slice(mid, len);

            },function(err){
                alert(err);
            });
            $scope.loading = false;
        }, 1000);

    };

    $scope.sendRequest = function(ixp){

        $scope.ixps = [];
        $scope.ixpsl = [];
        $scope.ixpsr = [];
        $scope.loading = true;
        setTimeout(function(){
            var data = {
              ixlan_id: ixp.ixlan_id,
              sender: "1",
              receiver: $scope.dstASN
            };
             pinderFactory.requestPeering(data)
            .then(function(data){
                $scope.showSuccessMessage = true;
                $scope.scrASN = "";
                $scope.dstASN = "";
            },function(err){
                alert(err);});
        }, 1000);
    }

});
