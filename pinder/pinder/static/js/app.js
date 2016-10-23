var app = angular.module('PinderApp', ['angularMoment']);
app.config(function($interpolateProvider, $httpProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})
.filter("timeago", function () {
        return function (input) {
            return moment(input).fromNow();
        };
});
