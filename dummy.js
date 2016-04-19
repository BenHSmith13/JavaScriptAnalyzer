"use strict";

var something = require('some-module');

var aVar = "Some_junk";

function myFunct(n){
  if(n == 0) { return 1; }
  if(n == 1) { return 5; }
  return myFunct(n-1) + n;
}