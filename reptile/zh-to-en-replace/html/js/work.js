(function () {
	var timer;
	function toCheckLogStatus(params) {
		this.postMessage("do_getLogStatus");
	}

	this.addEventListener('message', function (e) {
		this.postMessage('You said: ' + e.data);
		if (e.data == 'start_getLogStatus') {
			timer = setInterval(toCheckLogStatus, 10*1000);
		} else if (e.data == 'stop_getLogStatus') {
			clearInterval(timer);
			this.close();
		}
	}, false);
}());