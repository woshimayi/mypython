document.addEventListener("DOMContentLoaded", function() {
const maxTryCnt = 3;
let challengeStr = "";
let logining = 0; // 0 - not logging in, 1 - is logging in
let timeoutStatus;
let region = getRegionFullName();

loadStaticData();
regionCfg(region);

document.getElementById("Cancel").addEventListener("click", function() {
	document.getElementById("UserAccount").value = "";
	document.getElementById("Password").value = "";
});

document.getElementById("Reister").addEventListener("click", function() {
	window.top.location = "register.html";
});

document.getElementById("Login").addEventListener("click", function() {
	logining = 1;


	if (document.getElementById("UserAccount").value === "") {
		document.getElementById("UserAccount").focus();
		alert("Username cannot be empty!");
		logining = 0;
		return;
	}

	if (document.getElementById("Password").value === "") {
		document.getElementById("Password").focus();
		alert("Password cannot be empty!");
		logining = 0;
		return;
	}

	getChallengeStr();
});

function regionCfg(region) {
	const registerBtn = document.getElementById("Reister");
	switch (region) {
		case "Zhejiang":
			if (typeof g_disableRegBtn !== 'undefined' && g_disableRegBtn) {
				registerBtn.disabled = true;
			} else {
				registerBtn.disabled = false;
			}
			break;
		default:
			break;
	}
}

function loadStaticData(){
	const KEY_STATIC = "hgs_static_key"

	fetch("/staticInfo")
		.then(response => response.json())
		.then(data => {
			var elements = document.querySelectorAll("[" + KEY_STATIC +"]");

			for (var i = 0; i < elements.length; i++) {
				var key = elements[i].getAttribute(KEY_STATIC);
				elements[i].innerText = data[key];
			}
		})
		.catch(() => {
			alert("Network Error");
	});
}

document.getElementById("Password").addEventListener("keydown", function(e) {
	if (e.keyCode === 13) { // support return key to login
		document.getElementById("lgDevice").click();
		return false;
	}
});

function login(responseChallenge, newSession) {
	let url = `/lgDevice?userName=${encodeURIComponent(document.getElementById("UserAccount").value)}&responseChallenge=${encodeURIComponent(responseChallenge)}`;
	const pwd = document.getElementById("Password").value;
	const user = document.getElementById("UserAccount").value;

	if (pwd.includes("+") || pwd.length === 32 || user.includes("daemon")) {
		url += `&data=${encodeURIComponent(document.getElementById("Password").value)}`;
	}

	fetch(url)
		.then(response => response.json())
		.then(data => {
			switch (data.errorCode) {
				case 0:
					location.href = data.url;
					break;
				case 1:
					if (data.extData) {
						document.getElementById("session-id").textContent = data.extData;
						document.getElementById("session-row").style.display = "block";
					}
					if (data.lgErrCnt) {
						const remainCnt = 3 - data.lgErrCnt;
						if (remainCnt <= 0) {
							alert("You can try and fail 3 times in one minute! You need 60 seconds to log in again!");
						} else {
							alert(`Wrong username or password! You have ${remainCnt} chances left to log in!`);
						}
					} else {
						alert("Wrong username or password!");
					}
					break;
				case 2:
					alert("There is already a device logged in!");
					break;
				case 3:
					alert("Other errors!");
					break;
			}
			logining = 0;
		})
		.catch(() => {
			logining = 0;
			alert("Network Error");
		});
}

function getChallengeStr() {
	const passWordStr = document.getElementById("Password").value; // must get here to support return to login
	var url = `/getChallengeStr?userName=${encodeURIComponent(document.getElementById("UserAccount").value)}`;
	fetch(url)
		.then(response => response.json())
		.then(data => {
			if (data.challenge) {
				document.getElementById("promptInfo").textContent = "";
				const challengeStr = data.challenge;
				const responseChallenge = hex_md5(challengeStr + ":" + passWordStr);
				login(responseChallenge, data.session);
				return;
			}

			switch (data.errorCode) {
				case 0:
					if (!data.url) {
						document.getElementById("promptInfo").textContent = "An unknown error occurred";
						break;
					}
					location.href = data.url;
					logining = 1;
					return;
				case 1:
					document.getElementById("promptInfo").textContent = "Other devices have logged in. You cannot log in temporarily.";
					break;
				case 5:
					if (data.nextLogRemainSec) {
						alert(`You can try and fail at most 3 times in one minute! You need ${data.nextLogRemainSec} seconds to log in again!`);
					} else {
						alert("You can try and fail at most 3 times in one minute! Do not log in too frequently!");
					}
					break;
				default:
					document.getElementById("promptInfo").textContent = "An unknown error occurred";
					break;
			}
			logining = 0;
		})
		.catch(() => {
			document.getElementById("promptInfo").textContent = "The network is down and you cannot log in.";
			logining = 0;
		});
}
});