function httpRequest(url, callback) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", url, true);
	xhr.onreadystatechange = function() {
		if (xhr.readyState == 4){
			callback(true);
		}
	}
	xhr.onerror = function() {
		callback(false);
	}
	xhr.send();
}

setInterval(function() {
	httpRequest('https://www.google.com/', function(status) {
		chrome.browserAction.setIcon({path: 'images/'+(status?'online.png':'offline.png')});
	})
},1000);