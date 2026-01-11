$(function(){
/*----------------------------------------------------------------------------*/
$('body').show();
/*----------------------------------------------------------------------------*/
$('#selectUpgradeExeFileBtn').change(function(){
    var file = this.files[0];
    fileName = file.name;
    size = file.size;
    type = file.type;

	$("#upgradeExeFileBtn").attr("disabled", file.size?false:true);
});

function beforeSendExeFileHandler(jqXHR, settings){
	$("#upgradeExeFileInfo").text("开始上传文件!");
}

function errorExeFileHandler(e){
	var strInfo = "上传文件出错!错误码:" + e.status +", 错误描述:" + e.statusText;
	$("#upgradeExeFileInfo").text(strInfo);
	alert(strInfo);
}

function completeExeFileHandler(){
	$("#upgradeExeFileInfo").text(strategies.getCurrentDateTime() + " 上传文件成功!");
}

$('#upgradeExeFileBtn').click(function(){
    var formData = new FormData(document.querySelector("#upgradeExeFileForm"));
    $.ajax({
        url: 'uploadfile?execute=1',  //server script to process data
        type: 'POST',
        xhr: function() {  // custom xhr
            myXhr = $.ajaxSettings.xhr();
            return myXhr;
        },
        //Ajax事件
        beforeSend: beforeSendExeFileHandler,
        success: completeExeFileHandler,
        error: errorExeFileHandler,
        // Form数据
        data: formData,
        //Options to tell JQuery not to process data or worry about content-type
        cache: false,
        contentType: false,
        processData: false
    });
});
/*----------------------------------------------------------------------------*/

var g_osgiFuncDefs = {};

function osgiParseFuncs(funcName, funcDesc){
	var paraArr = funcDesc.split("(")[1].split(")")[0].split(",");

	var paraObj = {};

	/*if(funcName == "getLANHostStats"){
		console.log(funcName);
	}*/

	if(paraArr.length <= 1 && paraArr[0].length == 0){
		return;
	}
	
	for(para  = 0; para < paraArr.length;para++){
		var paraDesc = paraArr[para].trimLeft().trimRight().split(" ");
		switch(paraDesc[0]){
			case "int":
				paraObj[paraDesc[1]] = 0;
				break;

			case "String":
				paraObj[paraDesc[1]] = "yourString";
				break;

			case "byte[]":
				paraObj[paraDesc[1]] = "yourByteArray";
				break;

			case "String[]":
				paraObj[paraDesc[1]] = "yourStringArray";
				break;

			case "boolean":
				paraObj[paraDesc[1]] = false;
				break;

			case "BundleContext":
				paraObj[paraDesc[1]] = "yourContext";
				break;

			default:
				console.log(funcName + "," + paraDesc[0]);
				break;
		}
	}

	g_osgiFuncDefs[funcName] =  paraObj;
}

function osgiUpdateData(funcId){
	var id = "#osgi_" + funcId;

	if(!g_osgiFuncDefs[funcId]){
		$(id).text(funcId + " getting...");
		$.get("/osgi?function=" + funcId, function(data){
			$(id).text(data);
		});
	}
	
	$("#osgi_set_" + funcId).text(JSON.stringify(g_osgiFuncDefs[funcId], null, "\t"));
}

$('[page="OSGI"]').on("click", "a[hgs_sub_nav]", function(){
	var id = $(this).attr("hgs_sub_nav");
	$(".hgs_content .row:visible").hide();

	var target = ".hgs_content .row[hgs_sub_target=" + id + "]";
	$(target).show();

	if($("#osgi_" + id).text().length == 0){
		osgiUpdateData(id);
	}
})

$('[page="OSGI"]').on("click", ".osgiUpdateBtn", function(){
	osgiUpdateData($(this).attr("function"));
})


$('[page="OSGI"]').on("click", ".osgiSaveBtn", function(){
	var funcId = $(this).attr("function");
	var id = "#osgi_set_" + $(this).attr("function");

	try{
		JSON.parse($(id).val());
	}catch(SyntaxError){
		alert("非法的发送数据，JSON校验不合法!");
		return;
	}
	$.post("/osgi?function=" + funcId, $(id).val(), function(data){
		$("#osgi_" + funcId).text(data);
	});
})


function osgiGenerateSubNav(page, data){
	subDiv = $('[page="' + page + '"] ul')[0];

	var i = 0;
	var innerHtml = subDiv.innerHTML;
	var bFirst = innerHtml.length?false:true;
	for(x in data){
		innerHtml += '<li class="nav-item">';
		if(bFirst && i == 0){
			innerHtml += '<a class="nav-link changeView active" href="#" hgs_sub_nav="' + x + '" hgs_first_sub_nav="1" >' + x + '</a>';
		}else{
			innerHtml += '<a class="nav-link changeView" href="#" hgs_sub_nav="' + x + '" hgs_first_sub_nav="1" >' + x + '</a>';
		}
		innerHtml += '</li>';
		i++;
	}

	subDiv.innerHTML = innerHtml;
}



function osgiGenerateSubPage(page, data){
	subDiv = $('[page="' + page + '"] .hgs_content')[0];

	var i = 0;
	var bSendPara = true;
	var innerHtml = subDiv.innerHTML;
	for(x in data){
		osgiParseFuncs(x, data[x][0]);

		/*if(x == "getWANIfStats"){
			console.log(x);
		}*/

		bSendPara = g_osgiFuncDefs[x]?true:false;
		innerHtml += '<div class="row" hgs_sub_target="' + x + '" style="display: none;">';

		innerHtml += '<div style="margin-left: 15px;">'
		innerHtml += '<div>'+ x + '</div>';
		innerHtml += '<div>'+ data[x][0] + '</div>';
		innerHtml += '<div>'+ data[x][data[x].length - 1] + '</div>';

		innerHtml += '<div><input type="button" class="osgiUpdateBtn" value="刷新" function="' + x + '"></input>';
		if(bSendPara){
			innerHtml += '<input type="button" class="osgiSaveBtn" value="保存" function="' + x + '"></input>';
		}
		innerHtml += '</div>';


		if(bSendPara){
			innerHtml += '<div>发送数据(JSON格式):</div>';
			innerHtml += '<textarea rows="10" cols="78" id="osgi_set_' + x + '" class="hgs_textarea" >';
			innerHtml += '</textarea>';
		}

		innerHtml += '<div>服务器回应数据:</div>';
		innerHtml += '<textarea rows="20" cols="78" id="osgi_' + x + '" class="hgs_textarea" >';
		innerHtml += '</textarea>';
		innerHtml += '</div>';
		

		innerHtml += '</div>';
		i++;
	}

	subDiv.innerHTML = innerHtml;
}



function _osgiPageGenerate(data){
	for(m in data){
		for(n in data[m]){
			osgiGenerateSubNav(m, data[m][n]);
			osgiGenerateSubPage(m, data[m][n]);
			//break;
		}
	}

	//console.log(g_osgiFuncDefs);
}

function osgiPageGenerate(){
	$.get("/json/osgi_interface.json", function(data){
		delete data["comment"];
		_osgiPageGenerate(data);
	})
}


setTimeout(osgiPageGenerate, 1000);


osgiDebugCheckIn = function(path, data) {
	if($("#HGS_OSGI_DEBUG [hgs_key='EnableDebug']").is(":checked")){
		data.userTagData = 1;
	}else{
		data.userTagData = 0;
	}
}

/*----------------------------------------------------------------------------*/
var g_ahsapdFuncDefs = {};

function ahsapdReqUrl(funcId){
	var objName = $(".page[page='AHSAPD'] .subpage:visible").attr("page");
	var url = "/ahsapd?function=" + funcId;

	url += "&objName=" + objName;

	return url;
}

function ahsapdUpdateData(funcId){
	var id = "#ahsapd_" + funcId;

	if(!g_ahsapdFuncDefs[funcId]){
		$(id).text(funcId + " getting...");
		$.get(ahsapdReqUrl(funcId), function(data){
			$(id).text(data);
		});
	}
	
	$("#ahsapd_set_" + funcId).text(JSON.stringify(g_ahsapdFuncDefs[funcId], null, "\t"));
}

$('[page="AHSAPD"]').on("click", "a[hgs_sub_nav]", function(){
	var id = $(this).attr("hgs_sub_nav");
	$(".hgs_content .row:visible").hide();

	var target = ".hgs_content .row[hgs_sub_target=" + id + "]";
	$(target).show();

	if($("#ahsapd_" + id).text().length == 0){
		ahsapdUpdateData(id);
	}
})

$('[page="AHSAPD"]').on("click", ".ahsapdUpdateBtn", function(){
	ahsapdUpdateData($(this).attr("function"));
})


$('[page="AHSAPD"]').on("click", ".ahsapdSaveBtn", function(){
	var funcId = $(this).attr("function");
	var id = "#ahsapd_set_" + $(this).attr("function");

	try{
		JSON.parse($(id).val());
	}catch(SyntaxError){
		alert("非法的发送数据，JSON校验不合法!");
		return;
	}
	$.post(ahsapdReqUrl(funcId), $(id).val(), function(data){
		$("#ahsapd_" + funcId).text(data);
	});
})

$('[page="AHSAPD"]').on("click", "a[hgs_sub_nav]", function(){
	var id = $(this).attr("hgs_sub_nav");
	$(".hgs_content .row:visible").hide();

	var target = ".hgs_content .row[hgs_sub_target=" + id + "]";
	$(target).show();

	if($("#ahsapd_" + id).text().length == 0){
		ahsapdUpdateData(id);
	}
})

function ahsapdGenerateSubNav(page, data){
	var subDiv = $('[page="' + page + '"] ul')[0];

	var innerHtml = subDiv.innerHTML;
	innerHtml = innerHtml.trimLeft();
	innerHtml = innerHtml.trimRight();
	var bFirst = innerHtml.length?false:true;
	var title = data["method"];

	innerHtml += '<li class="nav-item">';
	if(bFirst){
		innerHtml += '<a class="nav-link changeView active" href="#" hgs_sub_nav="' + data["func"] + '" hgs_first_sub_nav="1" >' + title + '</a>';
	}else{
		innerHtml += '<a class="nav-link changeView" href="#" hgs_sub_nav="' + data["func"] + '" hgs_first_sub_nav="1" >' + title + '</a>';
	}
	innerHtml += '</li>';

	subDiv.innerHTML = innerHtml;
}

function ahsapdGenerateSubPage(page, data){
	var otherSendPara=["ahsapi_cfg_get_item"];
	var subDiv = $('[page="' + page + '"] .hgs_content')[0];
	var bSendPara = true;
	var innerHtml = subDiv.innerHTML;
	var x = data["func"];


	bSendPara = (x.indexOf("get") >= 0)?false:true;

	if(!bSendPara){
		for(var m in otherSendPara){
			if(x== otherSendPara[m]){
				bSendPara = true;
				break;
			}
		}
	}

	innerHtml += '<div class="row" hgs_sub_target="' + x + '" style2="display: none;">';

	innerHtml += '<div style="margin-left: 15px;">'


	innerHtml += '<div><input type="button" class="ahsapdUpdateBtn" value="刷新" function="' + x + '"></input>';
	if(bSendPara){
		innerHtml += '<input type="button" class="ahsapdSaveBtn" value="保存" function="' + x + '"></input>';
	}
	innerHtml += '</div>';


	if(bSendPara){
		innerHtml += '<div>发送数据(JSON格式): (注意:如果数据是只读的，请不要发送数据)</div>';
		innerHtml += '<textarea rows="10" cols="78" id="ahsapd_set_' + x + '" class="hgs_textarea" >';
		innerHtml += '</textarea>';
	}

	innerHtml += '<div>服务器回应数据:</div>';
	innerHtml += '<textarea rows="20" cols="78" id="ahsapd_' + x + '" class="hgs_textarea" >';
	innerHtml += '</textarea>';
	innerHtml += '</div>';
	

	innerHtml += '</div>';



	subDiv.innerHTML = innerHtml;
}

function ahsapdPageGenerate(){
	var m, n;
	$.get("/json/ahsapd_interface.json", function(data){
		//console.log(data);
		for(m in data){
			//console.log(m);
			for(n in data[m]){
				//console.log(data[m][n]);
				ahsapdGenerateSubNav(m, data[m][n]);
				ahsapdGenerateSubPage(m, data[m][n]);
			}
		}
	})
}

setTimeout(ahsapdPageGenerate, 2000);

/*----------------------------------------------------------------------------*/

hbusStatGet = function(id) {
	$.get("/hbusStats", function(data){
		$("#" + id).text(JSON.stringify(data, null, "\t"));
	})
}

hbusGetGlobalStat = function(data) {
	delete data.IPC.ProcessAndMsgQueueInfo;
	return data.IPC;
}

hbusGetMemoryStat = function(data) {
	data.shareMemoryPool.TotalBlockNum = data.shareMemoryPool.Total.blockNum;
	data.shareMemoryPool.TotalUsed = data.shareMemoryPool.Total.used;
	data.shareMemoryPool.TotalMallocCnt = data.shareMemoryPool.Total.mallocCnt;


	for(x in data.shareMemoryPool){
		if(typeof data.shareMemoryPool[x] == "object"){
			delete data.shareMemoryPool[x];
		}
	}

	return data.shareMemoryPool;
}

hbusProcessStatPreUpdate = function(data) {
	var focusProcessName = $("#ShowHbusStatProcessName").text();
	processInfos = data.IPC.ProcessAndMsgQueueInfo;
	for(x in processInfos){
		procInfo = processInfos[x];
		if(typeof procInfo.msgEndPos == "number"){
			if(procInfo.msgEndPos < procInfo.msgBeginPos){
				procInfo.freePosNum = procInfo.msgBeginPos - procInfo.msgEndPos -1; 
			}else{
				procInfo.freePosNum = (data.IPC.MaxMsgQueueNum - 1) - (procInfo.msgEndPos - procInfo.msgBeginPos);
			}
		}
		procInfo.WaitSemStatus = procInfo.WaitSem.SemStatus;
		procInfo.WaitCnt = procInfo.WaitSem.WaitCnt;
		procInfo.WaitPostCnt = procInfo.WaitSem.PostCnt;

		procInfo.ReplySemStatus = procInfo.ReplySem.SemStatus;
		procInfo.ReplyCnt = procInfo.ReplySem.WaitCnt;
		procInfo.ReplyPostCnt = procInfo.ReplySem.PostCnt;

		if(focusProcessName == procInfo.path){
			processStatClickRow(m, procInfo);
		}
	}
	
	return processInfos;
}


hbusProcessStatUpdate = function() {
	loadTableData("HGST_HBUS_PROCESS_STAT");
}

processStatClickRow = function (index, row) {
	var data = [];

	for(m in row.ReplySem.wait){
		data.push(row.ReplySem.wait[m]);
		data[data.length - 1].Action = "Reply";
	}

	for(m in row.WaitSem.wait){
		data.push(row.WaitSem.wait[m]);
		data[data.length - 1].Action = "Wait";
	}

	$("#ShowHbusStatProcessName").text(row.path);

	var id = "HGST_HBUS_SINGLE_PROCESS_STAT";
	$("#" + getTableIdByHgstId(id)).datagrid('loadData', data);
	//adjustTableHeight(id);
}

hbusMemBlockPreCheckout = function(data) {
	var blockStat = data.shareMemoryPool.blockStat;
	for(x in data.shareMemoryPool.blockStat){
		blockStat[x].availableBlockSize = blockStat[x].blockSize - 60;
	}

	return blockStat;	
}

/*----------------------------------------------------------------------------*/

hbusProcessListPreCheckout = function(data) {
	//var focusProcessName = $("#ShowHbusStatProcessName").text();
	processInfos = data.IPC.ProcessAndMsgQueueInfo;
	for(x in processInfos){
		procInfo = processInfos[x];
		if(typeof procInfo.msgEndPos == "number"){
			if(procInfo.msgEndPos < procInfo.msgBeginPos){
				procInfo.freePosNum = procInfo.msgBeginPos - procInfo.msgEndPos -1; 
			}else{
				procInfo.freePosNum = (data.IPC.MaxMsgQueueNum - 1) - (procInfo.msgEndPos - procInfo.msgBeginPos);
			}
		}
		procInfo.WaitSemStatus = procInfo.WaitSem.SemStatus;
		procInfo.WaitCnt = procInfo.WaitSem.WaitCnt;
		procInfo.WaitPostCnt = procInfo.WaitSem.PostCnt;

		procInfo.ReplySemStatus = procInfo.ReplySem.SemStatus;
		procInfo.ReplyCnt = procInfo.ReplySem.WaitCnt;
		procInfo.ReplyPostCnt = procInfo.ReplySem.PostCnt;

		/*if(focusProcessName == procInfo.path){
			processStatClickRow(m, procInfo);
		}*/

		if(procInfo.path.length == 0){
			return processInfos.slice(0, x - 1);
		}
	}
	
	return processInfos;
}


hbusProcessListUpdate = function() {
	loadTableData("HGST_HBUS_DAEMON_LIST");
}


hbusProcessListClickRow = function(index, row) {
	$("#hbusDaemonProcessName").text(row.path);

	$.get("/hbusMsgData?ipcId=" + row.ipcId, function(data){
		var id = "HGST_HBUS_DAEMON_PROCESS_MSG_LIST";

		$("#" + getTableIdByHgstId(id)).datagrid('loadData', data.data);

		adjustTableHeight(id);
	});
}

hbusProcessMsgListClickRow = function(index, row) {
	var text = row.data.replace(/\\n/g, "\n").trimLeft();

	$("#HGS_HBUS_DUMP_DATA").text(text);
}
/*----------------------------------------------------------------------------*/

antiAttackCheckout = function(data){
	return {timeout:data.timeout, tick:data.tick, skb_list_push:data.skb_list_push,
		skb_list_pop:data.skb_list_push, 
		rxTotalPkts:data.rxTotalPkts,rxTcpSynPkts:data.rxTcpSynPkts,rxTcpSynPkts:data.rxTcpSynPkts,
		txTotalPkts:data.txTotalPkts,txRstAndAckPkts:data.txRstAndAckPkts, txDropPkts:data.txDropPkts
	};
}

antiAttackStatUpdate = function(){
	loadTableData("HGST_ANTI_ATTACK_STAT");
} 

antiAttackListUpdate = function(){
	loadTableData("HGST_ANTI_ATTACK_LIST");
}

antiAttackPreUpdate = function(data){
	return data.dataList;
}
/*----------------------------------------------------------------------------*/

dumpmdmCheckout = function(id) {
	$.get("/hgdumpmdm", function(data){
		$("#" + id).text((new XMLSerializer()).serializeToString(data));
	})
}

dumpcfgCheckout = function(id) {
	$.get("/hgdumpcfg", function(data){
		//$("#" + id).text((new XMLSerializer()).serializeToString(data));
		$("#" + id).text(data);
	})
}

dumpbkcfgCheckout = function(id) {
	$.get("/hgdumpcfg?backup=1", function(data){
		$("#" + id).text(data);
	})
}

/*----------------------------------------------------------------------------*/


/*----------------------------------------------------------------------------*/

coredumpCheckout = function(data){
	var fileDescs = data.split("\n");
	var coreDumps = [];

	for(var i in fileDescs){
		var columns = fileDescs[i].split(" ");
		if(columns.length != 3){
			continue;
		}

		coreDumps.push({filename:columns[2], date:columns[1], size:columns[0]});
	}
	return {total:coreDumps.length, rows:coreDumps};
}

coredumpDownload = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_CORE_DUMP"));
	var CheckedData = dg.datagrid("getChecked");
	if(1 != CheckedData.length){
		alert("请只选中一行，再【下载】!");
		return true;
	}
	var saveAs = CheckedData[0].filename.split("/");
	download("/coredump?action=download&filename=" + CheckedData[0].filename, saveAs[saveAs.length - 1]);
}

coredumpDelete = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_CORE_DUMP"));
	var CheckedData = dg.datagrid("getChecked");
	if(1 != CheckedData.length){
		alert("请只选中一行，再【删除】!");
		return true;
	}

	$.get("/coredump?action=delete&filename=" + CheckedData[0].filename, function(data){
		coredumpUpdate();
	})
	
	return true;
}

coredumpUpdate = function(){
	loadTableData("HGST_CORE_DUMP");
}

coredumpCheckRow = function(index,row){

}

coredumpClickRow = function(index,row){

}

/*----------------------------------------------------------------------------*/

cfgFilesCheckout = function(data){
	var fileDescs = data.split("\n");
	var coreDumps = [];

	for(var i in fileDescs){
		var columns = fileDescs[i].split(" ");
		if(columns.length != 3){
			continue;
		}

		coreDumps.push({filename:columns[2], date:columns[1], size:columns[0]});
	}
	return {total:coreDumps.length, rows:coreDumps};
}

cfgFilesDownload = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_CONFIG_FILES"));
	var CheckedData = dg.datagrid("getChecked");
	if(1 != CheckedData.length){
		alert("请只选中一行，再【下载】!");
		return true;
	}
	var saveAs = CheckedData[0].filename.split("/");
	download("/cfgFiles?action=download&filename=" + CheckedData[0].filename, saveAs[saveAs.length - 1]);
}

cfgFilesDelete = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_CONFIG_FILES"));
	var CheckedData = dg.datagrid("getChecked");
	if(1 != CheckedData.length){
		alert("请只选中一行，再【删除】!");
		return true;
	}

	$.get("/cfgFiles?action=delete&filename=" + CheckedData[0].filename, function(data){
		cfgFilesUpdate();
	})
	
	return true;
}

cfgFilesUpdate = function(){
	loadTableData("HGST_CONFIG_FILES");
}

cfgFilesCheckRow = function(index,row){

}

cfgFilesClickRow = function(index,row){

}





$('#selectUpgradeCfgFileBtn').change(function(){
    var file = this.files[0];
    fileName = file.name;
    size = file.size;
    type = file.type;

	$("#upgradeCfgFileBtn").attr("disabled", file.size?false:true);
});

function beforeSendCfgFileHandler(jqXHR, settings){
	$("#upgradeCfgFileInfo").text("开始上传文件!");
}

function errorCfgFileHandler(e){
	var strInfo = "上传文件出错!错误码:" + e.status +", 错误描述:" + e.statusText;
	$("#upgradeCfgFileInfo").text(strInfo);
	alert(strInfo);
}

function completeCfgFileHandler(){
	$("#upgradeCfgFileInfo").text(strategies.getCurrentDateTime() + " 上传文件成功!");
	cfgFilesUpdate();
}

$('#upgradeCfgFileBtn').click(function(){
    var formData = new FormData(document.querySelector("#upgradeCfgFileForm"));
    $.ajax({
        url: 'cfgFiles?action=upload',  //server script to process data
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


/*----------------------------------------------------------------------------*/

$("#hbusIpcId").change(function(){
	//alert($("#hbusIpcId").val());
	$.get("/hbusDebug?debugIpcId="+$("#hbusIpcId").val())
})

/*----------------------------------------------------------------------------*/
osgiSwitchCheckout = function(){
	$.get("/osgiDebug?action=status", function(data){
		$("#runOsgiChecked").prop("checked", (data.trimRight() == "active"));
	})
}

osgiSwitchCheckin = function(){
	var strAction = $("#runOsgiChecked").is(':checked')?"start":"stop";
	$.get("/osgiDebug?action=" + strAction, function(){
		osgiSwitchCheckout();
	})

	return true;
}
/*----------------------------------------------------------------------------*/

cfgProcessRunDelayCheckin = function(){
	var enable = $("#cfgProcessRunDelayEnable").is(':checked');	

	$.post("/cfgProcessDelay?action=" + (enable?"enable":"disable"), $("#HGS_CFG_RUN_DELAY").val(), function(data){
		
	})

	return true;
}

cfgProcessRunDelayCheckout = function(){
	$.get("/cfgProcessDelay?action=get", function(data){
		var enable = (data.substr(0, 1) == "1");

		$("#cfgProcessRunDelayEnable").attr("checked", enable);
		$("#HGS_CFG_RUN_DELAY").val(data.substr(2));
	})
}

processRunLogCheckout = function(){
	$.get("/cfgProcessDelay?action=getLog", function(data){
		$("#HGS_PROCESS_START_LOG").val(data);
	})	
}
/*----------------------------------------------------------------------------*/

var cpuUsageChart = null;
var cpuOption = {};

cpuUsageCheckout = function(){
	if(!cpuUsageChart){
		cpuUsageChart = echarts.init(document.getElementById('HGS_CPU_USAGE'), null, {
			width: 900,
			height: 400
		});

		cpuOption  = g_checkRules["HGS_CPU_USAGE"]["echartsOption"];

		if (cpuOption && typeof cpuOption === 'object') {
			for(var i = 0; i < 100;i++){
				cpuOption.xAxis.data.push(i);
			}
			
			cpuUsageChart.setOption(cpuOption);
		}
	}

	setTimeout(updateCpuUsage, 1000);
}

updateCpuUsage = function(){
	$.get("/cpuUsage", function(data){
		var cpuUsageData = cpuOption.series;
		cpuUsageData[0].data = data.CpuUsageList;
		cpuUsageChart.setOption({
			series: cpuUsageData
		});

		if($('#HGS_CPU_USAGE').is(':hidden')){
			//console.log("---hide cpu usage")
			return;
		}
		//console.log("---===updateCpuUsage")
		setTimeout(updateCpuUsage, 1000);
	})
}


/*----------------------------------------------------------------------------*/

var processMemChart = null;
var processMemOption = {};

monitorProcessMem = function(){
	if(!processMemChart){
		processMemChart = echarts.init(document.getElementById('HGS_MEM_PROCESS'), null, {
			width: 900,
			height: 600
		});

		processMemOption  = g_checkRules["HGS_MEM_PROCESS"]["echartsOption"];

		if (processMemOption && typeof processMemOption === 'object') {
			processMemChart.setOption(processMemOption);
		}
	}

	updateProcessMemUsage();
}

updateProcessMemUsage = function(){
	$.get("/processMemData", function(data){
		processMemOption["legend"]["data"] = data["legend.data"];
		processMemOption["xAxis"]["data"] = data["xAxis.data"];
		processMemOption["series"] = data["series"];
		processMemChart.setOption(processMemOption);
	})
}

/*----------------------------------------------------------------------------*/

var processJavaMemChart = null;
var processJavaMemOption = {};

monitorProcessJavaMem = function(){
	if(!processJavaMemChart){
		processJavaMemChart = echarts.init(document.getElementById('HGS_MEM_JAVA_PROCESS'), null, {
			width: 900,
			height: 600
		});

		processJavaMemOption  = g_checkRules["HGS_MEM_JAVA_PROCESS"]["echartsOption"];

		if (processJavaMemOption && typeof processJavaMemOption === 'object') {
			processJavaMemChart.setOption(processJavaMemOption);
		}
	}

	updateProcessJavaMemUsage();
}

updateProcessJavaMemUsage = function(){
	$.get("/processMemData?process=java", function(data){
		processJavaMemOption["legend"]["data"] = data["legend.data"];
		processJavaMemOption["xAxis"]["data"] = data["xAxis.data"];
		processJavaMemOption["series"] = data["series"];
		processJavaMemChart.setOption(processJavaMemOption);
	})
}
/*----------------------------------------------------------------------------*/

var totalMemChart = null;
var totalMemOption = {};

monitorTotalMem = function(){
	if(!totalMemChart){
		totalMemChart = echarts.init(document.getElementById('HGS_MEM_TOTAL'), null, {
			width: 900,
			height: 600
		});

		totalMemOption  = g_checkRules["HGS_MEM_TOTAL"]["echartsOption"];

		if (totalMemOption && typeof totalMemOption === 'object') {
			totalMemChart.setOption(totalMemOption);
		}
	}

	updateTotalMemUsage();
}

updateTotalMemUsage = function(){
	$.get("/totalMemData", function(data){
		totalMemOption["legend"]["data"] = data["legend.data"];
		totalMemOption["xAxis"]["data"] = data["xAxis.data"];
		totalMemOption["series"] = data["series"];
		totalMemChart.setOption(totalMemOption);
	})
}

/*----------------------------------------------------------------------------*/

var ponStreamChart = null;
var ponStreamOption = {};

monitorPonStream = function(){
	if(!ponStreamChart){
		ponStreamChart = echarts.init(document.getElementById('HGS_PON_STREAM'), null, {
			width: 900,
			height: 600
		});

		ponStreamOption  = g_checkRules["HGS_PON_STREAM"]["echartsOption"];

		if (ponStreamOption && typeof ponStreamOption === 'object') {
			ponStreamChart.setOption(ponStreamOption);
		}
	}

	updatePonStream();
}

updatePonStream = function(){
	$.get("/extStatData", function(data){
		ponStreamOption["legend"]["data"] = data["legend.data"];
		ponStreamOption["xAxis"]["data"] = data["xAxis.data"];
		ponStreamOption["series"] = data["series"];
		ponStreamChart.setOption(ponStreamOption);
	})
}
/*----------------------------------------------------------------------------*/
var memUsageChart = null;
var memOption =  {};

memUsageCheckout = function(){
	if(!memUsageChart){
		memUsageChart = echarts.init(document.getElementById('HGS_MEM_USAGE'), null, {
			width: 900,
			height: 400
		});

		memOption  = g_checkRules["HGS_MEM_USAGE"]["echartsOption"];
		//console.log(memOption);

		if (memOption && typeof memOption === 'object') {
			//memUsageChart.setOption(memOption);
		}
	}

	$.get("/memUsage", function(data){
		var memUsageData = memOption.series;
		memUsageData[0].data[0].value = data["MemUsage"];
		memUsageData[0].data[1].value = data["MemFree"];

		memOption.title.subtext = data["MemTotal"] + " KB";
		memUsageChart.setOption(memOption);
	})
}

/*----------------------------------------------------------------------------*/
function createChart(chartVarName, optionVarName, domId, dataUrl) {
    if (!window[chartVarName]) {
        window[chartVarName] = echarts.init(document.getElementById(domId), null, {
            width: 900,
            height: 600
        });

        window[optionVarName] = g_checkRules[domId]["echartsOption"];

        if (window[optionVarName] && typeof window[optionVarName] === 'object') {
            window[chartVarName].setOption(window[optionVarName]);
        }
    }

    updateChartData(chartVarName, optionVarName, dataUrl);
}

function updateChartData(chartVarName, optionVarName, dataUrl) {
    $.get(dataUrl, function(data) {
        window[optionVarName]["legend"]["data"] = data["legend.data"];
        window[optionVarName]["xAxis"]["data"] = data["xAxis.data"];
        window[optionVarName]["series"] = data["series"];
        window[chartVarName].setOption(window[optionVarName]);
    });
}

/*----------------------------------------------------------------------------*/
var hbusMsgStatChart = null;
var hbusMsgStatOption = {};

monitorHbusMsgStat = function(){
	createChart('hbusMsgStatChart', 'hbusMsgStatOption', 'HGS_HBUS_MSG_STAT', '/hbusMsgStatData');
}
/*----------------------------------------------------------------------------*/
var hgcmsStatChart = null;
var hgcmsStatOption = {};

monitorHgcmsStat = function(){
	createChart('hgcmsStatChart', 'hgcmsStatOption', 'HGS_HGCMS_STAT', '/hgcmsStatData');
}
/*----------------------------------------------------------------------------*/
var mibStatChart = null;
var mibStatOption = {};

monitorMibStat = function(){
	createChart('mibStatChart', 'mibStatOption', 'HGS_MIB_STAT', '/mibStatData');
}
/*----------------------------------------------------------------------------*/
devInfoUpdate = function(){
	loadTableData("HGST_DBG_DEV_INFO");
}

devInfoClear = function(){
	var id = "HGST_DBG_DEV_INFO";
	var dg = $("#" + getTableIdByHgstId(id));

	var data = dg.datagrid("getData");

	for(var m in data.rows){
		data.rows[m].value = "";
	}

	generateTable(id, g_tableRules[id], data);
	//dg.datagrid('loadData',data);
}
/*----------------------------------------------------------------------------*/

regionCodeLoadSuccess = function(data){
	var dg = $("#" + getTableIdByHgstId("HGST_REGIONC_CODE"));
	for(var i in data.rows){
		if(data.rows[i].selected){
			dg.datagrid("checkRow", i);
			break;
		}
	}
}

regionCodeUpdate = function(){
	loadTableData("HGST_REGIONC_CODE");
}

regionCodeCheckin = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_REGIONC_CODE"));
	var data = dg.datagrid("getChecked")[0];

	$.post("/regionCode?action=set", JSON.stringify(data), function(){
		loadTableData("HGST_REGIONC_CODE");
	});
}

/*----------------------------------------------------------------------------*/
factoryParaUpdate = function(){
	loadTableData("HGST_FACTORY_PARA");
}
/*----------------------------------------------------------------------------*/
devCustomerParaUpdate = function(){
	loadTableData("HGST_DEV_CUSTOMER_PARA");
}
/*----------------------------------------------------------------------------*/

/*----------------------------------------------------------------------------*/
aosnetAosnetDebugCheckout = function(){
	$.get("/aosnetDebug", function(data){
		document.querySelector("#HGS_AOSNET_DEBUG [hgs_key=EnableRedir]").checked = data.EnableRedir;
		document.querySelector("#HGS_AOSNET_DEBUG [hgs_key=EnableDebug]").checked = data.EnableDebug;
		document.querySelector("#HGS_AOSNET_DEBUG [hgs_key=RunAOSNET]").checked = data.RunAOSNET;
	})
}

aosnetAosnetDebugCheckin = function(){
	var data = {};
	
	data.EnableRedir = $('#HGS_AOSNET_DEBUG [hgs_key=EnableRedir]').prop('checked')?1:0;
	data.EnableDebug = $('#HGS_AOSNET_DEBUG [hgs_key=EnableDebug]').prop('checked')?1:0;
	data.RunAOSNET = $('#HGS_AOSNET_DEBUG [hgs_key=RunAOSNET]').prop('checked')?1:0;

	$.post("/aosnetDebug", JSON.stringify(data), function(){
		
	})

	return true;
}
/*----------------------------------------------------------------------------*/

/*----------------------------------------------------------------------------*/
redisDebugCheckout = function(){
	$.get("/redisDebug", function(data){
		document.querySelector("#HGS_REDIS_DEBUG [hgs_key=EnableDebug]").checked = data.EnableDebug;
	})
}

redisDebugCheckin = function(){
	var data = {};
	
	data.EnableDebug = $('#HGS_REDIS_DEBUG [hgs_key=EnableDebug]').prop('checked')?1:0;

	$.post("/redisDebug", JSON.stringify(data), function(){
		
	})

	return true;
}
/*----------------------------------------------------------------------------*/

selfcheckStatusPreCheckout = function(data){
	return data.status;
}

selfcheckStatusCheckout = function(data){
	g_shareMemoryData = data.status;

	var currPageSize = g_tableRules["HGST_SELF_CHECK"]["easyui"]["pageSize"];

	try{
		currPageSize = $("#" + getTableIdByHgstId("HGST_SELF_CHECK")).datagrid("getPager").data("pagination").options.pageSize;
	}catch(err){

	}

	return {total:data.status.length, rows:data.status.slice(0, currPageSize)};
}
/*----------------------------------------------------------------------------*/

get32bitStat = function(){
	loadTableData("HGST_32BIT_STAT");
}

get64bitStat = function(){
	loadTableData("HGST_64BIT_STAT");
}

Stat32bitCheckout = function(data){	
	g_shareMemoryData = data;

	var currPageSize = g_tableRules["HGST_32BIT_STAT"]["easyui"]["pageSize"];
	
	/*There is an exeption in first time(due to the table dosen't exist). so try it*/
	try{
		currPageSize = $("#" + getTableIdByHgstId("HGST_32BIT_STAT")).datagrid("getPager").data("pagination").options.pageSize;
	}catch(err){

	}

	return {total:data.length, rows:data.slice(0, currPageSize)};
}

Stat64bitCheckout = function(data){	
	g_shareMemoryData = data;

	var currPageSize = g_tableRules["HGST_64BIT_STAT"]["easyui"]["pageSize"];
	
	/*There is an exeption in first time(due to the table dosen't exist). so try it*/
	try{
		currPageSize = $("#" + getTableIdByHgstId("HGST_64BIT_STAT")).datagrid("getPager").data("pagination").options.pageSize;
	}catch(err){

	}

	return {total:data.length, rows:data.slice(0, currPageSize)};
}
/*----------------------------------------------------------------------------*/

get4bytesShareMem = function(){
	loadTableData("HGST_SHAREMEM_4BYTES");
}

get8bytesShareMem = function(){
	loadTableData("HGST_SHAREMEM_8BYTES");
}

get16bytesShareMem = function(){
	loadTableData("HGST_SHAREMEM_16BYTES");
}

get64bytesShareMem = function(){
	loadTableData("HGST_SHAREMEM_64BYTES");
}

var g_shareMemoryData;
ShareMem4bytesCheckout = function(data){	
	g_shareMemoryData = data;

	var currPageSize = g_tableRules["HGST_SHAREMEM_4BYTES"]["easyui"]["pageSize"];
	
	/*There is an exeption in first time(due to the table dosen't exist). so try it*/
	try{
		currPageSize = $("#" + getTableIdByHgstId("HGST_SHAREMEM_4BYTES")).datagrid("getPager").data("pagination").options.pageSize;
	}catch(err){

	}

	return {total:data.length, rows:data.slice(0, currPageSize)};
}

ShareMem8bytesCheckout = function(data){	
	g_shareMemoryData = data;

	var currPageSize = g_tableRules["HGST_SHAREMEM_8BYTES"]["easyui"]["pageSize"];
	
	/*There is an exeption in first time(due to the table dosen't exist). so try it*/
	try{
		currPageSize = $("#" + getTableIdByHgstId("HGST_SHAREMEM_8BYTES")).datagrid("getPager").data("pagination").options.pageSize;
	}catch(err){

	}

	return {total:data.length, rows:data.slice(0, currPageSize)};
}
ShareMem16bytesCheckout = function(data){	
	g_shareMemoryData = data;

	var currPageSize = g_tableRules["HGST_SHAREMEM_16BYTES"]["easyui"]["pageSize"];
	
	/*There is an exeption in first time(due to the table dosen't exist). so try it*/
	try{
		currPageSize = $("#" + getTableIdByHgstId("HGST_SHAREMEM_16BYTES")).datagrid("getPager").data("pagination").options.pageSize;
	}catch(err){

	}

	return {total:data.length, rows:data.slice(0, currPageSize)};
}
ShareMem64bytesCheckout = function(data){	
	g_shareMemoryData = data;

	var currPageSize = g_tableRules["HGST_SHAREMEM_64BYTES"]["easyui"]["pageSize"];
	
	/*There is an exeption in first time(due to the table dosen't exist). so try it*/
	try{
		currPageSize = $("#" + getTableIdByHgstId("HGST_SHAREMEM_64BYTES")).datagrid("getPager").data("pagination").options.pageSize;
	}catch(err){

	}

	return {total:data.length, rows:data.slice(0, currPageSize)};
}
refreshPager = function(dg, id){
	var pager = dg.datagrid('getPager');
	var state = dg.data('datagrid');
	var opts = state.options;
	var PageSize = g_tableRules[id]["easyui"]["pageSize"];
	var pager = dg.datagrid('getPager');

	pager.pagination('refresh',{
		pageNumber:1,
		pageSize:PageSize
	});

	return {
		onSelectPage:function(pageNum, pageSize){
			opts.pageNumber = pageNum;
			opts.pageSize = pageSize;
			var startIndex = (pageNum - 1) * pageSize;
			var endIndex = startIndex + pageSize;
			var pageData = g_shareMemoryData.slice(startIndex, endIndex);

			newMemData = {
				total: g_shareMemoryData.length,
				rows: pageData
			}

			dg.datagrid('loadData',newMemData);
			pager.pagination('refresh', {
                pageNumber: pageNum,
                pageSize: pageSize
            });
		},
		onChangePageSize:function(pageSize){
			setTimeout(function(){
				resizeSubNavContentHeight();
				}, 1000);
		}
	}
}
/*----------------------------------------------------------------------------*/

$("#blinkUpdate").click(function(){
	var sendData = $("#blink_send_json").val();
	var url = "/" + $("#plugin").val()+"?function=" + $("#blinkFuncName").val();
 
	if ($("#plugin").val() == "HG_Slave_Capability") {
		if (sendData.length == 0) {
			alert("需要填写参数！");
			return;
		}
		$.post(url, $("#blink_send_json").val(), function(data){
			$("#blink_recv_json").val(data);
		})		
	}else{
		if(sendData.length == 0){
			$.get(url, function(data){
				$("#blink_recv_json").val(data);
			})
	
			return
		}
	
		$.post(url, $("#blink_send_json").val(), function(data){
			$("#blink_recv_json").val(data);
		})
	}
})

$("#blinkClear").click(function(){
	$("#blink_send_json").val("");
	$("#blink_recv_json").val("");
})
/*----------------------------------------------------------------------------*/

$("#mfUpdate").click(function(){
	var dataJson = {};
	var sendData = $("#mf_send_json").val();
	var url = "/hg_mf_test";

	const radio = document.querySelector('input[name="MfDebugMode"][value="1"]');
	if (radio.checked)
	{
		dataJson.DebugMode = "1";
	}
	else
	{
		dataJson.DebugMode = "0";
	}
	
	var sendDataTmp=sendData.replace(/\n/g, '');
	dataJson.sendData = sendDataTmp;
	$.post(url, JSON.stringify(dataJson), function(data){
		$("#mf_recv_json").val(data);
	})	
})

$("#mfClear").click(function(){
	$("#mf_send_json").val("");
	$("#mf_recv_json").val("");
})


$("#mfExtUpdate").click(function(){
	var dataJson = {};
	var sendData = $("#mf_ext_send_json").val();
	var url = "/hg_mf_test";
	
	dataJson.DataType = $("#mfDataType").val();
	dataJson.FuncName = $("#mfExtFuncName").val();
	
	if(sendData.length > 0)
	{
		var sendDataTmp=sendData.replace(/\n/g, '');
		dataJson.sendData = sendDataTmp;
	}
	$.post(url, JSON.stringify(dataJson), function(data){
		$("#mf_ext_recv_json").val(data);
	})
})

$("#mfExtClear").click(function(){
	$("#mf_ext_send_json").val("");
	$("#mf_ext_recv_json").val("");
})
/*----------------------------------------------------------------------------*/
})
