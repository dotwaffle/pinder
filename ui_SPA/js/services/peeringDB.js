app.factory('peeringdbFactory', function($http, $q){
    var service = {};
    var _baseUrl = "/js/data/";
    service.getByASN = function (asnumber){
        var deferred = $q.defer();
        $http({
            method: 'GET',
            url: _baseUrl+asnumber+'.json'
        }).success(function(data){
            deferred.resolve(data);
        }).error(function(){
            deferred.reject('There is a Backend error')
        });
        return deferred.promise;
    };
    
    service.getIXPS = function (){
        var deferred = $q.defer();
        $http({
            method: 'GET',
            url: _baseUrl+'IXPS.json'
        }).success(function(data){
            deferred.resolve(data);
        }).error(function(){
            deferred.reject('There is a Backend error')
        });
        return deferred.promise;
    };
    return service;
});