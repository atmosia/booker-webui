var app = angular.module("booker", ["ngRoute"]); 
app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "index.html"
    })
    .when("/something", {
        templateUrl : "something.html"
    });
});

//ng-app name is booker