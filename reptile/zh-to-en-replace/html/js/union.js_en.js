(function () {
	/* -------------------reboot.html------------------------------------------------- */
	var rebootCounter = 60;
	var startTime = Date.now(); // 记录倒计时开始时间

	function countdown() {
		var currentTime = Date.now();
		var elapsed = Math.floor((currentTime - startTime) / 1000); // 已过秒数
		var remaining = rebootCounter - elapsed;

		if (remaining <= 0) {
			handleRedirect(); // 跳转逻辑
			return;
		}

		updateDisplay(remaining); // 更新显示

		// 计算距离下一秒的剩余时间，精确触发
		var delay = 1000 - (currentTime % 1000);
		setTimeout(countdown, delay);
	}

	function handleRedirect() {
		if (location.search.startsWith("?newIp=")) {
			const newIp = location.search.split("=")[1];
			location.href = `${location.protocol}//${newIp}${location.port}`;
		} else {
			location.href = "/";
		}
	}

	function updateDisplay(remaining) {
		const el = document.querySelector("#countdownText");
		if (el) el.textContent = remaining;
	}

	if (window.location.href.includes("reboot.html")) {
		countdown(); // 启动倒计时
	}

	document.addEventListener("visibilitychange", () => {
		if (!document.hidden) {
			// 页面变为可见时，立即更新倒计时
			const currentTime = Date.now();
			const elapsed = Math.floor((currentTime - startTime) / 1000);
			const remaining = rebootCounter - elapsed;
			updateDisplay(remaining);
		}
	});

	/* -------------------reboot.html------------------------------------------------- */
	/* -------------------upgrade.html------------------------------------------------- */

	var upgradeCounter = 70; // 总倒计时时长（秒）
	var startTimeUpgrade = Date.now(); // 新增：记录升级倒计时开始时间

	function upgradeCountdown() {
		var currentTime = Date.now();
		var elapsed = Math.floor((currentTime - startTimeUpgrade) / 1000); // 已过秒数
		var remaining = upgradeCounter - elapsed;

		if (remaining <= 0) {
			// 倒计时结束时跳转
			if (location.search.includes("from=")) {
				location.href = "/hgsystem.html";
			} else {
				location.href = "/";
			}
			return;
		}

		// 更新显示
		if (document.querySelector("#upgradeCountdownText")) {
			document.querySelector("#upgradeCountdownText").textContent = (remaining>0)?remaining:0;
		}

		// 动态调整延迟，确保精准触发
		var delay = 1000 - (currentTime % 1000);
		setTimeout(upgradeCountdown, delay);
	}

	// 新增：页面可见性监听，返回前台时立即刷新显示
	document.addEventListener("visibilitychange", () => {
		if (!document.hidden && window.location.href.includes("upgrade.html")) {
			var currentTime = Date.now();
			var elapsed = Math.floor((currentTime - startTimeUpgrade) / 1000);
			var remaining = upgradeCounter - elapsed;
			if (document.querySelector("#upgradeCountdownText")) {
				document.querySelector("#upgradeCountdownText").textContent = (remaining>0)?remaining:0;
			}
		}
	});

	if (window.location.href.includes("upgrade.html")) {
		upgradeCountdown(); // 启动倒计时
		setTimeout(checkUpgradeStatus, 2000);
	}

	function failtoUpgardeHanle() {
		$("#promptInfo").html("Upgrade failed! Please click <a href='/' target='_blank'>here</a> to go back to the main page to upgrade!");
	}

	function checkUpgradeStatus() {
		// console.log("do checkUpgradeStatus:" + upgradeCounter);
		$.get("/getUpgradeStatus", function (data) {
			switch (data.retCode) {
				case 0:
					$("#upgradeInfo").text("The upgrade service process is not responding!");
					failtoUpgardeHanle();
					return;

				case 1:
					$("#upgradeInfo").text("Invalid update file!");
					failtoUpgardeHanle();
					return;

				case 2:
					$("#upgradeInfo").text("Upgrade file verification successful!");
					break;

				case 3:
					$("#upgradeInfo").text("Writing to Flash...");
					return;

				case 4:
					$("#upgradeInfo").text("Writing to flash failed!");
					failtoUpgardeHanle();
					return;

				case 5:
					$("#upgradeInfo").text("Writing to flash successfully!");
					break;

				case 6:
					$("#upgradeInfo").text("Restarting...");
					break;
			}
			setTimeout(checkUpgradeStatus, 2000);
		})
	}
	/* -------------------upgrade.html------------------------------------------------- */
	/* -------------------portal.html------------------------------------------------- */

	hgsDisconnectPrompt = (function () {
		var firstDisconnectedPromot = true;

		return function (state) {
			switch (state) {
				case 0:
					if (firstDisconnectedPromot) {
						firstDisconnectedPromot = false;
						$("#context").html('<h3 class="text-danger">The network has been disconnected! The device can no longer be connected!</h3>'
							+ '<h6 class="text-primary">When the network connection is restored, please manually <a href="/" style="color:#f00">refresh</a> the page!</h6>');
					}
					break;
				case 1:
					if (!firstDisconnectedPromot) {
						location.reload();
						//location = window.location.href;
					}
					break;
			}
		}
	})();
	hgsUpdateData = function (data, callbkFunc) {
		var waitTimeout = 0;

		if (!data.type) {
			data.type = "GET";
		}

		var url = "path"

		if (data.path) {
			if (data.type == "GET") {
				url = "/getHbusData?path=" + data.path
			} else {
				url = "/setHbusData?path=" + data.path
			}
			if (data.method) {
				url += "&method=" + data.method;
			}
			if (data.msgType) {
				url += "&msgType=" + data.msgType;
			}
			if (data.userTagData) {
				url += "&userTagData=" + data.userTagData;
			}
			if (data.waitTimeoutMs) {
				url += "&waitTimeoutMs=" + data.waitTimeoutMs;
			}
			if (data.extraPara) {
				if (data.extraPara[0] != '&') {
					url += "&";
				}
				url += data.extraPara;
			}
		} else if (data.url) {
			url = data.url;
			if (data.waitTimeoutMs) {
				if (url.indexOf("?") < 0) {
					url += "?";
				} else {
					url += "&";
				}
				url += "waitTimeoutMs=" + data.waitTimeoutMs;
				waitTimeout = data.waitTimeoutMs + 1000;
			}
		}

		url = url.replace(/.{i}./g, "._i_.");

		if (data.type == "GET") {
			$.ajax({
				type: 'GET',
				url: urlWithRandom(url),
				success: function (result) {
					hgsDisconnectPrompt(1);
					doCallBack(result);
				},
				error: function (xhr, ajaxOptions, thrownError) {
					if (xhr.status == 401) {
						if (window.location.href.indexOf("portal.html") < 0) {
							window.location.replace("portal.html");
						}
						return;
					}

					hgsDisconnectPrompt(xhr.readyState);
				},
				timeout: waitTimeout
			});

			return;
		}

		$.ajax({
			type: 'POST',
			url: urlWithRandom(url),
			data: data.notJson ? data.commitData : JSON.stringify(data.commitData),
			success: function (result) {
				hgsDisconnectPrompt(1);
				doCallBack(result);
			},
			error: function (xhr, ajaxOptions, thrownError) {
				if (xhr.status == 401) {
					console.log(window.location.href)
					if (window.location.href.indexOf(LOGIN_PAGE) < 0) {
						window.location.replace(LOGIN_PAGE);
					}
					return;
				}

				hgsDisconnectPrompt(xhr.readyState);
			},
			timeout: waitTimeout
		});


		function doCallBack(result) {
			if (callbkFunc) {
				if (data.resultPath) {
					callbkFunc(result[data.resultPath], data.objData);
				} else {
					callbkFunc(result, data.objData);
				}
			}
		}
	}
	function getWanIP() {
		$.get('/ownInternetIp', function (jsonData) {
			document.getElementById("localIP").innerHTML = jsonData.internetIp;
		});
	}

	if (window.location.href.indexOf("portal.html") >= 0) {
		setTimeout(getWanIP, 1000);
	}
	/* -------------------portal.html------------------------------------------------- */
	/* -------------------hgsCommand.html------------------------------------------------- */

	if (window.location.href.indexOf("hgsCommand.html") >= 0) {
		setTimeout(listenSendCmd, 1000);
	}
	function listenSendCmd() {
		$("#sendCmd").click(function () {
			$.post("/hgsCommand", $("#command").val(), function (data) {
				$("#result").val(data);
			})
		})
	}

}());