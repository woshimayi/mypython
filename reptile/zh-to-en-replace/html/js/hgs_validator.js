var strategies = {
	// UTF8字符集实际长度计算 
	getStrLen: function (str){
		var realLength = 0; 
		var len = str.length; 
		var charCode = -1; 
		for(var i = 0; i < len; i++){ 
		charCode = str.charCodeAt(i); 
		if (charCode >= 0 && charCode <= 128) {  
			realLength += 1; 
			}else{  
			// 如果是中文则长度加3 
			realLength += 3; 
			} 
		}  
		return realLength; 
	},
    isNotNum: function( value, errorMsg){
        if (isNaN(value)) {
            return errorMsg;
        }
    },
    isNonEmpty: function( value, errorMsg ){
        if ( value === '' ){
            return errorMsg;
        }
    },
    minLength: function( value, errorMsg , length){
        if ( this.getStrLen(value) < length ){
            return errorMsg;
        }
    },
    maxLength: function( value, errorMsg , length){
        if ( this.getStrLen(value) > length ){
            return errorMsg;
        }
    },
    minMaxLength: function( value, errorMsg , length){
		var strLen = this.getStrLen(value);
    	range = length.split(":");
        if (( strLen < parseInt(range[0]) )||(strLen > parseInt(range[1]))){
            return errorMsg;
        }
    },
    minMaxIntValue: function( value, errorMsg , length){
    	range = length.split(":");
        if (( value < parseInt(range[0]) )||(value > parseInt(range[1]))){
            return errorMsg;
        }
    },
    minMaxPositiveIntValue: function( value, errorMsg , length){
        if (value < 1 || value != parseInt(value)) {
            return errorMsg;
        }
    	range = length.split(":");
        if (( value < parseInt(range[0]) )||(value > parseInt(range[1]))){
            return errorMsg;
        }
    },
	isMinMaxIntString: function( value, errorMsg , length){
		value = value.trimStart().trimEnd();
		intVal = parseInt(value);
		if(intVal.toString().length != value.length){
			return errorMsg;
		}

		return this.minMaxIntValue(value, errorMsg , length);
    },
	isMinMaxIntStringOrEmpty: function( value, errorMsg , length){
		value = value.trimStart().trimEnd();
		if(value.length == 0){
			return;
		}

		return this.isMinMaxIntString(value, errorMsg , length);
    },
    isMobile: function( value, errorMsg ){
        if ( !/(^1[3|5|8][0-9]{9}$)/.test( value ) ){
            return errorMsg;
        }
    },
    isValidIP: function (value, errorMsg) {
        var reg = /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
        if(!reg.test(value)){
            return errorMsg;
        }
    },
	isValidMultipleIP: function (value, errorMsg, splitChar) {
		if(!splitChar){
			splitChar = ","
		}
        var ipArr = value.split(splitChar);
		for(x in ipArr){
			if(this.isValidIP(ipArr[x], errorMsg)){
				return errorMsg;
			}
		}
    },
    isEmptyOrValidIP: function (value, errorMsg){ 
        if(!value){
            return;
        }
        return this.isValidIP(value, errorMsg);
    },
    isValidMask: function (value, errorMsg) {
		if("255.255.255.255" == value){
			return;
		}
        var reg = /^(254|252|248|240|224|192|128|0)\.0\.0\.0|255\.(254|252|248|240|224|192|128|0)\.0\.0|255\.255\.(254|252|248|240|224|192|128|0)\.0|255\.255\.255\.(254|252|248|240|224|192|128|0)$/;
        if(!reg.test(value)){
            return errorMsg;
        }
    },
    isSameSubnet: function(value, errorMsg, para){
    	var subnetMask = this.convertIpStrToNum(value);
    	
    	if((subnetMask & this.convertIpStrToNum(para[0])) != (subnetMask & this.convertIpStrToNum(para[1]))){
      		return errorMsg;
    	}
	},
    isValidIPv4v6: function (value, errorMsg) {
        var reg = /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
        var valid = /:/.test(value) 
            &&value.match(/:/g).length<8
            &&/::/.test(value)
            ?(value.match(/::/g).length==1
            &&/^::$|^(::)?([\da-f]{1,4}(:|::))*[\da-f]{1,4}(:|::)?$/i.test(value))
            :/^([\da-f]{1,4}:){7}[\da-f]{1,4}$/i.test(value);  

        if (!reg.test(value) && !valid) {
            return errorMsg;
        }
    },
    isValidIPv6: function (value, errorMsg){
        value = $.trim(value);
        var valid = /:/.test(value) 
            &&value.match(/:/g).length<8
            &&/::/.test(value)
            ?(value.match(/::/g).length==1
            &&/^::$|^(::)?([\da-f]{1,4}(:|::))*[\da-f]{1,4}(:|::)?$/i.test(value))
            :/^([\da-f]{1,4}:){7}[\da-f]{1,4}$/i.test(value);
        if(!valid){
            return errorMsg;
        }
    },
    isValidIPv6SubNet: function (value, errorMsg){
        var prefix = value.split("/");

        if (prefix.length != 2){
            return errorMsg;
        }

        num = parseInt(prefix[1]);
        if(!num){
            return errorMsg;
        }
        if ( num <= 0 || num > 128){
            return errorMsg;
        }
        
        if(this.isValidIPv6(prefix[0], errorMsg)){
            return errorMsg;
        }
    },
	isValidMulIPv6: function (value, errorMsg, splitChar){
		if(!splitChar){
			splitChar = ","
		}
        var ipArr = value.split(splitChar);
		for(x in ipArr){
			if(this.isValidIPv6(ipArr[x], errorMsg)){
				return errorMsg;
			}
		}
    },
    isValidIpAddress6 : function(value,errorMsg)
    {
        var i = 0, num = 0;
    
        addrParts = value.split(':');
        if ( addrParts.length < 3 || addrParts.length > 8)
            return errorMsg;
        for ( i = 0; i < addrParts.length; i++)
        {
            if ( addrParts[i] != "")
                num = parseInt(addrParts[i], 16);
            if ( i == 0)
            {
                ;
                //         if ( (num & 0xf000) == 0xf000 )
                //            return false;  //can not be link-local, site-local or
                // multicast address
            }
            else if ( (i + 1) == addrParts.length)
            {
                if ( num == 0 || num == 1)
                    return errorMsg;
                //can not be unspecified or loopback address
            }
            if ( num != 0)
                break;
        }
        // return true;
    },
    isEmptyOrValidIPv6: function (value, errorMsg){ 
        if(!value){
            return;
        }
        return this.isValidIPv6(value, errorMsg);
    },
    isValidIPv6Prefix: function (value, errorMsg){
        var prefix = value.split("/");

        if (prefix.length != 2){
            return errorMsg;
        }

        num = parseInt(prefix[1]);
        if(!num){
            return errorMsg;
        }
        if ( num <= 0 || num > 128){
            return errorMsg;
        }
        
        if(this.isValidIPv6(prefix[0]+"1", errorMsg)){
            return errorMsg;
        }
    },
    isValidIPv6Last64Bits: function(address, errorMsg) {
        var ipv6;
       
        if(address[0] == ':'){
            return errorMsg;
        }
      
        ipv6 = '0000:0000:0000:0000:' + address;
        if (this.isValidIPv6(ipv6, errorMsg)) {
            return errorMsg;
        }
    },   
    isValidMacAddr : function(address, errorMsg){
        var c = '';
        var num = 0;
        var i = 0, j = 0;
        
        addrParts = address.split(':');
        if ( addrParts.length != 6 || address.length != 17) 
            return errorMsg;

        for (i = 0; i < 6; i++) {
            if ( addrParts[i] == '' )
                return errorMsg;
            for ( j = 0; j < addrParts[i].length; j++ ) {
                c = addrParts[i].toLowerCase().charAt(j);
                if ( (c >= '0' && c <= '9') ||
                    (c >= 'a' && c <= 'f') )
                    continue;
                else
                    return errorMsg;
            }

            num = parseInt(addrParts[i], 16);
            if ( num == NaN || num < 0 || num > 255 )
                return errorMsg;

            //multicast mac 
            if (i == 0 && (num & 0x01) != 0)
                return errorMsg;
        }
    },
	/*
	convertStandardMacStr - 转换成标准的MAC地址形式
	001122334455或00-11-22-33-44-55都会被转换成00:11:22:33:44:55
	 */
	convertStandardMacStr : function(macAddress, toUpperCase){
		var newMac = "";
		var mac = macAddress.trimStart();
		mac = mac.trimEnd();
		switch(mac.length){
			case 12:
				newMac = mac.substr(0,2)+":"+mac.substr(2,2)+":" + mac.substr(4,2)+":" + mac.substr(6,2)+":" + mac.substr(8,2)+":" + mac.substr(10,2);
				break;

			case 17:
				newMac = mac.replace(/-/g, ":");
				break;

			default:
				return;
		}
		
		if(this.isValidMacAddr(newMac,"invalid MAC")){
			return;
		}

		if(toUpperCase){
			newMac = newMac.toUpperCase();
		}else{
			newMac = newMac.toLowerCase();
		}

		return newMac;
	},
    isURL : function(value, errorMsg) {
		var re = /^((https|http|ftp|rtsp|mms)?:\/\/)?(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(\#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/; /*'*/
		
        if (re.test(value) == false) {
            return errorMsg;
        }
	},
    ischinese : function(value, errorMsg) {  
        for (var i = 0; i < value.length; i++) {
            if(value.charCodeAt(i) < 33 || value.charCodeAt(i) > 126) {            
                return errorMsg;  
            } 
        }                     
    },  
    isValidDomain : function(domain, errorMsg) {  
        if (!domain) {
            return;
        }
        // 去除域名两端的空格  
        domain = domain.trim();  
    
        // 正则表达式解释：  
        // ^ 字符串开始  
        // (https?:\/\/)? 可选的协议头  
        // (?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+ 域名部分，至少一个字符，可以包含字母、数字、短横线，但不能以短横线开始或结束，总长度受限于63个字符（但不包括TLD长度）  
        // (?:[a-zA-Z]{2,}|xn--[a-zA-Z0-9]+) TLD部分，至少两个字符的字母，或IDN（国际化域名）格式  
        // $ 字符串结束  
        // 注意：这里没有严格限制TLD的长度，因为ICANN允许最长63个字符的TLD，但很少见  
        const regex = /^(https?:\/\/)?(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+(?:[a-zA-Z]{2,}|xn--[a-zA-Z0-9]+)(?!.)?$/;
    //   console.log(regex.test(domain));
        // 使用正则表达式进行匹配  
        if (!regex.test(domain)) {
            return errorMsg;      
        }
    },
    //下面用于数据转换的函数
    convertBoolToDhcpMode: function(value, errorMsg, para){
        return value?"2":"0";
    },
    convertDhcpModeToBool: function(value, errorMsg, para){
        return (value=="2");
    },
    convertWifiBandToNum: function(value, errorMsg, para){
        return (value=="5G")?1:0;
    },
    convertRssiToDbm: function(value, errorMsg, para){
        return value;
    },
    convertDbmToRssi: function(value, errorMsg, para){
        return parseInt(value);
    },
    convertToOnlyLowcaseLetter: function(value){
        var lowercase = value.toLowerCase();
        lowercase = lowercase.replace("-", "");
        lowercase = lowercase.replace("-", "");
        lowercase = lowercase.replace("/", "");
        return lowercase;
    },
    convertYesNoToBool: function(value, errorMsg, para){
        return (value=="yes");
    },
	convertNumStrToBool: function(value, errorMsg, para){
		if(!value){
			return false;
		}
        return (value != "0");
    },
    convertBoolToYesNo: function(value, errorMsg, para){
        return value?"yes":"no";
    },
    convertNoZeroNumToText: function(value, errorMsg, para){
        return value?value:"";
    },
    convertTextToNoZeroNum: function(value, errorMsg, para){
        return parseInt(value)?value:"";
    },
    convertTextToNum: function(value, errorMsg, para){
        return parseInt(value);
    },
    convertBoolToNum: function(value, errorMsg, para){       
        return value?"1":"0";
    },
    convertBoolToNumber: function(value, errorMsg, para){       
        return value?1:0;
    },
    convertIpToText: function(value, errorMsg, para){
        return value=="0.0.0.0"?"":value;
    },
    convertIpStrToNum: function(value, errorMsg, para){
        ipSec = value.split(".");
        if(ipSec.length != 4){
        	return -1;
    	}

        return (parseInt(ipSec[0])<<24 | parseInt(ipSec[1])<<16 | parseInt(ipSec[2])<<8
        	| parseInt(ipSec[3]))>>>0;  //>>>0 to avoid negative number
    },
    convertIp6ToText: function(value, errorMsg, para){
        return value=="::"?"":value;
    },
    convertUpDownToConnectStatus: function(value, errorMsg, para){
        return value=="up"?"已连接":"未连接";
    },
    ConvertLocalTimeZoneForCheckin: function(value, errorMsg, para) {
        return value.split('GMT')[1];
    },
    ConvertLocalTimeZoneForCheckout: function(value, errorMsg, para) {
        return 'GMT'+value;
    },

    /*转换MAC地址带上冒号,例如20F41B606AC0 ---> 20:F4:1B:60:6A:C0*/
    convertMacWithColon: function(value, errorMsg, para){
    	var mac = value;
    	var newMac = mac.slice(0, 2) + ":"
             + mac.slice(2, 4) + ":"
             + mac.slice(4, 6) + ":"
             + mac.slice(6, 8) + ":"
             + mac.slice(8, 10) + ":"
             + mac.slice(10, 12);
        return newMac;
    },
    /*MAC地址去掉冒号,例如20:F4:1B:60:6A:C0 ---> 20F41B606AC0*/
    convertMacWithoutColon: function (value, errorMsg, para) {
        var arr=[],mac='';
        arr = value.split(':');
        for (let i = 0; i < arr.length; i++) {            
            mac += arr[i];
        }
        return mac;
    },
    convertSecsToTimeStr : function(value, errorMsg, para){
	    var onlinetimeStr = "";
	    var day = Math.floor(value/86400);
	    var hour = Math.floor((value%86400)/3600);
	    var min = Math.floor((value%3600)/60);
	    var sec = Math.floor(value%60);
	
	    if(day){
	        onlinetimeStr += day + "天"
	    }
	
	    onlinetimeStr += hour + "小时 "
	    if(min < 10){
	        onlinetimeStr += "0"
	    }
	    onlinetimeStr += min + "分 "
	    if(sec < 10){
	        onlinetimeStr += "0"
	    }
	    onlinetimeStr += sec + "秒 "
	
	    return onlinetimeStr;
	},
    convertToNoCacheUrl: function(url){
		return url;
        if(url.indexOf("?")==-1){
            return url + "?__=" + Math.random();
        }
        return url + "&__=" + Math.random();
    },
	convertGponStateToChinese : function(value, notMergeVal){
		var state = value.replace(/[()]/g, "|").split("|")[1];
		var ChineseStateEnum = {
			O1: "初始",
			O2: "待机",
			O3: "序列号",
			O4: "测距",
			O5: "运行",
			O6: "POPUP",
			O7: "紧急停止"
		}
		if(state){
			var ChineseState = ChineseStateEnum[state];

			if(ChineseState){
				if(notMergeVal){
					return ChineseState;
				}
				return ChineseState + " " + value;
			}
		}
		return value;
	},
    
    
    /*sortBy 数组排序函数,从小到大 */
    sortBy : function(name,minor){
        return function(o,p){
            var a,b;
            if(o && p && typeof o === 'object' && typeof p ==='object'){
                    a = o[name];
                    b = p[name];
                if(a === b){
                    return typeof minor === 'function' ? minor(o,p):0;
                }
                if(typeof a === typeof b){
                    return a < b ? -1:1;
                }
                return typeof a < typeof b ? -1 : 1;
                }
                else{
                    throw("error");
            }
        }
    },
    /*sortBy 数组排序函数,从大到小 */
    sortDescBy : function(name,minor){
        return function(o,p){
            var a,b;
            if(o && p && typeof o === 'object' && typeof p ==='object'){
                    a = o[name];
                    b = p[name];
                if(a === b){
                    return typeof minor === 'function' ? minor(o,p):0;
                }
                if(typeof a === typeof b){
                    return a > b ? -1:1;
                }
                return typeof a > typeof b ? -1 : 1;
                }
                else{
                    throw("error");
            }
        }
    },

	uncheckAllChildrenCheckboxs : function(id){
		/*
		Use querySelectorAll and querySelector. Don't use jquery selector because jquery can't 
		check or uncheck checkbox sometimes and I don't know why.
		*/
		checkList = document.querySelectorAll("#" + id + " [hgs_checked_value]");
		for(x in checkList){
			checkList[x].checked = false;
		}
	},

	formatDateTime : function(date, fmt) {
		const opt = {
			"Y+": date.getFullYear().toString(),        // 年
			"m+": (date.getMonth() + 1).toString(),     // 月
			"d+": date.getDate().toString(),            // 日
			"H+": date.getHours().toString(),           // 时
			"M+": date.getMinutes().toString(),         // 分
			"S+": date.getSeconds().toString()          // 秒
			// 有其他格式化字符需求可以继续添加，必须转化成字符串
		};
		for (let k in opt) {
			ret = new RegExp("(" + k + ")").exec(fmt);
			if (ret) {
				fmt = fmt.replace(ret[1], (ret[1].length == 1) ? (opt[k]) : (opt[k].padStart(ret[1].length, "0")))
			};
		};
		return fmt;
	},

	getCurrentDateTime : function(fmt){
		if(!fmt){
			fmt = "YYYY-mm-dd HH:MM:SS";
		}
		date = new Date();
		return this.formatDateTime(date, fmt);
	},

	datetimeToUnixTimestamp : function(datetime){
		var timeArr = datetime.replace(/-|:/g, " ").split(" ");
		if(timeArr.length == 6){
			timeArr.push(0);
		}
		var t = new Date(timeArr[0], timeArr[1]-1, timeArr[2], timeArr[3], timeArr[4], timeArr[5], timeArr[6]);
		return t.getTime();
	},
	
	unixTimestampToDatetime : function(timestamp, fmt){
		/*
		strategies.unixTimestampToDatetime(1562045557497));  //output: 2019-07-02 13:32:37
		strategies.unixTimestampToDatetime(1562045557497, "yyyy-MM-dd hh:mm:ss:S"); //output: 2019-07-02 13:32:37:497
		*/
		var date = new Date(timestamp);
	
		if(!fmt){
			fmt = "yyyy-MM-dd hh:mm:ss";
		}
	
		var o = {   
			"M+" : date.getMonth()+1,
			"d+" : date.getDate(),
			"h+" : date.getHours(),
			"m+" : date.getMinutes(),
			"s+" : date.getSeconds(),
			"q+" : Math.floor((date.getMonth()+3)/3),
			"S"  : date.getMilliseconds()
		};
	
		var datetime = (function(fmt){
			if(/(y+)/.test(fmt))   
				fmt=fmt.replace(RegExp.$1, (date.getFullYear()+"").substr(4 - RegExp.$1.length));   
			for(var k in o){
				if(new RegExp("("+ k +")").test(fmt))
					fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length))); 
			}
	
			return fmt;
		})(fmt);
		return datetime;
	},

    isValidTime : function (time, errorMsg) {
        var regexs = /^(([0-2][0-3])|([0-1][0-9])):[0-5][0-9]$/;
        if(!regexs.test(time)){
            return errorMsg;
        }        
    },


    compareIPv6 : function (ip1, ip2) {  
        let ip1s = ip1.split(':').map(segment => segment || '0000'); // 处理可能的地址压缩  
        let ip2s = ip2.split(':').map(segment => segment || '0000');  
      
        for (let i = 0; i < 8; i++) {  
            let value1 = parseInt(ip1s[i], 16);  
            let value2 = parseInt(ip2s[i], 16);  

            if (value1 > value2) {  
                return 1; // ip1大于ip2  
            } else if (value1 < value2) {  
                return -1; // ip1小于ip2  
            }  
        }  
      
        return 0; // ip1等于ip2  
    }
    
};

urlWithRandom = strategies.convertToNoCacheUrl;