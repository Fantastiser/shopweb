function  shopcart(){
		var href="shopcart";
		 a = document.getElementById("login").innerHTML;
		if(a=="[µÇÂ¼]")  href="login";
		else href ="shopcart"
		location.href=href;	
	}
	
function logout()
{
	$.ajax({
		type:'post',
		data:{"logout":"1"},
		url:'/ajax/logout',
		dataType:'json',
		success:function (result) {
			if (result['state']=="true") {
				alert(result['text']);
				 location.reload();
			}
		}
	});
}
function shopcart() {
	var name = document.getElementById("login").innerHTML;
	if(name == "[µÇÂ¼]" ){
	window.open('/shopcart');
	} else{
		window.open('/login');
	}

	
}