var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var data = JSON.stringify({
    "data": [
      [
        7.4,
        0.7,
        0,
        1.9,
        0.076,
        11,
        34,
        0.9978,
        3.51,
        0.56,
        9.4
      ]
    ]
  });
  
  var xhr = new XMLHttpRequest();
  xhr.withCredentials = true;
  
  xhr.addEventListener("readystatechange", function () {
    if (this.readyState === 4) {
      console.log(this.responseText);
    }
  });
  
  xhr.open("POST", "http://localhost:1234/invocations");
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.setRequestHeader("cache-control", "no-cache");
  xhr.setRequestHeader("Postman-Token", "09ff0c00-940b-49ed-928a-3a83e654031e");
  
  xhr.send(data);