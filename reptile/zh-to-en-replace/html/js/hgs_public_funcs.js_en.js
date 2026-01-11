$(function(){

/*----------------------------------------------------------------------------*/
removeDatagridTitleRowCheckBox = function(id) {
	var where = "#" + id + " .datagrid-header-check input[type=checkbox]";
	setTimeout(function(){
		$(where).hide();
	}, 100);
}
/*----------------------------------------------------------------------------*/

/**
 * 获取 blob
 * @param  {String} url 目标文件地址
 * @return {cb} 
 */
 function getBlob(url,cb) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'blob';
    xhr.onload = function() {
            if (xhr.status === 200) {
                cb(xhr.response);
            }
    };
    xhr.send();
}

/**
* 保存
* @param  {Blob} blob     
* @param  {String} filename 想要保存的文件名称
*/
function saveAs(blob, filename) {
if (window.navigator.msSaveOrOpenBlob) {
        navigator.msSaveBlob(blob, filename);
} else {
        var link = document.createElement('a');
        var body = document.querySelector('body');

        link.href = window.URL.createObjectURL(blob);
        link.download = filename;

        // fix Firefox
        link.style.display = 'none';
        body.appendChild(link);
        
        link.click();
        body.removeChild(link);

        window.URL.revokeObjectURL(link.href);
};
}

/**
* 下载
* @param  {String} url 目标文件地址
* @param  {String} filename 想要保存的文件名称
*/
download = function(url, filename) {
	getBlob(url, function(blob) {
		saveAs(blob, filename);
	})
}



/*----------------------------------------------------------------------------*/
$("#upgradeVersion").click(function(){
	$("#navMainMaintenance").click();
	setTimeout(function(){
		$("#nav_upgrade_version").click();
	}, 100);
})
/*------------------------------------*/

$('#selectUpgradeVerFileBtn').change(function(){
    var file = this.files[0];
    fileName = file.name;
    size = file.size;
    type = file.type;
    //your validation

	//alert(fileName);

	$("#upgradeVerBtn").attr("disabled", file.size?false:true);
});

function progressHandlingFunction(e){
    if(e.lengthComputable){
        //$('progress').attr({value:e.loaded,max:e.total});
		$('#upgardeProgressBar').attr({value:e.loaded,max:e.total});
    }
}

function beforeSendHandler(jqXHR, settings){
	//console.log(jqXHR);
	//console.log(settings);
	$("#upgradeInfo").text("Start upgrading the version!");
}

function errorHandler(){
	$.get("/getUpgradeStatus", function(data){
		switch(data.retCode){
			case 0:
				$("#upgradeInfo").text("Error in upgrading version!");
				break;

			case 2:
			case 3:
				$.get("/afterUpgradeImage");
				setTimeout(function(){
					if(window.location.href.indexOf("hgsys") > 0){
						window.location.href = "/upgrade.html?from=sys";
					}else{
						window.location.href = "/upgrade.html";
					}
				}, 2000);
				break;
		}
	})
	//$("#upgradeInfo").text("Error in upgrading version!");
	//alert("Error in upgrading version!");
}

var g_getUpgradeCnt = 0;
var g_upgradeStatus = 0;
var timer = 0;

function updateUpgradePrompt(message){
	$("#upgradeInfo").text(strategies.getCurrentDateTime() + " " + message);
}

function checkUpgradeStatus(){
	$.get("/getUpgradeStatus", function(data){
		g_getUpgradeCnt++;
		g_upgradeStatus = data.retCode;
		switch(data.retCode){
			case 0:
				if(g_getUpgradeCnt > 4){
					updateUpgradePrompt("The upgrade device process is not responding!");
				}else{
					updateUpgradePrompt("Uploading version file!");
				}
				break;

			case 1:
				updateUpgradePrompt("Invalid update file!");
				clearInterval(timer);
				$.get("/afterUpgradeImage");
				if(1 == g_getUpgradeCnt){
					doUpdateVersion();  //再上传版本文件试一次
				}
				return;


			case 2:
				updateUpgradePrompt("Upgrade file verification successful!");
				break;

			case 3:
				updateUpgradePrompt("Writing to Flash!");
				break;

			case 4:
				updateUpgradePrompt("Writing to flash failed!");
				clearInterval(timer);
				return;

			case 5:
				updateUpgradePrompt("Writing to flash successfully!");
				break;

			case 6:
				updateUpgradePrompt("Restarting!");
				break;

			case 7:
				updateUpgradePrompt("Upload version file successfully!");
				if(g_getUpgradeCnt < 3){
					break;
				}
				clearInterval(timer);
				$.get("/afterUpgradeImage");
				setTimeout(function(){
					if(window.location.href.indexOf("hgsys") > 0){
						window.location.href = "/upgrade.html?from=sys";
					}else{
						window.location.href = "/upgrade.html";
					}
				}, 2000);
				return;

			case 8:
				updateUpgradePrompt("The device is ready to receive uploaded version files!");
				break;
		}
		if (g_getUpgradeCnt > 60) {
			clearInterval(timer);
		}
	})
}

function completeHandler(){
	return;
}

var g_reTryCount = 0;

function getUpgradeStatus(){
	g_getUpgradeCnt = 0;
	timer = setInterval(checkUpgradeStatus, 2000);
}

function doUpdateVersion(){
	g_reTryCount++;
	if(g_reTryCount > 3){
		if(1 == g_upgradeStatus){
			$.get("/afterUpgradeImage");
		}
		return;
	}
	getUpgradeStatus();
	var formData = new FormData(document.querySelector("#upgradeVerForm"));
    $.ajax({
        url: 'upgradeImage',  //server script to process data
        type: 'POST',
        xhr: function() {  // custom xhr
            myXhr = $.ajaxSettings.xhr();
            if(myXhr.upload){ // check if upload property exists
                myXhr.upload.addEventListener('progress',progressHandlingFunction, false); // for handling the progress of the upload
            }
            return myXhr;
        },
        //Ajax事件
        beforeSend: beforeSendHandler,
        success: completeHandler,
        error: errorHandler,
        // Form数据
        data: formData,
        //Options to tell JQuery not to process data or worry about content-type
        cache: false,
        contentType: false,
        processData: false
    });
}

$('#upgradeVerBtn').click(function(){
	g_reTryCount = 0;
	$("#upgardeProgressBarDiv").show();
    //var formData = new FormData($('form')[0]);
	$.get("/preUpgradeImage", function(){

	});

	setTimeout(doUpdateVersion, 1000);
});

/*----------------------------------------------------------------------------*/
$('#selectUpgradeFileBtn').change(function(){
    var file = this.files[0];
    fileName = file.name;
    size = file.size;
    type = file.type;

	$("#upgradeFileBtn").attr("disabled", file.size?false:true);
});

function beforeSendFileHandler(jqXHR, settings){
	//console.log(jqXHR);
	//console.log(settings);
	$("#upgradeFileInfo").text("Start uploading files!");
}

function errorFileHandler(e){
	var strInfo = "Error uploading file! Error code:" + e.status +", Error description:" + e.statusText;
	$("#upgradeFileInfo").text(strInfo);
	alert(strInfo);
}

function completeFileHandler(){
	$("#upgradeFileInfo").text(strategies.getCurrentDateTime() + " 上传文件成功!");
}

$('#upgradeFileBtn').click(function(){
    var formData = new FormData(document.querySelector("#upgradeFileForm"));
    $.ajax({
        url: 'uploadfile',  //server script to process data
        type: 'POST',
        xhr: function() {  // custom xhr
            myXhr = $.ajaxSettings.xhr();
            return myXhr;
        },
        //Ajax事件
        beforeSend: beforeSendFileHandler,
        success: completeFileHandler,
        error: errorFileHandler,
        // Form数据
        data: formData,
        //Options to tell JQuery not to process data or worry about content-type
        cache: false,
        contentType: false,
        processData: false
    });
});

/*----------------------------------------------------------------------------*/

$('#selectUploadCmsCfgBtn').change(function(){
    var file = this.files[0];
    fileName = file.name;
    size = file.size;
    type = file.type;

	$("#uploadCmsCfgBtn").attr("disabled", file.size?false:true);
});

function beforeSendCfgFileHandler(jqXHR, settings){
	$("#upgradeFileInfo").text("Start uploading files!");
}

function errorCfgFileHandler(e){
	var strInfo = "Error uploading file! Error code:" + e.status +", Error description:" + e.statusText;
	$("#uploadCmsCfgInfo").text(strInfo);
	alert(strInfo);
}

function completeCfgFileHandler(){
	$("#uploadCmsCfgInfo").text(strategies.getCurrentDateTime() + " 上传文件成功!");
	setTimeout(function(){
		location = "reboot.html";
	}, 2000);
}

$('#uploadCmsCfgBtn').click(function(){
	var r=confirm("Restoring the configuration file will cause the system to restart. Are you sure you want to restore it?")
	if (r!=true){
		return;
	}

    var formData = new FormData(document.querySelector("#uploadCmsCfg"));
    $.ajax({
        url: 'hguploadcfg',  //server script to process data
        type: 'POST',
        xhr: function() {  // custom xhr
            myXhr = $.ajaxSettings.xhr();
            return myXhr;
        },
        //Ajax事件
        beforeSend: beforeSendCfgFileHandler,
        success: completeCfgFileHandler,
        error: errorCfgFileHandler,
        // Form数据
        data: formData,
        //Options to tell JQuery not to process data or worry about content-type
        cache: false,
        contentType: false,
        processData: false
    });
});


$("#exportCmsCfgBtn").click(function(){
	download("/hgdumpcfg", "backupConfig.dat");
})

/*----------------------------------------------------------------------------*/
function enableSlaveUpgradeBtn() {
	$("#slaveUpgradeVerBtn").attr("disabled",false);
}
function disableSlaveUpgradeBtn() {
	$("#slaveUpgradeVerBtn").attr("disabled",true);
}
$('#selectSlaveUpgradeVerFileBtn').change(function(){
    var file = this.files[0];
    fileName = file.name;
    size = file.size;
    type = file.type;

	$("#slaveUpgradeVerBtn").attr("disabled", file.size?false:true);
});

function beforeSendSlaveFirmwareHandler(jqXHR, settings){
	$("#slaveUpgradeInfo").text("Start uploading files!");
}

function completeSlaveFirmwareHandler(){
	$("#slaveUpgradeInfo").text(strategies.getCurrentDateTime() + " 上传文件成功!");
	enableSlaveUpgradeBtn();
}
function errorSlaveFirmwareHandler(){
	$.get("/getUpgradeStatus", function(data){
		switch(data.retCode){
			case 0:
				$("#slaveUpgradeInfo").text("Error in upgrading version!");
				enableSlaveUpgradeBtn();
				break;

			case 2:
			case 3:
				break;
		}
	})
}
var g_getSlaveUpgradeCnt = 0;
function checkSlaveUpgradeStatus() {
	$.get("/getUpgradeStatus", function(data){
		g_getSlaveUpgradeCnt++;
		switch(data.retCode){
			case 0:
				$("#slaveUpgradeInfo").text("Uploading version file!");
				break;

			case 1:
				$("#slaveUpgradeInfo").text("Invalid update file!");
				enableUpgradeBtn();
				return;
			case 2:
				$("#slaveUpgradeInfo").text("Upgrade file verification successful!");
				return;
			case 7:
				$("#slaveUpgradeInfo").text("Upload version file successfully!");
				break;
		}
		if(g_getSlaveUpgradeCnt < 10){
			setTimeout(checkSlaveUpgradeStatus, 2000);
		}
	})	
}
function doSlaveUpdateVersion()
{
	var formData = new FormData(document.querySelector("#slaveUpgradeVerForm"));
	checkSlaveUpgradeStatus();
    $.ajax({
        url: 'uploadfirmware?',  //server script to process data
        type: 'POST',
        xhr: function() {  // custom xhr
            myXhr = $.ajaxSettings.xhr();
            return myXhr;
        },
        //Ajax事件
        beforeSend: beforeSendSlaveFirmwareHandler,
        success: completeSlaveFirmwareHandler,
        error: errorSlaveFirmwareHandler,
        // Form数据
        data: formData,
        //Options to tell JQuery not to process data or worry about content-type
        cache: false,
        contentType: false,
        processData: false
    });
}

$('#slaveUpgradeVerBtn').click(function(){
	g_reTryCount = 0;
	disableSlaveUpgradeBtn();
	
	setTimeout(doSlaveUpdateVersion, 2000);
});
/*----------------------------------------------------------------------------*/
redirToTelnetCheckin = function(){
	var enable = $("#HGS_REDIR_TO_TELNET [hgs_key=RedirEnable]").is(':checked')?1:0;	

	$.get("/telnetRedir?action=set&enable=" + enable, function(data){
		
	})

	return true;
}

redirToTelnetCheckout = function(){
	$.get("/telnetRedir?action=get", function(data){
		$("#HGS_REDIR_TO_TELNET [hgs_key=RedirEnable]").attr("checked", data.RedirEnable?true:false);
	})
}
/*----------------------------------------------------------------------------*/
omciMirrorCfgUpdate = function(data){
	var omciMirrorCfg = data;
	console.log("omciMirrorCfg=",omciMirrorCfg);

	if(omciMirrorCfg.dest){
		$("#HGS_OMCI_MIRROR_CFG [hgs_key=dest][hgs_checked_value=" + omciMirrorCfg.dest + "]").attr("checked", true);
	}else{
		$("#HGS_OMCI_MIRROR_CFG [hgs_key=dest]").attr("checked", false);
	}
	if(omciMirrorCfg.persistent == "1"){
		$("#HGS_OMCI_MIRROR_CFG [hgs_key=persistent][hgs_checked_value=" + omciMirrorCfg.persistent + "]").attr("checked", true);
	}else{
		$("#HGS_OMCI_MIRROR_CFG [hgs_key=persistent]").attr("checked", false);
	}
}


omciMirrorCfgCheckin = function(){
	var omciMirrorCfg = {};
	var omciMirrorCheckList = document.querySelectorAll("#HGS_OMCI_MIRROR_CFG [hgs_checked_value]");

	for (x in omciMirrorCheckList){
		if (omciMirrorCheckList[x].checked) {
			omciMirrorCfg[omciMirrorCheckList[x].getAttribute("hgs_key")] = omciMirrorCheckList[x].getAttribute("hgs_checked_value");
		}
	}

	if(!omciMirrorCfg.dest){
		alert("No mirror source port is selected!");
		return true;
	}

	if (omciMirrorCfg.persistent)
		omciMirrorCfg.persistent = "1";
	else
		omciMirrorCfg.persistent = "0";

	$.post("/omciMirrorCfg?action=set", JSON.stringify(omciMirrorCfg), function(data){
		omciMirrorCfgUpdate(data);
	});

	return true;
}

omciMirrorCfgDelete = function(){
	var omciMirrorCheckList = document.querySelectorAll("#HGS_OMCI_MIRROR_CFG [hgs_checked_value]");

	for(x in omciMirrorCheckList){
		omciMirrorCheckList[x].checked = false;
	}

	$.get("/omciMirrorCfg?action=clear", function(){
		
	})

	return true;
}


omciMirrorCfgCheckout = function(){
	$.get("/omciMirrorCfg?action=get", function(data){
		omciMirrorCfgUpdate(data);
	})
}
/*----------------------------------------------------------------------------*/
isValidLoginPasswd = function (val){
	var reg = /^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[~!@#$%^&*()_+`\-={}|\[\]\\:";'<>?,.\/])(?!.*\s)/; 
	if (reg.test(val))
	{
		ret = true;
	}
	else
	{
		ret = false;
	}
	return ret;
}


telnetCfgCheckout = function(data){
	return data[0];
}

telnetCfgCheckin = function(objName,objData){
	/*console.log(objName);
	console.log(objData);*/
	if (objData.TelnetUserName == "root" || objData.TelnetUserName == "user") {
		alert('[Username] is not allowed to be set to root or user!');
		return true;		
	}
	if (objData.TelnetPassword.length < 8) {
		alert('[User new password] length cannot be less than 8 characters!');
		return true;		
	}

	if (isValidLoginPasswd(objData.TelnetPassword) == false) {
		$("#HGS_TELNET_CFG [hgs_key='TelnetPassword']").focus();
		alert('[User new password] must contain letters, numbers and special characters, without spaces!');
		return true;
	}

	objData.fullPath = "InternetGatewayDevice.DeviceInfo.X_CMCC_ServiceManage.";

	return [objData];
}
/*----------------------------------------------------------------------------*/

consoleCfgCheckout = function(data){
	return data[0];
}

consoleCfgCheckin = function(objName,objData){
	/*console.log(objName);
	console.log(objData);*/
/* 
	if (objData.AdminPassword.length < 8) {
		alert('【Password】length cannot be less than 8 characters!');
		return true;		
	}

	if (isValidLoginPasswd(objData.AdminPassword) == false) {
		$("#HGS_TELNET_CFG [hgs_key='AdminPassword']").focus();
		alert('[Password] must contain letters, numbers, and special characters, without spaces!');
		return true;
	}
*/
	objData.fullPath = "InternetGatewayDevice.DeviceInfo.X_CMCC_ServiceManage.";
 
	return [objData];
}
/*----------------------------------------------------------------------------*/

$(".eyePasswd").click(function () {
	var inputEle = $(this).parent().children("input").first();

	var newType = "";
	if(inputEle.attr("type") == "password"){
		newType = "text";
		$(this).attr("src", "img/close-eye.png")
	}else{
		newType = "password";
		$(this).attr("src", "img/eye.png")
	}
	inputEle.attr("type", newType);
})

/*----------------------------------------------------------------------------*/
$("#DoLogout").click(function(){
	$.get("/logout");
	setTimeout(function (params) {
		window.location.href = LOGIN_PAGE;
	},100);
})


/*----------------------------------------------------------------------------*/
// 将十六进制字符串转换为字节序列
hexToBytes = function(hex) {
	let bytes = new Uint8Array(hex.length / 2);
	for (let i = 0, c = 0; c < hex.length; c += 2, i++) {
		bytes[i] = parseInt(hex.substr(c, 2), 16);
	}
	return bytes;
}

gbkToUtf8 = function(bytes) {
	try {
		// 尝试用UTF-8解码
		const utf8Decoder = new TextDecoder('utf-8');
		let decodedText = utf8Decoder.decode(bytes);
		// 尝试检查解码结果是否有意义，例如是否包含奇怪的字符
		if (/[\uFFFD]/.test(decodedText)) { // 使用UTF-8解码时出现替换字符
			throw new Error('Detected decoding errors, not UTF-8');
		}
		// 如果没有异常，并且没有替换字符，认为是有效的UTF-8
		return decodedText;
	} catch (e) {
		// 如果UTF-8解码失败或者检测到错误，尝试GBK解码
		const gbkDecoder = new TextDecoder('gbk');
		return gbkDecoder.decode(bytes);
	}
}
/*----------------------------------------------------------------------------*/

getDeviceType = function(hostName, vendorId) {
    // 设备类型与关键词映射
    const deviceKeywords = {
        PHONE: ["android", "iphone", "mi", "honor", "meizu", "mate", "oppo", "vivo", "plus"],
        PAD: ["pad"],
        PC: ["ubuntu", "micro", "macbook", "pc", "desktop", "msft"],
        ROUTER: ["router"],
        STB: ["stb", "itv"]
    };

    // 转换字符串为小写并检查是否包含关键词
    function checkForKeywords(str) {
        if (!str) return "others"; // 空字符串或 null/undefined 直接返回 "others"
        str = str.toLowerCase(); // 转换为小写
        for (const [type, keywords] of Object.entries(deviceKeywords)) {
            for (const keyword of keywords) {
                if (str.includes(keyword)) {
                    return type;
                }
            }
        }
        return "others";
    }

    // 检查 hostName 和 vendorId
    const hostType = checkForKeywords(hostName);
    if (hostType !== "others") return hostType;
    return checkForKeywords(vendorId);
}
/*----------------------------------------------------------------------------*/

})
