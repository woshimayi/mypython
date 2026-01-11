$(function () {
	var time;
	var progress=0, timer=0;
	var reg100 = false,reg99 = false,reg60 = false,reg50=false;	
	var inputType = "Password";	
	var sum = 3;
	var region = getRegionFullName();
	var TIMES = 60;
	
	selectOnuLoidPwd();
	checkRegisterStu();
	
	$("#backToLogin").click(function () {
		window.top.location.href = "http://"+g_staticInfo["LanIpv4Addr"]+"/login.html";
	})
	$("#backBtn").click(function () {
		window.top.location.href = "http://"+g_staticInfo["LanIpv4Addr"]+"/login.html";
	})
	$("#backToRegBtn").click(function () {
		$(".form_box").show();
		$("#progress_info").addClass("hideElm");
		$("#backToReg").addClass("hideElm");
		clearInterval(timer);
		register_sm.initial();
	})
	$("#reset").click(function () {
		$("#Password").val("");
		$("#pwdLength").html(0);
	})
	$("#save").click(function () {
		register();
	});
	
	//errMsg20：20%时错误的信息
	//errMsg30: 30%时错误的信息
	//errMsg40：40%->50%超时提示(10min未成功到50%)
	//errMsg401，errMsg402：40%时错误的信息
	//errMsg401：连接平台失败次数 未超过最大限制(10次)
	//errMsg402：连接平台失败次数  超过最大限制(10次)
	//errMsg60：50%->60%超时提示(10min未成功到60%)；60%->99%超时提示(10min未成功到99%)；99%->100%超时提示(10min未成功到100%)
	var register_sm = new StateMachine({
		init:'initial_0_percent',
		transitions:[ 
			{name:"initial",             from:"*",                    to:"initial_0_percent"},
			{name:"register",            from:"initial_0_percent",    to:"register_20_percent"},
			{name:"ponRegistered",       from:"register_20_percent",  to:"uplink_30_percent"},
			{name:"ethUplinkConnected",  from:"initial_0_percent",    to:"uplink_30_percent"},
			{name:"tr69IPGot",           from:"uplink_30_percent",    to:"tr69IP_40_percent"},
			{name:"rmsConnected",        from:"tr69IP_40_percent",    to:"RMS_50_percent"},
			{name:"startService",        from:"RMS_50_percent",       to:"service_61_percent"},
			{name:"serviceDistributed",  from:"service_61_percent",   to:"success_100_percent"},
			{name:"failed",              from:"*",                    to:"FAIL"}
		],
		data:{
			progressInfo:{
				"20%"       :  "Registering OLT",
				"30%"       :  "Obtaining management IP",
				"40%"       :  "The management IP has been obtained and is connecting to the provincial digital home management platform",
				"50%"       :  "Waiting for the provincial digital home management platform to issue business data",
				"60%"       :  "The provincial digital home management platform is sending business data. Please do not turn off the power or unplug the optical fiber.",
				"61%"       :  "省级数字家庭管理平台正在下发 ",
				"62%"       :  " 业务数据，请勿断电或拔光纤",
				"100%"       :  "The business data of the provincial digital home management platform was successfully issued",
				"101%"      :  "省级数字家庭管理平台业务数据下发成功，共下发了 ",
				"102%"      :  " 个业务",
				"regMsgSuccess"  :  "Already registered successfully, no need to register again"
			},
			failInfo:{
				"errMsg20" : "Failed to register on OLT. Please check whether the optical signal light is off and whether the loid/password is correct.",
				"errMsg20_l" : "Failed to register on OLT, please check whether the optical signal light is off and whether the loid is correct",
				"errMsg20_p" : "Failed to register on OLT. Please check whether the optical signal light is off and the password is correct.",
				"errMsg30" : "The channel of the provincial digital home management platform is blocked, please contact the account manager or call 10086" or the IP address is not obtained",
				"errMsg40" : "The channel to the provincial digital home management platform is blocked. Please contact your account manager or call 10086",
				"errMsg401" : "Registration failed on the provincial digital home management platform, retrying",
				"errMsg402" : "If the registration on the provincial digital home management platform fails, please contact your account manager or call 10086",
				"errMsg60" : "If the provincial digital home management platform issues abnormal services, please contact your account manager or call 10086",
				"errMsg40_stu1" : "Error code 1, Password does not exist",
				"errMsg40_stu4" : "Error code 4, timeout",
				"errMsg40_stu5" : "Error code 5, already registered and no new work order to execute",
			}
		},
		methods:{
			//AfterTransition
			onAfterRegister: function () {//excute automatically
			},		
			onAfterPonRegistered: function () {//excute automatically
			},
			onAfterEthUplinkConnected: function () {//excute automatically
			},
			onAfterTr69IPGot: function () {
			},
			onAfterRmsConnected: function () {
			},
			onAfterStartService: function () {
			},
			onAfterServiceDistributed: function () {
			},
			onAfterFailed: function (lifecycle) {
				switch (lifecycle.from) {
					case "register_20_percent":
						if(g_regionCfg.onuAuthType == "Password"){
							this.showErrMsg("errMsg20_p");
						}else if (g_regionCfg.onuAuthType == "Loid") {
							this.showErrMsg("errMsg20_l");
						}else{
							this.showErrMsg("errMsg20");
						}
						break;
					case "uplink_30_percent":
						this.showErrMsg("errMsg30");
						break;
					case "tr69IP_40_percent":
						this.showErrMsg("errMsg40");
						break;
					case "RMS_50_percent":
					case "service_61_percent":
					case "service_70_percent":
					case "service_80_percent":
					case "service_90_percent":
						this.showErrMsg("errMsg60");
						break;
					default:
						break;
				}
	
				this.init_register_status();
			},
			setProgressBar: function (percent,newMsg) {
				$(".progress-bar").html(percent);
				document.getElementById("probar").style.width=percent;
	
				var num = parseInt(percent.slice(0,-1));
				if(newMsg){
					if (num >= 60 && num < 100) {
						$("#oltInfo").html(this.progressInfo["61%"]+newMsg+this.progressInfo["62%"]);
					}
					else if (num == 100) {
						$("#oltInfo").html(this.progressInfo["101%"]+newMsg+this.progressInfo["102%"]);
					}
					else{
						$("#oltInfo").html(newMsg);
					}
				}else{
					$("#oltInfo").html(this.progressInfo[percent]);
				}
			},
			showErrMsg: function (errMsg) {
				$("#progress_info").addClass("hideElm");
				$("#err").removeClass("hideElm");
				$("#errInfo").html(this.failInfo[errMsg]);
				$("#back").removeClass("hideElm");
				$("#backToReg").addClass("hideElm");
			},
			showErrReason: function (errMsg) {
				$("#errReason").html(this.failInfo[errMsg]);
			},
			init_register_status: function() {
				hgsUpdateData({type:"SET",url:"/regStatus?set"}, function(data) {
			});
			}
		}
	});
	
	register_sm.observe({
		onEnterRegister20Percent:function () {
			$(".form_box").hide();
			$(".progress").addClass("progress_color");
			$("#progress_info").removeClass("hideElm");	
			$("#backToReg").removeClass("hideElm");		
	
			register_sm.setProgressBar("20%");
			$(".progress").addClass("progress_color");
		},
		onEnterUplink30Percent:function () {
			$("#backToReg").addClass("hideElm");
			register_sm.setProgressBar("30%");
		},
		onEnterTr69ip40Percent:function () {
			register_sm.setProgressBar("40%");
		},
		onEnterRms50Percent:function () {
			register_sm.setProgressBar("50%");
		},
		onEnterService61Percent:function () {
			if (region != 'Sichuan') {
				register_sm.setProgressBar("60%");
			}
		},
		onEnterSuccess100Percent:function () {
			$("#back").removeClass("hideElm");
			// register_sm.setProgressBar("100%");
		},
		onEnterFAIL:function (lifecycle) {
			console.log("observe onEnterFAIL");
		},
	});
	
	function checkStateOfMachine()
	{
		if (times >= TIMES) {
			register_sm.failed();
			clearInterval(timer);
			return;
		}

	
		times++;	

		hgsUpdateData({type:"GET",url:"/regStatus"}, function(data) {
			switch (data.current_regstatus) {
				case "register_20_percent":
					if (register_sm.can("register")){
						register_sm.register();
						times = 0;
					}
					break;
				case "uplink_30_percent":
					if (register_sm.can("ponRegistered")){
						register_sm.ponRegistered();
						times = 0;
					}

					break;
				case "tr69IP_40_percent":
					if (register_sm.can("tr69IPGot")){
						register_sm.tr69IPGot();
						times = 0;
					}
	
					if (data.Msg == 'errMsg401') {
						register_sm.setProgressBar("40%", register_sm.failInfo["errMsg401"]);
					} 
					else if (data.Msg == 'errMsg402') {
						register_sm.showErrMsg("errMsg402");
						clearInterval(timer);
					}
					if (g_staticInfo["Region"] == "Hebei")
					{
						if (20 <= times && data.Status == '99')
						{
							TIMES = 20;
						}
					}


					if (region == 'Sichuan') {
						if (data.Status == '1') {
							register_sm.showErrMsg("errMsg401");
							register_sm.showErrReason("errMsg40_stu1");
							clearInterval(timer);
						}
						else if (data.Status == '4') {
							register_sm.showErrMsg("errMsg401");
							register_sm.showErrReason("errMsg40_stu4");
							clearInterval(timer);
						}
						else if (data.Status == '5') {
							register_sm.showErrMsg("errMsg401");
							register_sm.showErrReason("errMsg40_stu5");
							clearInterval(timer);
						}						
					}
					break;
				case "RMS_50_percent":
					if (register_sm.can("rmsConnected")){
						register_sm.rmsConnected();
						times = 0;
					}
					break;
				case "service_61_percent":
					if (register_sm.can("startService")){
						register_sm.startService();
						if (region == 'Sichuan') {
							if(data.service.length && parseInt(data.totalNum)>0){
								//正在下发n1,n2等data.totalNum个业务
								var arr = data.service.split('/');
								var msg = arr.toString() + 'wait' + data.totalNum + 'indivual';
								register_sm.setProgressBar('60%',msg);
							}
							else if (data.service.length && parseInt(data.totalNum)==0) {
								//正在下发n1,n2等业务
								var arr = data.service.split('/');
								var msg = arr.toString() + 'wait';
								register_sm.setProgressBar('60%',msg);
							}
							else if (!data.service.length && parseInt(data.totalNum)>0) {
								//正在下发data.totalNum个业务
								var msg = data.totalNum + 'indivual';
								register_sm.setProgressBar('60%',msg);
							}
							else{
								//正在下发业务
								register_sm.setProgressBar("60%");
							}
							times = 0;
							break;
						}
						times = 0;
					}	

					if (region != 'Sichuan') {
						if(data.service.length){
							var width;
							var arr = data.service.split('/');
		
							width = 10*(arr.length) + 60;
							if (width > 99) {
								width = 99;
							}
							width += '%';
							register_sm.setProgressBar(width,arr[arr.length-1]);
						}
					}

					if (data.Result == '2') {
						register_sm.failed();
					}
					break;
				case "success_100_percent":
					if (register_sm.can("tr69IPGot")){
						register_sm.tr69IPGot();
						times = 0;
					}
					if (register_sm.can("rmsConnected")){
						register_sm.rmsConnected();
						times = 0;
					}
					if (register_sm.can("startService")){
						register_sm.startService();
						times = 0;
					}				
					if (register_sm.can("serviceDistributed")){
						register_sm.serviceDistributed();
						times = 0;
					}
					if(data.service.length){
						var num = data.service.split('/').length;
						num = " " + num;
						var allService = data.service + num;
						register_sm.setProgressBar("100%",allService);
					}else{
						register_sm.setProgressBar("100%");
					}
					clearInterval(timer);
					break;
			}
		});
	}
	function register() {
		if ($("#Password").val() == "") {
			alert("Please fill in" + inputType + "！");
			return;
		}
		
		postPasswd();
	}
	
	function postPasswd() {
		var passwd = $("#Password").val();
		var regData = {};
	
		regData.type = "POST";
		regData.path = "hbus://mdm/InternetGatewayDevice.X_CMCC_UserInfo.";
		regData.commitData = {};
		regData.commitData.path = regData.path;
		regData.msgType = 212;
	
		if(inputType == "Password"){
			regData.commitData.para = {"Password":passwd};
		}else{
			regData.commitData.para = {"UserName":passwd};
		}

		register_sm.init_register_status();
		hgsUpdateData(regData,function (params) {
			times = 0;
			register_sm.register();
			timer = setInterval(checkStateOfMachine, 2000);
		})
	}
	function checkRegisterStu() {
		hgsUpdateData({type:"GET",url:"/regStatus"}, function(data) {
			if (data.Status == "0" && data.Result == "1") {
				$("#Password").attr("disabled",true);
				$("#save").attr("disabled",true);
				$("#reset").attr("disabled",true);
				alert("Already registered successfully, no need to register again");
			}
		})
	}
	
	$("#eye_password").click(function () {
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
	
	function selectOnuLoidPwd(){
		if(typeof g_regionCfg.onuAuthType == "undefined"){
			return;
		}
		switch(g_regionCfg.onuAuthType){
			case "Password":
				//do nothing
				break;
	
			case "Loid":
				inputType = "LOID";
				$("#pwdtext").text("Loid");
				$("#passwordTitle").text("LOID");
				$("#authTypeHint").text("LOID");
				$("#Password").attr("placeholder", "Please enter LOID");
				
				break;
	
			case "Loid+Password":
				break;
		}
	}

	function limitlenth(){
		switch(g_regionCfg.onuAuthType){
			case "Password":
				if (g_staticInfo["ProductType"] == "XGPON") {
					$("#Password").attr("maxlength",36);
				} else {
					$("#Password").attr("maxlength",10);
				}
				break;
	
			case "Loid":
				$("#Password").attr("maxlength",24);
				break;
	
			case "Loid+Password":
				break;
		}	
	}
	function caculatePwdLength()
	{
		var len = $("#Password").val().length;
		
		$("#pwdLength").html(len);
	
		if (len < 11) {
			$("#pwdLength").attr("style","color:green;font-size:large");
			$("#pwdLengthInfo").html("");
		} else {
			$("#pwdLength").attr("style","color:red;font-size:large");
			$("#pwdLengthInfo").html("Please check"+g_regionCfg.onuAuthType+"Is the length correct?");
		}
	}

	$("#Password").click(function () {
		limitlenth();
	})

	$("#Password").keyup(function () {
		caculatePwdLength();
	})
})
