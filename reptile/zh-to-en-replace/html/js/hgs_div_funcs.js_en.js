$(function(){

/*----------------------------------------------------------------------------*/
/*
some public functions
*/
function datagridEditRow(index, checkRow, id){
	var dg = $("#" + getTableIdByHgstId(id));

	rows = dg.datagrid("getRows").length;
	/*for(r = 0; r < rows;r++){
		dg.datagrid("endEdit", r);
	}*/

	dg.datagrid("beginEdit", index);

	if(checkRow){
		dg.datagrid('checkRow', index);
	}
}

/*----------------------------------------------------------------------------*/
ponInfoCheckout = function (data) {
	var objData = {};
	for (var i = 0; i < data.length; i++) {
		const obj = data[i];
		for (const k in obj) {
			objData[k] = obj[k];
		}
	}
	
	objData.FECSupport    = (objData.FECSupport == "1")?"support":"Not supported";
	objData.FECDownstream   = (objData.FECDownstream == "1") ? "Open" : "closure";
	
	if (isNaN(objData.TXPower) || objData.TXPower == 0) {
		objData.TXPower   = "-40.00" + "(dBm)";
	} else {
		objData.TXPower       = (10 * Math.log10(objData.TXPower / 10000)).toFixed(2) + "(dBm)";
	}

	if (isNaN(objData.RXPower) || objData.RXPower == 0) {
		objData.RXPower   = "-40.00" + "(dBm)";
	} else {
		objData.RXPower       = (10 * Math.log10(objData.RXPower / 10000)).toFixed(2) + "(dBm)";
	}
	objData.SupplyVottage = objData.SupplyVottage / 10000.00 + "(V)";
	objData.BiasCurrent   = objData.BiasCurrent * 2.0 / 1000 + "(mA)";
	objData.TransceiverTemperature = objData.TransceiverTemperature/256.0 + "(℃)";
/* 	
	$.get("/oltInfo", function(data){
		$("#olt_vendor").text(data.OltVendor?data.OltVendor:"unknown");
		$("#pon_up_time").text(data.PonUptime);
	})
 */
	resizeSubNavContentHeight();

	return objData;
}

downstreamOpticalInfoCheckout = function (data) {
	var objData = {"objName":data};

	hgsUpdateData({type:"GET",url:"/optical"},function (jsonData) {
		jsonData.noCheckout = true;
		jsonData.temperature += '℃';
		jsonData.bias += 'mA';
		jsonData.voltage += 'V';
		jsonData.txpower += 'dBm';
		jsonData.rxpower += 'dBm';
		loadHbusRespData(jsonData,objData);
	});
}
/*----------------------------------------------------------------------------*/
function isSubnetAP() {
	/* var getData = {type:"GET",
					path:"hbus://mdm/InternetGatewayDevice.Services.WifiMesh.", 
					msgType:211, 
					userTagData:1};

	hgsUpdateData(getData,function (data) {
		return parseInt(data.Enable);
	})	 */
	if (g_staticInfo["IsFTTR"] && !g_staticInfo["IsMasterGateway"])
	{
		return 1;
	}
	return 0;
}
/*----------------------------------------------------------------------------*/
/*
some functions about id=HGS_WAN
*/
/*------------------------------------*/
var wanBindInfo = {},ponBind = false,g_wanName = '';
initIpv6Disply = function(){
	if($("#selectWan").val()=="create_new_wan")
	{
		//init ipv6
		$("#WanIPv6AddrType").val("AutoConfigured");
		document.querySelector("#WanIPv6PrefixEnabled").checked = true;
		$("#WanIPv6PrefixOrigin").val("PrefixDelegation");
		
	}

}
iptvDisplay = function () {
	if ($("#iptvAccount").length) {
		if ($("#ServiceList").val() && ($("#ServiceList").val().indexOf("IPTV") > -1 || $("#ServiceList").val().indexOf("OTHER") > -1)) {
			if ($("#WanConnectType").val() == "router") {
				$("#iptvAccount").show();	
			}else{
				$("#iptvAccount").hide();
			}	
		} else {
			$("#iptvAccount").hide();
		}
	}
}
wanModeChange = function(){
	switch($("#WanConnectType").val()){
		case "bridge":
			$("#ForIpv4NatEnabled").hide();
			if($("#ServiceList").val() == "INTERNET"){
				$("#ForLanDhcpEnable").show();
			}else{
				$("#ForLanDhcpEnable").hide();
			}
			$("#ipv4OnlyCfg").hide();
			$("#ipv6OnlyCfg").hide();
			$("#rgPppoeAccount").hide();
			$("#ipv6NPTv6").hide();
			break;

		case "router":
			if(!$("#routerMtu").val()){
				$("#routerMtu").val("0");
			}

			$("#ForIpv4NatEnabled").show();
			$("#ForLanDhcpEnable").show();
			$("#ipv4OnlyCfg").show();
			$("#ipv6OnlyCfg").show();
			$("#HGS_WAN .notForTr069").show();
			$("#ipv6NPTv6").show();
			$("#DsLiteDiv").hide();

			switch($("#IPVersion").val()){
				case "1":
					$("#ipv6OnlyCfg").hide();
					$("#ipv6NPTv6").hide();
					break;
				case "2":
					$("#ipv4OnlyCfg").hide();
					$("#ForIpv4NatEnabled").hide();
					$("#DsLiteDiv").show();
					break;
				case "3":
					$("#DsLiteDiv").show();
					break;
			}

			switch($("#WanEncapType").val()){
				case "ipoe":
					$("#rgPppoeAccount").hide();
					if($("#selectWan").val()=="create_new_wan"){
						$("#routerMtu").val("1500");
					}
					break;
				case "pppoe":
					$("#rgPppoeAccount").show();
					$("#ipv4OnlyCfg").hide();
					if($("#selectWan").val()=="create_new_wan"){
						$("#routerMtu").val("1492");
					}
					pppoeDialDisplay();
					break;
			}
			break;
	}


	if($("#WanVlanEnabled").is(':checked')){		
		$("#rgWanVlanCfg").show();
	}else{
		$("#rgWanVlanCfg").hide();
	}

	if($("#ipv4AddrTypeStatic").is(':checked')){
		$("#ipv4StaticIpCfg").show();
	}else{
		$("#ipv4StaticIpCfg").hide();
	}



	$("#deleteWanBtn").attr("disabled", $("#selectWan").val()=="create_new_wan")

	$("#WanBindInterface").show();

	switch($("#ServiceList").val()){
		case "TR069":
			$("#WanBindInterface").hide();
			$("#HGS_WAN .notForTr069").hide();
			$("#WanConnectType").val("router");
			$("#WanIPv6PrefixEnabledDiv").hide();
			$("#HGS_WAN [hgs_key=MulticastVlan]").parent().parent().hide();
			break;
		case "VOIP":
		case "TR069,VOIP":
			$("#ForIpv4NatEnabled").hide();
			$("#WanBindInterface").hide();
			$("#HGS_WAN .notForTr069").hide();
			$("#WanConnectType").val("router");
			document.querySelector("#WanIPv6PrefixEnabled").checked = false;
			$("#WanIPv6PrefixEnabledDiv").hide();
			$("#HGS_WAN [hgs_key=MulticastVlan]").parent().parent().hide();
			break;
		case "OTT":	
			$("#HGS_WAN [hgs_key=MulticastVlan]").parent().parent().show();
			break;
		default:
			$("#WanIPv6PrefixEnabledDiv").show();
			$("#HGS_WAN [hgs_key=MulticastVlan]").parent().parent().show();
			break;
	}

	if($("#WanIPv6PrefixEnabled").is(':checked')){
		$("#WanIPv6PrefixCfgDiv").show();
	}else{
		$("#WanIPv6PrefixCfgDiv").hide(); 
	}


	switch($("#WanIPv6PrefixOrigin").val()){
		case "PrefixDelegation":
			$("#IPv6PrefixDiv").hide();
			break;
		case "Static":
			$("#IPv6PrefixDiv").show();
			break;
	}

	switch($("#WanIPv6AddrType").val()){
		case "AutoConfigured":
			$("#WanIPv6StaticIPCfgDiv").hide();
			$("#WanIPv6PrefixEnabledDiv").show();
			$("#WanDNS6Servers").hide();
			if($("#WanIPv6PrefixOrigin").val() != "Static")
			{
				$("#IPv6PrefixDiv").hide();
			}
			break;
		
		case "DHCPv6":
			$("#WanIPv6StaticIPCfgDiv").hide();
			$("#WanIPv6PrefixEnabledDiv").show();
			$("#WanDNS6Servers").hide();
			if($("#WanIPv6PrefixOrigin").val() != "Static")
			{
				$("#IPv6PrefixDiv").hide();
			}
			break;

		case "Static":
			$("#WanIPv6StaticIPCfgDiv").show();
			$("#WanIPv6PrefixEnabledDiv").hide();
			$("#WanIPv6PrefixCfgDiv").hide();
			$("#IPv6PrefixDiv").show();
			$("#WanDNS6Servers").show();
			break;
	}

	if ($("#ServiceList").val() == "TR069" || $("#ServiceList").val() == "VOIP") {
		$("#WanIPv6PrefixEnabledDiv").hide();
		$("#WanIPv6PrefixCfgDiv").hide();
		$("#DsLiteDiv").hide();
	}

	if($("#IPv6DsliteEnable").is(':checked')){
		$("#IPv6AftrModeDiv").show();
		if($("#IPv6AftrModeStatic").is(':checked')){
			$("#IPv6AftrDiv").show();
		}else{
			$("#IPv6AftrDiv").hide();
		}
	}else{
		$("#IPv6AftrModeDiv").hide();
		$("#IPv6AftrDiv").hide();
	}
	iptvDisplay();
	resizeSubNavContentHeight();
}


WanConnectTypeChange = function(){
	switch($("#WanConnectType").val()){
		case "bridge":
			//$("#WanEncapType").val("ipoe");
			break;

		case "router":
			$("#NatEnabled").prop("checked",true);
			if ($("#IPVersion").val() != 1) {
				$("#WanIPv6AddrType").val("AutoConfigured");
				document.querySelector("#WanIPv6PrefixEnabled").checked = true;
				$("#WanIPv6PrefixOrigin").val("PrefixDelegation");
			}
			break;
	}
	
	wanModeChange();
}

$("#WanConnectType").change(function(){
	WanConnectTypeChange();
})

WanConnectTypeChange();

/*------------------------------------*/
$("#ServiceList").change(function () {
	var getWandata = {type:"GET",
			path:"hbus://mdm/InternetGatewayDevice.WANDevice.{i}.WANConnectionDevice.{i}.WANIPConnection.{i}.;InternetGatewayDevice.WANDevice.{i}.WANConnectionDevice.{i}.WANPPPConnection.{i}.", 
			msgType:211, 
			userTagData:1};
	
	var service, serviceList = [], wanName, Name;
	var foundTr069 = false, foundVoip = false;

	iptvDisplay();
	pppoeDialDisplay();
	service = $("#ServiceList").val();
	wanName = $("#selectWan").find("option:selected").text();

	if (service.indexOf("TR069") == -1 && service.indexOf("VOIP") == -1) {
		return;
	}
	hgsUpdateData(getWandata, function (data) {
		if (data == "") {
			return;
		}

		for (let i = 0; i < data.length; i++) {
			const element = data[i];
			if (wanName != element.Name) {
				if (element.X_CMCC_ServiceList.indexOf("TR069") > -1 && service.indexOf("TR069") > -1) {
					foundTr069 = true;
					break;
				} 
				if(element.X_CMCC_ServiceList.indexOf("VOIP") > -1 && service.indexOf("VOIP") > -1) {
					foundVoip = true;
					break;
				}	
			} else {
				Name = element.X_CMCC_ServiceList;
			}
		}

		if (foundTr069 || foundVoip) {
			if (foundTr069) {
				serviceList.push("TR069");
			}
			if (foundVoip) {
				serviceList.push("VOIP");
			}

			alert(serviceList.toString() + "The business has been established, please select another business!");
			if (wanName == "Create a new WAN connection") {
				$("#ServiceList").val("");
			} else {
				$("#ServiceList").val(Name);
			}
			pppoeDialDisplay();
			return;
		}
	})
})
/*------------------------------------*/
$(".wanCfgChange").change(function(){
	
	wanModeChange()
})

/*------------------------------------*/

createNewWan = function(){
	$("#enableWan").prop("checked",true);
	if (g_staticInfo["Region"] == "Jiangsu" || g_staticInfo["Region"] == "JiangsuJK") {
		$("#IPVersion").val(3);
	} else {
		$("#IPVersion").val(1);
	}

	$("#WanEncapType").val("ipoe");
	$("#ServiceList").val("internet");
	$("#WanConnectType").val("router"); 

	$("#HGS_WAN [hgs_key=VlanId]").val("");
	$("#HGS_WAN [hgs_key=_802dot1p]").val(0);

	$("#HGS_WAN [hgs_key=ExternalIPAddress]").val("");
	$("#HGS_WAN [hgs_key=SubnetMask]").val("");
	$("#HGS_WAN [hgs_key=DefaultGateway]").val("");
	$("#HGS_WAN [hgs_key=DNSServers]").val("");
	$("#HGS_WAN [hgs_key=MulticastVlan]").val("-1");
	
	/*$("#NatEnabled").attr("checked", true);
	$("#WanVlanEnabled").attr("checked", true);
	$("#ipv4AddrTypeDhcp").attr("checked", true);
	$("#LanInterface-DHCPEnable").attr("checked", true);*/
	//jquery do not work as we expect, so don't use jquery
	document.querySelector("#NatEnabled").checked = true;
	document.querySelector("#WanVlanEnabled").checked = true;
	document.querySelector("#LanInterface-DHCPEnable").checked = true;
	document.querySelector("#ipv4AddrTypeDhcp").checked = true;
	document.querySelector("#IPv6AftrModeAuto").checked = true;
	
	$("#ServiceList").val("");

	wanUncheckAllBindInterface();

	for (const k in wanBindInfo) {
		if ($.isEmptyObject(wanBindInfo[k])) {
			if (document.querySelector("#HGS_WAN [hgs_checked_value='" + k + "']")) {
			document.querySelector("#HGS_WAN [hgs_checked_value='" + k + "']").removeAttribute("disabled");
			}
		} else {
			if (Object.keys(wanBindInfo[k]).length) {
				// 端口绑定了ipv,ipv6或绑定了vlan/vxlan
				document.querySelector("#HGS_WAN [hgs_checked_value='" + k + "']").setAttribute("disabled",true);
				if (Object.keys(wanBindInfo[k])[0] == 'port') {
					if (!wanBindInfo[k].port[0] || !wanBindInfo[k].port[1]) {
						// 端口未同时绑定了ipv,ipv6
						document.querySelector("#HGS_WAN [hgs_checked_value='" + k + "']").removeAttribute("disabled");	
					}
				}
			}
		}
	}

	if (!(isSubnetAP())){
		if (document.querySelector("#HgSlaveMcastEnable")) {
			if (ponBind) {
				document.querySelector("#HgSlaveMcastEnable").setAttribute("disabled",true);
			} else {
				document.querySelector("#HgSlaveMcastEnable").removeAttribute("disabled");
			}	
		}
	}

	WanConnectTypeChange()
	wanModeChange()
}

/*------------------------------------*/
selectWanChange = function(){
	if($("#selectWan").val() == "create_new_wan"){
		g_wanName = 'create_new_wan';
		createNewWan();
	}else{
		wanInfoByIdx(parseInt($("#selectWan").val()));
		g_wanName = $("#selectWan").find("option:selected").text();
		wanModeChange();
	}
}

$("#selectWan").change(function(){
	selectWanChange();
})

/*------------------------------------ */
$("#IPVersion").change(function(){
	switch($("#IPVersion").val()){
		case "1":
			break;
		case "2":
			initIpv6Disply();
			break;
		case "3":
			initIpv6Disply();
			break;
	}
	wanModeChange();
})

pppoeDialDisplay = function () {
	if ($(".pppoeDial").length) {
		if ($("#ServiceList").val() == "INTERNET") {
			$(".pppoeDial").show();
			ConnectionTriggerChange();
		}else {
			$(".pppoeDial").hide();
		}	
	}
}

$("#ConnectionTrigger").change(function(){
	ConnectionTriggerChange();
})

ConnectionTriggerChange = function () {
	$(".onlyManual").hide();
	$(".onlyOnDemand").hide();
	$(".AlwaysOn").hide();
	if ($("#ConnectionTrigger").val() == "Manual") {
		$(".onlyManual").show();
	} else if($("#ConnectionTrigger").val() == "OnDemand"){
		$(".onlyOnDemand").show();
	} else if ($("#ConnectionTrigger").val() == "AlwaysOn"){
		$(".AlwaysOn").show();
	} else {
		$("#ConnectionTrigger").val("AlwaysOn");
		$(".AlwaysOn").show();
	} 
}

$("#pppoeManualDial").click(function () {
	var wanid = $("#selectWan").val();
	var postData = {type:"POST",commitData:{para:{"WanName":wanid,"PppManualOperate":"Up"}}};
	postData.msgType = 213;
	postData.userTagData = 2;
	postData.path = "hbus://mdmd/editWan";
	postData.commitData.path = postData.path;
		
	hgsUpdateData(postData,function(result){
		if(IS_LOG_DATA_ENABLE()){
			LOG_DATA("server response:");
			console.log(result); 
		}
	})
})

$("#pppoeManualStop").click(function () {
	var wanid = $("#selectWan").val();
	var postData = {type:"POST",commitData:{para:{"WanName":wanid,"PppManualOperate":"Down"}}};
	postData.msgType = 213;
	postData.userTagData = 2;
	postData.path = "hbus://mdmd/editWan";
	postData.commitData.path = postData.path;
		
	hgsUpdateData(postData,function(result){
		if(IS_LOG_DATA_ENABLE()){
			LOG_DATA("server response:");
			console.log(result); 
		}
	})
})
/*------------------------------------*/
wanConnectionCfg = function(pathStr, data){
	if(IS_LOG_DATA_ENABLE()){
		console.log(pathStr)
		console.log(data)
	}

	webPara = data.commitData.para;
	jsonWanPara = {};

	jsonWanPara["WanName"] = webPara["WanName"];
	jsonWanPara["Enable"] = webPara["Enable"];

	var tmpStr = webPara["LanBind"]?webPara["LanBind"]:"";
	tmpStr += ","
	tmpStr += webPara["SSIDBind"]?webPara["SSIDBind"]:"";
	//tmpStr = tmpStr.replace(/;;/g, ";").replace(/;/g, ",").replace(/^,/g, "").replace(/,$/g, "");
	tmpStr = tmpStr.replace(/,/g, ",").replace(/^,/g, "").replace(/,$/g, "");
	jsonWanPara["LanInterface"] = tmpStr;

	if(webPara["VlanEnabled"])
	{
		if (webPara["VlanId"].indexOf('.') != -1) {
			alert("vlan id should be an integer");
			return 1;
		}		

		jsonWanPara["VLANMode"] = 2;
		if (g_staticInfo["Region"] == "Guangxi") {
			if (webPara["EncapType"] == "pppoe") {
				if (webPara["WanName"] == "create_new_wan") {
					//新建
					for (let index = 0; index < wanList.length; index++) {
						const wanitem = wanList[index];
						var nameArr = wanitem.Name.split('_');
						var lastChar = nameArr[nameArr.length-1];
						if (lastChar == parseInt(webPara["VlanId"])) {
							if (wanitem.ConnectionType.indexOf("PPPoE")>-1 ) {
								alert("There is already a PPPoE, VLAN"+webPara["VlanId"]+"WAN connection");
								return 1;
							}
						}
					}
				}
				else {
					//修改已建立wan
					//修改后，与已建立的wan是否是同样vlanid，且该wan为pppoe,把自身排除
					var editWanName = $("#selectWan option:selected").text();

					for (let index = 0; index < wanList.length; index++) {
						const wanitem = wanList[index];
						var nameArr = wanitem.Name.split('_');
						var lastChar = nameArr[nameArr.length-1];
						if (lastChar == parseInt(webPara["VlanId"]) && wanitem.ConnectionType.indexOf("PPPoE")>-1) {
							if (editWanName != wanitem.Name) {
								alert("There is already a PPPoE, VLAN"+webPara["VlanId"]+"WAN connection");
								return 1;
							}
						}
					}
				}			
			}	
		}

		jsonWanPara["VLANIDMark"] = parseInt(webPara["VlanId"]);
		jsonWanPara["802-1pMark"] = webPara["_802dot1p"];
		if(typeof webPara["MulticastVlan"] != "undefined"){
			if (webPara["MulticastVlan"].indexOf('.') != -1) {
				alert("Multicast vlan should be an integer");
				return 1;
			}		
			webPara["MulticastVlan"] = parseInt(webPara["MulticastVlan"]);	
			if((webPara["MulticastVlan"] < 0 && webPara["MulticastVlan"] != -1) || webPara["MulticastVlan"] > 4094){
				$("#HGS_WAN [hgs_key=MulticastVlan]").focus();
				alert("The legal range is 1-4094, -1 or 0 means not enabled, and other values ​​are illegal multicast VLANs!");
				return 1;
			}
			jsonWanPara["MulticastVlan"] = webPara["MulticastVlan"];
		}
		
		if(($("#ServiceList").val() != "INTERNET") && ($("#WanConnectType").val() == 'bridge')){
			jsonWanPara["LanInterface-DHCPEnable"] = 0;
		}else{
			jsonWanPara["LanInterface-DHCPEnable"] = webPara["LanInterface-DHCPEnable"];
		}
	}
	else
	{
		jsonWanPara["VLANMode"] = 0;
	}

	jsonWanPara["IPMode"] = webPara["IPVersion"];

	var strWanType = "";
	if(webPara["EncapType"] == "ipoe")
	{
		strWanType = "IP";
	}
	else
	{
		strWanType = "PPPoE";
	}

	if(webPara["ConnectType"] == "router")
	{
		strWanType += "_Routed";
		jsonWanPara["NPTv6Enable"] = webPara["NPTv6Enable"];
		if($("#ServiceList").val() == "VOIP"){
			jsonWanPara["NATEnabled"] = 0;
		}else{
			jsonWanPara["NATEnabled"] = webPara["NatEnabled"];
		}
	}
	else
	{
		strWanType += "_Bridged";
	}

	if(webPara["MTU"] < 500 && webPara["MTU"] != 0){
		alert("1-500 is an invalid MTU");
		return 1;
	}
	jsonWanPara["MTU"] = webPara["MTU"];

	jsonWanPara["ConnectionType"] = strWanType;

	if("PPPoE_Routed" == strWanType)
	{
		jsonWanPara["Username"] = webPara["UserName"];
		jsonWanPara["Password"] = webPara["UserPassword"];
		if ($(".pppoeDial").length && webPara["ServiceList"] == "INTERNET") {
			jsonWanPara["ConnectionTrigger"] = webPara["ConnectionTrigger"];
			if (webPara["ConnectionTrigger"] == "OnDemand") {
				jsonWanPara["IdleDisconnectTime"] = webPara["IdleDisconnectTime"];	
			} else if (webPara["ConnectionTrigger"] == "Manual") {
				jsonWanPara["PppManualOperate"] = "None";
			}
		}
	}

	if(webPara["ConnectType"] == "router")
	{
		if(webPara["IPv4AddrType"])
		{
			jsonWanPara["AddressingType"] = webPara["IPv4AddrType"];
		}

		if($("#ipv4AddrTypeStatic").is(':checked')){
			jsonWanPara["ExternalIPAddress"] = webPara["ExternalIPAddress"];
			jsonWanPara["SubnetMask"] = webPara["SubnetMask"];
			jsonWanPara["DefaultGateway"] = webPara["DefaultGateway"];
			jsonWanPara["DNSServers"] = webPara["DNSServers"];
		}

	}

	jsonWanPara["ServiceList"] = webPara["ServiceList"];
	if (!jsonWanPara["ServiceList"]) {
		alert("Business type cannot be empty!");
		return 1;
	}

	var arrLanInterfaces = jsonWanPara["LanInterface"].split(',');

	for (var i = 0; i < arrLanInterfaces.length; i++) {
		const element = arrLanInterfaces[i];

		if (!$.isEmptyObject(wanBindInfo[element]) && Object.keys(wanBindInfo[element])[0] == "port") {
			switch (jsonWanPara["IPMode"]) {
				case 1:
					if (!wanBindInfo[element].port[0] || wanBindInfo[element].port[0] == g_wanName) {
						continue;
					} else {
						alert(element + "Already bound, cannot be bound again!");
						return 1;
					}
					break;
				case 2:
					if (!wanBindInfo[element].port[1] || wanBindInfo[element].port[1] == g_wanName) {
						continue;
					} else {
						alert(element + "Already bound, cannot be bound again!");
						return 1;								
					}
					break;
				case 3:
					if ((wanBindInfo[element].port[0] && wanBindInfo[element].port[0] != g_wanName) || (wanBindInfo[element].port[1] && wanBindInfo[element].port[1] != g_wanName)) {
						alert(element + "Already bound, cannot be bound again!");
						return 1;
					}
					break;
				default:
					break;
			}
		}
	}

	// jsonWanPara["HgSlaveMcastEnable"] = webPara["HgSlaveMcastEnable"];
	if(jsonWanPara["IPMode"] != 1)
	{
		jsonWanPara["IPv6IPAddressOrigin"] = webPara["IPv6IPAddressOrigin"];
		if(webPara["IPv6IPAddress"]){
			jsonWanPara["IPv6IPAddress"] = $.trim(webPara["IPv6IPAddress"]);
		}
		
		if(webPara["IPv6DNSServers"]){
			var arr = webPara["IPv6DNSServers"].split(",");
			for (let k = 0; k < arr.length; k++) {
				arr[k] = $.trim(arr[k]);
			}
			
			jsonWanPara["IPv6DNSServers"] = arr.join(",");
		}
		
		jsonWanPara["IPv6PrefixDelegationEnabled"] = webPara["IPv6PrefixDelegationEnabled"];
		if(jsonWanPara["IPv6IPAddressOrigin"]  == "Static")
		{
			jsonWanPara["IPv6PrefixOrigin"] = "Static";
		}else
		{
			jsonWanPara["IPv6PrefixOrigin"] = webPara["IPv6PrefixOrigin"];
		}

		if(webPara["IPv6Prefix"]){
			jsonWanPara["IPv6Prefix"] = $.trim(webPara["IPv6Prefix"]);
		}

		if(webPara["IPv6DefaultGateway"]){
			jsonWanPara["IPv6DefaultGateway"] = $.trim(webPara["IPv6DefaultGateway"]);
		}

		jsonWanPara["IPv6DsliteEnable"] = webPara["IPv6DsliteEnable"];
		jsonWanPara["IPv6AftrMode"] = webPara["IPv6AftrMode"];
		
		if(webPara["IPv6Aftr"]){
			jsonWanPara["IPv6Aftr"] = webPara["IPv6Aftr"];
		}
	}

	for(var x in jsonWanPara){
		//delete undefine data
		if (typeof(jsonWanPara[x]) == "undefined"){
			delete jsonWanPara[x];
		}
	}

	if ($("#iptvAccount").length && 
		("IP_Routed" == strWanType) &&
		((webPara["ServiceList"] == "IPTV") || (webPara["ServiceList"] == "OTHER")))
	{
		jsonWanPara["IPTVAccount"] = $("#iptvAccount [hgs_key=iptvAccount]").val();
		jsonWanPara["IPTVPassword"] = $("#iptvAccount [hgs_key=iptvPassword]").val();
		
		if (($("#selectWan").val() != "create_new_wan"))
		{
			var iptvAccount = $("#iptvAccount [hgs_key=iptvAccount]").val();
			var iptvPassword = $("#iptvAccount [hgs_key=iptvPassword]").val();
			var nodePath = $("#iptvAccount [hgs_key=iptvAccount]").attr("fullpath");
			if (nodePath)
			{
				var path = "hbus://mdm/" + nodePath;
				var postData = {type:"POST",commitData:{para:{Type:31,Account:iptvAccount,Password:iptvPassword,Enable:1}}};
				postData.msgType = 212;
				postData.path = path;
				postData.commitData.path = postData.path;
				hgsUpdateData(postData,function(result){
					if(IS_LOG_DATA_ENABLE()){
						LOG_DATA("server response:");
						console.log(result); 
					}
				})
			}
		}
	}

	data.commitData.para = jsonWanPara;
	/* 
	setTimeout(function(){
		$("[target_page='wan_config']").click();
	}, 2000) */

	var wan_idx = $("#selectWan").val();
	var service = matchServiceNmae($("#ServiceList").val());
	var vlanid = $("#HGS_WAN [hgs_key=VlanId]").val();
	var type, newservice;

	if ($("#WanConnectType").val() == "bridge") {
		type = 'B';
	} else {
		type = 'R';
	}
	if (wan_idx != "create_new_wan") {
		newservice = wan_idx +'_' +service +'_' +type +'_VID_' +vlanid;
		$("#selectWan").find("option:selected").text(newservice);
	}
	else {
		setTimeout(function(){
			hgsUpdateData({type:"GET", url:"/wanidx"}, function (wandata) {
					var newidx = wandata.idx;
					newservice = newidx +'_' +service +'_' +type +'_VID_' +vlanid;
					$("#selectWan").append('<option value='+newidx+'>'+newservice+'</option>');
					var item = $("#selectWan option").sort(function(a,b){
						var tmpa = $(a).val();
						var tmpb = $(b).val();
						if (tmpa > tmpb) {
							return 1;
						}
						if (tmpa < tmpb) {
							return -1;
						}
						return 0;
					})
					$("#selectWan").empty();
					$("#selectWan").append(item);
					$("#selectWan").val(newidx);
			});
		}, 5000);
	}

	return 0;
}

function matchServiceNmae(ServiceList) {
	var service;
	switch (ServiceList) {
		case "INTERNET,VOIP":
			service = "VOIP_INTERNET";
			break;
		case "INTERNET,TR069":
			service = "TR069_INTERNET";
			break;
		case "TR069,VOIP":
			service = "TR069_VOIP";
			break;
		case "INTERNET,TR069,VOIP":
			service = "TR069_VOIP_INTERNET";
			break;
		case "IPTV,VOIP":
			service = "VOIP_IPTV";
			break;
		case "IPTV,TR069":
			service = "TR069_IPTV";
			break;
		case "IPTV,TR069,VOIP":
			service = "TR069_VOIP_IPTV";
			break;
		default:
			service = ServiceList;
			break;
	}

	return service;
}
/*------------------------------------*/
wanUncheckAllBindInterface = function(){
	/*
	Use querySelectorAll and querySelector. Don't use jquery selector because jquery can't 
	check or uncheck checkbox sometimes and I don't know why.
	*/
	lanBindList = document.querySelectorAll("#HGS_WAN [hgs_checked_value]");
	//console.log(lanBindList)
	for(x in lanBindList){
		lanBindList[x].checked = false;
	}
	
	if (!(isSubnetAP())){
		if (document.querySelector("#HgSlaveMcastEnable")) {
			document.querySelector("#HgSlaveMcastEnable").checked = false;	
		}
	}
}

wanUpdatePageData = function(respData){
	if(!respData["result"]){
		return;
	}
	wanConnection = respData["result"][0];
	if(!wanConnection){
		return;
	}

	webWanCon = {};

	if(IS_LOG_DATA_ENABLE()){
		console.log(respData);
		console.log(wanConnection);
	}
	

	if(!wanConnection["Name"]){
		return;
	}
	webWanCon["WanName"] = wanConnection["Name"];
	webWanCon["Enable"] = wanConnection["Enable"]?true:false;
	webWanCon["IPVersion"] = wanConnection["IPMode"];

	switch(wanConnection["ConnectionType"]){
		case "IP_Routed":
			webWanCon["EncapType"] = "ipoe";
			webWanCon["ConnectType"] = "router";
			break;
		case "PPPoE_Routed":
			webWanCon["EncapType"] = "pppoe";
			webWanCon["ConnectType"] = "router";
			break;
		case "IP_Bridged":
			webWanCon["EncapType"] = "ipoe";
			webWanCon["ConnectType"] = "bridge";
			break;
		case "PPPoE_Bridged":
			webWanCon["EncapType"] = "pppoe";
			webWanCon["ConnectType"] = "bridge";
			break;
	}

	if(!wanConnection["ServiceList"]){
		wanConnection["ServiceList"] = "INTERNET";
	}

	var ServiceList = wanConnection["ServiceList"].split(",").sort();
	webWanCon["ServiceList"] = "";
	for(x in ServiceList){
		if(x > 0){
			webWanCon["ServiceList"] += ",";
		}
		webWanCon["ServiceList"] += ServiceList[x];
	}

	if ((!g_staticInfo["SupportVoip"]) && (g_staticInfo["Region"] == "Guangxi")) {
		if (webWanCon["ServiceList"] == "INTERNET,VOIP") {
			$("#ServiceList").append('<option value="INTERNET,VOIP" class="FEATURE_VOIP">Internet + Voice</option>');
		} else {
			if ($("#ServiceList [value='INTERNET,VOIP']").length) {
				$("#ServiceList [value='INTERNET,VOIP']").remove();	
			}
		}		
	}

	if(wanConnection["VLANMode"]){
		webWanCon["VlanEnabled"] = true;
		webWanCon["VlanId"] = wanConnection["VLANIDMark"];
		webWanCon["_802dot1p"] = wanConnection["802-1pMark"].toString();
		webWanCon["MulticastVlan"] = wanConnection["MulticastVlan"];
	}else
	{
		webWanCon["VlanEnabled"] = false;
		webWanCon["_802dot1p"] = wanConnection["802-1pMark"].toString();
		webWanCon["MulticastVlan"] = wanConnection["MulticastVlan"];
	}
	webWanCon["BridgeRouterMixed"] = wanConnection["BridgeRouterMixed"];
	webWanCon["LanInterface-DHCPEnable"] = wanConnection["LanInterface-DHCPEnable"];

	webWanCon["NatEnabled"] = wanConnection["NATEnabled"]?true:false;
	webWanCon["NPTv6Enable"] = wanConnection["NPTv6Enable"]?true:false;
	

	if(wanConnection["Username"]){
		webWanCon["UserName"] = wanConnection["Username"];
	}

	if(wanConnection["Password"]){
		webWanCon["UserPassword"] = wanConnection["Password"];
	}

	if(wanConnection["ConnectionTrigger"]){
		webWanCon["ConnectionTrigger"] = wanConnection["ConnectionTrigger"];
	}

	if(wanConnection["IdleDisconnectTime"]){
		webWanCon["IdleDisconnectTime"] = wanConnection["IdleDisconnectTime"];
	}

	if(wanConnection["AddressingType"]){
		webWanCon["IPv4AddrType"] = wanConnection["AddressingType"];
	}

	if(wanConnection["IPv6IPAddressOrigin"]){
		webWanCon["IPv6IPAddressOrigin"] = wanConnection["IPv6IPAddressOrigin"];
	}else{
		webWanCon["IPv6IPAddressOrigin"] = "AutoConfigured";
	}

	if(wanConnection["IPv6IPAddress"]){
		//var IPv6AddrTmp = [];
		//IPv6AddrTmp = wanConnection["IPv6IPAddress"].split("/");
		//webWanCon["IPv6IPAddress"] = (IPv6AddrTmp.length >= 1)?IPv6AddrTmp[0]:"";
		webWanCon["IPv6IPAddress"] = wanConnection["IPv6IPAddress"];
	}else{
		webWanCon["IPv6IPAddress"] = "";
	}

	if(wanConnection["IPv6DNSServers"]){
		webWanCon["IPv6DNSServers"] = wanConnection["IPv6DNSServers"];
	}else{
		webWanCon["IPv6DNSServers"] = "";
	}

	if(wanConnection["IPv6PrefixDelegationEnabled"]){
		webWanCon["IPv6PrefixDelegationEnabled"] = wanConnection["IPv6PrefixDelegationEnabled"];
	}else{
		webWanCon["IPv6PrefixDelegationEnabled"] = false;
	}

	if(wanConnection["IPv6PrefixOrigin"]){
		webWanCon["IPv6PrefixOrigin"] = wanConnection["IPv6PrefixOrigin"];
	}else{
		webWanCon["IPv6PrefixOrigin"] = "PrefixDelegation";
	}

	if(wanConnection["IPv6Prefix"]){
		webWanCon["IPv6Prefix"] = wanConnection["IPv6Prefix"];
	}else{
		webWanCon["IPv6Prefix"] = "";
	}

	if(wanConnection["IPv6DefaultGateway"]){
		webWanCon["IPv6DefaultGateway"] = wanConnection["IPv6DefaultGateway"];
	}else{
		webWanCon["IPv6DefaultGateway"] = "";
	}

	webWanCon["IPv6DsliteEnable"] = wanConnection["IPv6DsliteEnable"]?true:false;
	if(wanConnection["IPv6AftrMode"]){
		webWanCon["IPv6AftrMode"] = wanConnection["IPv6AftrMode"];
	}

	if(wanConnection["IPv6Aftr"]){
		webWanCon["IPv6Aftr"] = wanConnection["IPv6Aftr"];
	}

	if(wanConnection["AddressingType"]){
		webWanCon["IPv4AddrType"] = wanConnection["AddressingType"];
	}
	if(wanConnection["ExternalIPAddress"]){
		webWanCon["ExternalIPAddress"] = wanConnection["ExternalIPAddress"];
	}
	if(wanConnection["SubnetMask"]){
		webWanCon["SubnetMask"] = wanConnection["SubnetMask"];
	}
	if(wanConnection["DefaultGateway"]){
		webWanCon["DefaultGateway"] = wanConnection["DefaultGateway"];
	}


	if(wanConnection["DNSServers"]){
		var dnsServerTmp = [];
		dnsServerTmp = wanConnection["DNSServers"].split(",");
		webWanCon["DNSServers"] = wanConnection["DNSServers"];
		if(dnsServerTmp.length == 2){
			if(dnsServerTmp[1] == "0.0.0.0"){
				webWanCon["DNSServers"] =dnsServerTmp[0];
			}
		}
	}


	if(wanConnection["MTU"]){
		webWanCon["MTU"] = wanConnection["MTU"];
	}

	// webWanCon["HgSlaveMcastEnable"] = wanConnection["HgSlaveMcastEnable"];
	
	if(IS_LOG_DATA_ENABLE()){
		console.log(webWanCon);
	}

	objData = {objName:"HGS_WAN", noCheckout:true}
	loadHbusRespData(webWanCon, objData);

	//wanConnection["LanInterface"] = "LAN1,LAN2,LAN3,SSID1,SSID2"
	var LanInterfaceList = wanConnection["LanInterface"].split(",");

	wanUncheckAllBindInterface();

	hgsUpdateData({type:"GET",url:"/wanBindInfo"}, function (data) {
		if (g_wanParaDisabled) {
			for(x in LanInterfaceList){
				if(LanInterfaceList[x]){
					document.querySelector("#HGS_WAN [hgs_checked_value='" + LanInterfaceList[x] + "']").checked = true;
				}
			}
		}
		else {
			wanBindInfo = data;
			var lanObj;
			for (const k in data) {
				lanObj = document.querySelector("#HGS_WAN [hgs_checked_value='" + k + "']");
				if(!lanObj){
					continue;
				}
				if ($.isEmptyObject(data[k])) {
					lanObj.removeAttribute("disabled");
				} else {
					if (Object.keys(data[k]).length) {
						// 端口绑定了ipv,ipv6或绑定了vlan/vxlan
						lanObj.setAttribute("disabled",true);
						if (Object.keys(data[k])[0] == 'port') {
							if (!data[k].port[0] || !data[k].port[1]) {
								// 端口未同时绑定了ipv,ipv6
								lanObj.removeAttribute("disabled");
							}
						}
					}
				}
			}
	
			for(x in LanInterfaceList){
				if(LanInterfaceList[x]){
					document.querySelector("#HGS_WAN [hgs_checked_value='" + LanInterfaceList[x] + "']").checked = true;
					document.querySelector("#HGS_WAN [hgs_checked_value='" + LanInterfaceList[x] + "']").removeAttribute("disabled");
				}
			}
		}
	})

	if (!(isSubnetAP())) {
		var path = "hbus://mdm/InternetGatewayDevice.WANDevice.{i}.WANConnectionDevice.{i}.WANIPConnection.{i}.";
		var getData = {type:"GET",
					path:path, 
					msgType:211, 
					userTagData:1};
		var flag = false;	
		var iptvobj = {}, iptvAccount = false;

		if ($("#iptvAccount").length) {
			iptvAccount = true;
		}	

		hgsUpdateData(getData, function (data) {
		for (const k in data) {
			if ( document.querySelector("#HgSlaveMcastEnable") && parseInt(data[k].HgSlaveMcastEnable) ) {
				ponBind = true;
				flag = true;
				document.querySelector("#HgSlaveMcastEnable").setAttribute("disabled",true);
				document.querySelector("#HgSlaveMcastEnable").checked = true;
				if (data[k].Name == webWanCon["WanName"]) {
					document.querySelector("#HgSlaveMcastEnable").removeAttribute("disabled");
				} else {
					document.querySelector("#HgSlaveMcastEnable").checked = false;
				}
			}

			if (iptvAccount) {
				if (((data[k].Name.indexOf("IPTV") > -1) || (data[k].Name.indexOf("OTHER") > -1)) && 
					(data[k].Name == wanConnection["Name"]) &&
					(data[k].ConnectionType == "IP_Routed")) {
					iptvobj.Name = data[k].Name;
					iptvobj.fullPath = data[k].fullPath;
				}	
			}
		}

		if (!flag) {
			ponBind = false;
		}

		if (iptvAccount){
			var path = "hbus://mdm/InternetGatewayDevice.WANDevice.{i}.WANConnectionDevice.{i}.WANIPConnection.{i}.X_CMCC_DHCPOPTION60.{i}.";
			var getData = {type:"GET",
						path:path, 
						msgType:211, 
						userTagData:1};
			
			if (!$.isEmptyObject(iptvobj)) {
				hgsUpdateData(getData, function (iptvdata) {
					$("#iptvAccount").hide();
					$("#iptvAccount [hgs_key=iptvAccount]").attr("fullpath","");
					if (iptvdata.length > 0) {
						for (const k in iptvdata) { 
							if (iptvdata[k].fullPath.indexOf(iptvobj.fullPath) > -1) {
								$("#iptvAccount").show();
								$("#iptvAccount [hgs_key=iptvAccount]").val(iptvdata[k].Account);
								$("#iptvAccount [hgs_key=iptvPassword]").val(iptvdata[k].Password);
								$("#iptvAccount [hgs_key=iptvAccount]").attr("fullpath",iptvdata[k].fullPath);
								break;
							}
						}	
					}
				})
			}else{
				$("#iptvAccount").hide();
				$("#iptvAccount [hgs_key=iptvAccount]").attr("fullpath","");
			}
		}
							
		})	
	}

	wanModeChange();
}

/*------------------------------------*/

$('[hgs_submit_div_id="HGS_WAN"]').click(function () {
	$('[hgs_submit_div_id="HGS_WAN"]').attr("disabled",true);

	setTimeout(function() {
		$('[hgs_submit_div_id="HGS_WAN"]').attr("disabled",true);
	}, 500);

	setTimeout(function() {
		$('[hgs_submit_div_id="HGS_WAN"]').attr("disabled",false);
	}, 5000);
})

wanInfoByIdx = function(wanIndex){
	data = {type:"POST", path:"hbus://mdmd/getWan", msgType:213, userTagData:3, waitTimeoutMs:10000,
	extraPara:"wanIndex=" + wanIndex,
	commitData:{
			cmdType: "wanConnection",
			para: {
				wanIndex: [wanIndex]
			}
		}
	};

	if(IS_LOG_DATA_ENABLE()){
		console.log(data);
	}
	hgsUpdateData(data, wanUpdatePageData)
}

var wanList;
wanCheckout = function(data){
	if(IS_LOG_DATA_ENABLE()){
		console.log(data);
	}
	if(200 != data.retCode){
		return;
	}
	wanList = data.result;
	if(!wanList){
		return;
	}
	wanList.sort(strategies.sortBy("Index"));
	var filteredArray;
	if ((!g_staticInfo["SupportVoip"]) && (g_staticInfo["Region"] == "Henan" || g_staticInfo["Region"] == "Anhui" || g_staticInfo["Region"] == "Zhejiang")) {
		filteredArray = wanList.filter(item => !item.Name.includes("VOIP"));
		wanList = filteredArray;
	} 
	else if (g_staticInfo["Region"] =="Beijing" || g_staticInfo["Region"] == "Jiangsu" || g_staticInfo["Region"] == "JiangsuJK") {
		if (!g_adminAccount) {
			filteredArray = wanList.filter(item => (item.Name.includes("INTERNET")&&(!item.Name.includes("VOIP"))&&(!item.Name.includes("TR069"))));
			wanList = filteredArray;
		}
	}

	var innerHtml = "";
	var count = 0;
	for(n in wanList){
		innerHtml += '<option value="' + wanList[n].Index +  '" >'+ wanList[n].Name + '</option>'
		count++;
	}

	innerHtml += '<option value="create_new_wan" >Create a new WAN connection</option>'
	$("#selectWan").html(innerHtml);

	if(count > 0){
		var index = 0;

		index = wanList[0].Index;
		$("#selectWan").val(index);	
		g_wanName = $("#selectWan").find("option:selected").text();
		$("#selectWan").trigger("change.foo");//Trigger listening function in hgs_customer.js 
		wanInfoByIdx(index);
	}else{
		ponBind = false;
		wanBindInfo = {};
		g_wanName = 'create_new_wan';
		createNewWan();
	}

	$('[hgs_submit_div_id="HGS_WAN"]').attr("disabled",false);
}

wanIpv4InfoCheckout = function(data){
	var result = [];
	var DNSServers = [];

	for(x in data.result){
		data.result[x].link = "ETH";
		if (isSubnetAP()) {
			if (data.result[x].ServiceList != 'INTERNET') {
				continue;	
			}
		}
		if ((!g_staticInfo["SupportVoip"]) && (g_staticInfo["Region"] == "Henan" || g_staticInfo["Region"] == "Anhui" || g_staticInfo["Region"] == "Zhejiang")) {
			if (data.result[x].ServiceList.indexOf("VOIP") > -1) {
				continue;
			}
		}
		if (!g_adminAccount) {
			if (g_staticInfo["Region"] =="Jiangxi") {
				if (data.result[x].ServiceList.indexOf("TR069") > -1) {
					continue;
				}
			}
		}
		data.result[x].ExternalIPAddress = (data.result[x].ExternalIPAddress == "0.0.0.0")?"":data.result[x].ExternalIPAddress;
		if (data.result[x].ExternalIPAddress) {
			if (data.result[x].SubnetMask) {
				data.result[x].SubnetMask = (data.result[x].SubnetMask == "0.0.0.0")?"":data.result[x].SubnetMask;	
			}else{
				data.result[x].SubnetMask = "255.255.255.255";
			}
		} else {
			data.result[x].SubnetMask = "";
		}
		
		data.result[x].DefaultGateway = (data.result[x].DefaultGateway == "0.0.0.0")?"":data.result[x].DefaultGateway;
		
		data.result[x].MACAddress = data.result[x].MACAddress.toUpperCase();
		if (data.result[x].AddressingType == "" && data.result[x].ConnectionType == "PPPoE_Routed") {
			data.result[x].AddressingType = "PPPoE";
		}
		else if (data.result[x].ConnectionType.indexOf("Bridged") > -1) {
			data.result[x].AddressingType = "";
		}

		if (data.result[x].ConnectionStatus == "Connected") {
			data.result[x].LastConnectionError = "ERROR_NONE";
		}
		
		if(data.result[x].IPMode != 2){
			
			DNSServers = data.result[x].DNSServers.split(",");
			if(DNSServers.length >=2)
			{
				data.result[x].MainDns = (DNSServers[0] == "0.0.0.0")?"":DNSServers[0];
				data.result[x].BackupDns = (DNSServers[1] == "0.0.0.0")?"":DNSServers[1];
			}else if(DNSServers.length == 1)
			{
				data.result[x].MainDns = (DNSServers[0] == "0.0.0.0")?"":DNSServers[0];
				data.result[x].BackupDns = "";
			}else
			{
				data.result[x].MainDns = "";
				data.result[x].BackupDns = "";
			}
			result.push(data.result[x]);
		}
	}

	result.sort(strategies.sortBy('Name'));	
	return result;
}

wanIpv6InfoCheckout = function(data){
	var result = [];
	var IPv6IPAddress = [];
	var DNSServers = [];

	for(x in data.result){
		if (isSubnetAP()) {
			if (data.result[x].ServiceList != 'INTERNET') {
				continue;	
			}
		}
		if ((!g_staticInfo["SupportVoip"]) && (g_staticInfo["Region"] == "Henan" || g_staticInfo["Region"] == "Anhui" || g_staticInfo["Region"] == "Zhejiang")) {
			if (data.result[x].ServiceList.indexOf("VOIP") > -1) {
				continue;
			}
		}
		if (!g_adminAccount) {
			if (g_staticInfo["Region"] =="Jiangxi") {
				if (data.result[x].ServiceList.indexOf("TR069") > -1) {
					continue;
				}
			}
		}
		if(data.result[x].ConnectionType == "IP_Bridged" || data.result[x].ConnectionType == "PPPoE_Bridged" )
		{
			data.result[x].IPv6IPAddressOrigin = ""; 
			data.result[x].IPv6DsliteEnable  = "";
		}else
		{
			data.result[x].IPv6DsliteEnable = (data.result[x].IPv6DsliteEnable == 1)?"yes":"no";
			DNSServers = data.result[x].IPv6DNSServers.split(",");
			data.result[x].IPv6MainDns = (DNSServers.length >= 1)?DNSServers[0]:"";
			data.result[x].IPv6BackupDns = (DNSServers.length >= 2)?DNSServers[1]:"";
		}
		//IPv6IPAddress = data.result[x].IPv6IPAddress.split("/");
		//data.result[x].IPv6IPAddress = (IPv6IPAddress.length >= 1)?IPv6IPAddress[0]:"";
		if (data.result[x].ConnectionStatus == "Connected") {
			data.result[x].LastConnectionError = "ERROR_NONE";
		}

		if(data.result[x].IPMode != 1){
			result.push(data.result[x]);
		}
	}
	return result;
}

wanIpv4InfoFullShow = function(data){
	$('#ipv4WanInfoPopDlg').dialog('open');
	loadTableData("HGST_IPV4_FULL_INFO");
}
wanIpv6InfoFullShow = function(data){
	$('#ipv6WanInfoPopDlg').dialog('open');
	loadTableData("HGST_IPV6_FULL_INFO");
}

/*------------------------------------*/
wanConnectionDelete = function(objName){
	wanIdx = parseInt($("#selectWan").val());

	data = {type:"POST", path:"hbus://mdmd/editWan", msgType:213, userTagData:4, waitTimeoutMs:5000,
		extraPara:"wanIndex=" + wanIdx,
		commitData:{
			cmdType: "wanConnection",
			para: {
				wanIndex: [wanIdx]
			}
		}
	};

	if(IS_LOG_DATA_ENABLE()){
		console.log(data);
	}
	
	hgsUpdateData(data)

	setTimeout(function(){
		$("[target_page='wan_config']").click();
	}, 1000)
}

/*------------------------------------*/
/*----------------------------------------------------------------------------*/
var uplinkway;
uplinkCheckout = function (data) {
	$.get("/uplink?action=get", function (data) {
		uplinkway = data.AccessType;
		$("#selectAccessType").val(data.AccessType);
	})
}

uplinkCheckin = function(data) {
	var flag = false;
	if (data.AccessType != "GBE"&& uplinkway == "GBE") {
		//lan上行
		if(confirm("LAN uplink switched to optical uplink, and will be restarted to take effect! Are you sure to [restart the device]?")){
			flag = true;
		}
	} else if (data.AccessType=="GBE"&& uplinkway != "GBE"){
		//GPON上行
		// if(confirm("Switch the optical uplink to LAN uplink, and the management address will be changed to 192.168.5.1, which will take effect after restart! Are you sure to [restart the device]?")){
		if(confirm("The optical uplink is switched to LAN uplink, and the reboot will take effect! After the reboot, the LAN side address will be changed to 192.168.100.1! Are you sure to [restart the device]?")){
			flag = true;
		}
	} else if (data.AccessType != uplinkway) {
		flag = true;
	}

	if (flag) {
		pathStr = "/uplink?action=set&type="+data.AccessType
		$.get(pathStr, function () {
			
		})
	}
	return;
}
/*----------------------------------------------------------------------------*/

agentIPTVBindUpdate = function () {
	loadTableData("HGST_AGENT_IPTV_BIND");
}

bindInterfaceLoadSuccess = function (params) {
	var tableId = getTableIdByHgstId(id);
	$('#'+tableId).datagrid({
		onBeginEdit: function(index, row){
			var ed = $(this).datagrid('getEditor', {index: index, field: 'bindInterface'});
			var bindInterface = $(this).datagrid("getRows")[index].bindInterface;
			var flag = false;
			
			if (ed){
				var combobox = $(ed.target).combobox({
					onChange: function(newValue, oldValue){
						flag = false;
						for (let i = 0; i < newValue.length; i++) {
							switch (newValue[i]) {
								case '1':
									if(row.subInterface == "eth0"){
										flag = true;
									}
									break;
								case '2':
									if(row.subInterface == "eth1"){
										flag = true;
									}
									break;
							}

							if (flag) {
								break;
							}
						}
						
						if (flag) {
							alert("The binding port cannot be the optical router wired port!");
							$(ed.target).combobox("setValue",oldValue);
						}
					}
				});
				
				bindInterface = bindInterface.split(',');
				$(ed.target).combobox("setValue",bindInterface);
			}
		}
	});	
	
}

agentIPTVBindCheckout = function(data) {
	var jsonBindData = data.bindData;
	var jsonOnlineDev = data.onlineDevs;
	var jsonMeshAgentInfo = data.meshAgenInfo;
	var resultArray = [];
	var bindif = 0;
	
	$.each(jsonBindData, function(key, value) {
		if (value == 3) {
			bindif = "1,2"
		}else{
			bindif = value.toString();
		}

		for (let i = 0; i < jsonOnlineDev.length; i++) {
			if (jsonOnlineDev[i].mac == key) {
				$.each(jsonMeshAgentInfo,function (agentkey, agentvalue) {
					if (agentkey == jsonOnlineDev[i].mac) {
						
						var newObj = {
							"mac": key,
							"bindInterface": bindif,
							"interface": jsonOnlineDev[i].if,
							"subInterface": agentvalue.ifname
						};	
						resultArray.push(newObj);
						return false;
					}
				});
				break;
				
			}
		}
	});

	return resultArray;
}
agentIPTVBindCheckin = function (objName, tableId, data, postData) {
	var arrData = [];
	for (const obj of data) {
		ifarr = obj.bindInterface.split(',')
		if (ifarr.length > 1) {
			obj.bindInterface = parseInt(ifarr[0]) + parseInt(ifarr[1]);
		}
		const newObj = {};
		newObj[obj.mac] = parseInt(obj.bindInterface);
		arrData.push(newObj);
	}
	
	const result = $.extend({}, ...arrData);
	
	postData.type = "POST";
	postData.url = "/agentIPTVBind?action=set";
	postData.commitData = result;
	
	setTimeout(agentIPTVBindUpdate, 2000);
}
/*----------------------------------------------------------------------------*/

ItmsCfg  = function(pathStr, data){
	setTimeout(function(){
		// data = {type:"GET", path:"hbus://tr069/inform", msgType:214, userTagData:2, waitTimeoutMs:50000};
		// hgsUpdateData(data)
		$("[hgs_sub_nav='platform_server']").click();
	}, 2000)	
}

ItmsCheckout = function(pathStr){
	document.querySelector("#PeriodicEnabled").checked = Number(pathStr["PeriodicInformEnable"]);
	//document.querySelector("#ConnectionEnabled").checked = Number(pathStr["ConnectionRequestAuthentication"]);
	if (pathStr["URL1"] && pathStr["URL2"]) {
		$("#RemoteManageURL").empty();
		var innerHtml = "<select hgs_key='URL'>";
		innerHtml += "<option value='" + pathStr["URL1"]  + "' >" + pathStr["URL1"] + "</option>";
		innerHtml += "<option value='" + pathStr["URL2"]  + "' >" + pathStr["URL2"] + "</option></select>";
		$("#RemoteManageURL").html(innerHtml);	
		$("#RemoteManageURL select").val(pathStr["URL"]);
	}
}

informStatusCfg = function(pathStr, jsonData){
	if(IS_LOG_DATA_ENABLE()){
		console.log(pathStr)
		console.log(jsonData)
	}
	
	var currentDate = new Date().toLocaleDateString(); 
		$("span[hgs_key='Status']").each(function() { 
		$(this).text("Reporting"); 
	}); 

	setTimeout(function(){
		// data = {type:"GET", path:"hbus://tr069/inform", msgType:214, userTagData:2, waitTimeoutMs:50000};
		// if(IS_LOG_DATA_ENABLE()){
		// 	console.log(data);
		// }
		// hgsUpdateData(data)
		$("[hgs_sub_nav='acs_link_info']").click();
	}, 2000)
}

var timer_inform;
function informStu(value) {
	var InformStatus = parseInt(value["InformStatus"]);
	var ConnectStatus = parseInt(value["ConnectStatus"]);

	if (0 == InformStatus) {
		value["InformStatus"] = "Report successfully";
	}	
	else if (3 == InformStatus) {
		value["InformStatus"] = "Reporting process interrupted";
	}
	else if (2 == InformStatus) {
		value["InformStatus"] = "Report no response";
	}
	else
	{
		value["InformStatus"] =  "Not reported";
	}

	if (1 == ConnectStatus)
	{
		value["ConnectStatus"] =  "The remote connection process initiated by RMS is successful";
	}
	else if (3 == ConnectStatus)
	{
		value["ConnectStatus"] =  "The remote connection process initiated by RMS is interrupted";
	}
	else
	{
		value["ConnectStatus"] =  "No remote connection request received";
	}	
}
informCheckout = function(value){
	if(IS_LOG_DATA_ENABLE()){
		console.log(value);
	}
	
	informStu(value);
	objData = {objName:"HGS_ITMS", noCheckout:true}
	loadHbusRespData(value, objData);

	timer_inform = setInterval(function(){
		var selectStr = "[hgs_sub_target='inter_connec_esatablish']" + ":visible";
		var elements = $(selectStr);
		var data = {type:"GET",
					path:"hbus://mdm/InternetGatewayDevice.ManagementServer.X_HG_RemoteStatus.", 
					msgType:211, 
					userTagData:1};
					
		if (elements.length) {
			hgsUpdateData(data, function (value) {
				informStu(value[0]);
				objData = {objName:"HGS_ITMS", noCheckout:true}
				loadHbusRespData(value[0], objData);
			})
		} else {
			clearInterval(timer_inform);
		}
	}, 1000)
}
	
informSelfCheckout = function(value){
	if(IS_LOG_DATA_ENABLE()){
		console.log(value);
	}
	
	var informStu = parseInt(value["InformStatus"]);
	var conStu = parseInt(value["ConnectStatus"]);
	if (0 == informStu) {
		value["Status"] = "Report successfully";
	}	
	else if (3 == informStu) {
		value["Status"] = "Reporting process interrupted";
	}
	else if (2 == informStu) {
		value["Status"] = "Report no response";
	}
	else
	{
		value["Status"] =  "Not reported";
	}

	if (1 == conStu)
	{
		value["ConnectStatus"] =  "The remote connection process initiated by RMS is successful";
	}
	else if (3 == conStu)
	{
		value["ConnectStatus"] =  "The remote connection process initiated by RMS is interrupted";
	}
	else
	{
		value["ConnectStatus"] =  "No remote connection request received";
	}

	// objData = {objName:"HGS_ITMS", noCheckout:true}
	// loadHbusRespData(value, objData);
	objData = {objName:"HGS_INFORM", noCheckout:true}
	loadHbusRespData(value, objData);
	// return value;
}

var timer_acs;
function acsStu(value) {
	var result = parseInt(value["Result"]);

    if (0 == result)
    {
        value["Result"] =  "Indicates that the business has started to be issued";
    }
    else if (1 == result)
    {
        value["Result"] =  "Business issued successfully";
    }
    else if (2 == result)
    {
        value["Result"] =  "Service delivery failed";
    }
    else
    {
        value["Result"] =  "No business is issued";
    }	
}	
resultToInfo = function(value){
	if(IS_LOG_DATA_ENABLE()){
		console.log(value);
	}
	
	acsStu(value);
	objData = {objName:"HGS_ACS_SETUP", noCheckout:true}
	loadHbusRespData(value, objData);

	timer_acs = setInterval(function(){
		var selectStr = "[hgs_sub_target='bussiness_cfg_status']" + ":visible";
		var elements = $(selectStr);
		var data = {type:"GET",
					path:"hbus://mdm/InternetGatewayDevice.X_CMCC_UserInfo.", 
					msgType:211, 
					userTagData:1};
					
		if (elements.length) {
			hgsUpdateData(data, function (value) {
				acsStu(value[0]);
				objData = {objName:"HGS_ACS_SETUP", noCheckout:true}
				loadHbusRespData(value[0], objData);
			})
		} else {
			clearInterval(timer_acs);
		}
	}, 1000)
}
/*----------------------------------------------------------------------------*/
ftpEnableCheck = function(){
	if($("#FtpEnable").is(":checked")){
		$("#ftpAccount").show();
	}else{
		$("#ftpAccount").hide();
	}
	resizeSubNavContentHeight();
}

$("#FtpEnable").click(function(){
	ftpEnableCheck();
})

FTPCfgCheckIn = function (data) {
	if (data.FtpEnable) {
		if (isValidLoginPasswd(data.FtpPassword) == false) {
			alert('[Login password] must contain letters, numbers and special characters, without spaces!');
			return true;
		}
		
		data.FtpPassword = processSpecialChars(data.FtpPassword);		
	}

	return data;
}
FTPCfgCheckout = function (data) {
	ftpEnableCheck();
}
/*----------------------------------------------------------------------------*/
bucpeDevInfoCheckout = function (data) {
	var objData = {};
	
	objData = data.deviceinfo;
	objData.UUID = data.UUID;

	return objData;
}

bucpeGisCheckout = function (data) {
	var objData = {};
	
	objData = data.deviceinfo;
	objData.appStatus = "set";
	return objData;
}

bucpeIfnameCheckout = function name(data) {
	var objData = {};
	for (var i = 0; i < data.length; i++) {
		const obj = data[i];
		if (data[i].X_CMCC_ServiceList == "INTERNET")
		{
			objData.wanIfname      = data[i].Ifname;
			objData.wanMac         = data[i].MACAddress;
			objData.wanIp          = data[i].ExternalIPAddress;
			objData.wanIfnameP2pIp = data[i].DefaultGateway;
			if (data[i].MaxMTUSize) {
				objData.wanIfnameMtu = data[i].MaxMTUSize;
			} else {
				objData.wanIfnameMtu = data[i].MaxMRUSize;
			}
			objData.wanIpMask      = data[i].SubnetMask;
			objData.firstDns = data[i].DNSServers.split(",")[0];
			objData.secendDns = data[i].DNSServers.split(",")[1];
		}
		else if (obj.fullPath.indexOf("LANHostConfigManagement") > -1)
		{
			// objData.lanDstIp       = "192.168.1.1"
			objData.lanGw          = g_staticInfo["LanIpv4Addr"];
			objData.lanMask        = data[i].SubnetMask;
			objData.lanRoute       = "UG";
			objData.lanMetric      = 1;
			objData.lanRotueNext   = "br0";
		}
	}

	var getData = {type:"GET",
				path:"hbus://miscd/getBucpe", 
				msgType:237, 
				userTagData:1};
	hgsUpdateData(getData, function (data) {
		console.log(data.ServerIp);
		$("#HGS_BUCPE_IFNAME [hgs_key='lanDstIp']").text(data.ServerIp);
	})
	
	return objData;
}

bucpeDelete = function(){
	var paths = "";
	var postData = {type:"POST", url:"/delObjs", waitTimeoutMs:5000, notJson:true, commitData:""};
	var getData = {type:"GET",
				path:"hbus://mdm/InternetGatewayDevice.Coordinate.{i}.", 
				msgType:211, 
				userTagData:1};
				
	hgsUpdateData(getData, function (data) {
		for (var i = 0; i < data.length; i++) {
			if (paths == "") {
				paths = data[i].fullPath;
			} else {
				paths += ';' + data[i].fullPath;
			}
		}	

		postData.commitData = paths;
		hgsUpdateData(postData,function(result){
			if(0 == result[0]){
				loadHbusData("HGS_BUCPE");
			}else{
				alert("Clear failed! Error code:" + result[0]);
			}
		})
	})
}
/*----------------------------------------------------------------------------*/
addVlanBind = function(){
	var id = "HGST_VLAN_BIND";
	var tableId = getTableIdByHgstId(id);

	$('#' + tableId).datagrid('appendRow',{
		lanSidePort:"eth1",
		lanSideVlan:"999",
		wanIfName: "1_INTERNET_R_VID_6"
	});

	adjustTableProfile(id);
	adjustTableHeight(id);

	return;
}
/*------------------------------------*/
delVlanBind = function(){
	var id = "HGST_VLAN_BIND";
	var tableId = getTableIdByHgstId(id);

	tableCheckData = $("#" + tableId).datagrid('getChecked');
	var index = $("#" + tableId).datagrid('getRowIndex', $("#" + tableId).datagrid('getSelected'));

	while(-1 != index){
		$("#" + tableId).datagrid('deleteRow', index);
		index = $("#" + tableId).datagrid('getRowIndex', $("#" + tableId).datagrid('getSelected'));
	}
	adjustTableProfile(id);
	adjustTableHeight(id);
}

vlanbindUpdate = function(){
	loadTableData("HGST_VLAN_BIND");
}
/*------------------------------------*/
vlanBindCheckout = function (data) {
	for (var index = 0; index < data.length; index++) {
		if (data[index].mode == "0") {
			data[index].vlanBind = "";
		}
	}

	if (!g_staticInfo["SupportWifi"]) {
		var arr = [];
		for (var i = 0; i < data.length; i++) {
			if (data[i].port.indexOf("SSID") == -1) {
				arr.push(data[i]);
			}	
		}
		return arr;	
	} else {
		if (g_staticInfo["Region"] =="Sichuan") {
			var arr = [];
			for (var i = 0; i < data.length; i++) {
				if (data[i].port.indexOf("SSID") == -1) {
					arr.push(data[i]);
				} else {
					if (data[i].port.indexOf("SSID1") == 0 || data[i].port.indexOf("SSID5") == 0) {
						arr.push(data[i]);
					}
				}
			}
			return arr;
		} else {
			return data;
		}
	}
}

vlanBindCheckin = function(objName, tableId, data){
	var dg = $("#" + getTableIdByHgstId("HGST_VLAN_BIND"));

	dg.datagrid('unselectAll');
	for(row in data){
		vlanBindList = data[row].vlanBind.replace(/，/g, ",").trim().split(",");
		newVlanBindList = "";
		for(n in vlanBindList){
			if(!vlanBindList[n].length){
				continue;
			}
			if(data[row].mode == 0){
				dg.datagrid('selectRow', row);
				setTimeout(vlanbindUpdate, 1000);
				alert(data[row].port + "When [Port Binding] is selected in [Binding Mode], the VLAN binding parameters cannot be set."" + data[row].vlanBind +"\" !请清空!");
				return true;
			}
			vlans = vlanBindList[n].trim().split("/");
			if(2 != vlans.length){
				dg.datagrid('selectRow', row);
				setTimeout(vlanbindUpdate, 1000);
				alert(data[row].vlanBind + "Is an invalid parameter!");
				return true;
			}

			for(i in vlans){
				vlan = parseInt(vlans[i]);

				if(vlan < 1 || vlan > 4094){
					dg.datagrid('selectRow', row);
					setTimeout(vlanbindUpdate, 1000);
					alert(vlan + "Is an invalid VLAN value, the VLAN value must be between [1-4094]!");
					return true;
				}

				vlans[i] = vlan;
			}

			newVlanBindList += vlans[0] + "/" + vlans[1] + ",";
		}
		data[row].vlanBind = newVlanBindList.replace(/,$/, "");;
	}
	
	setTimeout(vlanbindUpdate, 1000);
}

vlanBindonLoadSuccess = function(Data){
	var dg = $("#" + getTableIdByHgstId("HGST_VLAN_BIND"));
	
	hgsUpdateData({type:"GET",url:"/wanBindInfo"}, function (data) {
		for (var i = 0; i < Data.rows.length; i++) {
			if (Data.rows[i].vlanBind != '') {
				continue;
			}
			if (!$.isEmptyObject(data[Data.rows[i].port])) {
				var vb = dg.datagrid("getEditor", {index:i, field:"vlanBind"});
				$(vb.target).textbox({prompt:"The port has been bound!"});
				$(vb.target).textbox("readonly",true);				
			}
		}
	})
}
/*----------------------------------------------------------------------------*/

vxLanCfgChangeHandle = function(){
	if($("#VxLanWorkMode").val() == "1"){
		$("#VxLanL3Div").hide();
	}else{
		$("#VxLanL3Div").show();
	}

	if($("#VxLanVlanEnable").is(':checked')){
		$("#vxLanVlanIdDiv").show();
	}else{
		$("#vxLanVlanIdDiv").hide();
	}

	if($("#vxLanAddrTypeStatic").is(':checked')){
		$("#vxLanStaticIp").show();
	}else{
		$("#vxLanStaticIp").hide();
	}

	resizeSubNavContentHeight();
}

vxLanCfgInit = function(){
	$("#VxLanWorkMode").val("1");

	document.querySelector("#vxLanAddrTypeDhcp").checked = true;
	document.querySelector("#HGS_VXLAN [hgs_key=NATEnabled]").checked = true;
	document.querySelector("#VxLanVlanEnable").checked = true;
	vxLanCfgChangeHandle();
}

vxLanCfgInit();

$(".vxLanCfgChange").change(function(){
	vxLanCfgChangeHandle();
})

vxLanCreate = function(){
	$("#" + getTableIdByHgstId("HGST_VXLAN")).datagrid('unselectAll');

	var data = {
		TunnelKey: "",
		Enable: 1,
		TunnelRemoteIp: "",
		WorkMode: 1,
		MaxMTUSize: "",
		IPAddress: "",
		SubnetMask: "",
		AddressingType: "DHCP",
		NATEnabled: 1,
		DNSServers_Master: "",
		DNSServers_Slave: "",
		DefaultGateway: "",
		X_CMCC_VLANEnable: 1,
		X_CMCC_VLAN: "",
		X_CMCC_LanInterface: "",
		X_CMCC_WANInterface: "",
		Name: ""
	}
				
	hgsUpdateData({type:"GET",url:"/wanBindInfo"}, function (data) {
			var lanObj;

			for (const k in data) {
				lanObj = document.querySelector("#HGS_VXLAN #VXLAN_" + k);
				if(!lanObj){
					continue;
				}
				if ($.isEmptyObject(data[k])) {
					lanObj.removeAttribute("disabled");
				} else {
					lanObj.setAttribute("disabled",true);
				}
			}
			loadHbusRespData(data, {objName:"HGS_VXLAN"});
			vxLanCfgChangeHandle();
	})

	$('[hgs_submit_div_id="HGS_VXLAN"]').attr("disabled", false);
}

vxLanDelete = function(){
	var id = "HGST_VXLAN";
	var tableId = getTableIdByHgstId(id);

	selectRowData = $("#" + tableId).datagrid('getSelections');
	if(selectRowData.length == 0){
		alert("Please select a line and then delete it!");
		return;
	}

	var path = "hbus://mdm/" + selectRowData[0].fullPath;

	data = {type:"POST", msgType:216, 
		path:path, commitData:{path:path}}

	if(IS_LOG_DATA_ENABLE()){
		console.log(data)
	}

	hgsUpdateData(data,function(result){
		if(IS_LOG_DATA_ENABLE()){
			console.log("server response:");
			console.log(result);                   
		}
		vxLanUpdate();
		$("#" + getTableIdByHgstId("HGST_VXLAN")).datagrid('unselectAll');
	})

	vxLanCreate();
	$('[hgs_submit_div_id="HGS_VXLAN"]').attr("disabled", true);
}

vxLanUpdate = function(){
	loadTableData("HGST_VXLAN");
	vxLanCreate();
	$('[hgs_submit_div_id="HGS_VXLAN"]').attr("disabled", true);
}

vxLanCheckout = function(data){
	if($("#VXLAN_LAN1").attr("hgs_checked_value") == "LAN1"){
		var lanCfg = g_homegatewayParas["lanCfg"];
		for(var i = 1; i <= lanCfg.LanEthNum;i++){
			$("#VXLAN_LAN" + i).attr("hgs_checked_value", lanCfg["LAN" + i].replace(/.$/, ""));
		}
		var getData={Type:"GET",
					userTagData:1,
					msgType:211,
					path:"hbus://mdm/InternetGatewayDevice.LANDevice.{i}.WLANConfiguration.{i}."};				
		
		hgsUpdateData(getData, function (data) {
			for (var j = 0; j < data.length; j++) {
				const k = data[j].fullPath.substr(-2,1);
				$("#VXLAN_SSID" + k).attr("hgs_checked_value", data[j].fullPath.replace(/.$/, ""));
			}
		})
	}
	$("#VxLanWorkMode").val("1");

	var wanNames = [];

	for(var i in data){
		if(data[i].Name){
			wanNames.push({Name:data[i].Name, fullPath:data[i].fullPath.substr(0, data[i].fullPath.length - ".Name".length)});
		}
	}
	wanNames.sort(strategies.sortBy('Name'));

	if (!g_staticInfo["SupportVoip"]) {
		wanNames = wanNames.filter(item => !(item.Name.includes("VOIP") && !item.Name.includes("INTERNET")));
	} 
	var innerHtml = "";
	for(i in wanNames){
		if(1 == wanNames[i].Name.indexOf("_TR069_R_VID_")){
			//don't care only tr069 route wan connection
			continue;
		}
		innerHtml += "<option value='" + wanNames[i].fullPath  + "' >" + wanNames[i].Name + "</option>";
	}

	$("#vxLanSelectWan").html(innerHtml);

	var vxLanData = [];
	for(var i in data){
		if(!data[i].Name){
			for(n in wanNames){
				if(data[i].X_CMCC_WANInterface.replace(/\.$/, "") == wanNames[n].fullPath){
					data[i].Name = wanNames[n].Name;
					break;
				}
			}

			if(!data[i].Name){
				data[i].Name = "Unknown";
			}

			if(data[i].X_CMCC_VLAN == "0"){
				data[i].X_CMCC_VLAN = "";
			}

			data[i].WorkModeText = (data[i].WorkMode == 1)?"Bridge Mode":"Routing Mode";
			vxLanData.push(data[i]);
		}
	}

	vxLanCreate();

	$('[hgs_submit_div_id="HGS_VXLAN"]').attr("disabled", true);
	return vxLanData;
}

vxLanCheckin = function(pathStr, data){
	if((($("#VxLanWorkMode").val() == "2")) && ($("#vxLanAddrTypeStatic").is(':checked'))){
		IP = $("#HGS_VXLAN [hgs_key='IPAddress']").val();
		subnetmask = $("#HGS_VXLAN [hgs_key='SubnetMask']").val();
		gatewayIp = $("#HGS_VXLAN [hgs_key='DefaultGateway']").val();

		var err1 = strategies.isValidIP(IP, "Illegal IP address");
		var err2 = strategies.isValidIPv6(IP, "Illegal IP address");
		if (!err1) {
			var errmask1 = strategies.isValidMask(subnetmask, "Invalid subnet mask");
			var errgateway1 = strategies.isValidIP(gatewayIp, "Invalid gateway address");
			if (errmask1) {
				alert(errmask1);
				return;
			}
			if (errgateway1) {
				alert(errgateway1);
				return;
			}
		}
		if (!err2) {
			var errgateway2 = strategies.isValidIPv6(gatewayIp, "Invalid gateway address");
			if (errgateway2) {
				alert(errgateway2);
			}
		}

		errorMsg = strategies.isSameSubnet(subnetmask, 
			"Invalid parameter: IP address [" + IP + "], Subnet Mask[" + subnetmask + "],Gateway[" + gatewayIp + "]Not in the same network segment!", 
			[IP, gatewayIp]);
		if(errorMsg){
			$("#HGS_VXLAN [hgs_key='IPAddress']").focus();
			alert(errorMsg);
			return true;
		}
	}

	var para = data.commitData.para;
	if(typeof para.X_CMCC_VLANEnable != "undefined"){
		if(!para.X_CMCC_VLANEnable){
			para.X_CMCC_VLAN = 0;
		}
	}

	para.X_CMCC_WANInterface.replace(/.$/, "");

	selectRowData = $("#" + getTableIdByHgstId("HGST_VXLAN")).datagrid('getSelections');
	if(selectRowData.length == 0){
		//This is creating a new instance
		setTimeout(vxLanUpdate, 1000);
		return;
	}
	//edit the old one

	data.type = "POST";
	data.path = "hbus://mdm/" + selectRowData[0].fullPath;
	data.msgType = 212;
	data.commitData.path = data.path;
	
	hgsUpdateData(data)

	setTimeout(vxLanUpdate, 1000);
	return true;
}

vxLanClickRow = function(index,row){
	objData = {objName:"HGS_VXLAN", postHandler:vxLanCfgChangeHandle};
	

	if(row.X_CMCC_WANInterface){
		row.X_CMCC_WANInterface = row.X_CMCC_WANInterface.replace(/\.$/, "");
	}

	loadHbusRespData(row, objData);
	$('[hgs_submit_div_id="HGS_VXLAN"]').attr("disabled", false);
	
	strategies.uncheckAllChildrenCheckboxs("HGS_VXLAN");

	hgsUpdateData({type:"GET",url:"/wanBindInfo"}, function (data) {
		for (const k in data) {
			if ($.isEmptyObject(data[k])) {
				if (document.querySelector("#HGS_VXLAN #VXLAN_" + k)) {
					document.querySelector("#HGS_VXLAN #VXLAN_" + k).removeAttribute("disabled");
				}
			} else {
				document.querySelector("#HGS_VXLAN #VXLAN_" + k).setAttribute("disabled",true);
			}
		}

		var LanInterfaceList = row["X_CMCC_LanInterface"].split(",");
		for(x in LanInterfaceList){
			if(LanInterfaceList[x]){
				document.querySelector("#HGS_VXLAN [hgs_checked_value='" + LanInterfaceList[x].replace(/\.$/, "") + "']").checked = true;
				document.querySelector("#HGS_VXLAN [hgs_checked_value='" + LanInterfaceList[x].replace(/\.$/, "") + "']").removeAttribute('disabled');
			}
		}
	})
}

/*----------------------------------------------------------------------------*/

lanInfoCheckout = function(data){
	var lanData = [], lanIf = [], lanSta = [];
	var i = 0;

	for (i = 0; i < data.length; i++) {
		if (data[i].MACAddress) {
			lanData.push({LanName:g_homegatewayParas["lanCfg"][data[i].fullPath], 
				Status:data[i].Status=="Up"?"Connected":"Not connected", MACAddress:data[i].MACAddress.toUpperCase()});
			lanIf.push(data[i]);
		}else{
			lanSta.push(data[i]);
		}		
	}

	lanIf.sort(strategies.sortBy("fullPath"));
	lanSta.sort(strategies.sortBy("fullPath"));
	
	for (i = 0; i < lanIf.length; i++) {
		lanData[i].LanName = g_homegatewayParas["lanCfg"][lanIf[i].fullPath];
		lanData[i].Status = lanIf[i].Status=="Up"?"Connected":"Not connected";
		lanData[i].MACAddress = lanIf[i].MACAddress.toUpperCase();
		if (g_staticInfo["Region"] =="Sichuan") {
			$("#MACAddress").text(lanData[i].MACAddress);
		}
		if (lanIf[i].Status=="Up") {
			switch(lanIf[i].MaxBitRate){
				case "Auto":
					lanData[i].MaxBitRate = "automatic";
					break;

				default:
					lanData[i].MaxBitRate = lanIf[i].MaxBitRate + "M";
					break;
			};
			switch(lanIf[i].DuplexMode){
				case "Auto":
					lanData[i].DuplexMode = "automatic";
					break;

				case "Full":
					lanData[i].DuplexMode = "Full Duplex";
					break;

				case "Half":
					lanData[i].DuplexMode = "Half Duplex";
					break;
			};
		} else {
			lanData[i].MaxBitRate = "automatic";
			lanData[i].DuplexMode = "automatic";
		}
		
		lanData[i].strBytesSent = lanSta[i].strBytesSent;
		lanData[i].strBytesReceived = lanSta[i].strBytesReceived;
		lanData[i].strPacketsSent = lanSta[i].strPacketsSent;
		lanData[i].strPacketsReceived = lanSta[i].strPacketsReceived;		
	}
	
	return lanData;
}

lanInfoUpdate = function(){
	loadTableData("HGST_LAN_INFO");
}

/*----------------------------------------------------------------------------*/

hostInfoCheckout = function(data){
	for (var i =0; i < data.length; i++) {
		if (isSubnetAP()) {
			if (data[i].IfName == "SSID6") {
				data[i].IfName = "SSID5";
			}
		}
		data[i].MACAddress = data[i].MACAddress.toUpperCase();
		if (data[i].InterfaceType == "802.11") {
			if (parseInt(data[i].NegotiationRate/1000) == 0) {
				data[i].NegotiationRate = 1;
			} else {
				data[i].NegotiationRate = parseInt(data[i].NegotiationRate/1000);
			}
		}		
	}

	return data;
}

hostInfoUpdate = function(){
	loadTableData("HGST_HOST_INFO");
}

hostIpv6InfoUpdate = function(){
	loadTableData("HGST_HOST_IPV6_INFO");
}
/*----------------------------------------------------------------------------*/

function urlFilterEditRow(index, checkRow){
	var dg = $("#" + getTableIdByHgstId("HGST_URL_FILTER"));

	rows = dg.datagrid("getRows").length;
	for(r = 0; r < rows;r++){
		dg.datagrid("endEdit", r);
	}

	dg.datagrid("beginEdit", index);

	if(checkRow){
		dg.datagrid('checkRow', index);
	}
}

urlFilterCreate = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_URL_FILTER"));

	rowsData = dg.datagrid("getRows");
	if(rowsData.length > 0){
		if(!rowsData[rowsData.length - 1].fullPath){
			alert("You can only create a new line at a time, please save before creating a new one!")
			return;
		}
	}
	
	dg.datagrid('appendRow',{UrlAddress:""});
	rows = dg.datagrid("getRows").length;
	urlFilterEditRow(rows - 1, true);

	resizeSubNavContentHeight();
}

urlFilterDelete = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_URL_FILTER"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}
	tableCheckedData = CheckedData[0];
	
	postData = {type:"POST",
		commitData:{para:{UrlAddress:tableCheckedData.UrlAddress}}
	};
	
	if(tableCheckedData.fullPath){
		postData.msgType = 216;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{
		rowIndex = dg.datagrid("getRowIndex", CheckedData[0]);
		dg.datagrid("deleteRow", rowIndex);
		return;
	}

	postData.commitData.path = postData.path;
	hgsUpdateData(postData,function(result){
		if(IS_LOG_DATA_ENABLE()){
			LOG_DATA("server response:");
			console.log(result); 
		}
		urlFilterUpdate();
	})
}

urlFilterUpdate = function(){
	loadTableData("HGST_URL_FILTER");
}

urlFilterClickRow = function(index,row){
	urlFilterEditRow(index, true);
}

urlFilterCheckRow = function(index,row){
	urlFilterEditRow(index, false);
}

urlFilterCheckin = function(objName, tableId, data, postData){
	var dg = $("#" + getTableIdByHgstId("HGST_URL_FILTER"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}

	tableCheckedData = CheckedData[0];
	console.log("tableCheckedData.Url"+" "+tableCheckedData.Url)
	var msg = strategies.isURL(tableCheckedData.Url, "Illegal URL");
	if(msg){
		alert(msg);
		return true;
	}
	
	postData.type = "POST";
	postData.commitData = {para:{Url:tableCheckedData.Url}};
	
	if(tableCheckedData.fullPath){
		postData.msgType = 212;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{
		postData.msgType = 215;
		postData.path = "hbus://mdm/InternetGatewayDevice.X_CMCC_Security.UrlFilter.{i}.";
	}

	postData.commitData.path = postData.path;
	setTimeout(urlFilterUpdate, 1000);
}

/*----------------------------------------------------------------------------*/
macFilterCheckout = function (data) {
    var obj=[];
    if (data) {
        for (let i = 0; i < data.length; i++) {
            if (data[i].DestinationMACAddress && data[i].Enable && data[i].SourceMACAddress && data[i].fullPath) {
                obj.push(data[i]);
            }
        }
    }
    return obj;
}

function macFilterEditRow(index, checkRow){
	datagridEditRow(index, checkRow, "HGST_MAC_FILTER");
}

macFilterCreate = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_MAC_FILTER"));

	rowsData = dg.datagrid("getRows");
	if(rowsData.length > 0){
		if(!rowsData[rowsData.length - 1].fullPath){
			alert("You can only create a new line at a time, please save before creating a new one!")
			return;
		}
	}
	
	dg.datagrid('appendRow', {seleced:"true"});
	rows = dg.datagrid("getRows").length;
	macFilterEditRow(rows - 1, true);

	resizeSubNavContentHeight();
}

macFilterDelete = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_MAC_FILTER"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}
	tableCheckedData = CheckedData[0];
	
	postData = {type:"POST",
		commitData:{para:{UrlAddress:tableCheckedData.UrlAddress}}
	};
	
	if(tableCheckedData.fullPath){
		postData.msgType = 216;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{
		rowIndex = dg.datagrid("getRowIndex", CheckedData[0]);
		dg.datagrid("deleteRow", rowIndex);
		return;
	}

	postData.commitData.path = postData.path;
	hgsUpdateData(postData,function(result){
		if(IS_LOG_DATA_ENABLE()){
			LOG_DATA("server response:");
			console.log(result); 
		}
		macFilterUpdate();
	})
}

macFilterUpdate = function(){
	loadTableData("HGST_MAC_FILTER");
}

macFilterClickRow = function(index,row){
	//macFilterEditRow(index, true);
}

macFilterCheckRow = function(index,row){
	//macFilterEditRow(index, false);
}

macFilterCheckin = function(objName, tableId, data, postData){
	var dg = $("#" + getTableIdByHgstId("HGST_MAC_FILTER"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}
	
	tableCheckedData = CheckedData[0];
	var newStandardMac = "";
	if(tableCheckedData.SourceMACAddress){
		newStandardMac = strategies.convertStandardMacStr(tableCheckedData.SourceMACAddress,true);
		if(!newStandardMac){
			alert(tableCheckedData.SourceMACAddress + "Is an illegal source MAC address");
			return true;
		}
		tableCheckedData.SourceMACAddress = newStandardMac;
	}
	newStandardMac = "";
	if(tableCheckedData.DestinationMACAddress){
		newStandardMac = strategies.convertStandardMacStr(tableCheckedData.DestinationMACAddress,true);
		if(!newStandardMac){
			alert(tableCheckedData.DestinationMACAddress + "Is an illegal destination MAC address");
			return true;
		}
		tableCheckedData.DestinationMACAddress = newStandardMac;
	}

	if((tableCheckedData.SourceMACAddress == "")&&(tableCheckedData.DestinationMACAddress == "")){
		alert("At least one of the source MAC address or the destination MAC address must be filled in!");
		return true;
	}

	if(tableCheckedData.SourceMACAddress == tableCheckedData.DestinationMACAddress){
		alert("The source MAC address and destination MAC address cannot be the same!");
		return true;
	}

	tableCheckedData.Enable = 1;
	postData.type = "POST";
	postData.commitData = {para:tableCheckedData};
	
	if(tableCheckedData.fullPath){
		postData.msgType = 212;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{
		postData.msgType = 215;
		postData.path = "hbus://mdm/InternetGatewayDevice.X_CMCC_Security.MacFilter.{i}.";
	}

	postData.commitData.para.fullPath = undefined; //no need
	postData.commitData.path = postData.path;

	setTimeout(macFilterUpdate, 1000);
}

/*----------------------------------------------------------------------------*/

function ipFilterEditRow(index, checkRow){
	datagridEditRow(index, checkRow, "HGST_IP_FILTER");
}

ipFilterCreate = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_IP_FILTER"));

	rowsData = dg.datagrid("getRows");
	if(rowsData.length > 0){
		if(!rowsData[rowsData.length - 1].fullPath){
			alert("You can only create a new line at a time, please save before creating a new one!")
			return;
		}
	}
	
	dg.datagrid('appendRow', {selected:true, Enable:"1", Protocol:"ALL"});
	rows = dg.datagrid("getRows").length;
	ipFilterEditRow(rows - 1, true);

	resizeSubNavContentHeight();
}

ipFilterDelete = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_IP_FILTER"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}
	tableCheckedData = CheckedData[0];
	
	postData = {type:"POST",
		commitData:{para:{UrlAddress:tableCheckedData.UrlAddress}}
	};
	
	if(tableCheckedData.fullPath){
		postData.msgType = 216;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{
		rowIndex = dg.datagrid("getRowIndex", CheckedData[0]);
		dg.datagrid("deleteRow", rowIndex);
		return;
	}

	postData.commitData.path = postData.path;
	hgsUpdateData(postData,function(result){
		if(IS_LOG_DATA_ENABLE()){
			LOG_DATA("server response:");
			console.log(result); 
		}
		ipFilterUpdate();
	})
}

ipFilterUpdate = function(){
	loadTableData("HGST_IP_FILTER");
}

ipFilterClickRow = function(index,row){
	ipFilterEditRow(index, true);
}

ipFilterCheckRow = function(index,row){
	//ipFilterEditRow(index, false);
}

ipFilterCheckout = function(data){
	for(row in data){
		data[row].SourcePortStart = strategies.convertTextToNoZeroNum(data[row].SourcePortStart);
		data[row].SourcePortEnd = strategies.convertTextToNoZeroNum(data[row].SourcePortEnd);
		data[row].DestPortStart = strategies.convertTextToNoZeroNum(data[row].DestPortStart);
		data[row].DestPortEnd = strategies.convertTextToNoZeroNum(data[row].DestPortEnd);
	}

	$("#HGST_IP_FILTER").show();

	return data;
}

ipFilterCheckin = function(objName, tableId, data, postData){
	var dg = $("#" + getTableIdByHgstId("HGST_IP_FILTER"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}

	rowData = CheckedData[0];

	if(rowData.Name.length > 10){
		alert("[Rule Name] length cannot exceed 10 bytes!");
		return true;
	}

	var errMsg = "";

	errMsg = strategies.isEmptyOrValidIP(rowData.SourceIPStart, "Illegal [Source IP (from)]")
	if(errMsg){
		alert(errMsg);
		return true;
	}
	errMsg = strategies.isEmptyOrValidIP(rowData.SourceIPEnd, "Illegal [Source IP (stop)]")
	if(errMsg){
		alert(errMsg);
		return true;
	}
	errMsg = strategies.isEmptyOrValidIP(rowData.DestIPStart, "Illegal [Destination IP (starting)]")
	if(errMsg){
		alert(errMsg);
		return true;
	}
	errMsg = strategies.isEmptyOrValidIP(rowData.DestIPEnd, "Illegal [Destination IP (stop)]")
	if(errMsg){
		alert(errMsg);
		return true;
	}

	ipBegin = strategies.convertIpStrToNum(rowData.SourceIPStart);
	ipEnd = strategies.convertIpStrToNum(rowData.SourceIPEnd);
	if(ipEnd != -1 && ipBegin > ipEnd){
		alert("[Source IP (end)] must be greater than or equal to [Source IP (start)]");
		return true;
	}
	ipBegin = strategies.convertIpStrToNum(rowData.DestIPStart);
	ipEnd = strategies.convertIpStrToNum(rowData.DestIPEnd);
	if(ipEnd != -1 && ipBegin > ipEnd){
		alert("[Source IP (end)] must be greater than or equal to [Source IP (start)]");
		return true;
	}


	errMsg = strategies.isMinMaxIntStringOrEmpty(rowData.SourcePortStart, "Illegal [source port (starting)]", "1:65536")
	if(errMsg){
		alert(errMsg);
		return true;
	}
	errMsg = strategies.isMinMaxIntStringOrEmpty(rowData.SourcePortEnd, "Illegal [source port (stop)]", "1:65536")
	if(errMsg){
		alert(errMsg);
		return true;
	}
	errMsg = strategies.isMinMaxIntStringOrEmpty(rowData.DestPortStart, "Illegal [destination port (starting)]", "1:65536")
	if(errMsg){
		alert(errMsg);
		return true;
	}
	errMsg = strategies.isMinMaxIntStringOrEmpty(rowData.DestPortEnd, "Illegal [Destination Port (Stop)]", "1:65536")
	if(errMsg){
		alert(errMsg);
		return true;
	}

	rowData.SourcePortStart = parseInt(rowData.SourcePortStart);
	rowData.SourcePortEnd = parseInt(rowData.SourcePortEnd);
	if(rowData.SourcePortEnd && rowData.SourcePortStart > rowData.SourcePortEnd){
		alert("[Source port (end)] must be greater than or equal to [Source port (start)]");
		return true;
	}

	rowData.DestPortStart = parseInt(rowData.DestPortStart);
	rowData.DestPortEnd = parseInt(rowData.DestPortEnd);
	if(rowData.DestPortEnd && rowData.DestPortStart > rowData.DestPortEnd){
		alert("[Destination Port (End)] must be greater than or equal to [Destination Port (Start)]");
		return true;
	}


	postData.type = "POST";
	postData.commitData = {para:rowData};
	
	if(rowData.fullPath){
		postData.msgType = 212;
		postData.path = "hbus://mdm/" + rowData.fullPath;
	}else{
		postData.msgType = 215;
		postData.path = "hbus://mdm/InternetGatewayDevice.X_CMCC_Security.IPFilterIn.{i}.";
		if($("#ipFilterLanToWan").is(':checked')){
			postData.path = postData.path.replace(".IPFilterIn.", ".IPFilterOut.");
		}
	}

	//set undefined due to no further need
	postData.commitData.para.selected = undefined;
	postData.commitData.para.fullPath = undefined; 

	postData.commitData.path = postData.path;

	setTimeout(ipFilterUpdate, 1000);
}

ipFilterPreCheckout = function(data){
	if($("#ipFilterLanToWan").is(':checked')){
		data.path = data.path.replace(".IPFilterIn.", ".IPFilterOut.");
	}

	return data;
}

$(".ipFilterDir").click(function(){
	/*var id = $(this).attr("id");
	if(id == "ipFilterWanToLan"){

	}else{

	}
	console.log($(this).attr("id"));*/

	$("#HGST_IP_FILTER").hide();
	ipFilterCfgUpdate();
	ipFilterUpdate();
})

ipFilterCfgPreCheckout = function (data) {
	var jsonData = {};
	if($("#ipFilterLanToWan").is(':checked')){
		jsonData.Enable = data.IPFilterOutEnable;
		jsonData.Policy = data.IPFilterOutPolicy;
	} else {
		jsonData.Enable = data.IPFilterInEnable;
		jsonData.Policy = data.IPFilterInPolicy;
	}

	return jsonData;
}
ipFilterCfgCheckin = function (data) {
	var jsonData = {};
	if($("#ipFilterLanToWan").is(':checked')){
		jsonData.IPFilterOutEnable = data.Enable;
		jsonData.IPFilterOutPolicy = data.Policy;
	} else {
		jsonData.IPFilterInEnable = data.Enable;
		jsonData.IPFilterInPolicy = data.Policy;
	}

	return jsonData;
}
ipFilterCfgUpdate = function(){
	loadHbusData("HGS_IP_FILTER");
}

/*----------------------------------------------------------------------------*/
function vserverEditRow(index, checkRow){
	datagridEditRow(index, checkRow, "HGST_VIRTUAL_SERVER");
}

vserverCreate = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_VIRTUAL_SERVER"));

	rowsData = dg.datagrid("getRows");
	if(rowsData.length > 0){
		if(!rowsData[rowsData.length - 1].fullPath){
			alert("You can only create a new line at a time, please save before creating a new one!")
			return;
		}
	}

	WanInfo = {};
	columns = g_tableRules["HGST_VIRTUAL_SERVER"]["easyui"]["columns"][0];
	for(x in columns){
		if(columns[x].field == "WanName"){
			if(columns[x]["editor"]["options"]["data"].length > 0){
				WanInfo = columns[x]["editor"]["options"]["data"][0];
			}
			break;
		}
	}

	if(WanInfo.length == 0){
		alert("Please create a WAN connection first, then create the virtual host configuration!")
		return;
	}
	
	dg.datagrid('appendRow', {selected:true, PortMappingEnabled:"1", PortMappingProtocol:"TCP", WanName:WanInfo});
	rows = dg.datagrid("getRows").length;
	vserverEditRow(rows - 1, true);

	makeDatagridComboReadonly("HGST_VIRTUAL_SERVER");

	resizeSubNavContentHeight();
}

vserverDelete = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_VIRTUAL_SERVER"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}
	tableCheckedData = CheckedData[0];
	
	postData = {type:"POST",
		commitData:{para:{}}
	};
	
	if(tableCheckedData.fullPath){
		postData.msgType = 216;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{
		rowIndex = dg.datagrid("getRowIndex", CheckedData[0]);
		dg.datagrid("deleteRow", rowIndex);
		return;
	}

	postData.commitData.path = postData.path;
	hgsUpdateData(postData,function(result){
		if(IS_LOG_DATA_ENABLE()){
			LOG_DATA("server response:");
			console.log(result); 
		}
		vserverUpdate();
	})
}

vserverUpdate = function(){
	loadTableData("HGST_VIRTUAL_SERVER");
}

vserverClickRow = function(index,row){
	vserverEditRow(index, true);
}

vserverCheckRow = function(index,row){
	//vserverEditRow(index, false);
}

vserverCheckout = function(data){
	var newData = [];

	var WanInfo = [];
	for(row in data){
		if(typeof data[row].PortMappingProtocol != "undefined"){
			newData.push(data[row]);
		}else{
			WanInfo.push({WanName:data[row].Name, WanPath:data[row].fullPath});
		}
	}

	columns = g_tableRules["HGST_VIRTUAL_SERVER"]["easyui"]["columns"][0];
	//console.log(columns);
	if (!g_staticInfo["SupportVoip"]) {
		WanInfo = WanInfo.filter(item => !(item.WanName.includes("VOIP") && !item.WanName.includes("INTERNET")));
	}

	for(x in columns){
		if(columns[x].field == "WanName"){
			columns[x]["editor"]["options"]["data"] = WanInfo.sort(strategies.sortBy("WanName"));
			break;
		}
	}

	for(x in newData){
		for(n in WanInfo){
			if(newData[x].fullPath.substr(0, WanInfo[n].WanPath.length) == WanInfo[n].WanPath){
				newData[x].WanName = WanInfo[n];
				break;
			}
		}
	}

	/*console.log(data);
	console.log(newData);

	console.log(g_tableRules["HGST_VIRTUAL_SERVER"]["easyui"]["columns"])*/

	return newData;
}

vserverCheckin = function(objName, tableId, data, postData){
	var dg = $("#" + getTableIdByHgstId("HGST_VIRTUAL_SERVER"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}
	

	rowData = CheckedData[0];

	if(rowData.PortMappingDescription.length > 256){
		alert("【Note】The length cannot exceed 256 bytes!");
		return true;
	}

	var errMsg = "";

	errMsg = strategies.isValidIP(rowData.RemoteHost, "Illegal [External IP]")
	if(errMsg){
		alert(errMsg);
		return true;
	}
	errMsg = strategies.isValidIP(rowData.InternalClient, "Illegal [Intranet IP]")
	if(errMsg){
		alert(errMsg);
		return true;
	}

	errMsg = strategies.isMinMaxIntStringOrEmpty(rowData.PortMappingLeaseDuration, "Illegal [Lease Seconds], legal range 0-86400000", "0:86400000")
	if(errMsg){
		alert(errMsg);
		return true;
	}
	errMsg = strategies.minMaxIntValue(rowData.ExternalPort, "Illegal [External Network Port], legal range 1-65555", "1:65535")
	if(errMsg){
		alert(errMsg);
		return true;
	}
	errMsg = strategies.minMaxIntValue(rowData.InternalPort, "Illegal [Intranet Port], legal range 1-65555", "1:65535")
	if(errMsg){
		alert(errMsg);
		return true;
	}


	postData.type = "POST";
	postData.commitData = {para:rowData};
	
	if(rowData.fullPath){
		postData.msgType = 212;
		postData.path = "hbus://mdm/" + rowData.fullPath;
	}else{
		postData.msgType = 215;
		postData.path = "hbus://mdm/" + rowData.WanName + "PortMapping.{i}.";
	}

	//set undefined due to no further need
	postData.commitData.para.selected = undefined;
	postData.commitData.para.fullPath = undefined;
	postData.commitData.para.WanName = undefined;
	postData.commitData.path = postData.path;

	//console.log(postData);

	setTimeout(vserverUpdate, 1000);
}

vserverPreCheckout = function(data){
	return data;
}
/*----------------------------------------------------------------------------*/

dmzEnableUpdate = function(){
	if($("#DMZEnable").is(":checked")){
		$("#DmzLanIpDiv").show();
	}else{
		$("#DmzLanIpDiv").hide();
		$("#DmzLanIp").val("");
	}
	resizeSubNavContentHeight();
}

$("#DMZEnable").click(function(){
	dmzEnableUpdate();
})

dmzUpdate = function(data){
	var enabled = false;
	//if(data.DMZHostIPAddress){
	//	enabled = true;
	//}
	//document.querySelector("#DmzEnabled").checked = enabled;
	dmzEnableUpdate();
}
dmzCheckin = function (data) {
	if ($("#DMZEnable").is(":checked")) {
		var errorMsg = strategies.isSameSubnet(g_staticInfo["LanIpv4SubnetMask"], 
			"The IP address is illegal and should be in the same network segment as the LAN side IP!", 
			[data.DMZHostIPAddress, g_staticInfo["LanIpv4Addr"]]);
			
		if (errorMsg) {
			alert(errorMsg);
			return;
		}
	}
	return data;
}
/*----------------------------------------------------------------------------*/
QOSCfgCheckout = function (data) {
	var arr,i,id,id_pri;
	//show all elements of default queue
	//clear all elements of priority queue
	for (i = 0; i < 4; i++) {
		id = '#btn_app'+i;
		id_pri = '#btn_PRI'+i;
		$(id).attr('style','visibility:unset');
		$(id_pri).val('');
		// $(id_pri).hide();
	}

	if (!$.isEmptyObject(data)) {
		arr = data.Mode.split(',');
		if (arr.length) {
			for (i = 0; i < arr.length; i++) {
				const element = $.trim(arr[i]);//$.trim()去掉字符串前后的空格
				ActionLeftButton(element)
			}
		}

		if (data.Plan == "priority") {
			$("#qosPriorityQueue").show();
			$("#qosPriorityQueueWeight").hide();
		} else {
			$("#qosPriorityQueue").hide();
			$("#qosPriorityQueueWeight").show();
		}
	}
	
	resizeSubNavContentHeight();
}

QOSCfgCheckIn = function (pathStr, data) {
	var para = data.commitData.para;
	var mode = "";
	var arr = [], j = 0;

	for (var i = 0; i < 4; i++) {		
		id_pri = '#btn_PRI'+i;
		if ($(id_pri).val() != "") {
			arr[j++] = $(id_pri).val();
		}				
	}
	
	if (arr.length > 0) {
		mode = arr[0];
		for (j = 1; j < arr.length; j++) {
			mode += ",";
			mode += arr[j];
		}
	}

	para.Mode = mode;
	setTimeout(QOSCfgUpdate, 1000);
}
QOSCfgUpdate = function () {
	loadHbusData("HGS_QOS_CFG");
}
add2PriQueue = function (app) {
	for (i = 0; i < 4; i++) {
		id = '#btn_PRI'+i;
		var value = $(id).val();
		if (value == '') {
			$(id).val(app);
			break;
		}
	}	
}

ActionLeftButton = function (app) {
	switch (app) {
		case 'VOIP':
			$("#btn_app0").attr('style','visibility:hidden');
			add2PriQueue(app);
			break;
		case 'IPTV':
			$("#btn_app1").attr('style','visibility:hidden');
			add2PriQueue(app);
			break;
		case 'TR069':
			$("#btn_app2").attr('style','visibility:hidden');
			add2PriQueue(app);
			break;
		case 'INTERNET':
			$("#btn_app3").attr('style','visibility:hidden');				
			add2PriQueue(app);
			break;
		default: 
			break;
	}
}
ActionRightButton = function (inputObj) {
	switch (inputObj.value) {
		case 'VOIP':
			//把当前值设为空
			inputObj.value="";
			$("#btn_app0").attr('style','visibility:unset');
			break;
		case 'IPTV':
			inputObj.value="";
			$("#btn_app1").attr('style','visibility:unset');
			break;
		case 'TR069':
			inputObj.value="";
			$("#btn_app2").attr('style','visibility:unset');
			break;
		case 'INTERNET':
			inputObj.value="";
			$("#btn_app3").attr('style','visibility:unset');
			break;
		default:
			break;
	}
	
	//Reorganize the right queue 
	var arr = [], id;
	var i=0,j=0;

	for (i = 0; i < 4; i++) {
		id = '#btn_PRI'+i;
		if ($(id).val() != '') {
			arr[j++] = $(id).val();
			$(id).val('');
		}
	}

	for (i = 0; i < arr.length; i++) {
		id = '#btn_PRI'+i;
		$(id).val(arr[i]);
	}
}


qosClassificationCheckout = function (data) {
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_CLASSIFICATION"));

	dg.datagrid({singleSelect:false});

	for (var i = 0; i < data.length; i++) {
		data[i].queue = i+1;
	}

	removeDatagridTitleRowCheckBox("HGST_QOS_CLASSIFICATION");	
	return data;
}

qosClassficationOnLoadSuccess = function(data){
	/* do nothing*/
}

qosClassificationCheckin = function (objName, tableId, data, postData) {
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_CLASSIFICATION"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select at least one row before saving!");
		return true;
	}
	else if (1 == CheckedData.length) {
		tableCheckedData = CheckedData[0];
	
		postData.type = "POST";
		postData.commitData = {para:{DSCPMarkValue:tableCheckedData.DSCPMarkValue, 
									"802-1_P_Value":tableCheckedData["802-1_P_Value"],
									 ClassQueue:tableCheckedData.ClassQueue}};
		
		if(tableCheckedData.fullPath){
			postData.msgType = 212;
			postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
		}else{		
			postData.msgType = 215;
			postData.path = "hbus://mdm/InternetGatewayDevice.X_CMCC_UplinkQoS.Classification.{i}.";
		}
	
		postData.commitData.path = postData.path;		
	}
	else {
		for (var i = 0; i < CheckedData.length; i++) {
			delete CheckedData[i].queue;
		}
		postData.type = "POST";
		postData.url = "/setObjs";
		postData.commitData = CheckedData;
	}

	setTimeout(qosClassificationUpdate, 1000);
}

qosClassificationCreate = function () {
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_CLASSIFICATION"));
	
	dg.datagrid({singleSelect:true});
	removeDatagridTitleRowCheckBox("HGST_QOS_CLASSIFICATION");

	rowsData = dg.datagrid("getRows");
	if(rowsData.length > 0){
		if(!rowsData[rowsData.length - 1].fullPath){
			alert("You can only create a new line at a time, please save before creating a new one!");
			return;
		}			
	}
	
	// var Name = "802-1_P_Value";
	dg.datagrid('appendRow',{DSCPMarkValue:"", Name:"", ClassQueue:""});
	rows = dg.datagrid("getRows").length;
	qosClassificationEditRow(rows - 1, true);

	resizeSubNavContentHeight();
}

qosClassificationDelete = function () {
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_CLASSIFICATION"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select at least one row before saving!");
		return true;
	} 
	else if (CheckedData.length == 1) {
		if (typeof(CheckedData[0].fullPath) == "undefined") {
			rowIndex = dg.datagrid("getRowIndex", CheckedData[0]);
			dg.datagrid("deleteRow", rowIndex);
			return;
		}
	}
	
	var paths = "";
	for (var i in CheckedData) {
		if (paths == "") {
			paths = CheckedData[i].fullPath;
		} else {
			paths += ";" + CheckedData[i].fullPath;	
		}
	}

	var postData = {type:"POST",
					url:"/delObjs",
					waitTimeoutMs:5000,
					notJson:true,
					commitData:paths};
	
	hgsUpdateData(postData,function(result){
		if(IS_LOG_DATA_ENABLE()){
			LOG_DATA("server response:");
			console.log(result); 
		}
		qosClassificationUpdate();
	})
}

qosClassificationUpdate = function () {
	loadTableData("HGST_QOS_CLASSIFICATION");
	updateClassifyRule();
}

function qosClassificationEditRow(index, checkRow){
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_CLASSIFICATION"));

	rows = dg.datagrid("getRows").length;
	for(r = 0; r < rows;r++){
		dg.datagrid("endEdit", r);
	}

	dg.datagrid("beginEdit", index);

	if(checkRow){
		dg.datagrid('checkRow', index);
	}
}
function intRangeCheck(max, min, range){
	var arr = range.split('-');
	var errMsg = "";
	var errMsg1 = "Illegal [MAX], please enter a value"+range+"Integer between";
	var errMsg2 = "Illegal [Min], please enter a value"+range+"Integer between";

	if(isNaN(max)){
		return errMsg1;
	}else{
		if(isNaN(min)){
			return errMsg2;
		}else{
			if (parseInt(max) > arr[1]) {
				return errMsg1;
			}
			if (parseInt(min) < arr[0]) {
				return errMsg2;
			}
			if (parseInt(max) < parseInt(min)) {
				errMsg = "The Max value cannot be less than the Min value";
			}
		}
	}

	return errMsg;
}
function compareIpv6(ip1, ip2) 
{
	var ip1s = ip1.split(':');
	var ip2s = ip2.split(':');
	for (var i = 0; i < ip1s.length; i++) {
		if (ip1s[i] == '') {
			if (ip2s[i] == '') { //对应的项都为空，往下比较
				continue;
			} else {	
				return -1;
			}
		} else {
			if (ip2s[i]=="") {
				return 1;
			} 
			else { //确定对应的项不为空，将字符串转换为整数进行比较
				var value1 = parseInt(ip1s[i], 16);
				var value2 = parseInt(ip2s[i], 16);
				if (value1 > value2) {
					return 1;
				} 
				else if (value1 < value2) {
					return -1;
				} 
				else {
					continue;
				}
			}
		}
	}
//循环结束，表示两个地址相同
return 0;
}
qosClassificationTypeCheckin = function (objName, tableId, data, postData) {
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_CLASSIFICATION_TYPE"));

	var rows = dg.datagrid("getRows").length;
	CheckedData = dg.datagrid("getChecked");
	var tableCheckedData = CheckedData[0];
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}


	var errMsg1 = "", errMsg2 = "", err1 = "", err2 = "";
	var max = tableCheckedData.Max;
	var min = tableCheckedData.Min;
	var ProtocolList = tableCheckedData.ProtocolList;
	var hash = {};

	if (tableCheckedData.Type == "") {
		alert("[Match type] cannot be empty");
		return true;
	}

	var rowIndex = dg.datagrid("getRowIndex", CheckedData[0]);
	for (let i = 0; i < classifyType_qos.length; i++) {
		if (rowIndex == i) {
			if (hash[tableCheckedData.Type]) {
				alert("The [match type] record already exists and cannot be configured again");
				qosClassificationTypeEditRow(0, true);
				return true;
			}else{
				hash[tableCheckedData.Type] = 1;
			}
		} else {
			if (hash[classifyType_qos[i].Type]) {
				alert("The [match type] record already exists and cannot be configured again");
				qosClassificationTypeEditRow(0, true);
				return true;
			}else{
				hash[classifyType_qos[i].Type] = 1;
			}
		}	
	}
		
	if (tableCheckedData.Type != "NULLType") {
		if (max == "") {
			alert("【MAX】cannot be empty");
			qosClassificationTypeEditRow(0, true);
			return true;
		}
		else if (min == "") {
			alert("【Min】cannot be empty");
			qosClassificationTypeEditRow(0, true);
			return true;
		}	
	}

	var foundmax = false, foundmin = false;
	switch (tableCheckedData.Type) {
		case "WANInterface":
			for (var i in wanPath_qos) {
				if (wanPath_qos[i].Interface == max) {
					foundmax = true;
				}
				if (wanPath_qos[i].Interface == min) {
					foundmin = true;
				}
			}

			if (!foundmax) {
				errMsg1 = "[MAX] is illegal. All valid values ​​are listed in the drop-down box. Please click the drop-down box and select from it!"
			}
			if (!foundmin) {
				errMsg2 = "[MIN] is illegal. All valid values ​​are listed in the drop-down box. Please click the drop-down box and select from it!"
			}
			if (max != min) {
				errMsg1 = "When the match type is WANInterface, the [min] and [max] values ​​should be consistent."
			}
			break;
		case "LANInterface":
			for (var i in lanPath_qos) {
				if (lanPath_qos[i].Interface == max) {
					foundmax = true;
				}
				if (lanPath_qos[i].Interface == min) {
					foundmin = true;
				}
			}

			if (!foundmax) {
				errMsg1 = "[MAX] is illegal. All valid values ​​are listed in the drop-down box. Please click the drop-down box and select from it!"
			}
			if (!foundmin) {
				errMsg2 = "[MIN] is illegal. All valid values ​​are listed in the drop-down box. Please click the drop-down box and select from it!"
			}
			if (max != min) {
				errMsg1 = "When the matching type is LANInterface, the [min] and [max] values ​​should be consistent."
			}
			break;
		case "SMAC":
		case "DMAC":
			tableCheckedData.Max = tableCheckedData.Max.toUpperCase();
			tableCheckedData.Min = tableCheckedData.Min.toUpperCase();
			errMsg1 = strategies.isValidMacAddr(max, "Illegal [MAX] MAC address");
			errMsg2 = strategies.isValidMacAddr(min, "Illegal [Min] MAC address");
			if (!errMsg1 && !errMsg2) {
				var arr1 = max.split(':');
				var arr2 = min.split(':');
				for (var i = 0; i < arr1.length; i++) {
					if (arr1[i] > arr2[i]) {
						break;
					}

					if (arr1[i] < arr2[i]) {
						errMsg1 = "[MAX] MAC address must not be less than [Min] MAC address";
					}
				}
			}
			break;
		case "SIP":
		case "DIP":
			errMsg1 = strategies.isEmptyOrValidIP(max, "Illegal [MAX] IP address");
			errMsg2 = strategies.isEmptyOrValidIP(min, "Illegal [Min] IP address");
			err1 = strategies.isValidIPv6(max, "Illegal [MAX] IP address");
			err2 = strategies.isValidIPv6(min, "Illegal [Min] IP address");

			// 比较两个ipv4大小
			if (!errMsg1 && !errMsg2) {
				var arr1 = max.split('.');
				var arr2 = min.split('.');
				for (let i = 0; i < arr1.length; i++) {
					if (parseInt(arr1[i]) < parseInt(arr2[i])) {
						errMsg1 = "【MAX】IP address must not be less than 【Min】IP address";
					}
				}
			}
			else if (!err1 && !err2){ 
				//比较两个ipv6大小
				if (compareIpv6(max,min) == -1) {
					errMsg1 = "【MAX】IP address must not be less than 【Min】IP address";
				}else{
					errMsg1 = "";
					errMsg2 = "";
				}
			}
			else {
				if (!errMsg1 || !err1) {
					errMsg1 = "";
				}
				if (!errMsg2 || !err2) {
					errMsg2 = "";
				}
				if ((!errMsg1 || !err1) && (!errMsg2 || !err2)) {
					errMsg1 = "[MAX] and [Min] should both be IPv4 or IPv6 addresses";
				}
			}
			break;
		case "SPORT":
		case "DPORT":
			errMsg1 = intRangeCheck(max,min,"0-65536");	
			break;
		case "8021P":
			errMsg1 = intRangeCheck(max,min,"0-7");
			break;
		case "TOS":
			errMsg1 = intRangeCheck(max,min,"0-255");
			break;
		case "DSCP":
			errMsg1 = intRangeCheck(max,min,"0-63");
			break;
		case "TC":
			errMsg1 = intRangeCheck(max,min,"0-255");
			break;
		case "FL":
			errMsg1 = intRangeCheck(max,min,"0-1048575");
			break;
		case "IPVERSION":
			if (max != min) {
				errMsg1 = "When the matching type is EtherType, the [min] and [max] values ​​should be consistent."
			}
			break;	
		default:
			break;
	}

	if (errMsg1) {
		alert(errMsg1);
		qosClassificationTypeEditRow(0, true);
		return true;
	} else {
		if (errMsg2) {
			alert(errMsg2);
			qosClassificationTypeEditRow(0, true);
			return true;	
		}
	}

	if (ProtocolList == "") {
		alert("[Protocol] cannot be empty");
		return true;
	} else {
		var procArr = ProtocolList.split(',');
		var proclist = ["TCP","UDP","ICMP","ICMPv6","RTP"];
		for (var k in procArr) {
			if (proclist.indexOf(procArr[k]) == -1) {
				alert("[Protocol] is illegal, please select a valid protocol value from the drop-down box!");
				return true;
			}
		}
	}
	
	var objId = $("#classifyRule").val();
	var pathStr = "hbus://mdm/InternetGatewayDevice.X_CMCC_UplinkQoS.Classification." + objId;
	
	postData.type = "POST";
	postData.commitData = {para:{Type:tableCheckedData.Type,
								 Max:tableCheckedData.Max,
		                         Min:tableCheckedData.Min,
								 ProtocolList:tableCheckedData.ProtocolList}};
		
	if(tableCheckedData.fullPath){
		postData.msgType = 212;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{		
		postData.msgType = 215;
		postData.path = pathStr + ".type.{i}.";
	}

	postData.commitData.path = postData.path;
	setTimeout(qosClassificationTypeUpdate, 1000);
}

var wanPath_qos = [], lanPath_qos = [], classifyType_qos = [];
qosClassificationTypeCheckout = function (data) {
	var objId = $("#classifyRule").val();
	var j=0, k=0, z=0;
	var arr = [], wanData = [], lanData = [];

	for (var i = 0; i < data.length; i++) {
		if (data[i].fullPath.indexOf("Classification") > -1) {
			var classificationId = data[i].fullPath.match(/\d+/)[0];
			if (classificationId == objId) {
				if (data[i].Type == "") {
					data[i].Type = "NULLType";
				}
				else if (data[i].Type == "WANInterface" || data[i].Type == "LANInterface") {
					if (data[i].Max != "") {
						var tmpmax = data[i].Max.substr(data[i].Max.length-1,1) ;	
						if(tmpmax != "."){
							data[i].Max = data[i].Max +".";
						}
					}
					if (data[i].Min != "") {
						var tmpmin = data[i].Min.substr(data[i].Min.length-1,1) ;
						if(tmpmin != "."){
							data[i].Min = data[i].Min +".";
						}
					}	
				}

				arr[j++] = data[i];
			}	
		}
		else if (data[i].fullPath.indexOf("WANIPConnection") > -1 || data[i].fullPath.indexOf("WANPPPConnection") > -1){
			wanData[k++] = data[i];
		}
		else if (data[i].fullPath.indexOf("LANEthernetInterfaceConfig") > -1 || data[i].fullPath.indexOf("WLANConfiguration") > -1){
			lanData[z++] = data[i];
		}
	}

	wanPath_qos = getWanInfo(wanData);
	lanPath_qos = getlanInfo(lanData);
	classifyType_qos = arr;
	if (!g_staticInfo["SupportVoip"]) {
		wanPath_qos = wanPath_qos.filter(item => !(item.Name.includes("VOIP") && !item.Name.includes("INTERNET")));
	}
	
	setTimeout(function () {
		if (arr.length) {
			var dg = $("#" + getTableIdByHgstId("HGST_QOS_CLASSIFICATION_TYPE"));
			for (var m = arr.length-1; m >=0; m--) {
				if (arr[m].Type == "WANInterface" || arr[m].Type == "LANInterface") {
					dg.datagrid("checkRow",m);
				}
			}
			
			if (arr[0].Type != "WANInterface" && arr[0].Type != "LANInterface") {
				dg.datagrid("checkRow",0);
			}
		}		
	}, 300);

	updateClassifyRule();
	removeDatagridTitleRowCheckBox("HGST_QOS_CLASSIFICATION_TYPE");
	return arr;	
}

function updateClassifyRule() {
	var getData = {type:"GET",
					path:"hbus://mdm/InternetGatewayDevice.X_CMCC_UplinkQoS.Classification.{i}.", 
					msgType:211, 
					userTagData:1};

	hgsUpdateData(getData,function (data) {
		$("#classifyRule").find("option").remove();//delete all options
		//add option to classifyRule
		for (let i = 0; i < data.length; i++) {
			var idx = i+1;
			var objId = data[i].fullPath.match(/\d+/)[0];
			$("#classifyRule").append("<option value=" + objId + ">" + idx +"</option>");
		}
	})	
}
$("#context [page=network] [target_page=qos]").click(function () {
	updateClassifyRule();
})
$("#classifyRule").change(function () {
	var objId = $("#classifyRule").val();	
	var pathStr = "hbus://mdm/InternetGatewayDevice.X_CMCC_UplinkQoS.Classification.{i}.type.{i}.";
	var getData = {type:"GET",
					path:pathStr, 
					msgType:211, 
					userTagData:1};

	var id = "HGST_QOS_CLASSIFICATION_TYPE";
	hgsUpdateData(getData, function (result) {
		var j=0;
		var arr = [];
		for (let i = 0; i < result.length; i++) {
			var classificationId = result[i].fullPath.match(/\d+/)[0];
			if (classificationId == objId) {
				if (result[i].Type == "") {
					result[i].Type = "NULLType";
				}
				else if (result[i].Type == "WANInterface" || result[i].Type == "LANInterface") {
					if (result[i].Max != "") {
						var tmpmax = result[i].Max.substr(result[i].Max.length-1,1);
						if(tmpmax != "."){
							result[i].Max = result[i].Max +".";
						}
					}
					if (result[i].Min != "") {
						var tmpmin = result[i].Min.substr(result[i].Min.length-1,1);
						if(tmpmin != "."){
							result[i].Min = result[i].Min +".";
						}
					}	
				}

				arr[j++] = result[i];
			}
		}
		
		classifyType_qos = arr;
		var tableData = {total:arr.length, rows:arr};
		setTimeout(function () {
			if (result.length) {
				var dg = $("#" + getTableIdByHgstId("HGST_QOS_CLASSIFICATION_TYPE"));
				dg.datagrid("checkRow",0);
			}		
		}, 500);
		generateTable(id, g_tableRules[id], tableData);	
		resizeSubNavContentHeight();
	});
})

qosClassificationTypeCreate = function () {
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_CLASSIFICATION_TYPE"));

	rowsData = dg.datagrid("getRows");
	removeDatagridTitleRowCheckBox("HGST_QOS_CLASSIFICATION_TYPE");
	if(rowsData.length > 0){		
		if(!rowsData[rowsData.length - 1].fullPath){
			alert("You can only create a new line at a time, please save before creating a new one!")
			return;
		}			
	}

	dg.datagrid('appendRow',{Type:"", Max:"", Min:"", ProtocolList:""});
	rows = dg.datagrid("getRows").length;
	qosClassificationTypeEditRow(rows - 1, true);

	resizeSubNavContentHeight();
}

qosClassificationTypeDelete = function () {
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_CLASSIFICATION_TYPE"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}
	tableCheckedData = CheckedData[0];
	
	postData = {type:"POST",
		commitData:{para:""}
	};
	
	if(tableCheckedData.fullPath){
		postData.msgType = 216;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{
		rowIndex = dg.datagrid("getRowIndex", CheckedData[0]);
		dg.datagrid("deleteRow", rowIndex);
		return;
	}

	postData.commitData.path = postData.path;
	hgsUpdateData(postData,function(result){
		if(IS_LOG_DATA_ENABLE()){
			LOG_DATA("server response:");
			console.log(result); 
		}
		qosClassificationTypeUpdate();
	})
}

qosClassificationTypeUpdate = function () {
	loadTableData("HGST_QOS_CLASSIFICATION_TYPE");
}

qosClassificationTypeCheckRow = function (index,row) {
	qosClassificationTypeEditRow(index, false);
}

function getlanInfo(data) {
	var lanInfo = [], wlanInfo = [];
	var wlanPath = [], lanPath=[];

	for(var i in data){
		const fullPath = data[i].fullPath.replace(/\.[0-9]*\./g, ".{i}.");

		if (fullPath == "InternetGatewayDevice.LANDevice.{i}.LANEthernetInterfaceConfig.{i}.") {
			lanInfo.push(data[i]);
		} 
		else if (fullPath == "InternetGatewayDevice.LANDevice.{i}.WLANConfiguration.{i}.") {
			wlanInfo.push(data[i]);
		}
	}

	for (var i = 1; i <= lanInfo.length; i++) {
		const objtmp = {};
		objtmp.Name = "LAN"+i;
		objtmp.Interface = lanInfo[i-1].fullPath;
		lanPath.push(objtmp);
	}
	
	for (var i=1; i<=wlanInfo.length; i++) {
		const obj = {};
		obj.Name = "SSID"+i;
		obj.Interface = wlanInfo[i-1].fullPath;
		wlanPath.push(obj);
	}

	lanPath.push.apply(lanPath,wlanPath);
	return lanPath;
}

function qosClassificationTypeEditRow(index, checkRow){
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_CLASSIFICATION_TYPE"));

	rows = dg.datagrid("getRows").length;
	/* for(r = 0; r < rows;r++){
		dg.datagrid("endEdit", r);
	} */

	dg.datagrid("beginEdit", index);

	if(checkRow){
		dg.datagrid('checkRow', index);
	}

	var ed = dg.datagrid("getEditor", {index:index, field:"Type"});
	var edMax = dg.datagrid("getEditor", {index:index, field:"Max"});
	var edMin = dg.datagrid("getEditor", {index:index, field:"Min"});
	var edPro = dg.datagrid("getEditor", {index:index, field:"ProtocolList"});
	var arr = [];

	$(ed.target).combobox({
		onSelect:function (record) {
			var type = dg.datagrid("getRows")[index].Type;
			var max = dg.datagrid("getRows")[index].Max;
			var min = dg.datagrid("getRows")[index].Min;
			
			if (record.Type == "WANInterface") {
				$(edMax.target).combobox("loadData",wanPath_qos);
				$(edMin.target).combobox("loadData",wanPath_qos);
				if (!wanPath_qos.length) {
					alert("There is no valid WAN connection. You need to establish a WAN connection first!");
					$(edMax.target).combobox("setValue","");
					$(edMin.target).combobox("setValue","");
					return;
				}else{
					setTimeout(function () {
						if (type == "WANInterface") {
							$(edMax.target).combobox("setValue",max);
							$(edMin.target).combobox("setValue",min);
						} else {
							$(edMax.target).combobox("setValue",wanPath_qos[0]);
							$(edMin.target).combobox("setValue",wanPath_qos[0]);	
						}	
					}, 300);
				}
			}
			else if (record.Type == "LANInterface") {
				$(edMax.target).combobox("loadData", lanPath_qos);
				$(edMin.target).combobox("loadData", lanPath_qos);
				setTimeout(function () {
					if (type == "LANInterface") {
						$(edMax.target).combobox("setValue",max);
						$(edMin.target).combobox("setValue",min);
					} else {
						$(edMax.target).combobox("setValue",lanPath_qos[0]);
						$(edMin.target).combobox("setValue",lanPath_qos[0]);	
					}	
				},300);
			}
			else if (record.Type == "IPVERSION") {
				var maxMinData = [
					{"Name":"4", "Interface":"4"},
					{"Name":"6", "Interface":"6"}
				];

				$(edMax.target).combobox("loadData", maxMinData);
				$(edMin.target).combobox("loadData", maxMinData);
				setTimeout(function () {
					if (type == "IPVERSION") {
						$(edMax.target).combobox("setValue",max);
						$(edMin.target).combobox("setValue",min);	
					} else {
						$(edMax.target).combobox("setValue",maxMinData[0]);
						$(edMin.target).combobox("setValue",maxMinData[0]);
					}	
				}, 300);
			}
			else {
				$(edMax.target).combobox("loadData", arr);
				$(edMin.target).combobox("loadData", arr);
				if (type == record.Type) {
					$(edMax.target).combobox("setValue",max);
					$(edMin.target).combobox("setValue",min);
				} 
			}
			
			// $(edMax.target).combobox("setValue","");
			// $(edMin.target).combobox("setValue","");
		},
		onChange:function (newValue, oldValue) {
			var columns = g_tableRules["HGST_QOS_CLASSIFICATION_TYPE"]["easyui"]["columns"][0];
			var found = false;

			for(x in columns){
				if(columns[x].field == "Type"){
					if(columns[x]["editor"]["options"]["data"].length > 0){
						var typeData = columns[x]["editor"]["options"]["data"];
						for (let i = 0; i < typeData.length; i++) {
							if (typeData[i].Type == newValue) {
								found = true;
								break;
							}
						}
					}
					break;
				}
			}

			if (!found) {
				alert("All valid values ​​are listed in the drop-down box. Please click on the drop-down box and select from them!");
				$(ed.target).combobox("setValue","NULLType");
			}
		}
	});
	$(edMax.target).combobox({
		onChange:function (newValue, oldValue) {
			var found = false;
			var type = $(ed.target).combobox("getValue");

			if (type == "WANInterface") {
				/* for (var i in wanPath_qos) {
					if (wanPath_qos[i].Interface == newValue || newValue == "") {
						found = true;	
						break;
					}
				} */
			}
			else if (type == "LANInterface") {
				for (var i in lanPath_qos) {
					if (lanPath_qos[i].Interface == newValue || newValue == "") {
						found = true;
						break;	
					} 
				}
			}
			else if (type == "IPVERSION") {
				if (newValue == 4 || newValue == 6 || newValue == "") {
					found = true;
				}
			}

		//	if (type == "WANInterface" || type == "LANInterface" || type == "EtherType") {
			if (type == "LANInterface" || type == "IPVERSION") {
				if (!found) {
					alert("All valid values ​​are listed in the drop-down box. Please click on the drop-down box and select from them!");
					$(edMax.target).combobox("setValue","");
				}	
			}
		}
	});
	$(edMin.target).combobox({
		onChange:function (newValue, oldValue) {
			var found = false;
			var type = $(ed.target).combobox("getValue");

			if (type == "WANInterface") {
				/* for (var i in wanPath_qos) {
					if (newValue == wanPath_qos[i].Interface || newValue == "") {
						found = true;	
						break;
					}
				} */
			}
			else if (type == "LANInterface") {
				for (var i in lanPath_qos) {
					if (newValue == lanPath_qos[i].Interface || newValue == "") {
						found = true;	
						break;
					} 
				}
			}
			else if (type == "IPVERSION") {
				if (newValue == 4 || newValue == 6 || newValue == "") {
					found = true;
				}
			}

			//if (type == "WANInterface" || type == "LANInterface" || type == "EtherType") {
			if (type == "LANInterface" || type == "IPVERSION") {
				if (!found) {
					alert("All valid values ​​are listed in the drop-down box. Please click on the drop-down box and select from them!");
					$(edMin.target).combobox("setValue","");
				}	
			}
		}
	});
	$(ed.target).combobox("setValue",ed.oldHtml);	
}

qosClassificationTypeFullInfoShow = function(data){
	$('#qosClassificationTypeInfoPopDlg').dialog('open');
	loadTableData("HGST_QOS_CLASSIFICATION_TYPE_FULL_INFO");
}

qosClassificationTypeFullInfoCheckout = function(data){
	var j=0, k=0, z=0;
	var arr = [];
	
	arr = JSON.parse(JSON.stringify(classifyType_qos));

	for(var i in arr){
		if (arr[i].Type == "WANInterface" || arr[i].Type == "LANInterface") {
			if(arr[i].Max != ""){
				var tmpmax = arr[i].Max.substr(arr[i].Max.length-1,1) ;
				if(tmpmax != "."){
					arr[i].Max = arr[i].Max +".";
				}
			}
			if (arr[i].Min != "") {
				var tmpmin = arr[i].Min.substr(arr[i].Min.length-1,1) ;
				if(tmpmin != "."){
					arr[i].Min = arr[i].Min +".";
				}
			}	
		}
	}
	for (i = 0; i < arr.length; i++) {
		if (arr[i].Type == "WANInterface") {
			for (k = 0; k < wanPath_qos.length; k++) {
				if (arr[i].Max == wanPath_qos[k].Interface) {
					arr[i].Max = wanPath_qos[k].Name;
				}
				if (arr[i].Min == wanPath_qos[k].Interface) {
					arr[i].Min = wanPath_qos[k].Name;
				}
			}
		}
		else if (arr[i].Type == "LANInterface") {
			for (k = 0; k < lanPath_qos.length; k++) {
				if (arr[i].Max == lanPath_qos[k].Interface) {
					arr[i].Max = lanPath_qos[k].Name;
				}
				if (arr[i].Min == lanPath_qos[k].Interface) {
					arr[i].Min = lanPath_qos[k].Name;
				}
			}
		}
	}

	return arr;
}

qosAppCheckin = function (objName, tableId, data, postData) {
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_APP"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}

	rowsData = dg.datagrid("getRows");
	if (rowsData.length == 2) {
		if (rowsData[0].AppName == rowsData[1].AppName) {
			alert("The business is repeated, please reset it!");
			return true;
		}
	}
	tableCheckedData = CheckedData[0];
	
	postData.type = "POST";
	postData.commitData = {para:{AppName:tableCheckedData.AppName, ClassQueue:tableCheckedData.ClassQueue}};
	
	if(tableCheckedData.fullPath){
		postData.msgType = 212;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{		
		postData.msgType = 215;
		postData.path = "hbus://mdm/InternetGatewayDevice.X_CMCC_UplinkQoS.App.{i}.";
	}

	postData.commitData.path = postData.path;
	setTimeout(qosAppUpdate, 1000);	 
}

qosAppCheckRow = function(index,row){
	qosAppEditRow(index, false);
}

function qosAppEditRow(index, checkRow){
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_APP"));

	rows = dg.datagrid("getRows").length;
	for(r = 0; r < rows;r++){
		dg.datagrid("endEdit", r);
	}

	dg.datagrid("beginEdit", index);

	if(checkRow){
		dg.datagrid('checkRow', index);
	}
}

qosAppCreate = function () {
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_APP"));

	rowsData = dg.datagrid("getRows");
	if(rowsData.length > 0){
		if (rowsData.length == 2) {
			alert("There are only two businesses at most and no more can be added!");
			return;
		}
		if(!rowsData[rowsData.length - 1].fullPath){
			alert("You can only create a new line at a time, please save before creating a new one!")
			return;
		}			
	}

	dg.datagrid('appendRow',{AppName:"", ClassQueue:""});
	rows = dg.datagrid("getRows").length;
	qosAppEditRow(rows - 1, true);

	resizeSubNavContentHeight();
}

qosAppDelete = function () {
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_APP"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}
	tableCheckedData = CheckedData[0];
	
	postData = {type:"POST",
		commitData:{para:""}
	};
	
	if(tableCheckedData.fullPath){
		postData.msgType = 216;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{
		rowIndex = dg.datagrid("getRowIndex", CheckedData[0]);
		dg.datagrid("deleteRow", rowIndex);
		return;
	}

	postData.commitData.path = postData.path;
	hgsUpdateData(postData,function(result){
		if(IS_LOG_DATA_ENABLE()){
			LOG_DATA("server response:");
			console.log(result); 
		}
		qosAppUpdate();
	})
}

qosAppUpdate = function () {
	loadTableData("HGST_QOS_APP");
	removeDatagridTitleRowCheckBox("HGST_QOS_APP");
}

qosAppOnLoadSuccess = function(){
	removeDatagridTitleRowCheckBox("HGST_QOS_APP");
}

function priorityQueueEditRow(index, checkRow){
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_PRIORITY_QUEUE"));

	rows = dg.datagrid("getRows").length;
	/* for(r = 0; r < rows;r++){
		dg.datagrid("endEdit", r);
	} */

	dg.datagrid("beginEdit", index);

	if(checkRow){
		dg.datagrid('checkRow', index);
	}
}

priorityQueueCreate = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_PRIORITY_QUEUE"));

	rowsData = dg.datagrid("getRows");
	removeDatagridTitleRowCheckBox("HGST_QOS_PRIORITY_QUEUE");
	if(rowsData.length > 0){
		if(!rowsData[rowsData.length - 1].fullPath){
			alert("You can only create a new line at a time, please save before creating a new one!")
			return;
		}
	}
	
	dg.datagrid('appendRow',{Enable:""});
	rows = dg.datagrid("getRows").length;
	priorityQueueEditRow(rows - 1, true);

	resizeSubNavContentHeight();
}

priorityQueueDelete = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_PRIORITY_QUEUE"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}
	tableCheckedData = CheckedData[0];
	
	postData = {type:"POST",
		commitData:{para:""}
	};
	
	if(tableCheckedData.fullPath){
		postData.msgType = 216;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{
		rowIndex = dg.datagrid("getRowIndex", CheckedData[0]);
		dg.datagrid("deleteRow", rowIndex);
		return;
	}

	postData.commitData.path = postData.path;
	hgsUpdateData(postData,function(result){
		if(IS_LOG_DATA_ENABLE()){
			LOG_DATA("server response:");
			console.log(result); 
		}
		priorityQueueUpdate();
	})
}

priorityQueueUpdate = function(){
	loadTableData("HGST_QOS_PRIORITY_QUEUE");
	removeDatagridTitleRowCheckBox("HGST_QOS_PRIORITY_QUEUE");
}

priorityQueueClickRow = function(index,row){
	priorityQueueEditRow(index, true);
}

priorityQueueCheckRow = function(index,row){
	priorityQueueEditRow(index, false);
}

priorityQueueCheckout = function (data) {
	for (var i = 0; i < data.length; i++) {
		data[i].queue = i+1;
	}
	
	removeDatagridTitleRowCheckBox("HGST_QOS_PRIORITY_QUEUE");
	return data;
}

priorityQueueCheckin = function(objName, tableId, data, postData){
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_PRIORITY_QUEUE"));

	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select a row and save!");
		return true;
	}

	tableCheckedData = CheckedData[0];
	
	postData.type = "POST";
	postData.commitData = {para:{Enable:tableCheckedData.Enable}};
	
	if(tableCheckedData.fullPath){
		postData.msgType = 212;
		postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
	}else{		
		postData.msgType = 215;
		postData.path = "hbus://mdm/InternetGatewayDevice.X_CMCC_UplinkQoS.PriorityQueue.{i}.";
	}

	postData.commitData.path = postData.path;
	setTimeout(priorityQueueUpdate, 1000);
}

$("#context [page=qos] [hgs_sub_nav=upstream_qos_priority_queue]").click(function () {
	if ($("#HGS_QOS_CFG [hgs_key=Plan]").val() == "priority") {		
		$("#qosPriorityQueue").show();
		$("#qosPriorityQueueWeight").hide();
	} else {
		$("#qosPriorityQueue").hide();
		$("#qosPriorityQueueWeight").show();
	}	
})

function priorityQueueWeightEditRow(index, checkRow){
	var dg = $("#" + getTableIdByHgstId("HGST_QOS_PRIORITY_QUEUE_WEIGHT"));

	rows = dg.datagrid("getRows").length;
	for(r = 0; r < rows;r++){
		dg.datagrid("endEdit", r);
	}

	dg.datagrid("beginEdit", index);

	if(checkRow){
		dg.datagrid('checkRow', index);
	}
}

priorityQueueWeightCheckRow = function(index,row){
	priorityQueueWeightEditRow(index, false);
}

priorityQueueWeightUpdate = function () {
	loadTableData("HGST_QOS_PRIORITY_QUEUE_WEIGHT");
}

priorityQueueWeightCheckout = function (data) {
	for (var i = 0; i < data.length; i++) {
		data[i].queue = i+1;
	}
	
	return data;
}
priorityQueueWeightCheckin = function (objName, data) {
	var WeightSum = 0;

	for (let i = 0; i < data.length; i++) {
		const element = data[i];
		if (element.Enable == "1") {
			WeightSum += parseInt(element.Weight);
		}

		delete element.queue;
	}

	if (WeightSum != 100) {
		alert("The sum of the weights of enabled queues should equal 100%!");
		return true;
	}

	return data;
}

SpeedLimitModeChange = function (mode) {	
	switch (mode) {
		case 0:
			$("#interfaceLimit").hide();
			$("#vlanTagLimit").hide();
			$("#iPLimit").hide();
			break;
		case 1:
			$("#interfaceLimit").show();
			$("#vlanTagLimit").hide();
			$("#iPLimit").hide();
			break;
		case 2:
			$("#interfaceLimit").hide();
			$("#vlanTagLimit").show();
			$("#iPLimit").hide();
			break;
		case 3:
			$("#interfaceLimit").hide();
			$("#vlanTagLimit").hide();
			$("#iPLimit").show();
			break;							
		default:
			break;
	}
}
	
SpeedLimitModeChangeDown = function (mode) {	
	switch (mode) {
		case 0:
			$("#interfaceLimit_down").hide();
			$("#vlanTagLimit_down").hide();
			$("#iPLimit_down").hide();
			break;
		case 1:
			$("#interfaceLimit_down").show();
			$("#vlanTagLimit_down").hide();
			$("#iPLimit_down").hide();
			break;
		case 2:
			$("#interfaceLimit_down").hide();
			$("#vlanTagLimit_down").show();
			$("#iPLimit_down").hide();
			break;
		case 3:
			$("#interfaceLimit_down").hide();
			$("#vlanTagLimit_down").hide();
			$("#iPLimit_down").show();
			break;							
		default:
			break;
	}
}

$("#SpeedLimitMode_UP").change(function(){
	var mode = $("#SpeedLimitMode_UP").val();
	SpeedLimitModeChange(parseInt(mode));
})

$("#SpeedLimitMode_DOWN").change(function(){
	var mode = $("#SpeedLimitMode_DOWN").val();
	SpeedLimitModeChangeDown(parseInt(mode));
})
	
qosSpeedLimitCheckout = function (data) {
	var mode = data.SpeedLimitMode_UP;
	SpeedLimitModeChange(parseInt(mode));
}
qosSpeedLimitDownCheckout = function (data) {
	var mode = data.SpeedLimitMode_DOWN;
	SpeedLimitModeChangeDown(parseInt(mode));
}
qosSpeedLimitCheckin = function (data) {
	var commitData = {};
	switch (data.SpeedLimitMode_UP) {
		case 1:
			var interfaces = ["LAN1","LAN2","LAN3","LAN4","SSID1","SSID2","SSID3","SSID4","SSID5","SSID6","SSID7","SSID8"];
			var speed = data.InterfaceLimit_UP.split(",");
			for (var i = 0; i < speed.length; i++) {
				const element = speed[i].split("/");
				if (element.length != 2) {
					alert("The rate is illegal, please re-enter!");
					return;
				} else {
					if ($.inArray(element[0], interfaces) == -1) {
						alert("The user interface is illegal, please re-enter!");
						return;
					}
					if (!element[1] || isNaN(element[1])) {
						alert("The rate is illegal, please re-enter!");
						return;
					}
					if (parseFloat(element[1]) < 0) {
						alert("The rate cannot be a negative number, please re-enter!");
						return;
					}
				}
			}
			break;
		case 2:
			var speed = data.VlanTagLimit_UP.split(",");
			for (var i = 0; i < speed.length; i++) {
				const element = speed[i].split("/");
				if (element.length != 2) {
					alert("The rate is illegal, please re-enter!");
					return;
				} else {					
					if (!element[0] || isNaN(element[0]) || !element[1] || isNaN(element[1])) {
						alert("The rate is illegal, please re-enter!");
						return;
					}
					if (element[0] < 1 || element[0] > 4094) {
						alert("The valid value of VLANID is 1-4094, please re-enter!");
						return;
					}
					if (parseFloat(element[1]) < 0) {
						alert("The rate cannot be a negative number, please re-enter!");
						return;
					}
				}
			}				
			break;
		case 3:
			var speed = data.IPLimit_UP.split(",");
			for (var i = 0; i < speed.length; i++) {
				const element = speed[i].split("/");
				if (element.length != 2) {
					alert("The rate is illegal, please re-enter!");
					return;
				} else {
					var ip = element[0].split("-");
					if (ip.length != 2) {
						alert("The ip is illegal, it should be the ip1-ip2 address segment!");
					} else {						
						var err1 = strategies.isValidIP(ip[0],"The ip address is illegal!");
						var err2 = strategies.isValidIPv6(ip[0],"The ip address is illegal!");
						var err3 = strategies.isValidIP(ip[1],"The ip address is illegal!");
						var err4 = strategies.isValidIPv6(ip[1],"The ip address is illegal!");
						if ((err1 && err2) || (!err1 && err3) || (!err2 && err4)) {
							alert("The ip address is illegal!");
							return;
						}						
					}

					if (!element[1] || isNaN(element[1])) {
						alert("The rate is illegal, please re-enter!");
						return;
					}
					if (parseFloat(element[1]) < 0) {
						alert("The rate cannot be a negative number, please re-enter!");
						return;
					}
				}
			}	
			break;
				
		default:
			break;
	}
	return data;
}

qosSpeedLimitDownCheckin = function (data) {
	var commitData = {};
	switch (data.SpeedLimitMode_DOWN) {
		case 1:
			var interfaces = ["LAN1","LAN2","LAN3","LAN4","LAN5","LAN6","SSID1","SSID2","SSID3","SSID4","SSID5","SSID6","SSID7","SSID8"];
			var speed = data.InterfaceLimit_DOWN.split(",");
			for (var i = 0; i < speed.length; i++) {
				const element = speed[i].split("/");
				if (element.length != 2) {
					alert("The rate is illegal, please re-enter!");
					return;
				} else {
					if ($.inArray(element[0], interfaces) == -1) {
						alert("The user interface is illegal, please re-enter!");
						return;
					}
					if (!element[1] || isNaN(element[1])) {
						alert("The rate is illegal, please re-enter!");
						return;
					}
					if (parseFloat(element[1]) < 0) {
						alert("The rate cannot be a negative number, please re-enter!");
						return;
					}
				}
			}
			break;
		case 2:
			var speed = data.VlanTagLimit_DOWN.split(",");
			for (var i = 0; i < speed.length; i++) {
				const element = speed[i].split("/");
				if (element.length != 2) {
					alert("The rate is illegal, please re-enter!");
					return;
				} else {					
					if (!element[0] || isNaN(element[0]) || !element[1] || isNaN(element[1])) {
						alert("The rate is illegal, please re-enter!");
						return;
					}
					if (element[0] < 1 || element[0] > 4094) {
						alert("The valid value of VLANID is 1-4094, please re-enter!");
						return;
					}
					if (parseFloat(element[1]) < 0) {
						alert("The rate cannot be a negative number, please re-enter!");
						return;
					}
				}
			}				
			break;
		case 3:
			var speed = data.IPLimit_DOWN.split(",");
			for (var i = 0; i < speed.length; i++) {
				const element = speed[i].split("/");
				if (element.length != 2) {
					alert("The rate is illegal, please re-enter!");
					return;
				} else {
					var ip = element[0].split("-");
					if (ip.length != 2) {
						alert("The ip is illegal, it should be the ip1-ip2 address segment!");
					} else {						
						var err1 = strategies.isValidIP(ip[0],"The ip address is illegal!");
						var err2 = strategies.isValidIPv6(ip[0],"The ip address is illegal!");
						var err3 = strategies.isValidIP(ip[1],"The ip address is illegal!");
						var err4 = strategies.isValidIPv6(ip[1],"The ip address is illegal!");
						if ((err1 && err2) || (!err1 && err3) || (!err2 && err4)) {
							alert("The ip address is illegal!");
							return;
						}						
					}

					if (!element[1] || isNaN(element[1])) {
						alert("The rate is illegal, please re-enter!");
						return;
					}
					if (parseFloat(element[1]) < 0) {
						alert("The rate cannot be a negative number, please re-enter!");
						return;
					}
				}
			}	
			break;
				
		default:
			break;
	}
	return data;
}
	
/*----------------------------------------------------------------------------*/

ddnsUpdate = function(data){
	var newData = {};
	var WanInfo = [];

	for(r in data){
		if(typeof data[r].DDNSProvider != "undefined"){
			newData = data[r];
			/*
			if (data[r].DDNSCfgEnabled == "FALSE") { 
				data[r].DDNSCfgEnabled = 0;
			}
			else
			{
				data[r].DDNSCfgEnabled = 1;
			}
			*/
		}else{
			WanInfo.push({WanName:data[r].Name, WanPath:data[r].fullPath.substr(0, data[r].fullPath.length - "Name".length)});
		}
	}

	var innerHtml = "";
	for(i in WanInfo){
		innerHtml += "<option value='" + WanInfo[i].WanName  + "' >" + WanInfo[i].WanName + "</option>";
	}

	$("#ddnsSelectWan").html(innerHtml);

	return newData;
}
/*----------------------------------------------------------------------------*/
function isUnsafePasswdChar(compareChar){
	// var unsafeString = "\"<>%\\^[]`\+\$\,'#&;()";
	var unsafeString = "\"\\";		
	if ( unsafeString.indexOf(compareChar) == -1 && compareChar.charCodeAt(0) > 32 && compareChar.charCodeAt(0) < 127)
		return false;
	// found no unsafe chars, return false
	else
		return true;
}

function processSpecialChars(str){
	var i = 0;
	var retStr = '';

	for ( i = 0; i < str.length; i++)
	{
		if (isUnsafePasswdChar(str.charAt(i)) == true)
			retStr += '\\';
		retStr += str.charAt(i);
	}
	
	return retStr;
}

var g_modifyUserAccount = false;

userAccountCheckin = function(path, data){
	var para = data.commitData.para;
	if(para.UserOldPassword.length == 0){
		alert("[User old password] cannot be empty!");
		$('#HGS_USER_ACCOUNT [hgs_key="UserOldPassword"]').focus();
		return true;
	}
	if(para.UserNewPassword.length == 0){
		alert("【User new password】cannot be empty!");
		$('#HGS_USER_ACCOUNT [hgs_key="UserNewPassword"]').focus();
		return true;
	}
	if(para.ConfirmUserNewPwd.length == 0){
		alert("[Confirm new user password] cannot be empty!");
		$('#HGS_USER_ACCOUNT [hgs_key="ConfirmUserNewPwd"]').focus();
		return true;
	}
	if(para.UserNewPassword != para.ConfirmUserNewPwd){
		$('#HGS_USER_ACCOUNT [hgs_key="ConfirmUserNewPwd"]').focus();
		alert("[User New Password] and [Confirm User New Password] are inconsistent!");
		return true;
	}

	if (g_staticInfo["Region"] != "Sichuan") {
		if(para.UserNewPassword == para.UserOldPassword){
			$('#HGS_USER_ACCOUNT [hgs_key="UserNewPassword"]').focus();
			alert("[User New Password] and [User Old Password] cannot be exactly the same!");
			return true;
		}
	}

	if (para.ConfirmUserNewPwd.length < 8) {
		alert('[User new password] length cannot be less than 8 characters!');
		return true;		
	}

	if (isValidLoginPasswd(para.UserNewPassword) == false) {
		alert('[User new password] must contain letters, numbers and special characters, without spaces!');
		return true;
	}

	para.UserNewPassword = processSpecialChars(para.UserNewPassword);
	para.UserOldPassword = window.btoa(processSpecialChars(para.UserOldPassword));
	para.UserNewPassword = window.btoa(para.UserNewPassword);
	para.ConfirmUserNewPwd = undefined; 
	
	if(para.UserName == "user"){
		// data.path = "hbus://mdm/InternetGatewayDevice.X_BROADCOM_COM_LoginCfg.";
		// data.commitData.path = data.path;
		g_modifyUserAccount = true;
	}else{
		g_modifyUserAccount = false;
	}

	data.waitTimeoutMs = 5000;
}

userAccountResp = function(data){
	var flag = false;
	switch(data.retCode){
		case 0:
			if(g_adminAccount && g_modifyUserAccount){
				alert("User password modified successfully");
				if (g_staticInfo["Region"] != "Sichuan") {
					$("#HGS_USER_ACCOUNT [hgs_key=UserOldPassword]").val("");
				}
				$("#HGS_USER_ACCOUNT [hgs_key=UserNewPassword]").val("");
				$("#HGS_USER_ACCOUNT [hgs_key=ConfirmUserNewPwd]").val("");
			}else{
				alert("The password has been changed successfully, and you will be redirected to the login page!");
			}
			break;
		case 1:
			alert("【User old password】Error!");
			flag = true;
			break;
		case 2:
			alert("[User New Password] and [User Old Password] cannot be exactly the same!");
			flag = true;
			break;
	}

	if (flag) {
		return;
	}

	if ((false == g_adminAccount) && (true == g_modifyUserAccount)) {
		$.get("/logout");
		setTimeout(function (params) {
			window.location.href = LOGIN_PAGE;
		},100);
	}
}

userAccountCheckout = function(data){
	var newData = {};
	var AccountInfo = [];
	for(r in data){
		newData = data[r];
		AccountInfo.push({UserName:data[r].UserName});
	}

	var innerHtml = "";
	for(i in AccountInfo){
		innerHtml += "<option value='" + AccountInfo[i].UserName  + "' >" + AccountInfo[i].UserName + "</option>";
	}

	$("#accountSelect").html(innerHtml);
	
	if (g_staticInfo["Region"] =="Sichuan"){
		hgsUpdateData({type:"GET", url:"/factoryPara"}, function(data){
			$("#oldPassword").val(data.userpassword);
		})
	}

	return newData;
}
/*----------------------------------------------------------------------------*/
rebootCheckIn = function(data){
	if(confirm("The device will be restarted! It will take about 50 seconds to restart the device. Are you sure to [restart the device]?")){
		return;
	}

	return true;
}

scheRebootCheckin = function (data) {
	//2.0000
	if ($("#enableSche").is(':checked')) {
		if (data.Interval.indexOf('.') != -1) {
			alert("The number of days should be a positive integer");
			return;
		}
		if (data.Interval < 1 || data.Interval != parseInt(data.Interval)) {
			alert("The number of days should be a positive integer");
			return;
		}
	}

	return data;
}

enableScheduleReboot = function () {
	if ($("#enableSche").is(':checked')) {
		$("#rebootInterval").show();
		$("#rebootTime").show();
		$("#rebootForceFlow").show();
	}else{
		$("#rebootInterval").hide();
		$("#rebootTime").hide();
		$("#rebootForceFlow").hide();
	}	
}
$("#enableSche").click(function () {
	enableScheduleReboot();
})

scheRebootCheckout = function () {
	enableScheduleReboot();
}

rebootResp = function(data){
	if(0 == data.retCode){
		window.location.href = "/reboot.html";
		//alert("Restarting the device, please wait patiently for 40 seconds!");
	}else{
		alert("Restarting the device failed! Error code:" + data.retCode);
	}
}

restoreDefCheckIn = function(data){
	if(confirm("Restoring the default configuration will cause the device to restart! It takes about 50 seconds to restart the device. Are you sure to [Restore the default configuration]?")){
		return;
	}
	
	return true;
}

restoreDefResp = function(data){
	if(0 == data.retCode){
		alert("The default configuration has been restored successfully! The device is restarting, please wait patiently for 40 seconds!");
	}else{
		alert("Failed to restore default configuration! Error code:" + data.retCode);
	}
}

restoreFacCheckIn = function(data){
	if(confirm("Restoring factory settings will cause the device to restart! It takes about 40 seconds to restart the device. Are you sure to [Restore factory settings]?")){
		return;
	}
	
	return true;
}

restoreFacResp = function(data){
	if(0 == data.retCode){
		alert("Factory reset successful! Restarting the device, please wait patiently for 40 seconds!");
	}else{
		alert("Restoring factory settings failed! Error code:" + data.retCode);
	}
}
/*----------------------------------------------------------------------------*/

OnuAuthTypeChange = function(){
	switch($("#OnuAuthType").val()){
		case "1":
			$("#OnuPasswordRow").show();
			$("#OnuLoidRow").hide();
			break;

		case "2":
			$("#OnuPasswordRow").hide();
			$("#OnuLoidRow").show();
			break;

		case "3":
			$("#OnuPasswordRow").show();
			$("#OnuLoidRow").show();
			break;
	}
}

$("#OnuAuthType").change(function(){
	OnuAuthTypeChange();
})

onuCfgCheckin = function(data){
	var passwd = $("#OnuPasswordRow [hgs_key=Password]").val();
	var len;

	if (g_staticInfo["ProductType"] == "XGPON") {
		len = 36;
	} else {
		len = 10;
	}	

	switch($("#OnuAuthType").val()){
		case "1":
			if (passwd.length > len) {
				alert("The password must be at least 1 character long and at most"+len+"characters!");
				return;
			}
			data.UserName = "";
			break;

		case "2":
			data.Password = "";
			break;

		case "3":
			if (passwd.length > len) {
				alert("The password must be at least 1 character long and at most"+len+"characters!");
				return;
			}
			break;
	}

	setTimeout(function(){
		loadHbusData("HGS_ONU_PASSWORD");
	}, 2000)
	return data;
}
/*----------------------------------------------------------------------------*/
onuRegisterEnforceCheckin = function (data) {
	var hgConfigObj = {};
	if(data.RegisterForcePush) {
		data.RegisterForcePush = 1;
	}else {
		data.RegisterForcePush = 0;
	}

	return data;
}


onuRegisterEnforceCheckout = function (data) {
	var flag = false;
	if (data.RegisterForcePush == '1') {
		flag = true;
	} else if (data.RegisterForcePush == '0') {
		flag = false;
	}
	data.RegisterForcePush = flag;

	return data;
}
/*----------------------------------------------------------------------------*/
timeManageCheckin = function (data) {
	setTimeout(function () {
		loadHbusData("HGS_TIME_MANAGE");	
	},1000);
	
	return data;
}
/*----------------------------------------------------------------------------*/

getWanInfo = function(data){
	var wanInfo = [];

	for(var i in data){
		fullPath = data[i].fullPath.replace(/\.[0-9]*\./g, ".{i}.");
		if((fullPath != "InternetGatewayDevice.WANDevice.{i}.WANConnectionDevice.{i}.WANIPConnection.{i}.")
			&&(fullPath != "InternetGatewayDevice.WANDevice.{i}.WANConnectionDevice.{i}.WANPPPConnection.{i}.")){
			continue;
		}
		if(data[i].Name){
			wanInfo.push({Name:data[i].Name, Interface:data[i].fullPath, fullPath:data[i].fullPath,
				IfName:data[i].Ifname});
		}
	}

	return wanInfo.sort(strategies.sortBy('Name'));
}

/*----------------------------------------------------------------------------*/

staticRouteCheckout = function(data){
	var wanInfo = getWanInfo(data);
	var routeInfo = [], filteredArray = [];
	var found = false;

	filteredArray = wanInfo;
	if (!g_staticInfo["SupportVoip"]) {
		filteredArray = wanInfo.filter(item => !(item.Name.includes("VOIP") && !item.Name.includes("INTERNET")));
	} 
  
	for(var i in data){
		found = false;
		for(m in wanInfo){
			if(data[i].fullPath.indexOf(wanInfo[m].fullPath) == 0){
				found = true;
				break;
			}
		}
		if(!found){
			routeInfo.push(data[i]);
		}
	}

	columns = g_tableRules["HGST_STATIC_ROUTE_CFG"]["easyui"]["columns"][0];
	for(var x in columns){
		if(columns[x].field == "Interface"){
			columns[x]["editor"]["options"]["data"] = filteredArray; //.sort(strategies.sortBy("Name"));
			break;
		}
	}

	for(var i in routeInfo){
		if(routeInfo[i].Interface != "")
		{
			var tmp = routeInfo[i].Interface.substr(routeInfo[i].Interface.length-1,1) ;
			if(tmp != ".")
			{
				routeInfo[i].Interface = routeInfo[i].Interface +".";
			}
		}

	}
	return routeInfo;
}

staticRouteFullInfoCheckout = function(data){
	var wanInfo = getWanInfo(data);
	var routeInfo = [];
	var found = false;

	for(var i in data){
		found = false;
		for(m in wanInfo){
			if(data[i].fullPath.indexOf(wanInfo[m].fullPath) == 0){
				found = true;
				break;
			}
		}
		if(!found){
			routeInfo.push(data[i]);
		}
	}

	for(var i in routeInfo){
		if(routeInfo[i].Interface != "")
		{
			var tmp = routeInfo[i].Interface.substr(routeInfo[i].Interface.length-1,1) ;
			if(tmp != ".")
			{
				routeInfo[i].Interface = routeInfo[i].Interface +".";
			}
		}

	}

	for(var i in routeInfo){
		routeInfo[i].Enable = (routeInfo[i].Enable == "0") ?"no":"yes";
		for (var j in wanInfo) {
			if (routeInfo[i].Interface == wanInfo[j].Interface) {
				routeInfo[i].Interface = wanInfo[j].Name;
			}
		}
	}
		

	return routeInfo;
}

staticRouteCreate = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_STATIC_ROUTE_CFG"));
	rowsData = dg.datagrid("getRows");

	wanInfo = {};
	columns = g_tableRules["HGST_STATIC_ROUTE_CFG"]["easyui"]["columns"][0];
	for(x in columns){
		if(columns[x].field == "Interface"){
			if(columns[x]["editor"]["options"]["data"].length > 0){
				wanInfo = columns[x]["editor"]["options"]["data"][0];
			}
			break;
		}
	}
	
	dg.datagrid('appendRow', {Enable:{Enable:"1"}, Interface:wanInfo});

	rows = dg.datagrid("getRows").length;
	datagridEditRow(rows - 1, false, "HGST_STATIC_ROUTE_CFG");
	makeDatagridComboReadonly("HGST_STATIC_ROUTE_CFG");
	resizeSubNavContentHeight();

}

staticRouteCheckin = function(objName, data){
	var errMsg = "";
	for(var i in data){
		if(!data[i].fullPath){
			data[i].fullPath = "InternetGatewayDevice.Layer3Forwarding.Forwarding.{i}.";
		}
		errMsg = strategies.isValidIP(data[i].DestIPAddress, data[i].DestIPAddress + "It is illegal [Destination IP]")
		if(errMsg){
			alert(errMsg);
			return;
		}
		errMsg = strategies.isValidMask(data[i].DestSubnetMask,  data[i].DestSubnetMask + "Illegal [Destination Mask]")
		if(errMsg){
			alert(errMsg);
			return;
		}
		
		delete data[i].Type;
		delete data[i].MTU;
	}

	return data;
}

staticRouteDelete = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_STATIC_ROUTE_CFG"));
	var CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select at least one line and then [Delete]!");
		return true;
	}

	var paths = "";

	for(var i in CheckedData){
		if(i > 0){
			paths += ";";
		}
		paths += CheckedData[i].fullPath;
	}
	
	var postData = {type:"POST", url:"/delObjs", waitTimeoutMs:5000, notJson:true, commitData:paths};

	hgsUpdateData(postData,function(result){
		if(0 == result[0]){
			loadTableData("HGST_STATIC_ROUTE_CFG");
		}else{
			alert("Deletion failed! Error code:" + result[0]);
		}
	})

	return true;
}

staticRouteUpdate = function(){
	loadTableData("HGST_STATIC_ROUTE_CFG");
}

staticRouteCheckRow = function(index,row){

}

staticRouteClickRow = function(index,row){

}
staticRouteInfoFullShow = function(data){
	$('#staticRouteInfoPopDlg').dialog('open');
	loadTableData("HGST_STATIC_ROUTE_FULL_INFO");
}
/*----------------------------------------------------------------------------*/

staticIPv6RouteCheckout = function(data){
	var wanInfo = getWanInfo(data);
	var routeInfo = [], filteredArray = [];
	var found = false;

	filteredArray = wanInfo;
	if (!g_staticInfo["SupportVoip"]) {
		filteredArray = wanInfo.filter(item => !(item.Name.includes("VOIP") && !item.Name.includes("INTERNET")));
	}

	for(var i in data){
		found = false;
		for(m in wanInfo){
			if(data[i].fullPath.indexOf(wanInfo[m].fullPath) == 0){
				found = true;
				break;
			}
		}
		if(!found){
			routeInfo.push(data[i]);
		}
	}

	columns = g_tableRules["HGST_STATIC_IPV6_ROUTE_CFG"]["easyui"]["columns"][0];
	for(var x in columns){
		if(columns[x].field == "Interface"){
			columns[x]["editor"]["options"]["data"] = filteredArray; //.sort(strategies.sortBy("Name"));
			break;
		}
	}

	for(var i in routeInfo){
		if(routeInfo[i].Interface != "")
		{
			var tmp = routeInfo[i].Interface.substr(routeInfo[i].Interface.length-1,1) ;
			if(tmp != ".")
			{
				routeInfo[i].Interface = routeInfo[i].Interface +".";
			}
		}

	}
	return routeInfo;
}

staticIPv6RouteFullInfoCheckout = function(data){
	var wanInfo = getWanInfo(data);
	var routeInfo = [];
	var found = false;

	for(var i in data){
		found = false;
		for(m in wanInfo){
			if(data[i].fullPath.indexOf(wanInfo[m].fullPath) == 0){
				found = true;
				break;
			}
		}
		if(!found){
			routeInfo.push(data[i]);
		}
	}

	for(var i in routeInfo){
		if(routeInfo[i].Interface != "")
		{
			var tmp = routeInfo[i].Interface.substr(routeInfo[i].Interface.length-1,1) ;
			if(tmp != ".")
			{
				routeInfo[i].Interface = routeInfo[i].Interface +".";
			}
		}

	}
	
	for(var i in routeInfo){
		routeInfo[i].Enable = (routeInfo[i].Enable == "0") ?"no":"yes";
		for (var j in wanInfo) {
			if (routeInfo[i].Interface == wanInfo[j].Interface) {
				routeInfo[i].Interface = wanInfo[j].Name;
			}
		}
	}
	

	return routeInfo;
}

staticIPv6RouteCreate = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_STATIC_IPV6_ROUTE_CFG"));
	rowsData = dg.datagrid("getRows");

	wanInfo = {};
	columns = g_tableRules["HGST_STATIC_IPV6_ROUTE_CFG"]["easyui"]["columns"][0];
	for(x in columns){
		if(columns[x].field == "Interface"){
			if(columns[x]["editor"]["options"]["data"].length > 0){
				wanInfo = columns[x]["editor"]["options"]["data"][0];
			}
			break;
		}
	}
	
	dg.datagrid('appendRow', {Enable:{Enable:"1"}, Interface:wanInfo});

	rows = dg.datagrid("getRows").length;
	datagridEditRow(rows - 1, false, "HGST_STATIC_IPV6_ROUTE_CFG");
	makeDatagridComboReadonly("HGST_STATIC_IPV6_ROUTE_CFG");
	resizeSubNavContentHeight();

}

staticIPv6RouteCheckin = function(objName, data){
	var errMsg = "";
	for(var i in data){
		if(!data[i].fullPath){
			data[i].fullPath = "InternetGatewayDevice.X_CMCC_IPv6Layer3Forwarding.Forwarding.{i}.";
		}
		errMsg = strategies.isValidIPv6Prefix(data[i].DestIPPrefix, data[i].DestIPPrefix + "Illegal [destination IPv6 prefix]")
		if(errMsg){
			if(data[i].DestIPPrefix != "::/0"){
				alert(errMsg);
			}else{
				return data;
			}
			return;
		}

	}

	return data;
}

staticIPv6RouteDelete = function(){
	var dg = $("#" + getTableIdByHgstId("HGST_STATIC_IPV6_ROUTE_CFG"));
	CheckedData = dg.datagrid("getChecked");
	if(0 == CheckedData.length){
		alert("Please select at least one line and then [Delete]!");
		return true;
	}

	var paths = "";

	for(var i in CheckedData){
		if(i > 0){
			paths += ";";
		}
		paths += CheckedData[i].fullPath;
	}
	
	var postData = {type:"POST", url:"/delObjs", waitTimeoutMs:5000, notJson:true, commitData:paths};

	hgsUpdateData(postData,function(result){
		if(0 == result[0]){
			loadTableData("HGST_STATIC_IPV6_ROUTE_CFG");
		}else{
			alert("Deletion failed! Error code:" + result[0]);
		}
	})

	return true;
}

staticIPv6RouteUpdate = function(){
	loadTableData("HGST_STATIC_IPV6_ROUTE_CFG");
}

staticIPv6RouteCheckRow = function(index,row){

}

staticIPv6RouteClickRow = function(index,row){

}

staticIPv6RouteInfoFullShow = function(data){
	$('#staticIPv6RouteInfoPopDlg').dialog('open');
	loadTableData("HGST_STATIC_IPV6_ROUTE_FULL_INFO");
}
/*----------------------------------------------------------------------------*/
$("[hgs_sub_nav=wlan_para_config]").click(function () {
	$(".WEP").hide();
})
bandSteerAdjustSsidInfo = function(){
	if($("#bandSteeringEnable").is(':checked') && $("#WifiBand").val() == "5g")
	{
		$('#HGS_WLAN_BASIC_CFG [hgs_key="SSID"]').attr("disabled",true);
		$('#HGS_WLAN_BASIC_CFG [hgs_key="BeaconType"]').attr("disabled",true);
		$('#HGS_WLAN_BASIC_CFG [hgs_key="WPAEncryptionModes"]').attr("disabled",true);
		$('#HGS_WLAN_BASIC_CFG [hgs_key="KeyPassphrase"]').attr("disabled",true);			
	}
	else
	{
		if (Meshsync) {
			return;
		}
		$('#HGS_WLAN_BASIC_CFG [hgs_key="SSID"]').attr("disabled",false);
		$('#HGS_WLAN_BASIC_CFG [hgs_key="BeaconType"]').attr("disabled",false);
		$('#HGS_WLAN_BASIC_CFG [hgs_key="WPAEncryptionModes"]').attr("disabled",false);
		$('#HGS_WLAN_BASIC_CFG [hgs_key="KeyPassphrase"]').attr("disabled",false);		
	}	
}
allCfgBandSteerAdjustSsidInfo = function(){
	if($("#bandSteeringEnable_allcfg").is(':checked') && $("#WifiBand_allcfg").val() == "5g")
	{
		$('#HGS_WLAN_ALL_CFG [hgs_key="SSID"]').attr("disabled",true);
		$('#HGS_WLAN_ALL_CFG [hgs_key="BeaconType"]').attr("disabled",true);
		$('#HGS_WLAN_ALL_CFG [hgs_key="WPAEncryptionModes"]').attr("disabled",true);
		$('#HGS_WLAN_ALL_CFG [hgs_key="KeyPassphrase"]').attr("disabled",true);			
	}
	else
	{
		$('#HGS_WLAN_ALL_CFG [hgs_key="SSID"]').attr("disabled",false);
		$('#HGS_WLAN_ALL_CFG [hgs_key="BeaconType"]').attr("disabled",false);
		$('#HGS_WLAN_ALL_CFG [hgs_key="WPAEncryptionModes"]').attr("disabled",false);
		$('#HGS_WLAN_ALL_CFG [hgs_key="KeyPassphrase"]').attr("disabled",false);		
	}	
}
wlanParaChange = function(){
	var index =  document.querySelector("#WifiBand").selectedIndex; //or $("#WifiBand").prop("selectedIndex")
	var fullPath = document.querySelector("#WifiBand").options[index].getAttribute("fullPath");

	switch($("#WifiBand").val()){
		case "2d4g":
			$(".only_for_2d4g").show();
			$(".only_for_5g").hide();
			break;

		case "5g":
			$(".only_for_5g").show();
			$(".only_for_2d4g").hide();
			break;
	}

	$(".WPAEncryptMode").hide();
	$("#WifiEncryptModeRow").show();
	$("#WifiPasswordRow").show();
	$(".WEP").hide();
	$(".wep").hide();
	switch($("#WifiAuthMode").val()){
		case "WPA/WPA2":
			$(".WPAEncryptMode").show();
			break;

		case "WPA2":
		case "WPA2/WPA3":
		case "WPA3":
			$(".WPAEncryptMode[value=AESEncryption]").show();
			if($("#WifiEncryptMode").val() != "AESEncryption"){
				$("#WifiEncryptMode").val("AESEncryption");
			}
			break;

		case "WPA":
			$(".WPAEncryptMode[value=TKIPEncryption]").show();
			$("#WifiEncryptMode").val("TKIPEncryption");
			break;

		case "None":
			$("#WifiEncryptModeRow").hide();
			$("#WifiPasswordRow").hide();
			break;
		case "Basic":
			$(".WEP").show();
			$(".wep").show();
			$("#WifiEncryptModeRow").hide();
			$("#WifiPasswordRow").hide();
			break;
	}

	if ($("#WifiAuthMode").val() == "Basic") {
		switch ($("#BasicEncryptionModes").val()) {
			case "None":
				$(".WEP").show();
				$(".wep").hide();
				$("#BasicEncryptionModesRow").show();
				break;
			case "WEPEncryption":
				$(".WEP").show();
				$(".wep").show();
				resizeSubNavContentHeight();
				wepKeyChange();
				break;
		}	
	}
	bandSteerAdjustSsidInfo();
}
ssidPwdWlanParaChange = function(){
	$("#WifiEncryptMode_ssidpwd .WPAEncryptMode").hide();
	$("#WifiEncryptModeRow_ssidpwd").show();
	$("#WifiPasswordRow_ssidpwd").show();
	
	switch($("#WifiAuthMode_ssidpwd").val()){
		case "WPA/WPA2":
			$("#WifiEncryptMode_ssidpwd .WPAEncryptMode").show();
			break;

		case "WPA2":
		case "WPA2/WPA3":
		case "WPA3":
			$("#WifiEncryptMode_ssidpwd .WPAEncryptMode[value=AESEncryption]").show();
			if($("#WifiEncryptMode_ssidpwd").val() != "AESEncryption"){
				$("#WifiEncryptMode_ssidpwd").val("AESEncryption");
			}
			break;

		case "WPA":
			$("#WifiEncryptMode_ssidpwd .WPAEncryptMode[value=TKIPEncryption]").show();
			$("#WifiEncryptMode_ssidpwd").val("TKIPEncryption");
			break;

		case "None":
			$("#WifiEncryptModeRow_ssidpwd").hide();
			$("#WifiPasswordRow_ssidpwd").hide();
			break;
		case "Basic":
			$(".WEP").show();
			$(".wep").show();
			$("#WifiEncryptModeRow_ssidpwd").hide();
			$("#WifiPasswordRow_ssidpwd").hide();
			break;
	}
}
ssidPwdWlanParaChange_5g = function(){
	$("#WifiEncryptMode_ssidpwd_5g .WPAEncryptMode").hide();
	$("#WifiEncryptModeRow_ssidpwd_5g").show();
	$("#WifiPasswordRow_ssidpwd_5g").show();
	
	switch($("#WifiAuthMode_ssidpwd_5g").val()){
		case "WPA/WPA2":
			$("#WifiEncryptMode_ssidpwd_5g .WPAEncryptMode").show();
			break;

		case "WPA2":
		case "WPA2/WPA3":
		case "WPA3":
			$("#WifiEncryptMode_ssidpwd_5g .WPAEncryptMode[value=AESEncryption]").show();
			if($("#WifiEncryptMode_ssidpwd_5g").val() != "AESEncryption"){
				$("#WifiEncryptMode_ssidpwd_5g").val("AESEncryption");
			}
			break;

		case "WPA":
			$("#WifiEncryptMode_ssidpwd_5g .WPAEncryptMode[value=TKIPEncryption]").show();
			$("#WifiEncryptMode_ssidpwd_5g").val("TKIPEncryption");
			break;

		case "None":
			$("#WifiEncryptModeRow_ssidpwd_5g").hide();
			$("#WifiPasswordRow_ssidpwd_5g").hide();
			break;
		case "Basic":
			$(".WEP").show();
			$(".wep").show();
			$("#WifiEncryptModeRow_ssidpwd_5g").hide();
			$("#WifiPasswordRow_ssidpwd_5g").hide();
			break;
	}
}
allCfgWlanParaChange = function(){
	var index =  document.querySelector("#WifiBand_allcfg").selectedIndex; //or $("#WifiBand").prop("selectedIndex")

	switch($("#WifiBand_allcfg").val()){
		case "2d4g":
			$(".only_for_2d4g").show();
			$(".only_for_5g").hide();
			break;

		case "5g":
			$(".only_for_5g").show();
			$(".only_for_2d4g").hide();
			if("0" == $("#HGS_WLAN_ALL_CFG [hgs_key=X_CMCC_ChannelWidth]").val()){
				$("#HGS_WLAN_ALL_CFG [hgs_key=Channel] [value=165]").attr("disabled",false);
			}
			else{
				$("#HGS_WLAN_ALL_CFG [hgs_key=Channel] [value=165]").attr("disabled",true);
			}
			break;
	}

	$("#WifiEncryptMode_allcfg .WPAEncryptMode").hide();
	$("#WifiEncryptModeRow_allcfg").show();
	$("#WifiPasswordRow_allcfg").show();
	$(".WEP").hide();
	$(".wep").hide();
	switch($("#WifiAuthMode_allcfg").val()){
		case "WPA/WPA2":
			$("#WifiEncryptMode_allcfg .WPAEncryptMode").show();
			break;

		case "WPA2":
		case "WPA2/WPA3":
		case "WPA3":
			$("#WifiEncryptMode_allcfg .WPAEncryptMode[value=AESEncryption]").show();
			if($("#WifiEncryptMode_allcfg").val() != "AESEncryption"){
				$("#WifiEncryptMode_allcfg").val("AESEncryption");
			}
			break;

		case "WPA":
			$("#WifiEncryptMode_allcfg .WPAEncryptMode[value=TKIPEncryption]").show();
			$("#WifiEncryptMode_allcfg").val("TKIPEncryption");
			break;

		case "None":
			$("#WifiEncryptModeRow_allcfg").hide();
			$("#WifiPasswordRow_allcfg").hide();
			break;
		case "Basic":
			$(".WEP").show();
			$(".wep").show();
			$("#WifiEncryptModeRow_allcfg").hide();
			$("#WifiPasswordRow_allcfg").hide();
			break;
	}

	allCfgBandSteerAdjustSsidInfo();
}
wifi5WlanParaChange = function(){
	switch($("#WifiBand_wifi5").val()){
		case "2d4g":
			$(".only_for_2d4g").show();
			$(".only_for_5g").hide();
			break;

		case "5g":
			$(".only_for_5g").show();
			$(".only_for_2d4g").hide();
			if("0" == $("#HGS_WLAN_WIFI5_CFG [hgs_key=X_CMCC_ChannelWidth]").val()){
				$("#HGS_WLAN_WIFI5_CFG [hgs_key=Channel] [value=165]").attr("disabled",false);
			}
			else{
				$("#HGS_WLAN_WIFI5_CFG [hgs_key=Channel] [value=165]").attr("disabled",true);
			}
			break;
	}

	$("#WifiEncryptMode_wifi5 .WPAEncryptMode").hide();
	$("#WifiEncryptModeRow_wifi5").show();
	$("#WifiPasswordRow_wifi5").show();
	$(".WEP").hide();
	$(".wep").hide();
	switch($("#WifiAuthMode_wifi5").val()){
		case "WPA/WPA2":
			$("#WifiEncryptMode_wifi5 .WPAEncryptMode").show();
			break;

		case "WPA2":
		case "WPA2/WPA3":
		case "WPA3":
			$("#WifiEncryptMode_wifi5 .WPAEncryptMode[value=AESEncryption]").show();
			if($("#WifiEncryptMode_wifi5").val() != "AESEncryption"){
				$("#WifiEncryptMode_wifi5").val("AESEncryption");
			}
			break;

		case "WPA":
			$("#WifiEncryptMode_wifi5 .WPAEncryptMode[value=TKIPEncryption]").show();
			$("#WifiEncryptMode_wifi5").val("TKIPEncryption");
			break;

		case "None":
			$("#WifiEncryptModeRow_wifi5").hide();
			$("#WifiPasswordRow_wifi5").hide();
			break;
		case "Basic":
			$(".WEP").show();
			$(".wep").show();
			$("#WifiEncryptModeRow_wifi5").hide();
			$("#WifiPasswordRow_wifi5").hide();
			break;
	}
}
guestWlanParaChange = function(){
	$("#WifiEncryptMode_guest_2g .WPAEncryptMode").hide();
	$("#WifiEncryptModeRow_guest_2g").show();
	$("#WifiPasswordRow_guest_2g").show();
	
	switch($("#WifiAuthMode_guest_2g").val()){
		case "WPA/WPA2":
			$("#WifiEncryptMode_guest_2g .WPAEncryptMode").show();
			break;

		case "WPA2":
		case "WPA2/WPA3":
		case "WPA3":
			$("#WifiEncryptMode_guest_2g .WPAEncryptMode[value=AESEncryption]").show();
			if($("#WifiEncryptMode_guest_2g").val() != "AESEncryption"){
				$("#WifiEncryptMode_guest_2g").val("AESEncryption");
			}
			break;

		case "WPA":
			$("#WifiEncryptMode_guest_2g .WPAEncryptMode[value=TKIPEncryption]").show();
			$("#WifiEncryptMode_guest_2g").val("TKIPEncryption");
			break;

		case "None":
			$("#WifiEncryptModeRow_guest_2g").hide();
			$("#WifiPasswordRow_guest_2g").hide();
			break;
	}
}
guestWlanParaChange_5g = function(){
	$("#WifiEncryptMode_guest_5g .WPAEncryptMode").hide();
	$("#WifiEncryptModeRow_guest_5g").show();
	$("#WifiPasswordRow_guest_5g").show();
	
	switch($("#WifiAuthMode_guest_5g").val()){
		case "WPA/WPA2":
			$("#WifiEncryptMode_guest_5g .WPAEncryptMode").show();
			break;

		case "WPA2":
		case "WPA2/WPA3":
		case "WPA3":
			$("#WifiEncryptMode_guest_5g .WPAEncryptMode[value=AESEncryption]").show();
			if($("#WifiEncryptMode_guest_5g").val() != "AESEncryption"){
				$("#WifiEncryptMode_guest_5g").val("AESEncryption");
			}
			break;

		case "WPA":
			$("#WifiEncryptMode_guest_5g .WPAEncryptMode[value=TKIPEncryption]").show();
			$("#WifiEncryptMode_guest_5g").val("TKIPEncryption");
			break;

		case "None":
			$("#WifiEncryptModeRow_guest_5g").hide();
			$("#WifiPasswordRow_guest_5g").hide();
			break;
	}
}
wepKeyChange = function () {
	$(".wepkey").prop("disabled", true);
	var idx = $("#WEPKeyIndex").val();
	var WEPKey = "WEPKey" + idx;
	$("#"+WEPKey).prop("disabled", false);
}
$(".wlanParaChange").change(function(){
	wlanParaChange();
})

$("#WEPKeyIndex").change(function () {
	wepKeyChange();
})

function guestChange() {
	if ($("#enableWlanGuest").is(':checked')) {
		$("#wlanguestCfg").show();		
	} else {
		$("#wlanguestCfg").hide();
	}
}
$("#enableWlanGuest").click(function () {
	guestChange();
})

function wifi5Change() {
	if ($("#WifiEnabled_wifi5").is(':checked')) {
		$("#wifi5Cfg").show();		
	} else {
		$("#wifi5Cfg").hide();
	}
}
$("#WifiEnabled_wifi5").click(function () {
	wifi5Change();
})

function bandSteeringChange(){
	if ($("#bandSteeringEnable").is(':checked')) {
		$("#rssiThld").show();
		$("#wifi7Mlo").hide();
	} else {
		$("#rssiThld").hide();
		$("#wifi7Mlo").show(); 
	}
}
$("#bandSteeringEnable").click(function () {
	bandSteeringChange();
})
function wifi7mloChange(){
	if ($("#mloEnbale").is(':checked')) {
		$("#bandSteering").hide();
	} else {
		$("#bandSteering").show();
	}
}
$("#mloEnbale").click(function () {
	wifi7mloChange();
})
wlanParaChange();

//HGS_WLAN_ALL_CFG
allCfgWlanParaChange();
function allCfgbandSteeringChange(){
	if ($("#bandSteeringEnable_allcfg").is(':checked')) {
		$("#rssiThld_allcfg").show();
	} else {
		$("#rssiThld_allcfg").hide();
	}
}
$("#bandSteeringEnable_allcfg").click(function () {
	allCfgbandSteeringChange();
})
$(".allCfgWlanParaChange").change(function(){
	allCfgWlanParaChange();
})
//HGS_WLAN_WIFI5_CFG
wifi5WlanParaChange();
$(".wifi5WlanParaChange").change(function(){
	wifi5WlanParaChange();
})
//HGS_WLAN_SSIDPWD_CFG
ssidPwdWlanParaChange();
ssidPwdWlanParaChange_5g();
$(".ssidPwdwlanParaChange").change(function () {
	ssidPwdWlanParaChange();
})
$(".ssidPwdWlanParaChange_5g").change(function () {
	ssidPwdWlanParaChange_5g();
})
function wlanBackupParaChange() {
	if ($("#EnableBackup").is(':checked')) {
		$(".backupContent").show();
	} else {
		$(".backupContent").hide();
	}	
}
$("#EnableBackup").click(function () {
	if ($("#EnableBackup").is(':checked')) {
		$(".backupContent").show();
		if (!backUpWifiEnabled) {
			var SSID_2g = backUpSSIDName_2g + (g_staticInfo["Region"] == "Shaanxi"?"-WIFI5":"-Wi-Fi5");
			var SSID_5g = backUpSSIDName_5g + (g_staticInfo["Region"] == "Shaanxi"?"-WIFI5":"-Wi-Fi5");
			$("#ssidCmcc_backup_2g [hgs_key='SSID_2g']").val(SSID_2g);
			$("#ssidCmcc_backup_5g [hgs_key='SSID_5g']").val(SSID_5g);			
		}
	} else {
		$(".backupContent").hide();
	}
})



$(".guestwlanParaChange").change(function () {
	guestWlanParaChange();
})
$(".guestwlanParaChange_5g").change(function () {
	guestWlanParaChange_5g();
})
wlanSsidPwdCfgCheckout = function(data){
	var fullPath_2g = document.querySelector("#WifiBand_ssidpwd_2g").options[0].getAttribute("fullPath");
	var fullPath_5g = document.querySelector("#WifiBand_ssidpwd_5g").options[0].getAttribute("fullPath");
	var jsonData_2g = {}, jsonData_5g = {}, jsonData_5g_tmp = {};

	for(i in data){
		if (data[i].fullPath) {
			if (data[i].fullPath == fullPath_2g) {
				$("#ssidCmcc_ssidpwd_2g").empty();
				if (g_staticInfo["Region"] == "Zhejiang" || g_staticInfo["Region"] == "Sichuan") {
					$("#ssidCmcc_ssidpwd_2g").append('<input type="input" class="col-5" hgs_key="SSID">')
					jsonData_2g = data[i];
				}
				else
				{
					if(data[i].SSID){
						if(data[i].SSID.indexOf("CMCC-") == 0){
							$("#ssidCmcc_ssidpwd_2g").append('<span>CMCC-</span><input type="input" class="col-5" maxlength="27" hgs_key="SSID">(length: 1~32)');
							data[i].SSID = data[i].SSID.substr("CMCC-".length);
							jsonData_2g = data[i];
						}else{
							$("#ssidCmcc_ssidpwd_2g").append('<input type="input" class="col-5" maxlength="32" hgs_key="SSID">(length: 1~32)')
							jsonData_2g = data[i];
						}
					}else{
						$("#ssidCmcc_ssidpwd_2g").append('<span>CMCC-</span><input type="input" class="col-5" maxlength="27" hgs_key="SSID">(length: 1~32)');
					}
				}
			}
			else if (data[i].fullPath == fullPath_5g) {
				$("#ssidCmcc_ssidpwd_5g").empty();
				if (g_staticInfo["Region"] == "Zhejiang" || g_staticInfo["Region"] == "Sichuan") {
					$("#ssidCmcc_ssidpwd_5g").append('<input type="input" class="col-5" maxlength="32" hgs_key="SSID_5g">(length: 1~32)')
					jsonData_5g_tmp = data[i];
				}
				else
				{
					if(data[i].SSID){
						if(data[i].SSID.indexOf("CMCC-") == 0){
							$("#ssidCmcc_ssidpwd_5g").append('<span>CMCC-</span><input type="input" class="col-5" maxlength="27" hgs_key="SSID_5g">(length: 1~32)');
							data[i].SSID = data[i].SSID.substr("CMCC-".length);
							jsonData_5g_tmp = data[i];
						}else{
							$("#ssidCmcc_ssidpwd_5g").append('<input type="input" class="col-5" maxlength="32" hgs_key="SSID_5g">(length: 1~32)')
							jsonData_5g_tmp = data[i];
						}
					}else{
						$("#ssidCmcc_ssidpwd_5g").append('<span>CMCC-</span><input type="input" class="col-5" maxlength="27" hgs_key="SSID_5g">(length: 1~32)');
					}
				}

				if (!$.isEmptyObject(jsonData_5g_tmp)) {
					jsonData_5g.Enable_5g = jsonData_5g_tmp.Enable;
					jsonData_5g.SSID_5g = jsonData_5g_tmp.SSID;
					jsonData_5g.BeaconType_5g = jsonData_5g_tmp.BeaconType;
					jsonData_5g.WPAEncryptionModes_5g = jsonData_5g_tmp.WPAEncryptionModes;
					jsonData_5g.KeyPassphrase_5g = jsonData_5g_tmp.KeyPassphrase;
				}
			}
		}
	}

	if (!$.isEmptyObject(jsonData_2g) || !$.isEmptyObject(jsonData_5g)) {
		$.extend(jsonData_2g, jsonData_5g);
		return jsonData_2g;
	}

	ssidPwdWlanParaChange();
	ssidPwdWlanParaChange_5g();
	resizeSubNavContentHeight();	
	return;
}
wlanAllCfgCheckout = function(data){
	var index =  document.querySelector("#WifiBand_allcfg").selectedIndex; //or $("#WifiBand").prop("selectedIndex")
	var fullPath = document.querySelector("#WifiBand_allcfg").options[index].getAttribute("fullPath");
	var PreSharedKeyPath = fullPath + "KeyPassphrase";
	var obj = {}, jsonData = {}, bandSteeringObj = {};
	var idx = parseInt(fullPath.substr(-2,1)) + 2;
	
	//console.log(data);
	switch($("#WifiBand_allcfg").val()){
		case "2d4g":
			break;

		case "5g":
			break;
	}

	for(i in data){
		if (data[i].fullPath) {
			if (data[i].fullPath.indexOf("CMCC_WIFI_BandSteering") > -1) {		
				bandSteeringObj.bandSteeringEnable = data[i].Enable;
				bandSteeringObj.RSSIThreshold = data[i].RSSIThreshold;
				bandSteeringObj.RSSIThreshold5G = data[i].RSSIThreshold5G;
			}
			else if (data[i].fullPath.indexOf(PreSharedKeyPath) > -1) {		
				obj.KeyPassphrase = data[i].KeyPassphrase;
			}
			else if (data[i].fullPath == fullPath) {
				$("#ssidCmcc_allcfg").empty();
				if (g_staticInfo["Region"] == "Zhejiang" || g_staticInfo["Region"] == "Sichuan") {
					$("#ssidCmcc_allcfg").append('<input type="input" class="col-5" maxlength="32" hgs_key="SSID">(length: 1~32)')
					jsonData = data[i];
				}
				else
				{
					if(data[i].SSID){
						if(data[i].SSID.indexOf("CMCC-") == 0){
							$("#ssidCmcc_allcfg").append('<span>CMCC-</span><input type="input" class="col-5" maxlength="27" hgs_key="SSID">(length: 1~32)');
							data[i].SSID = data[i].SSID.substr("CMCC-".length);
							jsonData = data[i];
						}else{
							$("#ssidCmcc_allcfg").append('<input type="input" class="col-5" maxlength="32" hgs_key="SSID">(length: 1~32)')
							jsonData = data[i];
						}
					}else{
						$("#ssidCmcc_allcfg").append('<span>CMCC-</span><input type="input" class="col-5" maxlength="27" hgs_key="SSID">(length: 1~32)');
					}
				}
				if (parseInt(jsonData.AutoChannelEnable)) {
					jsonData.Channel = 0;
				}
			}
		}
	}

	if (!$.isEmptyObject(jsonData)) {
		delete jsonData.X_CMCC_WIFI5;
		$.extend(jsonData, obj,bandSteeringObj);
		return jsonData;
	}

	allCfgbandSteeringChange();
	allCfgWlanParaChange();
	resizeSubNavContentHeight();	
	return;
}
wlanWifi5CfgCheckout = function(data){
	var index =  document.querySelector("#WifiBand_wifi5").selectedIndex; //or $("#WifiBand").prop("selectedIndex")
	var fullPath = document.querySelector("#WifiBand_wifi5").options[index].getAttribute("fullPath");
	var obj = {}, jsonData = {};
	var idx = parseInt(fullPath.substr(-2,1)) + 3;
	var guestFullPath = fullPath.slice(0,-2) + idx + '.';
	var PreSharedKeyPath = guestFullPath + "KeyPassphrase";
	
	//console.log(data);
	switch($("#WifiBand_wifi5").val()){
		case "2d4g":
			break;

		case "5g":
			idx = parseInt(fullPath.substr(-2,1)) + 3;
			guestFullPath = fullPath.slice(0,-2) + idx + '.';
			PreSharedKeyPath = guestFullPath + "KeyPassphrase";
			break;
	}

	for(i in data){
		if (data[i].fullPath) {
			if (data[i].fullPath.indexOf(PreSharedKeyPath) > -1) {		
				obj.KeyPassphrase = data[i].KeyPassphrase;
			}
			else if (data[i].fullPath == guestFullPath) {
				$("#ssidCmcc_wifi5").empty();
				if (g_staticInfo["Region"] == "Zhejiang" || g_staticInfo["Region"] == "Sichuan") {
					$("#ssidCmcc_wifi5").append('<input type="input" class="col-5" maxlength="32" hgs_key="SSID">(length: 1~32)')
					jsonData = data[i];
				}
				else
				{
					if(data[i].SSID){
						if(data[i].SSID.indexOf("CMCC-") == 0){
							$("#ssidCmcc_wifi5").append('<span>CMCC-</span><input type="input" class="col-5" maxlength="27" hgs_key="SSID">(length: 1~32)');
							data[i].SSID = data[i].SSID.substr("CMCC-".length);
							jsonData = data[i];
						}else{
							$("#ssidCmcc_wifi5").append('<input type="input" class="col-5" maxlength="32" hgs_key="SSID">(length: 1~32)')
							jsonData = data[i];
						}
					}else{
						$("#ssidCmcc_wifi5").append('<span>CMCC-</span><input type="input" class="col-5" maxlength="27" hgs_key="SSID">(length: 1~32)');
					}
				}
				if (parseInt(jsonData.AutoChannelEnable)) {
					jsonData.Channel = 0;
				}
			}
		}
	}

	if (!$.isEmptyObject(jsonData)) {
		$.extend(jsonData, obj);
		return jsonData;
	}

	wifi5WlanParaChange();
	wifi5Change();
	resizeSubNavContentHeight();	
	return;
}
wlanCtlCfgCheckout = function (data) {
	var jsonData = [];
	
	for (const k in data) {
		if (data[k].fullPath) {
			if (data[k].fullPath.indexOf("WLANConfiguration") > -1) {
				jsonData = data[k];
			}
			else if (data[k].fullPath.indexOf("WifiMesh") > -1) {
				if (isSubnetAP() && data[k].MeshStatus == "1") {
					$(".Meshsync").attr("disabled",true);
				} else {
					$(".Meshsync").attr("disabled",false);
				}
			}
		}
	}
	resizeSubNavContentHeight();
	return jsonData;
}

var Meshsync = false;
wlanBasicCfgCheckout = function(data){
	var index =  document.querySelector("#WifiBand").selectedIndex; //or $("#WifiBand").prop("selectedIndex")
	var fullPath = document.querySelector("#WifiBand").options[index].getAttribute("fullPath");
	var PreSharedKeyPath = fullPath + "KeyPassphrase";
	var obj = {}, jsonData = {}, bandSteeringObj = {}, mloObj = {};
	var guestObj = {};
	var idx = parseInt(fullPath.substr(-2,1)) + 3;
	var guestFullPath = fullPath.slice(0,-2) + idx + '.';

	//console.log(data);
	switch($("#WifiBand").val()){
		case "2d4g":
			break;

		case "5g":
			idx = parseInt(fullPath.substr(-2,1)) + 3;
			guestFullPath = fullPath.slice(0,-2) + idx + '.';
			break;
	}

	if (isSubnetAP()) {
		for (const k in data) {
			if (data[k].fullPath) {
				if (data[k].fullPath.indexOf("WifiMesh") > -1) {
					if (data[k].MeshStatus == "1") {
						//组网成功
						Meshsync = true;
						$(".Meshsync").attr("disabled",true);
						break;
					}else{
						$(".Meshsync").attr("disabled",false);
						break;
					}
				}		
			}
		}
	} else {
		$(".Meshsync").attr("disabled",false);
	}

	for(i in data){
		if (data[i].fullPath) {
			if (data[i].fullPath.indexOf("CMCC_WIFI_BandSteering") > -1) {		
				bandSteeringObj.bandSteeringEnable = data[i].Enable;
				bandSteeringObj.RSSIThreshold = data[i].RSSIThreshold;
				bandSteeringObj.RSSIThreshold5G = data[i].RSSIThreshold5G;
			}
			else if (data[i].fullPath.indexOf(PreSharedKeyPath) > -1) {		
				obj.KeyPassphrase = data[i].KeyPassphrase;
			}
			else if (data[i].fullPath == fullPath) {
				$("#ssidCmcc").empty();
				if (g_staticInfo["Region"] == "Zhejiang" || g_staticInfo["Region"] == "Sichuan") {
					$("#ssidCmcc").append('<input disabled='+Meshsync+' type="input" class="col-5" maxlength="32" hgs_key="SSID">(长度:1~32)');
					jsonData = data[i];
				}
				else
				{
					if(data[i].SSID){
						if(data[i].SSID.indexOf("CMCC-") == 0){
							$("#ssidCmcc").append('<span>CMCC-</span><input disabled='+Meshsync+' type="input" class="col-5" maxlength="27" hgs_key="SSID">(长度:1~32)');
							data[i].SSID = data[i].SSID.substr("CMCC-".length);
							jsonData = data[i];
						}else{
							$("#ssidCmcc").append('<input disabled='+Meshsync+' type="input" class="col-5" maxlength="32" hgs_key="SSID">(长度:1~32)');
							jsonData = data[i];
						}
					}else{
						$("#ssidCmcc").append('<span>CMCC-</span><input disabled='+Meshsync+' type="input" class="col-5" maxlength="27" hgs_key="SSID">(长度:1~32)');
					}
				}
			}
			else if (data[i].fullPath.indexOf("HgConfig") > -1) {
				mloObj.MloEnbale = data[i].MloEnbale;
			}
			/* else if (data[i].fullPath == guestFullPath) {
				guestObj.guestEnable = data[i].Enable;
				guestObj.guestBeaconType = data[i].BeaconType;
				guestObj.guestSSIDEnable = data[i].Enable;
				$("#guestssidCmcc").empty();
				if(data[i].SSID){
					if (g_staticInfo["Region"] == "Zhejiang" || g_staticInfo["Region"] == "Sichuan") {
						$("#guestssidCmcc").append('<input type="input" class="col-5" hgs_key="guestSSID">')
						if(data[i].SSID == "CMCC-QLINK"){
							guestObj.guestSSID = data[0].SSID + (g_staticInfo["Region"] == "Shaanxi"?"-WIFI5":"-Wi-Fi5");
						}else{
							guestObj.guestSSID = data[i].SSID;
						}
					}
					else
					{
						if(data[i].SSID.indexOf("CMCC-") == 0){
							$("#guestssidCmcc").append('<span>CMCC-</span><input type="input" class="col-5" hgs_key="guestSSID">');
							if(data[i].SSID == "CMCC-QLINK"){
								guestObj.guestSSID = data[0].SSID + (g_staticInfo["Region"] == "Shaanxi"?"-WIFI5":"-Wi-Fi5");
							}else{
								guestObj.guestSSID = data[i].SSID.substr("CMCC-".length);
							}
							
						}else{
							$("#guestssidCmcc").append('<input type="input" class="col-5" hgs_key="guestSSID">')
							guestObj.guestSSID = data[i].SSID;
						}
					}
				}else{
					$("#guestssidCmcc").append('<span>CMCC-</span><input type="input" class="col-5" hgs_key="guestSSID">');
				}
				if(data[i].SSID == "CMCC-QLINK"){
					$("#WifiGuestPassword").show();
				}else{
					if (data[i].BeaconType == 'None') {
						$("#WifiGuestPassword").hide();
					} else {
						$("#WifiGuestPassword").show();
					}
				}

				guestObj.X_CMCC_WIFI5 = data[i].X_CMCC_WIFI5;
				guestObj.guestPreSharedKey = data[i].KeyPassphrase;
			} */
		}
	}

	if (!$.isEmptyObject(jsonData)) {
		delete jsonData.X_CMCC_WIFI5;
		$.extend(jsonData, obj,bandSteeringObj,guestObj,mloObj);
		return jsonData;
	}

	wifi7mloChange();
	bandSteeringChange();
	// guestChange();
	wlanParaChange();
	resizeSubNavContentHeight();	
	return;
}

wlanAdvCfgCheckout = function(data) {
	var index =  document.querySelector("#advWifiBand").selectedIndex; //or $("#WifiBand").prop("selectedIndex")
	var fullPath = document.querySelector("#advWifiBand").options[index].getAttribute("fullPath");
	var jsonData = {};

	for(i in data){
		if (data[i].fullPath) {
			if (data[i].fullPath == fullPath) {				
				jsonData = data[i];
				if (parseInt(jsonData.AutoChannelEnable)) {
					jsonData.Channel = 0;
				}
				// break;
			}
			else if (data[i].fullPath.indexOf("WifiMesh") > -1) {
				if (isSubnetAP() && data[i].MeshStatus == "1") {
					$(".Meshsync").attr("disabled",true);
				} else {
					$(".Meshsync").attr("disabled",false);
				}
			}
		}
	}

	if (!$.isEmptyObject(jsonData)) {
		// $.extend(jsonData, obj);
		return jsonData;
	}

	var axtext = $("#HGS_WLAN_ADV_CFG [hgs_key=Standard]").find("[value=ax]").text();
	switch($("#advWifiBand").val()){
		case "2d4g":
			$(".only_for_2d4g").show();
			$(".only_for_5g").hide();
			if (g_staticInfo["IsFTTR"] && (axtext == "b/g/n/ax" || axtext == "a/n/ac/ax")) {
				$("#HGS_WLAN_ADV_CFG [hgs_key=Standard]").find("[value=ax]").text("b/g/n/ax");
			} else {
				$("#HGS_WLAN_ADV_CFG [hgs_key=Standard]").find("[value=ax]").text("ax");
			}
			break;

		case "5g":
			$(".only_for_5g").show();
			$(".only_for_2d4g").hide();
			if("0" == $("#HGS_WLAN_ADV_CFG [hgs_key=X_CMCC_ChannelWidth]").val()){
				$("#HGS_WLAN_ADV_CFG [hgs_key=Channel] [value=165]").attr("disabled",false);
			}
			else
			{
				$("#HGS_WLAN_ADV_CFG [hgs_key=Channel] [value=165]").attr("disabled",true);
			}

			if (g_staticInfo["IsFTTR"] && (axtext == "b/g/n/ax" || axtext == "a/n/ac/ax")) {
				$("#HGS_WLAN_ADV_CFG [hgs_key=Standard]").find("[value=ax]").text("a/n/ac/ax");
			} else {
				$("#HGS_WLAN_ADV_CFG [hgs_key=Standard]").find("[value=ax]").text("ax");
			}
			break;
	}

	resizeSubNavContentHeight();
	return;
}

var backUpSSIDName_2g,backUpSSIDName_5g;
var backUpWifiEnabled = false;
wlanBackupCfgCheckout = function(data){
	var fullPath1 = "InternetGatewayDevice.LANDevice.1.WLANConfiguration.1.";
	var fullPath5 = "InternetGatewayDevice.LANDevice.1.WLANConfiguration.5.";
	var fullPath_2g = "InternetGatewayDevice.LANDevice.1.WLANConfiguration.4.";
	var fullPath_5g = "InternetGatewayDevice.LANDevice.1.WLANConfiguration.8.";
	var obj = {};
	var enablewifi5 = true;

	for(i in data){
		if (data[i].fullPath) {
			if (data[i].fullPath.indexOf(fullPath_2g) > -1) {
				obj.SSID_2g = data[i].SSID;
				obj.KeyPassphrase_2g = data[i].KeyPassphrase;
				enablewifi5 = enablewifi5 && parseInt(data[i].X_CMCC_WIFI5) && parseInt(data[i].Enable);
			}
			else if (data[i].fullPath.indexOf(fullPath_5g) > -1) {
				obj.SSID_5g = data[i].SSID;
				obj.KeyPassphrase_5g = data[i].KeyPassphrase;
				enablewifi5 = enablewifi5 && parseInt(data[i].X_CMCC_WIFI5) && parseInt(data[i].Enable);
			}
			else if (data[i].fullPath.indexOf(fullPath1) > -1) {
				backUpSSIDName_2g = data[i].SSID;
			}
			else if (data[i].fullPath.indexOf(fullPath5) > -1) {
				backUpSSIDName_5g = data[i].SSID;
			}
		}
	}

	if(obj.SSID_2g == "CMCC-QLINK"){
		obj.SSID_2g = backUpSSIDName_2g + (g_staticInfo["Region"] == "Shaanxi"?"-WIFI5":"-Wi-Fi5");
	}
	obj.Enable = enablewifi5;
	if ($.isArray(data)) {
		backUpWifiEnabled = enablewifi5;
	}
	
	wlanBackupParaChange();
	if (!$.isEmptyObject(obj)) {
		return obj;
	}

	resizeSubNavContentHeight();	
	return;
}
wlanGuestCfgCheckout = function(data){
	var jsonData_2g = {}, jsonData_5g = {};
	var fullPath_2g = "InternetGatewayDevice.LANDevice.1.WLANConfiguration.3.";
	var fullPath_5g = "InternetGatewayDevice.LANDevice.1.WLANConfiguration.7.";
	
	for(i in data){
		if (data[i].fullPath) {
			if (data[i].fullPath == fullPath_2g) {
				jsonData_2g = data[i];
			}
			else if (data[i].fullPath == fullPath_5g) {
				jsonData_5g.Enable_5g = data[i].Enable;
				jsonData_5g.SSID_5g = data[i].SSID;
				jsonData_5g.BeaconType_5g = data[i].BeaconType;
				jsonData_5g.WPAEncryptionModes_5g = data[i].WPAEncryptionModes;
				jsonData_5g.KeyPassphrase_5g = data[i].KeyPassphrase;
			}
			else if (data[i].fullPath.indexOf("WifiMesh") > -1) {
				if (isSubnetAP() && data[i].MeshStatus == "1") {
					$(".Meshsync").attr("disabled",true);
				} else {
					$(".Meshsync").attr("disabled",false);
				}
			}
		}
	}

	if (!$.isEmptyObject(jsonData_2g) || !$.isEmptyObject(jsonData_5g)) {
		$.extend(jsonData_2g, jsonData_5g);
		return jsonData_2g;
	}
	
	guestWlanParaChange();
	guestWlanParaChange_5g();
	resizeSubNavContentHeight();	
	return;
}
$("#advWifiChanlBw_allcfg").change(function () {
	if ($("#advWifiChanlBw_allcfg").val() == '0') {
		$("#HGS_WLAN_ALL_CFG [hgs_key=Channel] [value=165]").attr("disabled",false);
	} else {
		$("#HGS_WLAN_ALL_CFG [hgs_key=Channel] [value=165]").attr("disabled",true);
	}	
})
$("#advWifiChanlBw_wifi5").change(function () {
	if ($("#advWifiChanlBw_wifi5").val() == '0') {
		$("#HGS_WLAN_WIFI5_CFG [hgs_key=Channel] [value=165]").attr("disabled",false);
	} else {
		$("#HGS_WLAN_WIFI5_CFG [hgs_key=Channel] [value=165]").attr("disabled",true);
	}	
})
$("#advWifiChanlBw").change(function () {
	if ($("#advWifiChanlBw").val() == '0') {
		$("#HGS_WLAN_ADV_CFG [hgs_key=Channel] [value=165]").attr("disabled",false);
	} else {
		$("#HGS_WLAN_ADV_CFG [hgs_key=Channel] [value=165]").attr("disabled",true);
	}	
})
$("#WifiGuestAuthMode").change(function () {
	if ($("#WifiGuestAuthMode").val() == 'None') {
		$("#WifiGuestPassword").hide();
	} else {
		$("#WifiGuestPassword").show();
	}	
})

$("#WifiBand_ssidpwd").change(function(){
	$("[hgs_sub_nav='wlan_ssidpwd_config']").click();
})
$("#WifiBand_allcfg").change(function(){
	$("[hgs_sub_nav='wlan_all_config']").click();
})
$("#WifiBand_wifi5").change(function(){
	$("[hgs_sub_nav='wlan_wifi5_config']").click();
})
$("#WifiBand").change(function(){
	$("[hgs_sub_nav='wlan_basic_config']").click();
})
$("#advWifiBand").change(function () {
	loadHbusData("HGS_WLAN_ADV_CFG");
})
function getStringLength(str) {  
    const normalized = str.normalize('NFC');  
 
//    const graphemes = normalized.match(/[\u{0001F3FB}-\u{0001F3FF}]|\p{M}|\p{L}|\p{N}|\p{P}|\p{S}|\p{Z}|\p{Cc}|\p{Cf}|\p{Co}|\p{Cs}|\p{Cn}|\p{Lm}|\p{Ll}|\p{Lu}|\p{Lt}|\p{Mc}|\p{Me}|\p{Mn}|\p{Nd}|\p{Nl}|\p{No}|\p{Pc}|\p{Pd}|\p{Pe}|\p{Pf}|\p{Pi}|\p{Po}|\p{Ps}|\p{Sc}|\p{Sk}|\p{Sm}|\p{So}|\p{Zl}|\p{Zp}|\p{Zs}/gu);
    const chineseRegex = /[\u3400-\u4dbf\u4e00-\u9fff\uff00-\uffef]/g;  
    const matcheCNs = str.match(chineseRegex) || [];
	var strLen = (graphemes.length - matcheCNs.length) + matcheCNs.length*4;

	return strLen;  
} 
wlanSsidPwdCfgCheckin = function(objName, objData){
	var fullPath_2g = document.querySelector("#WifiBand_ssidpwd_2g").options[0].getAttribute("fullPath");
	var fullPath_5g = document.querySelector("#WifiBand_ssidpwd_5g").options[0].getAttribute("fullPath");
	var objData_2g = {}, objData_5g = {};

	if ($("#ssidCmcc_ssidpwd_2g>span").length == 0) {
		objData_2g.SSID = objData.SSID;
	} else {
		objData_2g.SSID = "CMCC-" + objData.SSID;
	}
	if ($("#ssidCmcc_ssidpwd_5g>span").length == 0) {
		objData_5g.SSID = objData.SSID_5g;
	} else {
		objData_5g.SSID = "CMCC-" + objData.SSID_5g;
	}

	var ssidName = "",ssidName_5g = ""; // 包含英文字符、中文字符和emoji  
	ssidName = objData.SSID;
	ssidName_5g = objData.SSID_5g;
	var ssidNameLen = getStringLength(ssidName);
	var ssidNameLen_5g = getStringLength(ssidName_5g);

	if(ssidNameLen > 32){
		alert("The 2.4G SSID can contain 1 to 32 digits or characters at most.");
		return;
	}else if(ssidNameLen == 0){
		alert("2.4G SSID cannot be empty.");
		return;
	}

	if(ssidNameLen_5g > 32){
		alert("The 5G SSID can contain 1 to 32 digits or characters.");
		return;
	}else if(ssidNameLen_5g == 0){
		alert("5G SSID cannot be empty.");
		return;
	}	


	objData_2g.fullPath = fullPath_2g;
	objData_2g.Enable = objData.Enable;
	objData_2g.BeaconType = objData.BeaconType;
	objData_2g.WPAEncryptionModes = objData.WPAEncryptionModes;
	objData_2g.KeyPassphrase = objData.KeyPassphrase;

	objData_5g.fullPath = fullPath_5g;
	objData_5g.Enable = objData.Enable_5g;
	objData_5g.BeaconType = objData.BeaconType_5g;
	objData_5g.WPAEncryptionModes = objData.WPAEncryptionModes_5g;
	objData_5g.KeyPassphrase = objData.KeyPassphrase_5g;
	
	setTimeout(function(){
		$("[hgs_sub_nav='wlan_ssidpwd_config']").click();
	}, 5000)
	return [objData_2g,objData_5g];
}
wlanAllCfgCheckin = function(objName, objData){
	var index =  document.querySelector("#WifiBand_allcfg").selectedIndex; //or $("#WifiBand").prop("selectedIndex")
	var fullPath = document.querySelector("#WifiBand_allcfg").options[index].getAttribute("fullPath");
	
	if ($("#ssidCmcc_allcfg>span").length == 0) {
		objData.SSID = objData.SSID;
	} else {
		objData.SSID = "CMCC-" + objData.SSID;
	}
	console.log("objData.SSID=",objData.SSID);
	let ssidName = ""; // 包含英文字符、中文字符和emoji  
	ssidName = objData.SSID;
	ssidNameLen = getStringLength(ssidName)

	if(ssidNameLen > 32){
		alert("The SSID can contain 1 to 32 digits or characters.");
		return;
	}
	if(ssidNameLen == 0){
		alert("ssid cannot be empty.");
		return;
	}


	if (parseInt(objData.Channel)) {
		objData.AutoChannelEnable = 0;
	} else {
		objData.AutoChannelEnable = 1;
	}
	objData.fullPath = fullPath;
	
	bandSteeringObj = {fullPath:"InternetGatewayDevice.CMCC_WIFI_BandSteering.",Enable:objData.bandSteeringEnable?1:0};
	if (bandSteeringObj.Enable) {
		bandSteeringObj.RSSIThreshold = objData.RSSIThreshold;
		bandSteeringObj.RSSIThreshold5G = objData.RSSIThreshold5G;	
	}

	delete objData.bandSteeringEnable;
	delete objData.RSSIThreshold;
	delete objData.RSSIThreshold5G;
	delete objData.ChannelsInUse;
	
	setTimeout(function(){
		$("[hgs_sub_nav='wlan_all_config']").click();
	}, 5000)
	return [objData, bandSteeringObj];
}
wlanWifi5CfgCheckin = function(objName, objData){
	var index =  document.querySelector("#WifiBand_wifi5").selectedIndex; //or $("#WifiBand").prop("selectedIndex")
	var fullPath = document.querySelector("#WifiBand_wifi5").options[index].getAttribute("fullPath");
	var guestidx = parseInt(fullPath.substr(-2,1)) + 3;
	var guestFullPath = fullPath.slice(0,-2) + guestidx + '.';
	
	if($("#WifiBand_wifi5").val() == "5g"){
		guestidx = parseInt(fullPath.substr(-2,1)) + 3;
		guestFullPath = fullPath.slice(0,-2) + guestidx + '.';
	}
	
	if (!$("#WifiEnabled_wifi5").is(':checked')) {
		//if wifi5 is closed,can't config other wifi5 parameters
		var obj={};
		obj.Enable = objData.Enable;
		obj.X_CMCC_WIFI5 = false;
		obj.fullPath = guestFullPath;
		return [obj];
	}
	
	if ($("#ssidCmcc_wifi5>span").length == 0) {
		objData.SSID = objData.SSID;
	} else {
		objData.SSID = "CMCC-" + objData.SSID;
	}
	console.log("objData.SSID=",objData.SSID);
	let ssidName = ""; // 包含英文字符、中文字符和emoji  
	ssidName = objData.SSID;
	ssidNameLen = getStringLength(ssidName)

	if(ssidNameLen > 32){
		alert("The SSID can contain 1 to 32 digits or characters.");
		return;
	}
	if(ssidNameLen == 0){
		alert("ssid cannot be empty.");
		return;
	}

	if (parseInt(objData.Channel)) {
		objData.AutoChannelEnable = 0;
	} else {
		objData.AutoChannelEnable = 1;
	}
	if (objData.Enable) {
		objData.X_CMCC_WIFI5 = true;
	} else {
		objData.X_CMCC_WIFI5 = false;
	}
	objData.fullPath = guestFullPath;
	
	delete objData.ChannelsInUse;
	
	setTimeout(function(){
		$("[hgs_sub_nav='wlan_wifi5_config']").click();
	}, 5000)
	return [objData];
}

wlanBasicCfgCheckin = function(objName, objData){
	var index =  document.querySelector("#WifiBand").selectedIndex; //or $("#WifiBand").prop("selectedIndex")
	var fullPath = document.querySelector("#WifiBand").options[index].getAttribute("fullPath");
	var guestObj = {}, mloObj = {}, hgmloObj = {};	
	var guestidx = parseInt(fullPath.substr(-2,1)) + 3;
	var guestFullPath = fullPath.slice(0,-2) + guestidx + '.';
	if($("#WifiBand").val() == "5g"){
		guestidx = parseInt(fullPath.substr(-2,1)) + 3;
		guestFullPath = fullPath.slice(0,-2) + guestidx + '.';
	}
	if ($("#ssidCmcc>span").length == 0) {
		objData.SSID = objData.SSID;
	} else {
		objData.SSID = "CMCC-" + objData.SSID;
	}
	
	let ssidName = ""; // 包含英文字符、中文字符和emoji  
	ssidName = objData.SSID;
	ssidNameLen = getStringLength(ssidName)

	if(ssidNameLen > 32){
		alert("The SSID can contain 1 to 32 digits or characters.");
		return;
	}
	if(ssidNameLen == 0){
		alert("ssid cannot be empty.");
		return;
	}

	objData.fullPath = fullPath;
	/* 
	guestObj = {fullPath:guestFullPath};
	guestObj.Enable = objData.guestEnable;
	if (guestObj.Enable){
		
		if ($("#guestssidCmcc>span").length == 0) {
			guestObj.SSID = objData.guestSSID;
		} else {
			guestObj.SSID = "CMCC-" + objData.guestSSID;
		}
		guestObj.BeaconType = "WPA/WPA2";
		guestObj.KeyPassphrase = objData.guestPreSharedKey;
		guestObj.X_CMCC_WIFI5 = true;
	} else{
		guestObj.X_CMCC_WIFI5 = false;
	}
	 */
	if ($("#mloEnbale").length) {
		mloObj = {fullPath:"InternetGatewayDevice.HgConfig.",MloEnbale:objData.MloEnbale?1:0};
		hgmloObj = {fullPath:"InternetGatewayDevice.LANDevice.1.WLANConfiguration.1.",HgMLOEnable:objData.MloEnbale?1:0};		
	}

	if ($("#bandSteeringEnable").length) {
		bandSteeringObj = {fullPath:"InternetGatewayDevice.CMCC_WIFI_BandSteering.",Enable:objData.bandSteeringEnable?1:0};
		if (bandSteeringObj.Enable) {
			bandSteeringObj.RSSIThreshold = objData.RSSIThreshold;
			bandSteeringObj.RSSIThreshold5G = objData.RSSIThreshold5G;
		}
	}

	delete objData.bandSteeringEnable;
	delete objData.RSSIThreshold;
	delete objData.RSSIThreshold5G;
	delete objData.guestPreSharedKey;
	delete objData.guestEnable;
	delete objData.guestSSIDEnable;
	delete objData.guestSSID;
	delete objData.guestBeaconType;
	delete objData.ChannelsInUse;
	delete objData.X_CMCC_WIFI5;
	delete objData.MloEnbale;
	
	setTimeout(function(){
		$("[hgs_sub_nav='wlan_basic_config']").click();
	}, 5000)
	return [objData, bandSteeringObj,guestObj,mloObj,hgmloObj];
}

wlanAdvCfgCheckin = function(objName, objData){
	var index =  document.querySelector("#advWifiBand").selectedIndex; //or $("#WifiBand").prop("selectedIndex")
	var fullPath = document.querySelector("#advWifiBand").options[index].getAttribute("fullPath");

	objData.fullPath = fullPath;
	if (parseInt(objData.Channel)) {
		objData.AutoChannelEnable = 0;
	} else {
		objData.AutoChannelEnable = 1;
	}
	return [objData];
}
wlanBackupCfgCheckin = function(objName, objData){
	var fullPath_2g = "InternetGatewayDevice.LANDevice.1.WLANConfiguration.4.";
	var fullPath_5g = "InternetGatewayDevice.LANDevice.1.WLANConfiguration.8.";
	var obj1 = {}, obj2 = {};
	obj1.fullPath = fullPath_2g;
	obj2.fullPath = fullPath_5g;
	
	if (!$("#EnableBackup").is(':checked')) {
		//if wifi5 is closed,can't config other wifi5 parameters
		obj1.X_CMCC_WIFI5 = false;
		obj1.Enable = false;
		obj1.SSID = "CMCC-SSID4";
		obj2.X_CMCC_WIFI5 = false;
		obj2.Enable = false;
		obj2.SSID = "CMCC-SSID4-5G";
		return [obj1,obj2];
	}else{
		obj1.Enable = true;
		obj1.SSID = objData.SSID_2g;
		obj1.X_CMCC_WIFI5 = true;
		obj1.KeyPassphrase = objData.KeyPassphrase_2g;
		obj1.BeaconType = "WPA/WPA2";
		obj2.Enable = true;
		obj2.SSID = objData.SSID_5g;
		obj2.X_CMCC_WIFI5 = true;
		obj2.KeyPassphrase = objData.KeyPassphrase_5g;
		obj2.BeaconType = "WPA/WPA2";
	}
	
	setTimeout(function(){
		$("[hgs_sub_nav='wlan_backup_config']").click();
	}, 5000)
	return [obj1,obj2];
}
wlanGuestCfgCheckin = function(objName, objData){
	var objData_2g = {}, objData_5g = {};
	var fullPath_2g = "InternetGatewayDevice.LANDevice.1.WLANConfiguration.3.";
	var fullPath_5g = "InternetGatewayDevice.LANDevice.1.WLANConfiguration.7.";
	
	objData_2g.fullPath = fullPath_2g;
	objData_2g.SSID = objData.SSID;
	objData_2g.Enable = objData.Enable;
	objData_2g.BeaconType = objData.BeaconType;
	objData_2g.WPAEncryptionModes = objData.WPAEncryptionModes;
	objData_2g.KeyPassphrase = objData.KeyPassphrase;

	objData_5g.fullPath = fullPath_5g;
	objData_5g.SSID = objData.SSID_5g;
	objData_5g.Enable = objData.Enable_5g;
	objData_5g.BeaconType = objData.BeaconType_5g;
	objData_5g.WPAEncryptionModes = objData.WPAEncryptionModes_5g;
	objData_5g.KeyPassphrase = objData.KeyPassphrase_5g;
	
	return [objData_2g,objData_5g];
}
/*----------------------------------------------------------------------------*/

wlanInfInfoUpdate = function(){
	loadTableData("HGST_WLAN_INFO");
}

wlanInfInfoCheckout = function(data){
	var submesh = false;
	var jsonData = [];

	if (isSubnetAP()) {
		for(i in data){
			if (data[i].fullPath && data[i].fullPath.indexOf("WifiMesh") > -1) {
				if (data[i].MeshStatus == "1") {
					//组网成功
					submesh = true;
					break;
				} else {
					submesh = false;
					break;
				}
			}
		}
	}

	for(i in data){
		if (data[i].fullPath.indexOf("WifiMesh") > -1) {
			continue;
		}
		else if (data[i].fullPath.indexOf("WLANConfiguration.6") > -1) {
			continue;
		}

		data[i].X_CMCC_APModuleEnable = parseInt(data[i].Enable)?"Open":"closure";
		if (data[i].Status != "Disabled") {
			data[i].Status = parseInt(data[i].Enable)?"Up":"Disabled";
		}
		
		switch(data[i].WPAEncryptionModes){
			case "TKIPandAESEncryption":
				data[i].WPAEncryptionModes = "TKIP/AES";
				break;

			case "TKIPEncryption":
				data[i].WPAEncryptionModes = "TKIP";
				break;
				
			case "AESEncryption":
				data[i].WPAEncryptionModes = "AES";
				break;
		}
		jsonData.push(data[i]);
	}

	if(jsonData.length >= 2){
		jsonData[0].Band = "2.4G";
		jsonData[1].Band = "5G";
	}
	
	return jsonData;
}

/*----------------------------------------------------------------------------*/
wlanShareCheckout = function(data){
	var jsonData = [];

	for (const k in data) {
		if (data[k].fullPath) {
			if (data[k].fullPath.indexOf("X_CMCC_WLANShare") > -1) {
				jsonData = data[k];
			}		
		}
	}

	resizeSubNavContentHeight();
	return jsonData;
}

wlanShareCheckin = function(objName, objData){
	//objData.fullPath = "InternetGatewayDevice.LANDevice.1.X_CMCC_WLANShare.{i}.";
	objData.fullPath = "InternetGatewayDevice.LANDevice.1.X_CMCC_WLANShare.1.";

	return [objData];
}

$("#SSIDWps").change(function(){
	loadHbusData("HGS_WLAN_WPS");
})

/*----------------------------------------------------------------------------*/
wlanWpsCheckout = function(data){
	var index =  document.querySelector("#SSIDWps").selectedIndex; //or $("#WifiBand").prop("selectedIndex")
	var fullPath = document.querySelector("#SSIDWps").options[index].getAttribute("fullPath");

//	console.log(data);
	switch($("#SSIDWps").val()){
		case "2d4g":
			break;

		case "5g":
			break;
	}

	for(i in data){
		if(data[i].fullPath == fullPath){
		//	console.log(data[i]);
			return data[i];
		}
	}

	resizeSubNavContentHeight();
	return;
}

wlanWpsCheckin = function(objName, objData){
	var index =  document.querySelector("#SSIDWps").selectedIndex; //or $("#WifiBand").prop("selectedIndex")
	var fullPath = document.querySelector("#SSIDWps").options[index].getAttribute("fullPath");

	objData.fullPath = fullPath;

	return [objData];
}
/*----------------------------------------------------------------------------*/

wlanSignalCheckout = function (data) {
	resizeSubNavContentHeight();
	return data;
}
/*----------------------------------------------------------------------------*/

$("#scanResultListTable").on("click", ".select_ssid", function(){
    if($("#hgc_enableRelay").is(':checked')){
        $("#relay_ssid").val($(this).children().first().next().text());
		$("#relay_enable").val(1);
        $("#relay_authmode").val($(this).attr("SecurityMode"));
        if ($("#relay_authmode").val() == 'None') {
            $("#relay_pwd").hide();
        } else {
            $("#relay_pwd").show();
        }        
    }
})
var seconds = 15;

_doWifiScan = function(){
	
    getsuccess = 0;
    seconds = 17;
	
    console.log("#scanWifiNeedSecs------->" + $("#scanWifiNeedSecs").text())
    console.log("new scanning");
	
    $("#scanWifiNeedSecs").text(seconds);
    $("#waitWifiScanResultImg").css("display", "block");

	var pathStr = "hbus://mdm/InternetGatewayDevice.NeighboringWiFiDiagnostic.";
	var postData = {type:"POST", path:pathStr, commitData:{path:pathStr,para:{DiagnosticsState:'Requested'}},msgType:212};
	var getData={Type:"GET",
				userTagData:1,
				msgType:211,
				path:"hbus://mdm/InternetGatewayDevice.NeighboringWiFiDiagnostic."};
	hgsUpdateData(postData,function (result) {
		hgsUpdateData(getData, function (data) {
			if (data.DiagnosticsState == 'Complete') {
				getScanResult()	
			}
		})
	})					

	setTimeout(scanCountdown, 1000);
	$("#scanWifiOverPrompt").hide();
    $("#_L_nm_surf_realy_scanProgressing").show();

    function getScanResult(){
		var getData={Type:"GET",
					userTagData:1,
					msgType:211,
					path:"hbus://mdm/InternetGatewayDevice.NeighboringWiFiDiagnostic.Result.{i}.;"};				

		hgsUpdateData(getData, function(data){
			if(!$.isEmptyObject(data) )
			{
			// console.log("get date,timenow="+data["timenow"]+",,timereq="+data["timereq"]);
				// if(parseInt(data["BeaconPeriod"]) <=100)
				// {
					$("#scanResultListTable").show();
            		showScanResult(data);
					console.log("getScanResult ret 1");
                    console.log("set second 0");
					getsuccess =1;                    
					seconds = 0;

					return 1;
				// }else{
					/* console.log("getScanResult ret 0");
					console.log('seconds: '+ seconds);
					$("#scanWifiNeedSecs").text(seconds);
					$("#waitWifiScanResultImg").css("display", "block");
					hgsUpdateData(getData, function (data) {
						console.log("new req 2===");
					})
					return 0; */
				// }
			}else
				{
					console.log("getScanResult ret 0");
					console.log('seconds: '+ seconds);
					$("#scanWifiNeedSecs").text(seconds);
					$("#waitWifiScanResultImg").css("display", "block");
					hgsUpdateData(getData, function (data) {
						console.log("new req 2===");
					})
										
					return 0;
				/* 
				$("#scanWifiNeedSecs").text(seconds);
				$("#waitWifiScanResultImg").css("display", "block");
				hgsUpdateData(getData, function (data) {
					console.log("new req 3===");
				})
				console.log("getScanResult else ret 0");
				return 0; */
			}
        })
    }

    function showScanResult(data){
        var innerHtml = "";
        var neighbourInfo = data;

        innerHtml += "<tr style='background-color: #8c8; font-weight: bold;'>"
        innerHtml += "<td>Serial number</td>"
        innerHtml += "<td>SSID</td>"
        innerHtml += "<td>Channel</td>"
        innerHtml += "<td>BSSID</td>";
        innerHtml += "<td>Frequency band</td>";
        innerHtml += "<td>Signal strength (dbm)</td>";
        innerHtml += "<td>Authentication method</td>";
        innerHtml += "</tr>"

        for(var i in neighbourInfo){
            var style = "";
            if(i & 1){
                style = "cursor: pointer"
            }else{
                style = "background-color: #ddd; cursor: pointer"
            }
            innerHtml += "<tr style='" + style 
                + "' class='select_ssid' encmode='" + neighbourInfo[i]["EncryptionMode"] 
                + "' SecurityMode='" + neighbourInfo[i]["SecurityModeEnabled"] 
                + "' band='" + neighbourInfo[i]["OperatingFrequencyBand"] 
                + "'>"

            var m = i;
            m++;
            innerHtml += "<td>"  + m + "</td>";
            innerHtml += "<td>"  + neighbourInfo[i]["SSID"] + "</td>";
            innerHtml += "<td>"  + neighbourInfo[i]["Channel"] + "</td>";
            innerHtml += "<td>"  + neighbourInfo[i]["BSSID"] + "</td>";
            innerHtml += "<td>"  + neighbourInfo[i]["OperatingFrequencyBand"] + "</td>";
            innerHtml += "<td>"  + String(parseInt(neighbourInfo[i]["SignalStrength"])-10) + "</td>";
            innerHtml += "<td>"  + neighbourInfo[i]["SecurityModeEnabled"] + "</td>";
            innerHtml += "</tr>"
        }
		
        $("#scanResultListTable").html(innerHtml);
    }

    function scanCountdown(){
        seconds--;
        $("#scanWifiNeedSecs").text(seconds);
        $("#scanResultListTable").hide();
        console.log("enter scanCountdown====");
        if(getsuccess==1 || seconds <= 0){
            $("#waitWifiScanResultImg").css("display", "none");
            $("#_L_nm_surf_realy_scanProgressing").hide();
            $("#scanWifiOverPrompt").show();
            $("#scanResultListTable").show();
			if(getsuccess==1){
				console.log("getScanResult =1 set second 0");
				seconds = 0;
			}
            return;
        }
        else if(seconds % 4 == 0){
			getScanResult()
            if(getsuccess==1){
				console.log("getScanResult =1 set second 0");
				seconds = 0;
			}				
        }
		
        setTimeout(scanCountdown, 1000);
    }
}

doWifiScan = function(){
    setTimeout(_doWifiScan, 1000);
}

repeaterCfgDisplay = function(){
    if($("#hgc_enableRelay").is(':checked')){    
        $("#configRelay").show();    
        $("#wifiScanText").show();
        $("#selectedRelayInfo").show()
        $("#relay").show()
        if (seconds > 0) {
            $("#scanResultListTable").empty();           
        }      
    }else{
        $("#configRelay").hide();
        $("#wifiScanText").hide();
        $("#selectedRelayInfo").hide();
        $("#relay").hide();
    }
}

repeaterCheckout = function(){
    repeaterCfgDisplay();
	loadHbusData("HGS_RELAY");
	// resizeSubNavContentHeight();
}

var func_onclick=function(){
	repeaterCfgDisplay();   
    doWifiScan();
}

$("#HGS_RELAY [name=hgc_enableRelay]").click(function () {
	if($("#hgc_enableRelay").is(':checked')){
		console.log("click hgc_enableRelay");
		doWifiScan();
	}else{
		var pathStr = "hbus://mdm/InternetGatewayDevice.WlanUpConnect.";
		var postData = {type:"POST", path:pathStr, commitData:{path:pathStr,para:{Enable:0}},msgType:212};
		
		hgsUpdateData(postData,function (result) {
			loadHbusData("HGS_RELAY");
		})					
		
		return;
	}
})

$("#do_relay").click(function(){
	$("#relayModal").modal('show');
	var width = 0,sty_width = '';
	var time = 0,i=1;
	var timer = setInterval(function () {
		if (width >= 100 && time >= 5000) {
			clearInterval(timer);		
			$(".FEATURE_WIFI [hgs_sub_nav=wlan_repeater_config]").click();
			$("#relayModal [data-dismiss=modal]").click();
			$(".progress-bar").attr('style','background-color: #5cb85c;width:0%');
		} else {
			width += i;
			sty_width = 'width:' + width + '%';
			$(".progress-bar").attr('style','background-color: #5cb85c;'+sty_width);
		}
		i += 2;
		time += 500;
	}, 500);
})

$("#rescanrepeater").click(function(){
	console.log("click refresh");
    if (seconds <= 0) {       
        func_onclick();      
    }
	resizeSubNavContentHeight();
})


$("#hgc_repeaterCfg").click(function(event){
    if($(this).attr("class").indexOf("viewHiddenDlg") == -1){
        //current class has no viewHiddenDlg(changed by js dynamically), do nothing
        event.stopPropagation();    //  阻止事件冒泡
        return;
    }
	
    if ( !$("#hgc_enableRelay").is(':checked') ) {
		alert("Please turn on wireless relay first");
		return;
    } 

	repeaterCfgDisplay();
	$("#scanWifiOverPrompt").hide();
	$("#HGS_RELAY").hide();
	resizeSubNavContentHeight();
	if (seconds <= 0) {       
        func_onclick();      
    }
})

$("#cancelrepeater").click(function () {
	$(".FEATURE_WIFI [hgs_sub_nav=wlan_repeater_config]").click();
})

relayCheckout = function(jsonData){
	$("#configRelay").hide();   
	$("#HGS_RELAY").show();   

	var getData = {type:"GET",
					path:"hbus://mdm/InternetGatewayDevice.Services.WifiMesh.", 
					msgType:211, 
					userTagData:1};

	if (isSubnetAP()) {
		hgsUpdateData(getData,function (data) {
			if (data[0].Status == "Up" || data[0].Status == "ServiceDown") {
				//组网成功
				$('[hgs_submit_div_id="HGS_REPEATER"]').attr("disabled",true);
				$("#HGS_RELAY #repeatertip").html("The WIFI parameters have been synchronized from the main gateway and cannot be modified.");
			}else{
				$('[hgs_submit_div_id="HGS_REPEATER"]').attr("disabled",false);
				$("#HGS_RELAY #repeatertip").html("");					
			}
		})	
	}

    if(jsonData.Enable  == '1'){		 
        $("#relay_status").show();
		$("#relay_status_tip").hide();
        seconds = 0;
    }else{       
        $("#relay_status").hide();
		$("#relay_status_tip").show();
    }	

	resizeSubNavContentHeight();
}

/*----------------------------------------------------------------------------*/

usbInfoUpdate = function(){
	loadTableData("HGST_USB_INFO");
}


usbInfoCheckout = function(data){
	var arrData=[];
	var usbStu = 0;
	var num = 0;

	for (var i = 0; i < data.length; i++) {
		if (data[i].fullPath.indexOf("LANUSBInterfaceConfig") > -1) {
			usbStu = parseInt(data[i].X_HG_USBPortStatus);
		} 
		else if (data[i].fullPath.indexOf("LANUSBInterfaceNumberOfEntries") > -1){
			num = parseInt(data[i].LANUSBInterfaceNumberOfEntries);
		}
	}

	if (usbStu) {
		USB1stu = "Connected";
	}else{
		USB1stu = "Not connected";
	}
	
	arrData = [{Name:"USB1", "Status":USB1stu}];
	return arrData;
}

/*----------------------------------------------------------------------------*/

logInfoUpdate = function(){
	loadTableData("HGST_LOG_INFO");
}


var g_logData;

logInfoCheckout = function(data){
	var logData = [];
	var rawData = data.split("\n");
	var levels = ["[emerg]", "[alert]", "[crit]", "[err]", "[warning]", "[notice]", "[info]", "[debug]"];
	

	for(i in rawData){
		timeArr = rawData[i].substr(0, 22).split(" ");
		if(timeArr.length < 3){
			continue;
		}
		logStr = rawData[i].substr(22);

		level = parseInt(timeArr[0]);
		logData.push({Time:timeArr[1] + " " + timeArr[2], 
		dbgLevel:level, Level:levels[parseInt(timeArr[0])], log:logStr});
	}
	//return logData;

	g_logData = logData;


	var currPageSize = g_tableRules["HGST_LOG_INFO"]["easyui"]["pageSize"];
	
	/*There is an exeption in first time(due to the table dosen't exist). so try it*/
	try{
		currPageSize = $("#" + getTableIdByHgstId("HGST_LOG_INFO")).datagrid("getPager").data("pagination").options.pageSize;
	}catch(err){

	}
	

	return {total:logData.length, rows:logData.slice(0, currPageSize)};
}


logFilter = function(dg){
	var filter = [
		{
			field:'dbglevel',
			type:'numberbox',
			options:{precision:1},
			op:['equal','notequal','less','greater']
		},
		{
			field:'Level',
			type:'combobox',
			options:{
				'panelHeight':"auto",
				"data":[
					{value:"",text:"All levels"},
					{value:"0",text:"emerg"},
					{value:"1",text:"alert"},
					{value:"2",text:"crit"},
					{value:"3",text:"err"},
					{value:"4",text:"warning"},
					{value:"5",text:"notice"},
					{value:"6",text:"info"},
					{value:"7",text:"debug"}
				],
				onChange:function(value){
					if (value == ''){  //不过滤,只能为空
						dg.datagrid('removeFilterRule', 'dbgLevel');
					} else {
						dg.datagrid('addFilterRule', {
							field: 'dbgLevel',
							op: 'lessorequal',
							value: value
						});
					}
					dg.datagrid('doFilter');
				}
			}
		}
	];


	return filter;
}

logPage = function(dg){
	var pager = dg.datagrid('getPager');
	var state = dg.data('datagrid');
	var opts = state.options;

	pager.pagination('refresh',{
		pageNumber:1,
		pageSize:50
	});

	return {
		onSelectPage:function(pageNum, pageSize){
			opts.pageNumber = pageNum;
			opts.pageSize = pageSize;

			var newData = {
				total: g_logData.length,
				rows: g_logData
			}

			dg.datagrid('loadData',newData);
			pager.pagination('refresh',{
				pageNumber:pageNum,
				pageSize:pageSize
			});

		},
		onChangePageSize:function(pageSize){
			setTimeout(function(){
				resizeSubNavContentHeight();
				}, 1000);
		}
	}
}

logDownload = function(){
	download("/log?action=download", "syslog.txt");
}

logDelete = function(){
	var r=confirm("Are you sure you want to delete all log files?");
	if (r!=true){
		return;
	}

	hgsUpdateData({type:"GET", url:"/log?action=delete"}, function(data){
		setTimeout(function(){
			loadTableData("HGST_LOG_INFO");
		}, 1000);
	})
}

/*----------------------------------------------------------------------------*/

pingCheckout = function(data){
	var wanInfo = getWanInfo(data);
	var innerHtml = "";
	
	if (!g_staticInfo["SupportVoip"]) {
		wanInfo = wanInfo.filter(item => !(item.Name.includes("VOIP") && !item.Name.includes("INTERNET")));
	}
	
	for(i in wanInfo){
		innerHtml += "<option value='" + wanInfo[i].IfName  + "' >" + wanInfo[i].Name + "</option>";
	}

	$("#pingSelectWan").html(innerHtml);
	return;
}

pingGetData = function(countdown) {
    hgsUpdateData({type: "GET", url: "/getPingData"}, function(data) {
		if (countdown <= 0) {
			var pingdata = data.split("---ping--over---");
			$("#PingTestData").text(pingdata[0]);
			return;
		}

        if (data.includes("---ping--over---")) {
            var pingResult = data.split("---ping--over---")[0].trim();
            $("#PingTestData").text(pingResult);
            return;
        }
        if (countdown > 0) {
            countdown--;
            setTimeout(pingGetData, 1000, countdown);
        } else {
            $("#PingTestData").text("Failed to receive complete ping data or end marker within the specified time!");
        }
    });
}

pingCheckin = function(data){
	var pingParam = "";
	var ipVersion = " -4 ";
	var errorMsg = "";
	var countNum = "5";
	var pingCfg = {};

	if ($("#pingProtocol").val() == "IPv6") {
		ipVersion = " -6 ";
		errorMsg = strategies.isValidIPv6(data.Dest, "Invalid parameter: IP address [" + data.Dest + "]");
	} else if ($("#pingProtocol").val() == "IPv4") {
		ipVersion = " -4 ";
		errorMsg = strategies.isValidIP(data.Dest, "Invalid parameter: IP address [" + data.Dest + "]");
	} else {
		errorMsg = "Err ipVersion";
	}

	if (errorMsg) {
		errorMsg = strategies.isURL(data.Dest, "Invalid parameter: IP address or domain name [" + data.Dest + "]");
	}

	if (errorMsg) {
		$("#HGS_PING [hgs_key='Dest']").focus();
		alert(errorMsg);
		return true;
	}

	pingParam  = ipVersion;
	pingParam += "-c " + countNum;
	pingParam += " " + $.trim(data.Dest);

	if (g_staticInfo["IsFTTR"] && g_staticInfo["IsMasterGateway"]) {
		pingParam += " -I " + $("#pingSelectWan").val();
	}

	pingCfg.pingParam = pingParam;
	pingCfg.Url = $.trim(data.Dest);
	pingCfg.wanName = $("#pingSelectWan").val();

	$.post("/ping", JSON.stringify(pingCfg), function(data){
		$("#PingTestData").text(data);
		setTimeout(pingGetData, 1000, 20);
	});

	return;
}

/*----------------------------------------------------------------------------*/
tracertCheckout = function(data){
	var wanInfo = getWanInfo(data);
	var innerHtml = "";

	if (!g_staticInfo["SupportVoip"]) {
		wanInfo = wanInfo.filter(item => !(item.Name.includes("VOIP") && !item.Name.includes("INTERNET")));
	}

	for(i in wanInfo){
		innerHtml += "<option value='" + wanInfo[i].IfName  + "' >" + wanInfo[i].Name + "</option>";
	}

	$("#tracertSelectWan").html(innerHtml);
	return;
}

tracertGetData = function(countdown){
	hgsUpdateData({type:"GET", url:"/getTracertData"}, function(data){
		$("#TracertTestData").text(data);
		// countdown--;
		if(countdown == 0){
			console.log("countdown over");
			// return;
		}
		if(data.indexOf("---traceroute--over---") >= 0){
			return;
		}
		setTimeout(tracertGetData, 1000, countdown);
	}) 
}

tracertCheckin = function(data){
	var command = "";
	var ipVersion = " -4 ";
	var errorMsg = "";
	var tracertParam = "";
	var tracertCfg = {};

	if($("#tracertProtocol").val() == "IPv6"){
		ipVersion = " -6 ";
		errorMsg = strategies.isValidIPv6(data.Dest, "Invalid parameter: IP address [" + data.Dest + "]");
	}else if($("#tracertProtocol").val() == "IPv4"){
		ipVersion = " -4 ";
		errorMsg = strategies.isValidIP(data.Dest, "Invalid parameter: IP address [" + data.Dest + "]");
	}else{
		errorMsg = "Err ipVersion!";
	}

	if(errorMsg){
		errorMsg = strategies.isURL(data.Dest, "Invalid parameter: IP address or domain name [" + data.Dest + "]");
	}
	if(errorMsg){
		$("#HGS_TRACERT [hgs_key='Dest']").focus();
		alert(errorMsg);
		return true;
	}
	tracertParam = ipVersion;
	tracertParam += " -I -n ";
	tracertParam += " -m " + data.TTL;
	tracertParam += " -q " + data.NumberPerHop;
	tracertParam += " -w " + data.TimeoutSec;
	if (g_staticInfo["IsFTTR"] && g_staticInfo["IsMasterGateway"]) {
		tracertParam += " -i " + $("#tracertSelectWan").val();
	}
	tracertParam += " " + $.trim(data.Dest);

	tracertCfg.tracertParam = tracertParam;
	tracertCfg.Url = $.trim(data.Dest);
	tracertCfg.wanName = $("#tracertSelectWan").val();

	var countdown = parseInt(data.TTL) + 100;

	$.post("/tracert", JSON.stringify(tracertCfg), function(data){
		$("#TracertTestData").text(data);
		setTimeout(tracertGetData, 1000, countdown);
	});

	return;
}

/*----------------------------------------------------------------------------*/

radvdCheckin = function(objName,objData){
	objData.fullPath = "InternetGatewayDevice.LANDevice.1.X_CMCC_RouterAdvertisement.";
	return [objData];
}

radvdCheckout = function(data){
	return data[0];
}

/*----------------------------------------------------------------------------*/


ipv6DnsCfgTypeChange = function(){
	switch($("#Ipv6DnsCfgType").val()){
		case "WANConnection":
			$("#Ipv6LanDnsStatic").hide();
			$("#Ipv6WanConnFullPath").show();
			var id = "IPv6DNSWANConnection";
			var path = "InternetGatewayDevice.LANDevice.1.X_CMCC_IPv6Config.";
			wanConnFullPath(id, path);
			break;

		case "Static":
			$("#Ipv6LanDnsStatic").show();
			$("#Ipv6WanConnFullPath").hide();
			break;

		case "HGWProxy":
			$("#Ipv6LanDnsStatic").hide();
			$("#Ipv6WanConnFullPath").hide();
			break;
	}
}
function wanConnFullPath(id,path) {
	var wanNames = [];
	var getData={Type:"GET",
				userTagData:1,
				msgType:211,
				path:"hbus://mdm/InternetGatewayDevice.WANDevice.{i}.WANConnectionDevice.{i}.WANIPConnection.{i}.;InternetGatewayDevice.WANDevice.{i}.WANConnectionDevice.{i}.WANPPPConnection.{i}.;"};				

	getData.path += path;
	
	hgsUpdateData(getData, function (data) {
		for(var i in data){
			fullPath = data[i].fullPath.replace(/\.[0-9]*\./g, ".{i}.");
			if((fullPath != "InternetGatewayDevice.WANDevice.{i}.WANConnectionDevice.{i}.WANIPConnection.{i}.")
				&&(fullPath != "InternetGatewayDevice.WANDevice.{i}.WANConnectionDevice.{i}.WANPPPConnection.{i}.")){
				continue;
			}
			if(data[i].Name){
				wanNames.push({Name:data[i].Name, fullPath:data[i].fullPath, X_CMCC_IPMode:data[i].X_CMCC_IPMode});
			}
		}

		wanNames.sort(strategies.sortBy('Name'));
	
		var innerHtml = "";
		for(i in wanNames){
			if (parseInt(wanNames[i].X_CMCC_IPMode) != 1) {
				innerHtml += "<option value='" + wanNames[i].fullPath  + "' >" + wanNames[i].Name + "</option>";	
			}
		}

		var selector = "#"+id;
		$(selector).html(innerHtml);	

		for (var j in data) {
			if (data[j].fullPath == path) {
				switch (id) {
					case "IPv6DNSWANConnection":
						var tmp = data[j].IPv6DNSWANConnection.substr(data[j].IPv6DNSWANConnection.length-1,1) ;
						if(tmp != ".")
						{
							data[j].IPv6DNSWANConnection = data[j].IPv6DNSWANConnection +".";
						}
						$(selector).val(data[j].IPv6DNSWANConnection);
						break;
					case "DelegatedWanConnection":
						var tmp = data[j].DelegatedWanConnection.substr(data[j].DelegatedWanConnection.length-1,1) ;
						if(tmp != ".")
						{
							data[j].DelegatedWanConnection = data[j].DelegatedWanConnection +".";
						}
						$(selector).val(data[j].DelegatedWanConnection);
						break;
					default:
						break;
				}
			}
		}
	})
}
$(".ipv6DnsCfgTypeChange").change(function(){

	ipv6DnsCfgTypeChange();
})

dhcpv6Checkin = function(objName,objData){
	if (strategies.compareIPv6('0000:0000:0000:0000:'+objData.MinAddress,'0000:0000:0000:0000:'+objData.MaxAddress) != -1) {
		alert("结束地址应大于起始地址! ");
		return;
	}	
	var ipv6LanObj = {};
	ipv6LanObj.fullPath = "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.IPInterface.1.X_CMCC_IPv6Address.";
	ipv6LanObj.LocalAddress = objData.LocalAddress;
	var dhcpv6ServerObj = {};
	dhcpv6ServerObj.fullPath = "InternetGatewayDevice.LANDevice.1.X_CMCC_DHCPv6Server.";
	dhcpv6ServerObj.Enable = objData.Enable;
	dhcpv6ServerObj.MinAddress = objData.MinAddress;
	dhcpv6ServerObj.MaxAddress = objData.MaxAddress;

	var ipv6LanDnsObj = {};
	ipv6LanDnsObj.fullPath = "InternetGatewayDevice.LANDevice.1.X_CMCC_IPv6Config.";
	ipv6LanDnsObj.IPv6DNSConfigType = objData.IPv6DNSConfigType;
	if(objData.IPv6DNSConfigType == "WANConnection")
	{
		ipv6LanDnsObj.IPv6DNSWANConnection = objData.IPv6DNSWANConnection;
	}
	else if(objData.IPv6DNSConfigType == "Static")
	{
		ipv6LanDnsObj.IPv6DNSServers = objData.IPv6DNSServers;
	}
	return [ipv6LanObj , dhcpv6ServerObj, ipv6LanDnsObj ];

}

dhcpv6Checkout = function(data){
	var arr = [];
	for( var i in data){
		Object.assign(arr,data[i]);
	}

	//console.log(arr);
	ipv6DnsCfgTypeChange();
	return arr;
}

/*----------------------------------------------------------------------------*/

prefixModeChange = function(){
	switch($("#prefixMode").val()){
		case "WANDelegated":
			$("#prefixWanConnFullPath").show();
			$("#prefixAddr").hide();
			var id = "DelegatedWanConnection";
			var path = "InternetGatewayDevice.LANDevice.1.X_CMCC_IPv6Config.PrefixInformation.1.";
			wanConnFullPath(id, path);
			break;

		case "Static":
			$("#prefixWanConnFullPath").hide();
			$("#prefixAddr").show();
			break;

	}
}
$(".prefixModeChange").change(function(){

	prefixModeChange();
})

prefixCheckin = function(objName,objData){
	objData.fullPath = "InternetGatewayDevice.LANDevice.1.X_CMCC_IPv6Config.PrefixInformation.1.";
	return [objData];
}

prefixCheckout = function(data){

	
	prefixModeChange();
	return data[0];
}
/*----------------------------------------------------------------------------*/
voipLinkCheckout = function(data){

	var arr = [];
	for( var i in data){
		Object.assign(arr,data[i]);
	}
	arr.VoipPhoneNum = arr.URI;
	arr.VoipPhoneStatus = (arr.Status == "Up")? "Successful registration":"Not yet registered successfully";
	if(arr.Status == "Up")
	{
		arr.VoipPhoneError = "";
	}else
	{
		switch(arr.X_CMCC_LastRegisterError){
			case "0":
				arr.VoipPhoneError = "";
				break;
			case "1":
				arr.VoipPhoneError = "IAD module error";
				break;
			case "2":
				arr.VoipPhoneError = "Access route is unavailable";
				break;
			case "3":
				arr.VoipPhoneError = "Access server is not responding";
				break;
			case "4":
				arr.VoipPhoneError = "Wrong account";
				break;
			case "5":
				arr.VoipPhoneError = "Unknown error";
				break;
		}
	}
	
	return arr;
}

/*----------------------------------------------------------------------------*/
voipConfigCheckout = function (data) {
	var accountData = {};
	
	for (let i = 0; i < data.length; i++) {
		if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.") {
			accountData["Enable"] = (data[i].Enable == "Enabled")? true: false;
		} 
		else if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.SIP.") {
			if (data[i].AuthPassword == '') {
				if (g_staticInfo["Region"] != "Guangxi") {
					data[i].AuthPassword = '******';
				}
			}
			Object.assign(accountData, {"AuthUserName":data[i].AuthUserName,"AuthPassword":data[i].AuthPassword,"URI":data[i].URI});
		}
		else if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.") {
			Object.assign(accountData, {
				"RegistrarServer":data[i].RegistrarServer,
				"RegistrarServerPort":data[i].RegistrarServerPort,
				"ProxyServer":data[i].ProxyServer,
				"ProxyServerPort":data[i].ProxyServerPort,
				"OutboundProxy":data[i].OutboundProxy,
				"OutboundProxyPort":data[i].OutboundProxyPort,
				"X_CMCC_Standby-RegistrarServer":data[i]["X_CMCC_Standby-RegistrarServer"],
				"X_CMCC_Standby-RegistrarServerPort":data[i]["X_CMCC_Standby-RegistrarServerPort"],
				"X_CMCC_Standby-ProxyServer":data[i]["X_CMCC_Standby-ProxyServer"],
				"X_CMCC_Standby-ProxyServerPort":data[i]["X_CMCC_Standby-ProxyServerPort"],
				"X_CMCC_Standby-OutboundProxy":data[i]["X_CMCC_Standby-OutboundProxy"],
				"X_CMCC_Standby-OutboundProxyPort":data[i]["X_CMCC_Standby-OutboundProxyPort"]
			});
		}
	}

	return accountData;
}

voipConfigCheckin = function(objName,objData){
	var LineObj = {};
	LineObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.";
	LineObj.Enable = objData.Enable ? "Enabled":"Disabled";

	var LineSIPObj = {};
	LineSIPObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.SIP.";
	LineSIPObj.AuthUserName = objData.AuthUserName;
	if (objData.AuthPassword == "******") {
		// LineSIPObj.AuthPassword = "";
	}
	else {
		LineSIPObj.AuthPassword = objData.AuthPassword;
	}
	LineSIPObj.URI = objData.URI;

	var ConfigObj = {};
	ConfigObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.";
	ConfigObj.RegistrarServer = objData.RegistrarServer;
	ConfigObj.RegistrarServerPort = objData.RegistrarServerPort;
	ConfigObj.ProxyServer = objData.ProxyServer;
	ConfigObj.ProxyServerPort = objData.ProxyServerPort;
	ConfigObj.OutboundProxy = objData.OutboundProxy;
	ConfigObj.OutboundProxyPort = objData.OutboundProxyPort;
	ConfigObj["X_CMCC_Standby-RegistrarServer"] = objData["X_CMCC_Standby-RegistrarServer"];
	ConfigObj["X_CMCC_Standby-RegistrarServerPort"] = objData["X_CMCC_Standby-RegistrarServerPort"];
	ConfigObj["X_CMCC_Standby-ProxyServer"] = objData["X_CMCC_Standby-ProxyServer"];
	ConfigObj["X_CMCC_Standby-ProxyServerPort"] = objData["X_CMCC_Standby-ProxyServerPort"];
	ConfigObj["X_CMCC_Standby-OutboundProxy"] = objData["X_CMCC_Standby-OutboundProxy"];
	ConfigObj["X_CMCC_Standby-OutboundProxyPort"] = objData["X_CMCC_Standby-OutboundProxyPort"];	
	
	return [LineObj , LineSIPObj , ConfigObj];
}

voipAdvancedCfgCheckout = function (data) {
	var AdvData = {};
	for (let i = 0; i < data.length; i++) {
		if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.") {
			AdvData["DTMFMethod"] = data[i].DTMFMethod;
			AdvData["X_TIANYI_COM_FixedJitterBufferEnabled"] = data[i].X_TIANYI_COM_FixedJitterBufferEnabled;
			AdvData["X_TIANYI_COM_JitterBufferDynMin"] = data[i].X_TIANYI_COM_JitterBufferDynMin;
			AdvData["X_TIANYI_COM_JitterBufferDynMax"] = data[i].X_TIANYI_COM_JitterBufferDynMax;
		} 
		else if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.VoiceProcessing.") {
			Object.assign(AdvData, {"ReceiveGain":data[i].ReceiveGain,
					"TransmitGain":data[i].TransmitGain,
					"EchoCancellationEnable":parseInt(data[i].EchoCancellationEnable)});
		}
		else if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.") {
			Object.assign(AdvData, {"UseCodecPriorityInSDPResponse":data[i].UseCodecPriorityInSDPResponse,
					"RegisterExpires":data[i].RegisterExpires,
					"RegisterRetryInterval":data[i].RegisterRetryInterval,
					"X_CMCC_SessionUpdateTimer":data[i].X_CMCC_SessionUpdateTimer,
					"X_CMCC_PrackEnable":data[i].X_CMCC_PrackEnable,
					"X_CMCC_BootDeRegisterEnable":data[i].X_CMCC_BootDeRegisterEnable,
					"X_CMCC_SubscribeEnable":data[i].X_CMCC_SubscribeEnable,
					"SilenceSuppression":data[i].SilenceSuppression,
					"X_CMCC_HeartbeatSwitch":data[i].X_CMCC_HeartbeatSwitch,
					"X_CMCC_HeartbeatCycle":data[i].X_CMCC_HeartbeatCycle,
					"HookFlashDownTime":data[i].HookFlashDownTime,
					"HookFlashUpTime":data[i].HookFlashUpTime,
					"TimeSyncMode":data[i].TimeSyncMode,
					"CallIDShowMode":data[i].CallIDShowMode,
					"CIDPriorityMode":data[i].CIDPriorityMode,
					"PreferRemoteCodecSwitch":data[i].PreferRemoteCodecSwitch});
		}
	}

	return AdvData;
}

voipAdvancedCfgCheckin = function(objName,objData){
	var Obj = {};
	Obj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.";
	Obj.DTMFMethod = objData.DTMFMethod;
	Obj.X_TIANYI_COM_FixedJitterBufferEnabled = objData.X_TIANYI_COM_FixedJitterBufferEnabled;
	Obj.X_TIANYI_COM_JitterBufferDynMin = objData.X_TIANYI_COM_JitterBufferDynMin;
	Obj.X_TIANYI_COM_JitterBufferDynMax = objData.X_TIANYI_COM_JitterBufferDynMax;

	var voiceProcessingObj = {};
	voiceProcessingObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.VoiceProcessing.";
	voiceProcessingObj.ReceiveGain = objData.ReceiveGain;
	voiceProcessingObj.TransmitGain = objData.TransmitGain;
	voiceProcessingObj.EchoCancellationEnable = objData.EchoCancellationEnable;

	var voiceRegisterObj = {};
	voiceRegisterObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.";
	voiceRegisterObj.UseCodecPriorityInSDPResponse = objData.UseCodecPriorityInSDPResponse;
	voiceRegisterObj.RegisterExpires = objData.RegisterExpires;
	voiceRegisterObj.RegisterRetryInterval = objData.RegisterRetryInterval;
	voiceRegisterObj.X_CMCC_SessionUpdateTimer = objData.X_CMCC_SessionUpdateTimer;
	voiceRegisterObj.X_CMCC_PrackEnable = objData.X_CMCC_PrackEnable;
	voiceRegisterObj.X_CMCC_BootDeRegisterEnable = objData.X_CMCC_BootDeRegisterEnable;
	voiceRegisterObj.X_CMCC_SubscribeEnable = objData.X_CMCC_SubscribeEnable;
	voiceRegisterObj.SilenceSuppression = objData.SilenceSuppression;
	voiceRegisterObj.X_CMCC_HeartbeatSwitch = objData.X_CMCC_HeartbeatSwitch;
	voiceRegisterObj.X_CMCC_HeartbeatCycle = objData.X_CMCC_HeartbeatCycle;
	voiceRegisterObj.HookFlashDownTime = objData.HookFlashDownTime;
	voiceRegisterObj.HookFlashUpTime = objData.HookFlashUpTime;
	voiceRegisterObj.TimeSyncMode = objData.TimeSyncMode;
	voiceRegisterObj.CallIDShowMode = objData.CallIDShowMode;
	voiceRegisterObj.CIDPriorityMode = objData.CIDPriorityMode;
	voiceRegisterObj.PreferRemoteCodecSwitch = objData.PreferRemoteCodecSwitch;
	
	return [Obj , voiceProcessingObj , voiceRegisterObj];
}

voipCodecCheckin = function (objName, tableId, data, postData) {
	var dg = $("#" + getTableIdByHgstId("HGST_VOIP_CODEC"));

	CheckedData = dg.datagrid("getChecked");
	if(CheckedData.length){
		tableCheckedData = CheckedData[0];
		
		postData.type = "POST";
		postData.commitData = {para:{Codec:tableCheckedData.Codec,
									 Priority:tableCheckedData.Priority,
									 Enable:tableCheckedData.Enable}};
		
		if(tableCheckedData.fullPath){
			postData.msgType = 212;
			postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
		}else{		
			postData.msgType = 215;
			postData.path = "hbus://mdm/InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.Codec.List.{i}.";
		}
	
		postData.commitData.path = postData.path;
		setTimeout(voipCodecUpdate, 1000);
	}
}

voipCodecCheckout = function (data) {
	var codecData = [];

	for (let i = 0; i < data.length; i++) {
		if (i == 4) {
			//only the firt four are valid data
			break;
		}
		codecData[i] = data[i];
	}

	return codecData;
}

voipCodecUpdate = function () {
	loadTableData("HGST_VOIP_CODEC");
}

voipSupplyCfgCheckout = function (data) {
	var SupplyData = {};
	
	for (let i = 0; i < data.length; i++) {
		if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.") {
			SupplyData["Reversed_polarity"] = parseInt(data[i].Reversed_polarity)?true:false; 
		} 
		else if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.CallingFeatures.") {
			Object.assign(SupplyData, {"HotlineEnable":parseInt(data[i].X_CU_HotlineEnable),
					"HotlineTimer":data[i].X_CU_HotlineTimer,
					"HotlineNumber":data[i].X_CU_HotlineNumber,
					"CallWaitingEnable":parseInt(data[i].CallWaitingEnable),
					"ConferenceEnable":parseInt(data[i].ConferenceEnable),
					"X_BROADCOM_COM_CallHoldEnable":parseInt(data[i].X_BROADCOM_COM_CallHoldEnable)});
		}
		else if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.X_CMCC_IMS.") {
			SupplyData["hold-service"] = parseInt(data[i]["hold-service"]); 
		}
	}

	return SupplyData;
}

voipSupplyCfgCheckin = function(objName,objData){
	var Obj = {};
	Obj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.";
	Obj.Reversed_polarity = objData.Reversed_polarity?1:0;

	var CallingFeaturesObj = {};
	CallingFeaturesObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.CallingFeatures.";
	CallingFeaturesObj.X_CU_HotlineEnable = objData.HotlineEnable;
	CallingFeaturesObj.X_CU_HotlineTimer = objData.HotlineTimer;
	CallingFeaturesObj.X_CU_HotlineNumber = objData.HotlineNumber;
	CallingFeaturesObj.CallWaitingEnable = objData.CallWaitingEnable;
	CallingFeaturesObj.ConferenceEnable = objData.ConferenceEnable;
	CallingFeaturesObj.X_BROADCOM_COM_CallHoldEnable = objData.X_BROADCOM_COM_CallHoldEnable;
	
	var CallingFeaturesObj2 = {};
	CallingFeaturesObj2.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.X_CMCC_IMS.";
	CallingFeaturesObj2["hold-service"] = objData["hold-service"]?1:0;

	return [Obj , CallingFeaturesObj, CallingFeaturesObj2];
}

voipQosCfgCheckout = function (data) {
	var qosData = {};

	$("#S_DSCPMark").html("");
	$("#R_DSCPMark").html("");
	$("#S_X_CMCC_802-1pMark").html("");
	$("#R_X_CMCC_802-1pMar").html("");

	var innerDSCPHTML = "";
	var inner8021PHTML = "<option value=-1>Do not modify</option>";
	for (let i = 0; i < 64; i++) {
		innerDSCPHTML += "<option value=" + i + ">" + i + "</option>";
	}
	for (let i = 0; i < 8; i++) {
		inner8021PHTML += "<option value=" + i + ">" + i + "</option>";
	}

	$("#S_DSCPMark").html(innerDSCPHTML);
	$("#R_DSCPMark").html(innerDSCPHTML);
	$("#S_X_CMCC_802-1pMark").html(inner8021PHTML);
	$("#R_X_CMCC_802-1pMark").html(inner8021PHTML);
	
	if (data.length) {
		qosData["S_DSCPMark"] = data[0]["DSCPMark"];
		qosData["S_X_CMCC_802-1pMark"] = data[0]["X_CMCC_802-1pMark"];
		qosData["R_DSCPMark"] = data[1]["DSCPMark"];
		qosData["R_X_CMCC_802-1pMark"] = data[1]["X_CMCC_802-1pMark"];	
		$("#S_DSCPMark").val(qosData["S_DSCPMark"]);
		$("#S_X_CMCC_802-1pMark").val(qosData["S_X_CMCC_802-1pMark"]);
		$("#R_DSCPMark").val(qosData["R_DSCPMark"]);
		$("#R_X_CMCC_802-1pMark").val(qosData["R_X_CMCC_802-1pMark"]);
	}

	return qosData;
}
voipQosCfgCheckin = function (objName,objData) {
	var SIPObj = {};
	SIPObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.";
	SIPObj.DSCPMark = objData.S_DSCPMark;
	SIPObj["X_CMCC_802-1pMark"] = objData["S_X_CMCC_802-1pMark"];

	var RTPObj = {};
	RTPObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.RTP.";
	RTPObj.DSCPMark = objData.R_DSCPMark;
	RTPObj["X_CMCC_802-1pMark"] = objData["R_X_CMCC_802-1pMark"];
	
	return [SIPObj , RTPObj];
}

voipFaxCheckout = function (data) {
	var faxData = {};
	
	for (let i = 0; i < data.length; i++) {
		if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.X_CT-COM_G711Fax.") {
			faxData["Enable"] = parseInt(data[i].Enable);
			faxData["FaxMode"] = data[i].FaxMode;
			faxData["ControlType"] = data[i].ControlType;
		}
	}

	return faxData;
}

voipFaxCheckin = function (objName,objData) {
	var FaxObj = {};
	FaxObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.X_CT-COM_G711Fax.";
	FaxObj.Enable = objData.Enable;
	FaxObj.FaxMode = objData.FaxMode;
	FaxObj.ControlType = objData.ControlType;
	
	return [FaxObj];	
}

var voipProtocol;
voipProtocolCheckout = function (data) {
voipProtocol = data.X_CMCC_ServerType;
	if (data.X_CMCC_ServerType == '2') {
		$(".SIP").hide();
		$(".H248").show();
	} else {
		$(".H248").hide();
		$(".SIP").show();
	}
	return data;
}
voipProtocolCheckin = function (data) {
	var curProtocol = $("#HGS_VOIP_PROTOCOL [hgs_key='X_CMCC_ServerType']").val();
	var reboot=false;
	if ((voipProtocol == '0' || voipProtocol == '1') && curProtocol == '2') {
		reboot = true;
	} 
	else if (voipProtocol == '2' && (curProtocol == '0' || curProtocol == '1')){
		reboot = true;
	}

	if (reboot) {
		if(confirm("After executing this operation, the device needs to be restarted to ensure that the configuration data takes effect. Do you want to continue?")){
			var pathStr = "hbus://mdm/rebootDev";
			var postData = {type:"POST",path:pathStr,commitData:{para:{}},msgType:201,userTagData:6,waitTimeoutMs:5000};
			postData.commitData.path = postData.path;
			setTimeout(function () {
				hgsUpdateData(postData);
			},1000);
		}else{
			return data;
		}	
	}
}
voipAdvancedCfgH248Checkout = function (data) {
	var AdvData = {};
	for (let i = 0; i < data.length; i++) {
		if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.") {
			AdvData["DTMFMethod"] = data[i].DTMFMethod;
		} 
		else if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.VoiceProcessing.") {
			Object.assign(AdvData, {"ReceiveGain":data[i].ReceiveGain,
					"TransmitGain":data[i].TransmitGain,
					"EchoCancellationEnable":parseInt(data[i].EchoCancellationEnable)});
		}
		else if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.") {
			Object.assign(AdvData, {"SilenceSuppression":data[i].SilenceSuppression,
					"RtpPortStart":data[i].RtpPortStart,
					"RtpPortEnd":data[i].RtpPortEnd,
					"HookFlashDownTime":data[i].HookFlashDownTime,
					"HookFlashUpTime":data[i].HookFlashUpTime});
		}
	}

	return AdvData;
}
voipAdvancedCfgH248Checkin = function(objName,objData){
	var Obj = {};
	Obj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.";
	Obj.DTMFMethod = objData.DTMFMethod;

	var voiceProcessingObj = {};
	voiceProcessingObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.VoiceProcessing.";
	voiceProcessingObj.ReceiveGain = objData.ReceiveGain;
	voiceProcessingObj.TransmitGain = objData.TransmitGain;
	voiceProcessingObj.EchoCancellationEnable = objData.EchoCancellationEnable;

	var voiceRegisterObj = {};
	voiceRegisterObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.";
	voiceRegisterObj.SilenceSuppression = objData.SilenceSuppression;
	voiceRegisterObj.RtpPortStart = objData.RtpPortStart;
	voiceRegisterObj.RtpPortEnd = objData.RtpPortEnd;
	voiceRegisterObj.HookFlashDownTime = objData.HookFlashDownTime;
	voiceRegisterObj.HookFlashUpTime = objData.HookFlashUpTime;
	
	return [Obj , voiceProcessingObj , voiceRegisterObj];
}

voipCodecH248Update = function () {
	loadTableData("HGST_VOIP_CODEC_H248");
}
voipCodecH248Checkin = function (objName, tableId, data, postData) {
	var dg = $("#" + getTableIdByHgstId("HGST_VOIP_CODEC_H248"));

	CheckedData = dg.datagrid("getChecked");
	if(CheckedData.length){
		tableCheckedData = CheckedData[0];
		
		postData.type = "POST";
		postData.commitData = {para:{Codec:tableCheckedData.Codec,
									 Priority:tableCheckedData.Priority,
									 Enable:tableCheckedData.Enable}};
		
		if(tableCheckedData.fullPath){
			postData.msgType = 212;
			postData.path = "hbus://mdm/" + tableCheckedData.fullPath;
		}else{		
			postData.msgType = 215;
			postData.path = "hbus://mdm/InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.1.Codec.List.{i}.";
		}
	
		postData.commitData.path = postData.path;
		setTimeout(voipCodecH248Update, 1000);
	}
}

voipCodecH248Checkout = function (data) {
	var codecData = [];

	for (let i = 0; i < data.length; i++) {
		if (i == 4) {
			//only the firt four are valid data
			break;
		}
		codecData[i] = data[i];
	}

	return codecData;
}

voipSupplyCfgH248Checkout = function (data) {
	var SupplyData = {};
	
	for (let i = 0; i < data.length; i++) {
		if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.X_CT-COM_H248.") {
			Object.assign(SupplyData, {
					"HeartbeatMode":data[i].HeartbeatMode,
					"HeartbeatCycle":data[i].HeartbeatCycle,
					"HeartbeatCount":data[i].HeartbeatCount});
		} 
		else if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.") {
			SupplyData.CallIDShowMode = data[i].CallIDShowMode;
		}
	}

	return SupplyData;
}
voipSupplyCfgH248Checkin = function(objName,objData){
	var Obj = {};
	Obj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.X_CT-COM_H248.";
	Obj.HeartbeatMode = objData.HeartbeatMode;
	Obj.HeartbeatCycle = objData.HeartbeatCycle;
	Obj.HeartbeatCount = objData.HeartbeatCount;

	var CallingFeaturesObj = {};
	CallingFeaturesObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.";
	CallingFeaturesObj.CallIDShowMode = objData.CallIDShowMode;
	
	return [Obj , CallingFeaturesObj];
}


function dealOmciVoip() {
	var getData = {type:"GET",
					path:"hbus://mdm/InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.", 
					msgType:211};

	hgsUpdateData(getData,function (data) {
		if (data.IS_OMCI_VOIP == '1') {
			$(".omciVoip").hide();
		} else{
			$(".omciVoip").show();
		}
	})	
}
$("#context [page=application] [target_page=voip_protocol]").click(function () {
	dealOmciVoip();
})
/*----------------------------------------------------------------------------*/

$("#DoLogout").click(function(){
	$.get("/logout");
	setTimeout(function (params) {
		window.location.href = LOGIN_PAGE;
	},100);
})


/*----------------------------------------------------------------------------*/

$("#ISPDNSEnable").click(function(){
	if($("#ISPDNSEnable").is(':checked')){
		$(".ipv4DnsServer").show();
	}else{
		$(".ipv4DnsServer").hide();
	}
})

dhcpv4Checkout = function(data){
	var dhcpData = {};

	dhcpData.IPInterfaceIPAddress = data[0].IPInterfaceIPAddress;
	$("#HGS_DHCPV4 [hgs_key=IPInterfaceIPAddress]").attr("oldValue", dhcpData.IPInterfaceIPAddress);
	dhcpData.IPInterfaceSubnetMask = data[0].IPInterfaceSubnetMask;

	dhcpData.DHCPServerEnable = data[1].DHCPServerEnable;
	dhcpData.MinAddress = data[1].MinAddress;
	dhcpData.MaxAddress = data[1].MaxAddress;
	dhcpData.SubnetMask = data[1].SubnetMask;
	dhcpData.DHCPLeaseTime = data[1].DHCPLeaseTime;
	dhcpData.ISPDNSEnable = data[1].ISPDNSEnable;

	if(parseInt(dhcpData.ISPDNSEnable)){
		$(".ipv4DnsServer").show();
	}else{
		$(".ipv4DnsServer").hide();
	}

	var dnsServerTmp = data[1].DNSServers.split(",");
	if(dnsServerTmp.length == 2){
		dhcpData.ipv4DNSServer1 = dnsServerTmp[0];
		dhcpData.ipv4DNSServer2 = dnsServerTmp[1];
	}else{
		dhcpData.ipv4DNSServer1 = dnsServerTmp[0];	
	}

	objData = {objName:"HGS_DHCPV4", noCheckout:true}
	loadHbusRespData(dhcpData, objData);
}

dhcpv4PreCheckin = function(data, dhcpData){
	var errMsg;
	var changeIp = false;

	var MinAddress = strategies.convertIpStrToNum(dhcpData.MinAddress);
	var MaxAddress = strategies.convertIpStrToNum(dhcpData.MaxAddress);
	var IPInterfaceIPAddress = strategies.convertIpStrToNum(dhcpData.IPInterfaceIPAddress);

	dhcpData.SubnetMask = dhcpData.IPInterfaceSubnetMask;

	if(MaxAddress <= MinAddress){
		$("#HGS_DHCPV4 [hgs_key=MaxAddress]").focus();
		alert("[Address pool end address] must be greater than [Address pool start address]");
		return true;
	}

	errMsg = strategies.isSameSubnet(dhcpData.SubnetMask, "[Address pool end address] and [Address pool start address] are not in the same subnet!", 
		[dhcpData.MinAddress, dhcpData.MaxAddress]);
	if(errMsg){
		$("#HGS_DHCPV4 [hgs_key=MaxAddress]").focus();
		alert(errMsg);
		return true;
	}

	errMsg = strategies.isSameSubnet(dhcpData.SubnetMask, "[IP address] is not in the same subnet as the address pool!", 
		[dhcpData.MinAddress, dhcpData.IPInterfaceIPAddress])
	if(errMsg){
		$("#HGS_DHCPV4 [hgs_key=MaxAddress]").focus();
		alert(errMsg);
		return true;
	}

	if((IPInterfaceIPAddress >= MinAddress) && (IPInterfaceIPAddress <= MaxAddress)){
		$("#HGS_DHCPV4 [hgs_key=IPInterfaceIPAddress]").focus();
		alert("The LAN side IP address cannot be in the allocation range of the address pool!")
		return true;
	}
	
	if(dhcpData.IPInterfaceIPAddress != $("#HGS_DHCPV4 [hgs_key=IPInterfaceIPAddress]").attr("oldValue")){
		var r=confirm("You have changed the IP address. Changing the IP address will automatically restart the device. Are you sure to change the [IP address]?");
		if (r!=true){
			return true;
		}
		r=confirm("Please make sure your PC or other terminal and the newly modified IP [" + dhcpData.IPInterfaceIPAddress + 
			"]In the same address segment, otherwise it cannot be accessed normally, are you sure?");
		if (r!=true){
			return true;
		}
		changeIp = true;
	}

	var dhcpNewData = [];

	if(changeIp){
		dhcpNewData.push({
			fullPath:"InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.IPInterface.1.",
			IPInterfaceIPAddress:dhcpData.IPInterfaceIPAddress, 	
			IPInterfaceSubnetMask:dhcpData.IPInterfaceSubnetMask
		});
	}

	var ipv4DNSServers;
	if($("#ISPDNSEnable").is(':checked')){
		if (!$("#ipv4DNSServer1").val()) {
			alert("DNSServer1 cannot be empty!");
			return;
		}
		if (!$("#ipv4DNSServer1").val()) {
			ipv4DNSServers = $("#ipv4DNSServer1").val();
		}else{
			ipv4DNSServers = $("#ipv4DNSServer1").val()+','+$("#ipv4DNSServer2").val();
		}
	}

	dhcpNewData.push({
		fullPath:"InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.",
		DHCPServerEnable:dhcpData.DHCPServerEnable, 	
		MinAddress:dhcpData.MinAddress,
		MaxAddress:dhcpData.MaxAddress,
		SubnetMask:dhcpData.SubnetMask,
		DHCPLeaseTime:dhcpData.DHCPLeaseTime,
		ISPDNSEnable:dhcpData.ISPDNSEnable,
		DNSServers:ipv4DNSServers
	});

	if(changeIp){
		var data = {url:"/changeLanIp",
			type : "POST",
			commitData:dhcpNewData
		};

		hgsUpdateData(data, function(result){
			location = "/reboot.html?newIp=" + dhcpData.IPInterfaceIPAddress;
		})
		return;
	}
	

	return dhcpNewData;
}

/*----------------------------------------------------------------------------*/
osgiInfoCheckout = function(data){
	for (let i = 0; i < data.length; i++) {
		const element = data[i];
		if (element.Status == "Active") {
			element.Status = "start up";
		} else {
			element.Status = "stop";
		}
	}
	return data;
}

osgiInfoUpdate = function(){
	loadTableData("HGST_OSGI_INFO");
}

osgiLoadSuccess = function (data) {
	$(".easyui-switchbutton").switchbutton({
		onText:"open",
		offText:"close",
		onChange:function (checked) {
			var id = $(this).attr("id");
			var idx = id.substr(id.length-1,1);
			if (checked) {
				var pathStr = "hbus://mdm/InternetGatewayDevice.SoftwareModules.ExecutionUnit."+ idx + ".";
				var postData = {type:"POST", path:pathStr, commitData:{path:pathStr,para:{RequestedState:"Active"}},msgType:212};
				hgsUpdateData(postData,function (result) {
					setTimeout(osgiInfoUpdate, 500);
				})
			}
		}
	})
}

showFormat = function (value,row,index) {
	var tmp = "";
	var idx = row.fullPath.substr(row.fullPath.length-2,1);
	if (row.Status == "start up") {
		tmp = '<input id="swt_'+idx+'" class="easyui-switchbutton" checked disabled>';
	} else {
		tmp = '<input id="swt_'+idx+'" class="easyui-switchbutton">';
	}
	
	return tmp;
}
/*----------------------------------------------------------------------------*/

mirrorCfgUpdate = function(data){
	var mirrorCfg = data;

	$("#HGS_MIRROR_CFG [hgs_key=wanMirrorEnable]").attr("checked", mirrorCfg.wanMirrorEnable?true:false);

	if(mirrorCfg.source){
		$("#HGS_MIRROR_CFG [hgs_key=source][hgs_checked_value=" + mirrorCfg.source + "]").attr("checked", true);
	}else{
		$("#HGS_MIRROR_CFG [hgs_key=source]").attr("checked", false);
	}

	if(mirrorCfg.dest){
		$("#HGS_MIRROR_CFG [hgs_key=dest][hgs_checked_value=" + mirrorCfg.dest + "]").attr("checked", true);
	}else{
		$("#HGS_MIRROR_CFG [hgs_key=dest]").attr("checked", false);
	}
	if(mirrorCfg.persistent == "1"){
		$("#HGS_MIRROR_CFG [hgs_key=persistent][hgs_checked_value=" + mirrorCfg.persistent + "]").attr("checked", true);
	}else{
		$("#HGS_MIRROR_CFG [hgs_key=persistent]").attr("checked", false);
	}
}


mirrorCfgCheckin = function(){
	var mirrorCfg = {};
	var mirrorCheckList = document.querySelectorAll("#HGS_MIRROR_CFG [hgs_checked_value]");

	for(x in mirrorCheckList){
		if(mirrorCheckList[x].checked){
			mirrorCfg[mirrorCheckList[x].getAttribute("hgs_key")] = mirrorCheckList[x].getAttribute("hgs_checked_value");
		}
	}

	if((!mirrorCfg.source) && (!mirrorCfg.wanMirrorEnable)){
		alert("No mirror source port is selected!");
		return true;
	}

	if(!mirrorCfg.dest){
		alert("No mirroring destination port is selected!");
		return true;
	}

	if(mirrorCfg.source == mirrorCfg.dest){
		alert("The mirror source port and destination port cannot be the same port!");
		return true;
	}
	if (mirrorCfg.persistent)
		mirrorCfg.persistent = "1";
	else
		mirrorCfg.persistent = "0";

	$.post("/mirrorCfg?action=set", JSON.stringify(mirrorCfg), function(data){
		mirrorCfgUpdate(data);
	});

	return true;
}

mirrorCfgDelete = function(){
	var mirrorCheckList = document.querySelectorAll("#HGS_MIRROR_CFG [hgs_checked_value]");

	for(x in mirrorCheckList){
		mirrorCheckList[x].checked = false;
	}

	$.get("/mirrorCfg?action=clear", function(){
		
	})

	return true;
}

mirrorCfgCheckout = function(){
	$.get("/mirrorCfg?action=get", function(data){
		mirrorCfgUpdate(data);
	})
}

/*----------------------------------------------------------------------------*/

ipv4RouteTableCheckout = function(){
	$.get("/routeTable?protocol=IPV4", function(data){
		$("#HGS_IPV4_ROUTE_TEXT").val(data);
	})
}

ipv6RouteTableCheckout = function(){
	$.get("/routeTable?protocol=IPV6", function(data){
		$("#HGS_IPV6_ROUTE_TEXT").val(data);
	})	
}

ipv4PolicyRouteTableCheckout = function(){
	$.get("/routeTable?protocol=IPV4&isPolicy=true", function(data){
		$("#HGS_IPV4_POLICY_ROUTE_TEXT").val(data);
	})
}

ipv6PolicyRouteTableCheckout = function(){
	$.get("/routeTable?protocol=IPV6&isPolicy=true", function(data){
		$("#HGS_IPV6_POLICY_ROUTE_TEXT").val(data);
	})	
}
/*----------------------------------------------------------------------------*/
voipDigitalmapCheckout = function (data) {
	var dData = {};
	
	for (let i = 0; i < data.length; i++) {
		if (data[i].fullPath == "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.") {
			dData["DigitMapEnable"] = parseInt(data[i].DigitMapEnable);
			$("#DigitMap").text(data[i].DigitMap);
			dData["ImmediatlyDigit"] = data[i].ImmediatlyDigit;
		} 
	}

	return dData;
}


voipDigitalmapCheckin = function (objName,objData) {
	var voiceProfileObj = {};
	voiceProfileObj.fullPath = "InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.";
	voiceProfileObj.DigitMapEnable = objData.DigitMapEnable;
	voiceProfileObj.DigitMap = $("#DigitMap").val();
	voiceProfileObj.ImmediatlyDigit = objData.ImmediatlyDigit;
	
	return [voiceProfileObj];	
}
/*----------------------------------------------------------------------------*/
var t_mesh;
var topoData = {};
$("a[hgs_sub_nav='meshtopo']").click(function () {
	clearInterval(t_mesh);
	meshTopo();
	t_mesh = setInterval(meshtopoUpdata, 2000);
});

function meshtopoUpdata() {
	if (!$("#HGS_MESH_TOPO").is(":visible")) {
		clearInterval(t_mesh);
		return;
	}

	meshTopo();
}

function meshTopo() {
    $.get('/onlineDevTopo',function (jsonData) {
		if (JSON.stringify(jsonData) != JSON.stringify(topoData)) {			
			topoData = jsonData;
			drawTopo(jsonData);	
		}
    });
}
/*----------------------------------------------------------------------------*/

$("#exportCfgFileBtn").click(function(){
	download("/hgdumpcfg", "backupConfig.dat");
})
$('#selectCfgFileBtn').change(function(){
    var file = this.files[0];
    fileName = file.name;
    size = file.size;
    type = file.type;

	$("#upgradeCfgBtn").attr("disabled", file.size?false:true);
});
$('#upgradeCfgBtn').click(function(){
    var formData = new FormData(document.querySelector("#cfgFileForm"));
    $.ajax({
        url: 'hguploadcfg',  //server script to process data
        type: 'POST',
        xhr: function() {  // custom xhr
            myXhr = $.ajaxSettings.xhr();
            return myXhr;
        },
        //Ajax事件
        beforeSend: beforeSendCfgFile,
        success: completeCfgFile,
        error: errorCfgFile,
        // Form数据
        data: formData,
        //Options to tell JQuery not to process data or worry about content-type
        cache: false,
        contentType: false,
        processData: false
    });
});
function beforeSendCfgFile(jqXHR, settings){
	$("#upgradeCfgInfo").text("Start uploading files!");
}
function completeCfgFile(){
	$("#upgradeCfgInfo").text(strategies.getCurrentDateTime() + " 上传文件成功!");
	// cfgFilesUpdate();
}
function errorCfgFile(e){
	var strInfo = "Error uploading file! Error code:" + e.status +", Error description:" + e.statusText;
	$("#upgradeCfgInfo").text(strInfo);
	alert(strInfo);
}


/*----------------------------------------------------------------------------*/

hostDevInfoCheckout = function(data){

	for(var x in data){
		if(data[x]["HostName"]){
			bytes = hexToBytes(data[x]["HostName"]);
			data[x]["HostName"] = gbkToUtf8(bytes);
		}
		data[x]["DeviceType"] = getDeviceType(data[x]["HostName"], data[x]["VenderId"]);
	}

	return data;
}

})


hostIpv6DevInfoCheckout = function(data){

	for(var x in data){
		if(data[x]["HostName"]){
			bytes = hexToBytes(data[x]["HostName"]);
			data[x]["HostName"] = gbkToUtf8(bytes);
		}
		data[x]["DeviceType"] = getDeviceType(data[x]["HostName"], data[x]["VenderId"]);
	}

	return data;
}

/*----------------------------------------------------------------------------*/

smbAnymousUpdate = function(){
	if($("#smbAnymous").is(":checked")){
		$("#smbAccount").hide();
	}else{
		$("#smbAccount").show();
	}
	resizeSubNavContentHeight();
}

smbEnableCheck = function () {
	if($("#smbEnable").is(":checked")){
		$("#smbAnymousDiv").show();
		smbAnymousUpdate();
	}else{
		$("#smbAnymousDiv").hide();
		$("#smbAccount").hide();
	}	
}

$("#smbEnable").click(function() {
	smbEnableCheck();
})

$("#smbAnymous").click(function(){
	smbAnymousUpdate();
})

sambaUpdate = function(data){
	// smbAnymousUpdate();
	smbEnableCheck();
}
