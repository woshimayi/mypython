$.get_fwupgrade_href = function() {
    $.ajax({
                    type: "get",//请求方式
                    url: "demo.json",//地址，就是json文件的请求路径
                    dataType: "json",//数据类型可以为 text xml json  script  jsonp
                    async: false,
                    success: function(data){//返回的参数就是 action里面所有的有get和set方法的参数
                        var dataArrays = data;
                        var status = dataArrays.region1;
                        var url = dataArrays.region2;
                        alert(status, url)
                    }
                });
};





$.get_upgrade_status = function() {
    $.ajax({
        url: 'upg_get_status.htm'+$.ID_2,
        type: 'GET',
        dataType: 'json',
        contentType: "application/json; charset=utf-8",
        timeout: 90000,
        success: function(json) {
            if ( $.reset_login(json) )
                return false;
            if ( json.status == "1" ) {
                //$.removeCookie('interim');
                location.href = "fwUpdateCheck.htm";
            }
        },
    });
};


response.setContentType("application/json;charset=utf-8");//指定返回的格式为JSON格式
JSONObject ob =new  JSONObject();//创建json对象
ob.accumulate("name","小明");//添加元素
ob.accumulate("age", 18);
PrintWriter out =response.getWriter() ;
out.print(ob);
out.close();







$.getJSON("http://192.168.1.250/fwUpdate.htm",{param:"status", param:"url"},function(data){
  $.each(data.root,function(idx,item){  
    if(idx==0){  
      return true;//同continue，返回false同break  
    }  
    console.log("name:"+item.status+",value:"+item.url);
  });  
}); 