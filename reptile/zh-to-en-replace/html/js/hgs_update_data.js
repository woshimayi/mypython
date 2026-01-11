var g_checkRules = {};

var g_tableRules = {};

var g_debugCfg = {};

var g_homegatewayParas = {};

var g_staticInfo = {};

var g_adminAccount = true;
var g_wanParaDisabled = false;

$(function () {

$("#hgs_copyright").click(function(){
	loadDebugCfg();
})

makeDatagridComboReadonly = function(id){
	$("#" + id + " .combo input").attr("readonly", "true");
}

$(".saveBtn").click(function () {
	var objNames = $(this).attr(HGS_SUBMIT_DIV_ID).split(" ");
	var divId = $(this).attr(HGS_SUBMIT_DIV_ID);
	
	$(this).attr("disabled",true);
	setTimeout(function() {
		$("["+HGS_SUBMIT_DIV_ID+"='"+divId+"']").attr("disabled",false);
	}, 500);

	for (var i in objNames) {
		//console.log(objNames[i]);
		if(0 == objNames[i].indexOf("HGST_")){
			if(!submitTableData(objNames[i])){
				return;
			}
			continue;
		}
		if (!submitData(objNames[i])) {
			return;
		}
	}
})


$(".deleteBtn").click(function(){
	var objName = $(this).attr(HGS_SUBMIT_DIV_ID)

	if(!g_checkRules[objName]["customerCheckin"]){
		return;
	}

	deleteFunc = g_checkRules[objName]["customerCheckin"]["delete"];
	if(!deleteFunc){
		return;
	}

	window[deleteFunc](objName);
})

function submitTableData(objName) {
	var found = $("#" + objName).html().match(new RegExp(/<\s*script[^>]*>/, 'ig'));
	if(found){
		alert("发现有注入脚本性质的非法攻击行为,退出当前登录,请重新登录!");
		$("#DoLogout").click();
		return;
	}

	if(!g_tableRules[objName]["customerCheckin"]){
		return;
	}

	//getData
	var tableId = getTableIdByHgstId(objName);

	adjustTableProfile(objName, false)
	var tableData = $("#" + tableId).datagrid('getData')
	adjustTableProfile(objName, true)

	data = {};
	if(g_tableRules[objName]["define"]){
		tableCheckData = $("#" + tableId).datagrid('getChecked');
		if(g_tableRules[objName]["define"]["keyValue"]){
			if(g_tableRules[objName]["define"]["checkRow"]){
				for(x in tableData.rows){
					for(y in tableCheckData){
						if(tableData.rows[x].key == tableCheckData[y].key){
							data[tableData.rows[x].key] = true;
						}
					}
	
					if(!data[tableData.rows[x].key]){
						data[tableData.rows[x].key] = false;
					}
				}
			}else if(g_tableRules[objName]["define"]["textBox"]){
				for(x in tableData.rows){
					data[tableData.rows[x].key] = tableData.rows[x].value;
				}
			}else{
				for(x in tableData.rows){
					data[tableData.rows[x].key] = data[tableData.rows[x].value];
				}
			}
		}else{
			data = tableCheckData;
		}
	}else {
		if(g_tableRules[objName]["profile"] && g_tableRules[objName]["profile"]["getChanges"]){
			tableData = $("#" + tableId).datagrid('getChanges');
			data = tableData;
		}else{
			data = tableData.rows;
		}
	}
	
	if(IS_LOG_DATA_ENABLE()){
		console.log(data);
	}

	if(!data){
		return;
	}
	

	if(!g_tableRules[objName]["customerCheckin"]){
		return;
	}

	var checkinObj = g_tableRules[objName]["customerCheckin"];
	if(!checkinObj){
		return;
	}

	if(hbusSetObjs(objName, checkinObj, data)){
		return;
	}

	var postData = {};

	if(checkinObj["checkin"]){
		if(window[checkinObj["checkin"]](objName, tableId, data, postData)){
			return;
		}
	}

	if(checkinObj["otherCheckin"]){
		if(window[checkinObj["otherCheckin"]](objName, tableId, data, postData)){
			return;
		}
	}

	//if(!(postData.type)){
	if(Object.getOwnPropertyNames(postData).length == 0){
		//postData is still empty object
		url = checkinObj["url"];
		if(url){
			postData = {type:"POST", url:url, waitTimeoutMs:checkinObj["waitTimeoutMs"], commitData:data}
		}else{
			url = checkinObj["hbusPostPath"];
			if(!url){
				return;
			}
		
			postData = {type:"POST", path:url, commitData:data, msgType:checkinObj["msgType"]}
			
			if(checkinObj["userTagData"]){
				postData.userTagData = checkinObj["userTagData"];
			}

			if(checkinObj["waitTimeoutMs"]){
				postData.waitTimeoutMs = checkinObj["waitTimeoutMs"];
			}
		}
	}

	if(IS_LOG_DATA_ENABLE()){
		console.log(postData)
	}

	if(IS_DISABLE_COMMIT()){
		if(postData.url == "/debug"){
			//This case always allows to commit
		}else if(IS_DISABLE_COMMIT()){
			console.log("disable commit")
        	return;
		}
    }

	hgsUpdateData(postData,function(result){
		if(IS_LOG_DATA_ENABLE()){
			LOG_DATA("server response:");
			console.log(result); 
		}
	})

	return true;
}

function submitData(objName) {
	var selectStr = "#" + objName + " [" + KEY_ATTR_NAME + "]:visible";
	var elements = $(selectStr);

	var jsonData = {};
	var obj = {};

	if (IS_LOG_DATA_ENABLE()) {
		console.log(objName + " submitBtn click");

		/*var debugObj = {};

		debugObj = addKeyValue(objName, debugObj, elements, true);
		LOG_DATA("raw checkin data:")
		LOG_DATA(debugObj);*/
	}

	obj = addKeyValue(objName, obj, elements, false);
	if (!obj) {
		return false;
	}
	obj = addOtherKeyValue(objName, obj);
	if (!obj) {
		return false;
	}

	if (IS_LOG_DATA_ENABLE()){
		console.log("new checkin data:")
		console.log(obj);
	}
	

	var customerCheckin;

	if (!g_checkRules[objName]) {
		return;
	}
    if(g_checkRules[objName]){
        if(g_checkRules[objName]["customerCheckin"]){
            customerCheckin = g_checkRules[objName]["customerCheckin"];
			if(hbusSetObjs(objName, customerCheckin, obj)){
				return true;
			}
            if(customerCheckin["checkin"]){
                LOG_DATA("customerCheckin function for " + objName + ":" + customerCheckin)
                obj = window[customerCheckin["checkin"]](obj);
                if(!obj){
                    LOG_DATA("Invalid data")
                    return false;
                }
            }

            var setPath = customerCheckin["hbusSetPath"]

            if(setPath){
                var newJsonData = {};
                var newJsonData2 = {};

                var hbusSetPaths = setPath.split(":");
                var p = hbusSetPaths.length - 1;

                if(/^\d+$/.test(hbusSetPaths[p])){ 
                    newJsonData = [];  //change newJsonData to array if path is number
                    newJsonData[parseInt(hbusSetPaths[p])] = obj;
                }else{
                      newJsonData[hbusSetPaths[p]] = obj;
                }

                for(p--; p >= 0; p--){
                    if(IS_LOG_DATA_ENABLE()){
                        console.log(hbusSetPaths[p]);
                    }
                    newJsonData2[hbusSetPaths[p]] = newJsonData;
                }
                obj = newJsonData2;
            }
        }
    }

	jsonData = obj;
    
    var commitData = JSON.stringify(jsonData);

    LOG_DATA("-----------commit data------")
    LOG_DATA(commitData);

    var pathStr = "";
	var msgType = 0;
	var userTagData = 0;
	var path = "";
	var url = "";
    
	if(g_checkRules[objName]["customerCheckin"]){
		path = g_checkRules[objName]["customerCheckin"]["hbusPostPath"];
	}
	
	if((!(path)) && g_checkRules[objName]["customerCheckout"]){
		path = g_checkRules[objName]["customerCheckout"]["hbusGetPath"];
	}

	if(path){
		pathStr = path;

		var method = g_checkRules[objName]["customerCheckin"]["hbusMethod"];
		if(method){
			pathStr += "&method=" + method;
		}else{
			method = "set";
		}  
	}

	if(g_checkRules[objName]["customerCheckin"]["msgType"]){
		msgType = g_checkRules[objName]["customerCheckin"]["msgType"];
	}else if(g_checkRules[objName]["customerCheckout"]["msgType"]){
		msgType = g_checkRules[objName]["customerCheckout"]["msgType"];
	}

	if(g_checkRules[objName]["customerCheckin"]["userTagData"]){
		userTagData = g_checkRules[objName]["customerCheckin"]["userTagData"];
	}else if(g_checkRules[objName]["customerCheckout"] && g_checkRules[objName]["customerCheckout"]["userTagData"]){
		userTagData = g_checkRules[objName]["customerCheckout"]["userTagData"];
	}

	if(g_checkRules[objName]["customerCheckin"]["url"]){
		url = g_checkRules[objName]["customerCheckin"]["url"];
	}
    
    LOG_DATA(pathStr);

	data = {type:"POST", msgType:msgType, userTagData:userTagData,
		path:pathStr, url:url, commitData:{path:path, para:jsonData}};

	if(g_checkRules[objName]["customerCheckin"]["waitTimeoutMs"]){
		data.waitTimeoutMs = g_checkRules[objName]["customerCheckin"]["waitTimeoutMs"];
	}


	if(IS_LOG_DATA_ENABLE()){
		console.log(data)
	}

    if(customerCheckin && customerCheckin["otherCheckin"]){
        if(window[customerCheckin["otherCheckin"]](pathStr, data)){
            return;
        }
    }

	if(IS_LOG_DATA_ENABLE()){
		console.log(data)
	}


	if(IS_DISABLE_COMMIT()){
        console.log("disable commit")
        return;
    }


    if(customerCheckin && customerCheckin["otherIdCheckin"]){
		hgsUpdateData(data, function(result){
            if(IS_LOG_DATA_ENABLE()){
                LOG_DATA("server response:");
                console.log(result);                   
            }
            if(0 == result.result){
                //commitData(customerCheckin["otherIdCheckin"]);
            }
        })
    }else{
		hgsUpdateData(data,function(result){
            if(IS_LOG_DATA_ENABLE()){
                LOG_DATA("server response:");
                console.log(result);                   
            }
			if(customerCheckin && customerCheckin["respHanlder"]){
				window[customerCheckin["respHanlder"]](result);
			}
        })
    }

	return true;
}

function addOtherKeyValue(objName, obj) {
	var selectStr = "#" + objName + " [" + KEY_ATTR_SET + "]";
	var elements = $(selectStr);

	return addKeyValue(objName, obj, elements, false);
}

function mergeElementValue(obj, element, key, value) {
	var elementValue = "";

	switch (element.type) {
		case "checkbox":
			elementValue = element.getAttribute(HGS_CHECKED_VALUE);
			if (!elementValue) {
				obj[key] = value;
				break;
			}
			if (!element.checked) {
				break;
			}

			if (obj[key]) {
				obj[key] += "," + elementValue; //Append another value if key has alreay existed in obj.
			} else {
				obj[key] = elementValue;
			}
			break;

		default:
			obj[key] = value;
			break;
	}

	return obj;
}

function commonCheckin(element, checkRulsObj, key, value){
    var checkInfo = {};

    for(m in checkRulsObj){
        strategy = checkRulsObj[m].strategy;
        errorMsg = checkRulsObj[m].errorMsg;
        para = checkRulsObj[m].para;

        if(checkRulsObj[m].valueConvert){
            checkInfo.hasValue = true;
            checkInfo.value = strategies[strategy](value, errorMsg, para);
            value = checkInfo.value;
            continue;
        }
        
        if(para){
            paras = para.split(":")
            errorMsg = errorMsg.replace("[$1]", paras[0]);
            if(paras.length > 1){
                errorMsg = errorMsg.replace("[$2]", paras[1]);
            }
        }
        errorMsg = strategies[strategy](value, errorMsg, para);
        if(errorMsg){
            $(element).focus();
            alert(errorMsg);
            checkInfo.errorMsg = errorMsg;
            return checkInfo;
        }
    }

    return checkInfo;
}

function addKeyValue(objName, obj, elements, rawValue) {
	for (var i = 0; i < elements.length; i++) {
		value = "";
		switch (elements[i].type) {
			case "checkbox":
				value = elements[i].checked;
				break;

			case "radio":
				if (elements[i].checked) {
					value = elements[i].value;
					break;
				}
				continue;

			default:
				value = elements[i].value;
				break;
		}

		key = elements[i].getAttribute(KEY_ATTR_NAME);
		if(g_debugCfg.EnableLogHtmlEle){
			console.log(i + ". key:" + key + " value:[" + value + "]");
		}
		if (rawValue) {
			obj = mergeElementValue(obj, elements[i], key, value);
			continue;
		}

		if(g_checkRules[objName]){
			var inputElements = g_checkRules[objName]["inputElements"];
			if(inputElements && inputElements[key]){
				commonCheckRules = inputElements[key]["checkin"];
				//console.log(commonCheckRules);
				if(commonCheckRules){
					var checkInfo = commonCheckin(elements[i], commonCheckRules, key, value);
					if(checkInfo.errorMsg){
						return;
					}
					if(checkInfo.hasValue){
						value = checkInfo.value;
					}
				}
			}
		}

		obj = mergeElementValue(obj, elements[i], key, value);
	}

	return obj;
}


$(".changeView").click(function(){
    if(g_log_layout){
        console.log($(this).text().trim(), ".changeView click");
    }
    loadVisibleHgsDivData();
});

getAllHbusPath = function(path){
	var fullPath = "";
	if(path instanceof Array){
		for(i in path){
			fullPath += path[i];
		}

		return fullPath;
	}

	return path;
}

loadVisibleHgsDivData = function(){
    var hgsDivs = $("[id^='HGS_']:visible");

    LOG_DATA("Found " + hgsDivs.length + " divs which need to update data");
    for(var i = 0;i < hgsDivs.length;i++){
        id = hgsDivs[i].getAttribute("id");
        loadHbusData(id);
    }

    //for tables
    var hgstDivs = $("[id^='HGST_']:visible");
    LOG_DATA("Found " + hgstDivs.length + " table divs which need to update data");

    for(var i = 0;i < hgstDivs.length;i++){
        id = hgstDivs[i].getAttribute("id");
        loadTableData(id);
    }
}

loadHbusRespData = function(data, objData){
	if(!(objData && objData.objName)){
		return;
	}

	var objName = objData.objName;

	if(IS_LOG_DATA_ENABLE() || IS_HBUS_SIMU()){
		console.log("Get hbus data:");
		console.log(data);
	}

	if(!g_checkRules[objName]){
		return;
	}

	if(g_checkRules[objName]["customerCheckout"]){
		checkoutFunc = g_checkRules[objName]["customerCheckout"]["preCheckout"];
		if(checkoutFunc){
			data = window[checkoutFunc](data);
			if(typeof data == "undefined"){
				return;
			}
		}
	}

	var inputElements = g_checkRules[objName]["inputElements"];

	if(IS_LOG_DATA_ENABLE()){
		console.log("inputElements:");
		console.log(inputElements);
	}
	for(m in inputElements){
		var selectStr = "#" + objName + " [" + KEY_ATTR_NAME + "=" + m +"]";

		if(inputElements[m]["hbusGetPath"]){
			var path = getAllHbusPath(inputElements[m]["hbusGetPath"]);
			var paths = path.split(":");
			var tmpObj;

			tmpObj = data[paths[0]];
			if ($.isEmptyObject(tmpObj) || tmpObj.length == 0) {                    
				break;
			}
			for(var i = 1;i < paths.length;i++){
				tmpObj = tmpObj[paths[i]]
			}
			
			if (typeof(tmpObj[m]) == undefined){
				value = "";
			}else if(0 == tmpObj[m]){
				value = tmpObj[m]
			}else{
				value = tmpObj[m]?tmpObj[m]:"";
			}
		}else{
			if(typeof(data[m]) != "undefined"){
				value = data[m];
			}else{
				value = "";
			}            
		}

		if(g_debugCfg.EnableLogHtmlEle){
			console.log("raw value for key[" + m + "]:" + value)
		}
		

		if(inputElements[m]["checkout"]){
			if(inputElements[m]["checkout"][0]){
				if(inputElements[m]["checkout"][0]["strategy"]){
					strategy = inputElements[m]["checkout"][0]["strategy"];
					value = strategies[strategy](value);
					LOG_DATA(strategy + ": convert raw value for key [" + m + "]: [" + value + "]")
				}
			}
		}

		if(inputElements[m].id){
			elements = $("#" + inputElements[m].id);
		}else{
			elements = $(selectStr);
		}
		
		element = elements[0];
		if(!element){
			continue;
		}
		if(!element.type){
			element.innerText = value;
			continue;
		}
		if(IS_LOG_DATA_ENABLE()){
			//console.log("element type for key[" + m + "]:" + element.type)
		}

		switch(element.type){
			case "checkbox":
				element.checked = value;
				break;
				
			case "radio":
				for(i in elements){
					element = elements[i];
					if(element.value == value){
						element.checked = true;
						break;
					}
				}
				break;
				
			default:
				element.value = value;
				break;
		}
	}

	if(objData.noCheckout){
		if(objData.postHandler){
			objData.postHandler(data);
		}
		return;
	}

	if(g_checkRules[objName]["customerCheckout"]){
		checkoutFunc = g_checkRules[objName]["customerCheckout"]["checkout"];
		if(checkoutFunc){
			LOG_DATA("execute costomer checkout function:" + checkoutFunc + " for " + objName);
			window[checkoutFunc](data);
		}
	}

	if(objData.postHandler){
		objData.postHandler(data);
	}
}

hbusGetObjs = function(objName, checkoutObj){
	if(220 != checkoutObj.msgType){
		return;
	}

    var data = {url:"/getObjs",
		objData:{
			objName:id
		}
	};
	
	if(checkoutObj.postPaths){
		data.type = "POST";
		data.commitData = [];
		if(checkoutObj.waitTimeoutMs){
			data.waitTimeoutMs = checkoutObj.waitTimeoutMs;
		}else{
			data.waitTimeoutMs = 5000;
		}
		for(m in checkoutObj.postPaths){
			data.commitData.push({fullPath:checkoutObj.postPaths[m]})
		}
	}

	hgsUpdateData(data, function(result){
		if(IS_LOG_DATA_ENABLE()){
			console.log(result);
		}

		if(checkoutObj["preCheckout"]){
			result = window[checkoutObj["preCheckout"]](result);
		}
		
		if(window[checkoutObj["checkout"]]){
			result = window[checkoutObj["checkout"]](result);
			if(typeof result == "undefined"){
				return;
			}
			loadHbusRespData(result, data.objData);
		}
	})

	return true;
}

hbusSetObjs = function(objName, customerCheckin, objData){
	if(221 != customerCheckin.msgType){
		return;
	}


	if(customerCheckin["preCheckin"]){
		objData = window[customerCheckin["preCheckin"]](objName, objData);
		if(typeof objData != "object"){
			return true;
		}
	}

    var data = {url:"/setObjs",
		type : "POST",
		commitData:objData
	};


	hgsUpdateData(data, function(result){
		if(IS_LOG_DATA_ENABLE()){
			console.log(result);
		}
		if(objName.indexOf("HGS_") == 0){
			loadHbusData(objName);
		}else{
			loadTableData(objName);
		}
	})

	return true;
}

loadHbusData = function(objName){
    if(!objName){
        return;
    }

    LOG_DATA("load hbus data for " + objName);

    var url = "";
    var value;
	var data = {};

    if(!g_checkRules[objName]){
        LOG_DATA("Error: No rules in config.json for " + objName);
        return;
    }
    if(!g_checkRules[objName]["customerCheckout"]){
        LOG_DATA("Error: No customerCheckout rules in config.json for " + objName);
        return;
    }

	if(hbusGetObjs(objName, g_checkRules[objName]["customerCheckout"])){
		return;
	}

    if(!g_checkRules[objName]["customerCheckout"]["hbusGetPath"]){
		if(g_checkRules[objName]["customerCheckout"]["checkout"]){
			window[g_checkRules[objName]["customerCheckout"]["checkout"]](objName);
			return;
		}
        LOG_DATA("Error: No hbusGetPath in config.json for " + objName);
        return;
    }

	
    var path = getAllHbusPath(g_checkRules[objName]["customerCheckout"]["hbusGetPath"]);
    url += path;
	if(g_checkRules[objName]["customerCheckout"]["hbusMethod"]){
		var method = g_checkRules[objName]["customerCheckout"]["hbusMethod"];
		if(method){
			url += "&method=" + method;
		}
	}
    
    LOG_DATA(url);

	var msgType;
	var userTagData;

	if(g_checkRules[objName]["customerCheckout"]["msgType"]){
		msgType = g_checkRules[objName]["customerCheckout"]["msgType"];
	}else if(g_checkRules[objName]["customerCheckin"]["msgType"]){
		msgType = g_checkRules[objName]["customerCheckin"]["msgType"];
	}

	if(g_checkRules[objName]["customerCheckout"]["userTagData"]){
		userTagData = g_checkRules[objName]["customerCheckout"]["userTagData"];
	}else if(g_checkRules[objName]["customerCheckin"]["userTagData"]){
		userTagData = g_checkRules[objName]["customerCheckin"]["userTagData"];
	} 

	data = {path:url, msgType:msgType, userTagData:userTagData, 
		objData:{
			objName:objName
		}
	};

	if(IS_LOG_DATA_ENABLE()){
		console.log(data);
	}

	hgsUpdateData(data, loadHbusRespData);
}

convertTableToDefineData = function(id, data){
	result = [];

	if(!g_tableRules[id]["define"]){
		return data;
	}

	if(g_tableRules[id]["define"]["keyValue"]){
		if(g_tableRules[id]["define"]["checkRow"]||g_tableRules[id]["define"]["textBox"]){
			var keyData = g_tableRules[id]["keyData"];

			for(x in keyData){
				tmp = {key:x};

				for(m  in keyData[x]){
					tmp[m] = keyData[x][m];
				}

				for(y in data){
					if(y == x){
						if(g_tableRules[id]["define"]["textBox"]){
							tmp.value= data[y];
						}
						if(data[y]){
							tmp.checked = "checked";
						}
						continue; 
					}
				}
				result.push(tmp);
			}
		}else{
			for(x in data){
				result.push({key:x, value:data[x]})
			}
		}
	}

	return result;
}


loadTableData = function(id){
    if(!g_tableRules[id]){
        return;
    }
    
    if(!g_tableRules[id]["customerCheckout"]){
		testData = {total:4, rows:[
			{
				port:"LAN1",
				mode:"1",
				vlanBind: "100/100"
			},
			{
				port:"LAN2",
				mode:"1",
				vlanBind: "100/100,200/88"
			},
			{
				port:"LAN3",
				mode:"0",
				vlanBind: ""
			},
			{
				port:"LAN4",
				mode:"0",
				vlanBind: ""
			}
		]}
		
		//$("#" + getTableIdByHgstId(id)).datagrid("beginEdit", 0)

		try{
			generateTable(id, g_tableRules[id], testData);

			return;
			var tableId = "#" + getTableIdByHgstId(id);
			//$(tableId).combobox('readonly',true); 
			$(tableId).datagrid("beginEdit", 0)
			//console.log($(".combo:visible"))
			//$("#_easyui_textbox_input1").attr("readonly", "true");

			//$(".combo [id^='_easyui_textbox_input']").attr("readonly", "true");
			//$("#HGST_VLAN_BIND .combo:visible [id^='_easyui_textbox_input']").attr("readonly", "true");
			//$("#" + id + " .combo [id^='_easyui_textbox_input']").attr("readonly", "true");
			$("#" + id + " .combo input").attr("readonly", "true");
			
		}catch(err){

		}
		
		
        return;
    }

	var data = {};
    var checkoutObj = g_tableRules[id]["customerCheckout"];
    if(checkoutObj["hbusGetPath"]){
		data = {path:getAllHbusPath(checkoutObj["hbusGetPath"]), msgType:checkoutObj["msgType"], userTagData:checkoutObj["userTagData"], 
			objData:{
				objName:id
			}
		};

		if(checkoutObj["preCheckout"]){
			data = window[checkoutObj["preCheckout"]](data);
		}
        hgsUpdateData(data, function(result){
			if(IS_LOG_DATA_ENABLE()){
				console.log(result);
			}
            try
            {
                result = window[checkoutObj["checkout"]](result);
				result = convertTableToDefineData(id, result);
            }
            catch(err)
            {
                //alert("catch err")
				//return;   //can't return, otherwise can't generate table
            }

			if(result.total){
				tableData = {total:result.total, rows:result.rows};
			}else{
				tableData = {total:result.length, rows:result};
			}
            
        	//console.log(tableData);
            generateTable(id, g_tableRules[id], tableData)

			resizeSubNavContentHeight();
        })
        return;
    }


    if(!checkoutObj["url"]){
		generateTable(id, g_tableRules[id]);
        return;
    }

    var path = checkoutObj["url"];
    data = {url:checkoutObj["url"],
		objData:{
			objName:id
		}
	};

	if(checkoutObj.postPaths){
		data.type = "POST";
		data.commitData = [];
		if(checkoutObj.waitTimeoutMs){
			data.waitTimeoutMs = checkoutObj.waitTimeoutMs;
		}
		for(m in checkoutObj.postPaths){
			data.commitData.push({fullPath:checkoutObj.postPaths[m]})
		}
	}

	hgsUpdateData(data, function(result){
		if(IS_LOG_DATA_ENABLE()){
			console.log(result);
		}

		if(checkoutObj["preCheckout"]){
			result = window[checkoutObj["preCheckout"]](result);
		}
		
		if(window[checkoutObj["checkout"]]){
			result = window[checkoutObj["checkout"]](result);
		}

		result = convertTableToDefineData(id, result);

		if(result.total){
			tableData = {total:result.total, rows:result.rows};
		}else{
			tableData = {total:result.length?result.length:0, rows:result};
		}

		//tableData = {total:result.length, rows:result};
		//console.log(tableData);
		generateTable(id, g_tableRules[id], tableData);

		resizeSubNavContentHeight();
	})
}

getTableIdByHgstId = function(id){
    return (id + "_table").toLocaleLowerCase();
}

adjustTableProfile = function(id, edit){
	if(!g_tableRules[id]){
		return;
	}
	if(!g_tableRules[id]["profile"]){
		return;
	}
	var profile = g_tableRules[id]["profile"];
	var tableId = "#" + getTableIdByHgstId(id);


	if(profile["edit"]){
		if(typeof edit ===  'undefined'){
			edit = true;
		}
		if(profile["edit"]["editAllRows"]){
			var rows = $(tableId).datagrid("getRows").length;

			for(i = 0;i < rows; i++){
				if(edit){
					$(tableId).datagrid("beginEdit", i);
				}else{
					$(tableId).datagrid("endEdit", i);
				}
			}
		}
	}
	
	var dg = $(tableId);
	if(profile["filter"]){
		dg = $(tableId).datagrid();
		dg.datagrid("enableFilter");
		dg.datagrid("enableFilter",  window[profile["filter"]](dg));
	}

	if(profile["pagination"]){

		//dg.datagrid({loadFilter:window[profile["pagination"]]});
		var pager = dg.datagrid('getPager');

		pager.pagination(window[profile["pagination"]](dg, id));
	}

	if(profile["combobox"]){
		if(profile["combobox"]["readonly"]){
			makeDatagridComboReadonly(id);
		}
	}
}

generateTable = function(id, tableDesc, tableData){
    var tableId = getTableIdByHgstId(id);

    var hgstTableDiv = $("#" + tableId);
	if(hgstTableDiv.length){
        LOG_DATA("Table " + tableId + " has already created!");
		if(tableDesc["profile"]){
			if(tableDesc["profile"].easyuiUpdateEverytime){
				$("#" + tableId).datagrid(tableDesc["easyui"]);
			}
		}
    }else{
        LOG_DATA("Table " + tableId + " need be created!")

        var html = "<table id='" + tableId + "' class='easyui-datagrid' ></table>"

        $("#" + id).html(html);
        if(tableDesc["style"]){
            $("#" + tableId).css(tableDesc["style"])
        }

		for(m in tableDesc["easyui"]){
			funcName = tableDesc["easyui"][m];
			if((typeof funcName === "string") && m.toString().search(/^on[A-Za-z]/) == 0){
				tableDesc["easyui"][m] = window[funcName];
			}else{
				if (m == "columns") {
					for (var i = 0; i < tableDesc["easyui"][m][0].length; i++) {
						const element = tableDesc["easyui"][m][0][i];
						if (element["formatter"]) {
							element["formatter"] = window[element["formatter"]];
						}
					}
				}
			}
		}

        $("#" + tableId).datagrid(tableDesc["easyui"]);
    }

    if(IS_LOG_DATA_ENABLE()){
        console.log("Load table data:")
        console.log(tableData);
    }

    //$("#" + tableId).datagrid('getPanel').removeClass('lines-both lines-no lines-right lines-bottom').addClass('lines-no');

    if(tableDesc["cssClass"] && tableDesc["cssClass"]["addClass"]){
        $("#" + tableId).datagrid('getPanel').addClass(tableDesc["cssClass"]["addClass"]);
    }
    
	if(tableData){
		$("#" + tableId).datagrid('loadData', tableData);

		if(tableDesc["define"] && tableDesc["define"]["checkRow"]){
			for(r in tableData.rows){
				if(tableData.rows[r].checked){
					$("#" + tableId).datagrid('checkRow', r);
				}
			}
		}
	}

	adjustTableProfile(id);
	adjustTableHeight(id);
	

    try{
        window[tableDesc["customerCheckout"]["postLoadData"]](tableData);
    }catch(err){

    }
}

adjustTableHeight = function(id){
	//调整高度,如果不做调整的话，原有容器不能适应高度变化的表格
	var adjustTarget = $("#" + id).parent().parent();
	if(!adjustTarget){
		return;
	}

	//增加30px以便出现水平滚动条后仍然能够容纳�?
	adjustTarget.height($("#" + id).height() + 30);
	adjustTarget.resize(); //如果没有这行代码，内容很可能在容器之外，即使内容能够放得下

	resizeSubNavContentHeight();
}

hgsDisconnectPrompt = (function(){
	var firstDisconnectedPromot = true;
	
	return function(state){
		switch(state){
			case 0:
				if(firstDisconnectedPromot){
					firstDisconnectedPromot = false;
					/*$("#disconnectedPrompt").html('<h3 class="text-danger">网络已经断开!已经无法连接设备!</h3>' 
					+'<h6 class="text-primary">当网络连接恢复时，请手动重新<a href="/" style="color:#f00">刷新</a>页面!</h6>');*/
				}
				$("#disconnectedPrompt").html('<h3 class="text-danger">网络已经断开!已经无法连接设备!</h3>');
				break;
			case 1:
				if(!firstDisconnectedPromot){
					$("#disconnectedPrompt").html('');
					//location.reload();
					//location = window.location.href;
				}
				break;
		}
	}
})();


hgsUpdateData = function(data, callbkFunc){
	var waitTimeout = 0;

    if(!data.type){
        data.type = "GET";
    }

    var url = "path"
    
    if(data.path){
        if(data.type == "GET"){
            url = "/getHbusData?path=" + data.path
        }else{
            url = "/setHbusData?path=" + data.path
        }
        if(data.method){
            url += "&method=" + data.method;
        }
		if(data.msgType){
			url += "&msgType=" + data.msgType;
		}
		if(data.userTagData){
			url += "&userTagData=" + data.userTagData;
		}
		if(data.waitTimeoutMs){
			url += "&waitTimeoutMs=" + data.waitTimeoutMs;
		}
		if(data.extraPara){
			if(data.extraPara[0] != '&'){
				url += "&";
			}
			url += data.extraPara;
		}
    }else if(data.url){
        url = data.url;
		if(data.waitTimeoutMs){
			if(url.indexOf("?") < 0){
				url += "?";
			}else{
				url += "&";
			}
			url += "waitTimeoutMs=" + data.waitTimeoutMs;
			waitTimeout = data.waitTimeoutMs + 1000;
		}
    }

	url = url.replace(/.{i}./g, "._i_.");

    if(data.type == "GET"){
		/*$.get(urlWithRandom(url), function(result, status){
			//$.get $.post can't catch 401
			console.log(status);
			doCallBack(result);
		});*/

		$.ajax({
			type: 'GET',
			url: urlWithRandom(url),
			/*statusCode: {
				//here also can catch 401, but after error function
				401: function () {
				}
			},*/
			success: function (result) {
				hgsDisconnectPrompt(1);
				doCallBack(result);
			},
			error: function (xhr, ajaxOptions, thrownError) {
				if (xhr.status == 401) {
					if(window.location.href.indexOf(LOGIN_PAGE) < 0){
						window.location.replace(LOGIN_PAGE);
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
		data: data.notJson?data.commitData:JSON.stringify(data.commitData),
		success: function (result) {
			hgsDisconnectPrompt(1);
			doCallBack(result);
		},
		error: function (xhr, ajaxOptions, thrownError) {
			if (xhr.status == 401) {
				console.log(window.location.href)
				if(window.location.href.indexOf(LOGIN_PAGE) < 0){
					window.location.replace(LOGIN_PAGE);
				}
				return;
			}

			hgsDisconnectPrompt(xhr.readyState);
		},
		timeout: waitTimeout
	});


    function doCallBack(result){
        if(callbkFunc){
            if(data.resultPath){
                callbkFunc(result[data.resultPath], data.objData);
            }else{
                callbkFunc(result, data.objData);
            }
        }
    }
}





loadHomeGatewayParas = function(){
	hgsUpdateData({type:"GET", path:"hbus://mdm/", msgType:201, userTagData:3}, function(data){
		g_homegatewayParas["lanCfg"] = data;
		if(data.LanEthNum < 4){
			$(".FEATURE_LANETH_NUM4").remove();
		}
	})
	hgsUpdateData({type:"GET", path:"hbus://mdm/", msgType:201, userTagData:4}, function(data){
		g_homegatewayParas["lanMapping"] = data;
	})
}

getLanMappingIfName = function(ifName){
	if(g_homegatewayParas["lanMapping"][ifName]){
		return g_homegatewayParas["lanMapping"][ifName];
	}

	return "";
}

var loadStatickv;
function loadStaticKeyValue(){
    loadStatickv = hgsUpdateData({type:"GET", url:"/staticInfo"}, function(data){
		var staticInfo = JSON.parse(data);
		g_staticInfo = staticInfo;

        elements = $("[" + KEY_STATIC +"]");
        for(var i = 0;i < elements.length;i++){
            key = elements[i].getAttribute(KEY_STATIC);       
            elements[i].innerText = staticInfo[key];
        }
		
		$(".FEATURE_REPEATER").remove();
		$(".FEATURE_GUEST").remove();
		$("#SlaveMcast").remove();
		
		if(!staticInfo["SupportVoip"]){
			$(".FEATURE_VOIP").remove();
		}

		if(staticInfo["Region"]!="SMT"){
			$(".FEATURE_SMT").remove();
		}

		if(!staticInfo["SupportWifi"]){
			$(".FEATURE_WIFI").remove();
		} else {
			if(!staticInfo["SupportWifi6"]){
				$(".FEATURE_WIFI6").remove();
			}
			if(!staticInfo["SupportWifi7"]){
				$(".FEATURE_WIFI7").remove();
			}
		}

		if(!staticInfo["SupportUSB"]){
			$(".FEATURE_USB").remove();
		}

		if (staticInfo["IsFTTR"] && !staticInfo["IsMasterGateway"]) {
			$(".FEATURE_MASTER").remove();
		}
		else if (staticInfo["IsFTTR"] && staticInfo["IsMasterGateway"]) {
			if (!staticInfo["IsCombo"]) {
				$(".FEATRUE_COMBO").remove();
			}
		}
		
		if(!staticInfo["IsFTTR"])
		{
			if (staticInfo["Region"] !="Sichuan" && staticInfo["Region"] !="Shaanxi") {
				$(".FEATURE_GUEST").remove();
			}
			$(".FEATURE_MESH").remove();
		}

		if (g_staticInfo["Region"] != "Beijing") {
			$(".FEATURE_IPV6_ONLINE_DEV").remove();
		}

		if (staticInfo["Region"] =="Sichuan") 
		{
			$(".FEATURE_WLANBasicCfg").remove();
			$(".FEATURE_WLANAdvanceCfg").remove();
			$("#oldPasswordTitle").text("用户初始密码");
			$("#oldPassword").attr("type","text");
			$("#oldPassword").attr("disabled",true);
			$("#oldPasswordImg").remove();
		}else{
			$(".FEATURE_WLANSSIDPWDCfg").remove();
			$(".FEATURE_WLANAllCfg").remove();
			$(".FEATURE_WIFI5").remove();
			$('[hgs_sub_nav="wlan_control"]').addClass("active");
			if (staticInfo["Region"] == "Guangxi") {
				$("#enableSche").attr("disabled",true);
				if (staticInfo["IsFTTR"] && !staticInfo["IsMasterGateway"]) {
					$(".FEATURE_SCHEDULE_REBOOT").remove();
				}
			}
		}

		if ((g_staticInfo["Region"] == "Henan") || 
			(!g_staticInfo["IsMasterGateway"] && g_staticInfo["Region"] != "Jicai" && g_staticInfo["Region"] != "SMT")) {
			$(".FEATRUE_uplink").remove();
		}

		CheckWlanType(staticInfo["ModelName"]);
		if(window.location.href.indexOf(LOGIN_PAGE) >= 0){
			return;
		}
		loadHomeGatewayParas();
	})
}

function CheckWlanType(modeName) {	
	if (modeName == "TEWA-861G") {
		$("#HGS_WLAN_CFG [hgs_key=Standard] option[value='ax']").remove();
	}
}

loadDebugCfg = function(){
    hgsUpdateData({type:"GET", url:"/debug?getData"}, function(data){
		if(data == "{}")
		{
			return;
		}
		g_debugCfg = data;
        enable_console_log = g_debugCfg.EnableConsolelog?1:0;
		g_log_data = g_debugCfg.EnableWebDataLog?1:0;
		g_disable_commit = g_debugCfg.DisableCommitData?1:0;
	})
}



loadStaticInfo = function(){
	loadStaticKeyValue();
	if(window.location.href.indexOf(LOGIN_PAGE) >= 0){
		return;
	}
	
	hgsUpdateData({type:"GET", url:"/json/config.json"}, function(data){
		g_checkRules = data;
	})
	
	hgsUpdateData({type:"GET", url:"/json/tableCfg.json"}, function(data){
		if (g_staticInfo["IsFTTR"] && !g_staticInfo["IsMasterGateway"]) {
			var arr = data.HGST_HOST_INFO.easyui.columns[0];
			var found = 0;
			for (var i = 0; i < arr.length; i++) {
				if (arr[i].field == "HostName" || arr[i].field == "Name") {
					found ++;
					arr.splice(i,1);
				}
				if (found == 2) {
					break;
				}
			}
		}
		g_tableRules = data;
	})

	loadDebugCfg();
}

loadStaticInfo();

checkLogStatus = function(){
	//console.log("checkLogStatus");
	var skipAuth = false;
	if(window.location.href.indexOf(LOGIN_PAGE) > 0){
		return;
	}

	if(window.location.href.indexOf("/register.html") > 0){
		return;
	}

	var worker = new Worker('js/work.js');
	worker.postMessage('start_getLogStatus');
	worker.onmessage = function (event) {
		// console.log("recieve message from worker: ",event.data);
		hgsUpdateData({type:"GET", url:"/getLogStatus", waitTimeoutMs:500}, function(data){
			if(data.busyLevel){
				$('#welcome').css('color', (data.busyLevel > 3000)?'red':'#007BFF');
			}
			
			if(data.skipAuth){
				skipAuth = true;
				return;
			}
			if(!data.login){
				window.location.href = LOGIN_PAGE;
				worker.postMessage('stop_getLogStatus');
				worker.terminate();
				return;
			}
		})	
	}

	if(skipAuth){
		return;
	}

	// setTimeout(checkLogStatus, 10*1000);
}

checkLogStatus();

$.when(loadStatickv).done(function () {
	if(window.location.href.indexOf(LOGIN_PAGE) < 0){
		hgsUpdateData({type:"GET", url:"/getLogStatus"}, function(data){
			if(!data.isAdmin){
				g_adminAccount = false;
				if (g_staticInfo["Region"] =="Beijing" || g_staticInfo["Region"] =="Jiangsu" || g_staticInfo["Region"] == "JiangsuJK") {
					$(".FEATURE_WAN").removeClass("FEATURE_ADMIN");
					$("#ServiceList").empty();
					$("#ServiceList").append('<option value="INTERNET">上网</option>');
				}
				if (g_staticInfo["Region"] =="Beijing"){
					g_wanParaDisabled = true;
					$("#HGS_WAN :input:not([hgs_key='UserName']):not([hgs_key='UserPassword']):not([hgs_key='MTU']):not([hgs_submit_div_id='HGS_WAN'])").attr("disabled",true);
					$("#deleteWanBtn").remove();
				}		
				$(".FEATURE_ADMIN").remove();
	
				if (g_staticInfo["Region"] =="Jiangxi") {
					$(".FEATURE_AUTHENTICATION").remove();
				}
				if ($("[page=remote_manage] .side_bar").children().length == 0) {
					$("[target_page=remote_manage]").parent().remove();
				}else {
					$("[page=remote_manage] ul li a:first").addClass("active");
					$("[hgs_submit_div_id=HGS_ONU_PASSWORD]").attr("disabled",true);
				}
	
				if ($("[page=lanside_config] .side_bar").children().length == 0) {
					$("[target_page=lanside_config]").parent().remove();
				}
	
				if (g_staticInfo["Region"] =="Anhui") {
					$(".FEATURE_MACFILTER").remove();
				}
	
				if ($("[page=network] .nav_sub").children().length == 0) {
					$("[target_page=network]").parent().remove();
				}
				else{
					$("[page=network] ul li a:first").attr("hgs_first_target_page",1);
					$("[page=network] ul li a:first").addClass("active");
				}
			}
			else
			{
				if (g_staticInfo["Region"] == "Zhejiang") {
					$("#WifiBand").empty();
					$("#WifiBand").append('<option value="2d4g" fullPath="InternetGatewayDevice.LANDevice.1.WLANConfiguration.1." >SSID1</option>')
					$("#WifiBand").append('<option class="FEATURE_ADMIN" value="2d4g" fullPath="InternetGatewayDevice.LANDevice.1.WLANConfiguration.2." >SSID2</option>');
					$("#WifiBand").append('<option class="FEATURE_ADMIN" value="2d4g" fullPath="InternetGatewayDevice.LANDevice.1.WLANConfiguration.3." >SSID3</option>');
					$("#WifiBand").append('<option class="FEATURE_ADMIN" value="2d4g" fullPath="InternetGatewayDevice.LANDevice.1.WLANConfiguration.4." >SSID4</option>');
					$("#WifiBand").append('<option value="5g" fullPath="InternetGatewayDevice.LANDevice.1.WLANConfiguration.5." >SSID5</option>');
				}			
			}
			$('body').show();
		})
	
		setTimeout(function(){
			$('body').show();
		}, 2000)
	}
});

})
