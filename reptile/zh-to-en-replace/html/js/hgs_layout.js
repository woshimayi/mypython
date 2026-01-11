$(function () {

/*
顶部导航栏按钮点击时切换当前active状态
*/
$(".nav-tabs .nav-link").click(function () {
	$(".nav-tabs .nav-link:visible").removeClass("active");
	$(this).addClass("active");
});

//顶部导航栏按钮点击时先隐藏所有hgs_target所在的div，然后显示和hgs_nav属性值一致的hgs_target所在的div
$("#collapsibleNavbar [hgs_nav]").click(function(){
	$(".container > [hgs_target]").hide();
	$(".container .row[hgs_target=" + $(this).attr("hgs_nav") + "]").show();
})


/*
左侧侧边导航栏按钮(药丸形状)点击时切换当前active状态
*/
/*$(".nav-pills .nav-link").click(function () {
	$(".nav-pills .nav-link:visible").removeClass("active");
	$(this).addClass("active");
});*/

/*
这个函数编译动态创建的左侧侧边导航栏按钮(药丸形状)也能生效,使用此函数，上面的函数就不要使用了,避免重复执行
*/
$(".nav-pills").on("click", ".nav-link", function () {
	$(".nav-pills .nav-link:visible").removeClass("active");
	$(this).addClass("active");
});



//左侧侧边导航栏按钮(药丸形状)点击时先隐藏所有hgs_target所在的div，然后显示和hgs_nav属性值一致的hgs_target所在的div
$("a[hgs_sub_nav]").click(function(){
	$(".hgs_content .row:visible").hide();

	var target = ".hgs_content .row[hgs_sub_target=" + $(this).attr("hgs_sub_nav") + "]";
	$(target).show();
	//$(target + " .row").show();
	//console.log($(this).attr("hgs_sub_nav"))
	$("[hgs_sub_target=" + $(this).attr("hgs_sub_nav") + "] .row").show();

	//$(target).children("[id^=HGST_]")
	var tableId = $(target).children().first().attr("id");
	if(tableId && (tableId.indexOf("HGST_") == 0)){
		//如果是table，就需要刷新数据
		updateTableData(tableId);
		return;
	}


	var href_ele = $(target).children("[hgs_href]");
	if(href_ele.length > 0){
		href = href_ele.attr("hgs_href")
		$.get(urlWithRandom(href), function(data){
			if(href_ele.attr("class") && href_ele.attr("class").indexOf("code") >= 0){
				$(href_ele).text(data);
			}else{
				$(href_ele).html(data);
			}
			
			resizeTargetHeight(target); //需要在这里调整高度，否则无效
		})
		return;
	}

	resizeTargetHeight(target);
})


resizeEachContentHeight = function(target){
	var counter = 0;
	for(;target;target = target.parent()){
		if((!target.attr("class"))&&((!target.attr("id")))){
			break;
		}
		if(!target.parent()){
			break;
		}
		if(target.height() && target.parent().height()){
			if(target.parent().height() < target.height()){
				target.parent().height(target.height() + 10);
			}
		}
		counter++;
		if(counter > 5){
			break;
		}
		if(target.attr("class")){
			if(target.attr("class").indexOf("hgs_content") >= 0){
				break;
			}
		}
	}
}

isMobilePhone = function(){
	if(window.screen.width < 640){
		//这里只做简单判断就足够了
		return true;
	}

	return false;
}

/*
resizeSubNavContentHeight -- 用于调整因为hgs_sub_nav内容区的内容发生变化时（撑高会变矮），
调整左侧导航栏和内容区的高度，若不调整，可能会出现footnote和内容区重合等现象
 */

resizeSubNavContentHeight = function(target){

	var hgsDivs = $("[id^='HGS']:visible");

	for(var i = 0;i < hgsDivs.length;i++){
		resizeEachContentHeight($(hgsDivs[i]))
	}

	var hgsContent = $("[class~='hgs_content']:visible");
	if(!hgsContent.length){
		return;
	}

	var hgsSubTarget = $("[hgs_sub_target]:visible");
	if(0 == hgsSubTarget.length){
		return;
	}

	var hgsSubTargetSons = $("[hgs_sub_target]:visible > *:visible");
	var hgsContentTotalHeight = 0;
	for(var m = 0;m < hgsSubTargetSons.length;m++){
		
		var children = $(hgsSubTargetSons[m]).children();
		var totalHeight = 0;
		if(children.length > 0){
			children.each(function(){
				totalHeight = totalHeight + $(this).outerHeight(true);
			});
			hgsContentTotalHeight += totalHeight; 
		}else{
			hgsContentTotalHeight += $(hgsSubTargetSons[m]).height();
		}
	}

	$(hgsContent[0]).height(hgsContentTotalHeight + 10);

	if(isMobilePhone()){
		//对于手机屏幕,不做任何处理
		return;
	}
	

	var hgsSideBar = $("[class~='side_bar']:visible");
	var hgsUL = $("[class~='side_bar']:visible  ul:visible");
	var hgsContent = $("[class~='hgs_content']:visible");

	if((!hgsSideBar.length) || (!hgsContent.length) || (!hgsUL.length)){
		return;
	}

	var hgsSideBarHeight = $(hgsSideBar[hgsSideBar.length - 1]).height();
	var hgsULHeight = 0;	
	for (let j = 0; j < hgsUL.length; j++) {
		hgsULHeight += $(hgsUL[j]).height();
	}
	var hgsContentHeight = $(hgsContent[0]).height();

	if (hgsSideBarHeight < hgsULHeight) {
		$(hgsSideBar[hgsSideBar.length - 1]).height(hgsULHeight);
		hgsSideBarHeight = hgsULHeight;
	}
	
	if(hgsSideBarHeight < hgsContentHeight || hgsSideBarHeight > hgsContentHeight + 10){
		if (hgsContentHeight >= hgsULHeight) {
			$(hgsSideBar[hgsSideBar.length - 1]).height(hgsContentHeight + 10);	
		}
	}
}


resizeTargetHeight = function(target){
	if(isMobilePhone()){
		//对于手机屏幕,不做任何处理
		return;
	}
	/*以内容高度定位侧边导航栏高度和col高度
	如果内容高度高于导航栏高度，则提高导航栏高度
	如果导航栏高度高于内容高度，则提高内容的col的高度
	反之，导航栏和内容都高于实际所需高度，则减少它们高度为合适为止
	*/ 


	if($(target).length == 0){
		return;
	}

	var targetDivHeight = $(target).height();
	var contentDiv = $(target);
	var i = 0;
	var childHeight = 0;

	childHeight = contentDiv.children().height();
	for(;contentDiv;contentDiv = contentDiv.parent(), i++){
		//console.log(contentDiv.height())
		if(contentDiv.attr("class")){
			//console.log(contentDiv.attr("class"))
			if(contentDiv.attr("class").indexOf("hgs_content") >= 0){
				break;
			}
		}
		if(i > 6){
			// try 6 times at most
			return;
		}
	}

	if(contentDiv){
		//console.log(contentDiv.attr("class"))
	}else{
		return;
	}

	var contentHeight = targetDivHeight;     //获取内容的row高度     
	var childrenHeight = contentDiv.children().height();  //获取子内容的row高度

	if(!contentHeight){
		return;
	}

	if(contentHeight < childrenHeight){
		contentHeight = childrenHeight;
	}
	if(contentHeight < childHeight){
		contentHeight = childHeight;
	}

	var subNavObj = contentDiv.prev();  //获取侧边导航栏对象


	/*侧边导航栏内嵌的ul元素的实际所需高度,这个高度在侧边导航栏按钮确定后是不变的，不会随着点击按钮变化而变化
	但这个侧边栏高度可能随着内容变化而变化
	*/
	var subNavChildHeight = subNavObj.children().height();  
	if(!subNavChildHeight){
		return;
	}

	/*取侧边导航栏和内容中两者高度较大值为最后高度*/
	var adjustHeight = contentHeight;
	adjustHeight += 20;   //增加20px，以便内容过宽出现水平滚动条时内容仍然在期望的区域内
	
	if(adjustHeight < subNavChildHeight){
		adjustHeight = subNavChildHeight;
	}

	contentDiv.height(adjustHeight);   //设置侧边内容的col的高度
	if($(window).width() < 576){
		//设置侧边导航栏高度为实际内容高度(在屏幕高度不够的状况下,侧边栏和内容已经不在同一水平线上)
		subNavObj.height(subNavChildHeight);    
		return;
	}
	subNavObj.height(adjustHeight);            //设置侧边导航栏高度
}

getSingleTargetHeight = function(targetId){
	target = "#" + targetId;
	if($(target).length == 0){
		return;
	}
	var contentDiv = $(target);
	var preContentDiv = contentDiv;
	var i = 0;

	for(;contentDiv;contentDiv = contentDiv.parent(), i++){
		if(contentDiv.attr("hgs_sub_target")){
			break;
		}
		if(i > 6){
			// try 6 times at most
			return 0;
		}
		preContentDiv = contentDiv;
	}

	return preContentDiv.height();
}

resizeMultiTargetHeight = function(hgsDivs){
	var totalHeight = 0;
	var height;

	for(var i = 0;i < hgsDivs.length;i++){
		var id = hgsDivs[i].getAttribute("id");
		height = getSingleTargetHeight(id)
		totalHeight += height;
	}

	totalHeight += 20;

	var contentDiv = hgsDivs[0];
	var i = 0;

	for(;contentDiv;contentDiv = contentDiv.parentNode, i++){
		if(contentDiv.getAttribute("class")){
			//console.log(contentDiv.attr("class"))
			if(contentDiv.getAttribute("class").indexOf("hgs_content") >= 0){
				break;
			}
		}
		if(i > 6){
			// try 6 times at most
			return;
		}
	}

	var subNavObj = contentDiv.previousElementSibling;  //获取侧边导航栏对象
	if(subNavObj){
		subNavObj.style.height = totalHeight + "px";
	}
}


//把所有[hgs_target]隐藏
$(".container > [hgs_target]").hide();

//然后显示第一页的[hgs_target]
$(".container > [hgs_target='GCC']").show();


//隐藏所有.hgs_content下的.row
$(".hgs_content .row").hide();

//$("[hgs_sub_nav=gcc_freq]").click();  //这行代码就不需要了，看下一行的注释
//激活active的row，注意:每个页面都有active的row，在html的class中已经写好，默认是每个页面的第一个row
$(".row.active").show();




//获取所以表格的定义
var g_tablesDesc = {}
//对于IE11追加随机数变量"?"+Math.random(),防止缓存导致后面updateTableData异常,其余浏览器不需要追加
if(window.location.href.indexOf(LOGIN_PAGE) < 0){
	$.get("json/tableCfg.json?"+Math.random(), function(data){
		//g_tablesDesc = JSON.parse(data);
		g_tablesDesc = data;
	})
}


updateTableData = function(id){
	if(!g_tablesDesc[id]){
		return;
	}
	var tableDesc = g_tablesDesc[id];
	if(!tableDesc["customerCheckout"]){
		return;
	}
	if(!tableDesc["customerCheckout"]["dataUrl"]){
		return;
	}

	var dataUrl = tableDesc["customerCheckout"]["dataUrl"];

	//获取表格内容数据
	$.get(dataUrl, function(rawJsonData){
		//把JSON格式转换成对象
		var rawData = JSON.parse(rawJsonData)

		/*按如下格式组合成表格数据
		total:表示函数(大于0的整数)
		rows:是个数字
		*/
		tableData = {total:rawData.length, rows:rawData};
		generateTable(id, tableDesc, tableData)
	});
}

setTimeout(function(){
	$("[hgs_sub_nav=gcc_freq]").click();
}, 100) //需要有一定的延时(>100ms),才能加载成功


getTableIdByHgstId = function(id){
	return (id + "_table").toLocaleLowerCase();
}

function generateTable(id, tableDesc, tableData){
	var tableId = getTableIdByHgstId(id);

	var hgstTableDiv = $("#" + tableId);
	if(hgstTableDiv.length){
		//console.log("Table " + tableId + " has already created!")
	}else{
		//console.log("Table " + tableId + " need be created!")
		//如果还没有创建过，先创建

		var html = "<table id='" + tableId + "' class='easyui-datagrid' ></table>"

		$("#" + id).html(html);
		if(tableDesc["style"]){
			//用于设置表格的宽度(width)和边界(border)等
			$("#" + tableId).css(tableDesc["style"])
		}

		$("#" + tableId).datagrid(tableDesc["easyui"]); //设置easyui的风格的表格
	}

	if(tableDesc["cssClass"] && tableDesc["cssClass"]["addClass"]){
		//自定义风格的表格class,区别于easyui的风格的表格
		$("#" + tableId).datagrid('getPanel').addClass(tableDesc["cssClass"]["addClass"]);
	}
	

	//加载数据
	$("#" + tableId).datagrid('loadData', tableData);

	
	//调整高度,如果不做调整的话，原有容器不能适应高度变化的表格
	var adjustTarget = $("#" + id).parent().parent();
	if(!adjustTarget){
		return;
	}

	//增加30px以便出现水平滚动条后仍然能够容纳下
	adjustTarget.height($("#" + id).height() + 30);
	adjustTarget.resize(); //如果没有这行代码，内容很可能在容器之外，即使内容能够放得下


	resizeTargetHeight($("#" + id).parent()); //总体调整侧边导航栏和内容的高度

	/*try{
		window[tableDesc["customerCheckout"]["postLoadData"]](tableData);
	}catch(err){

	}*/
}


urlWithRandom = function(url){
	return url;
	if(!url){  //for IE11
		return;
	}
	if(url.indexOf("?")==-1){
		return url + "?__=" + Math.random();
	}
	return url + "&__=" + Math.random();
}

$(".container").hide();  /*先隐藏container,后面再show,是为了避免闪烁*/
$(".page").hide();       /*隐藏调所有的page*/


/*插入元素，content_left_margin这个类是为了留出左边边距*/
$('<div class="content_left_margin"></div>').insertBefore(".content_input_title")

/*添加类，如果宽度够,留margin,列宽占比分别为1:3:6
如果宽度不够，不留margin,列宽占比分别为2:6
*/
$('h6').attr("style='margin-left:-10px'");
$(".row .content_left_margin").addClass("col-sm-1");
$(".row .content_input_title").addClass("col-4 col-sm-4 col-md-3");
$(".row .content_input").addClass("col-8 col-sm-7 col-md-8");


$(".nav_main a").click(function(){
	$(".nav_main a").removeClass("active");
	$(this).addClass("active");
	$(".page").hide();
	$(".page[page=" +  $(this).attr("target_page") + "]").show();
	$("#focus_page").text($(this).text());
	$(".page[page=" +  $(this).attr("target_page") + "]").click()

	//激活第一个子页面target_page
	$(".page[page=" +  $(this).attr("target_page") + "] [hgs_first_target_page]").click()
	//激活第一个子页面的第一个sub_nav
	//$(".page[page=" +  $(this).attr("target_page") + "] [hgs_first_sub_nav]").click() //暂时不做这个，会导致重复加载数据.chenxi 2021-10-21
	
})


$(".nav_sub a").click(function(){
	$(".nav_sub a").removeClass("active");
	$(this).addClass("active");
	$(".subpage").hide();
	$(".subpage[page=" +  $(this).attr("target_page") + "]").show();
	//激活子页面active区域(模拟点击第一个药丸按钮)
	$("[page='"+ $(this).attr("target_page") + "'] .nav .active").click();
})

$("[target_page='status']").click();


setTimeout(function(){
	$(".container").show();
	$("[target_page='device_info']").click();
}, 100) //需要有一定的延时(>100ms),才能加载成功

})	