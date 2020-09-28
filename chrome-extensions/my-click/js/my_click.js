function my_click(el) {
	var today=new Date();
	var h=today.getHours();
	var m=today.getMinutes();
	var s=today.getSeconds();
	m=m>=10?m:('0'+m)
	s=s>=10?s:('0'+s)
	el.innerHTML = h+":"+m+":"+s;
	setTimeout(function(){my_click(el)}, 1000);
}

var click_div = document.getElementById('click_div');
my_click(click_div)