app.factory('pinderFactory', function($http, $q){
    var service = {};
    var _baseUrl = "/api/requests/";
    service.requestPeering = function (body){
        var deferred = $q.defer();
        $http({
            method: 'POST',
            url: _baseUrl,
            data: body
        }).success(function(data){
            deferred.resolve(data);
        }).error(function(err){
            deferred.reject('There is a Backend error')
        });
        return deferred.promise;
    };
    return service;
});
