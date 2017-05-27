function moves() {
	var username = $("#information").val();
	$.ajax({
		type:'GET',
		data:{"information":username},
		url:'/ajax/shop',
		dataType:'json',
		success:function (result) {
			if (result['state']=="true")
			{
				alert('666');
				window.open('/shop');
			}
				
		}
	});
}
function registers() {
	var username = $("#username").val();
	var password1 = $("#password1").val();
	var password2 = $("#password2").val();
	var email = $("#email").val();
	$.ajax({
		type:'GET',
		data:{"username":username,"password1":password1,"password2":password2,"email":email},
		url:'/ajax/register',
		dataType:'json',
		success:function (result) {
			if (result['state']=="true")
			{
				alert(result["text"]);
				self.location('/login');
			}
			else
				alert(result["text"]);
		}
	});
	
}
function login() {
	var username = $("#username").val();
	var password = $("#password").val();
	$.ajax({
		type:'GET',
		data:{"username":username,"password":password},
		url:'/ajax/login',
		dataType:'json',
		success:function (result) {
			if (result['state']=="true") {
				alert(result['text']);
				 location.href="/shop?user="+username
			}
			else{
				alert(result['text']);
			}
		}
	});
}