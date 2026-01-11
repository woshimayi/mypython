var g_removeClassEle = g_regionCfg.removeFeatures;


$(function () {


function selectOnuAuthOptions(){
	if(typeof g_regionCfg.onuAuthType == "undefined"){
		return;
	}
	switch(g_regionCfg.onuAuthType){
		case "Password":
			$(".rm_onuLoid").remove();
			$(".rm_onuLoidPlusPassword").remove();
			
			$(".rm_onuLoidInput").remove();
			$("#OnuAuthType").val(1);
			break;

		case "Loid":
			$(".rm_onuPassword").remove();
			$(".rm_onuLoidPlusPassword").remove();

			$(".rm_onuPasswordInput").remove();
			$("#OnuAuthType").val(2);
			break;

		case "Loid+Password":
			$(".rm_onuLoid").remove();
			$(".rm_onuPassword").remove();
			$("#OnuAuthType").val(3);
			break;
	}
	
}

function replaceLanBindText() {
	if (!g_regionCfg.lanBind) {
		return;
	}

	for (const k in g_regionCfg.lanBind) {
		$("#WanBindInterface [hgs_checked_value ='" + k + "']")[0].nextSibling.nodeValue = g_regionCfg.lanBind[k];
	}
}

function show2_4gGuest() {
	$("#WifiBand").empty();
	$("#WifiBand").append('<option value="2d4g" fullPath="InternetGatewayDevice.LANDevice.1.WLANConfiguration.1." >SSID1</option>')
	$("#WifiBand").append('<option class="FEATURE_ADMIN" value="2d4g" fullPath="InternetGatewayDevice.LANDevice.1.WLANConfiguration.2." >SSID2</option>');
	$("#WifiBand").append('<option class="FEATURE_ADMIN" value="2d4g" fullPath="InternetGatewayDevice.LANDevice.1.WLANConfiguration.3." >SSID3</option>');
	$("#WifiBand").append('<option class="FEATURE_ADMIN" value="2d4g" fullPath="InternetGatewayDevice.LANDevice.1.WLANConfiguration.4." >SSID4</option>');
	$("#WifiBand").append('<option value="5g" fullPath="InternetGatewayDevice.LANDevice.1.WLANConfiguration.5." >SSID5</option>');
}

function showIptvAccount() {
	if(!g_regionCfg.showIPTVAccount){
		$("#iptvAccount").remove();
	}
}

function showFooterAtBottom() {
	$("body").css("padding-bottom","50px");
	$(".foot_note").css("position","fixed");
	$(".foot_note").css("left","0px");
	$(".foot_note").css("bottom","0px");
	$(".foot_note").css("width","100%");
	$(".foot_note").css("z-index",9999);
}

function showWlanAxAsOther() {
	$("#HGS_WLAN_ADV_CFG [hgs_key=Standard]").find("[value=ax]").text("b/g/n/ax");
}

function adjustHtmlElements(){
	if(g_removeClassEle){
		for(var i in g_removeClassEle){
			$("." + g_removeClassEle[i]).remove();
		}
	}

	if(!g_regionCfg.registerPopup){
		$(".FEATURE_REGISTER_POPUP").remove();
	}

	if(!g_regionCfg.DeviceOthersInformation){
		$(".DEVICE_OTHERS_INFORMATION").remove();
	}

	if(!g_regionCfg.SoftWareBuildTime){
		$(".SOFT_WARE_BUILD_TIME").remove();
	}

	if(g_regionCfg.HideBSSID){
		$(".HIDE_OTHERS_BSSID").remove();
	}

	if(!g_regionCfg.HideBSSID){
		$(".SHOW_LAN_MAC").remove();
	}

	if(!g_regionCfg.networkAccessLicense){
		// $(".NETWORK_ACCESS_LICENSE").remove();
	}

	if(g_regionCfg.noMirrorCfg){
		$(".FEATURE_MIRROR").remove();
	}else{
		if(!g_regionCfg.omciMirrorCfg){
			$(".FEATURE_OMCI_MIRROR").remove();
		}
	}

	if (g_regionCfg.RMSOnlyRead) {
		$('#HGS_REMOTE_MANAGE input[type="button"]').prop('disabled', true);
		$("#selectWan").bind("change.foo",handle)
		function handle(event) {
			var text = $("#selectWan").find("option:selected").text();
			if (text.indexOf("TR069") > -1) {
				$("#HGS_WAN .saveBtn").hide();
				$("#HGS_WAN .deleteBtn").hide();
				if (g_regionCfg.disableRmsParameters) {
					$("#HGS_WAN .paraDisable").attr("disabled",true);
				}
			} else {
				$("#HGS_WAN .saveBtn").show();
				$("#HGS_WAN .deleteBtn").show();
				if (g_regionCfg.disableRmsParameters) {
					$("#HGS_WAN .paraDisable").attr("disabled",false);
				}				
			}			
		}
	}
	if (g_regionCfg.disableRmsParameters) {		
		$('#HGS_REMOTE_MANAGE .paraDisable').attr("disabled",true);
	}

	if (g_regionCfg.show2_4gGuest) {
		show2_4gGuest();
	}

	if (!g_regionCfg.scheduleReboogCfg) {
		$(".FEATURE_SCHEDULE_REBOOT").remove();
	}
	selectOnuAuthOptions();
	replaceLanBindText();
	showIptvAccount();

	if (g_regionCfg.showFooterAtBottom) {
		showFooterAtBottom();
	}

	if (g_regionCfg.showWlanAxAsOther) {
		showWlanAxAsOther();	
	}

	if (!g_regionCfg.bucpe) {
		$(".FEATURE_BUCPE").remove();
	}

	if (!g_regionCfg.showpppoeDial) {
		$(".pppoeDial").remove();
	}

	if (!g_regionCfg.showTelnet) {
		$(".FEATURE_TELNET").remove();
	}

	if (g_regionCfg.noConsole) {
		$(".FEATURE_CONSOLE").remove();
	}	
	
	if (g_regionCfg.noRouteTable) {
		$(".TEATURE_IPV4ROUTE").remove();
		$(".TEATURE_IPV6ROUTE").remove();
	}

	if (g_regionCfg.noPolicyRoute) {
		$(".TEATURE_IPV4POLICYROUTE").remove();
		$(".TEATURE_IPV6POLICYROUTE").remove();
	}
	
	if (!g_regionCfg.ipv4DNS) {
		$(".FEATURE_IPv4DNS").remove();
	}

	if (!g_regionCfg.WLANSignalCfg) {
		$(".FEATURE_WLANSIGNAL").remove();
	}

	if (g_regionCfg.OpticalManageReadOnly) {
		$('#HGS_OPTICAL_MANAGE_INFO input[type="button"]').prop("disabled",true);
	}
	
	if (g_regionCfg.notDisplayFiberLANWIFI) {
		$('#HGS_OPTICAL_MANAGE_INFO option[value="0"]').remove();
	}
}

adjustHtmlElements();

})
