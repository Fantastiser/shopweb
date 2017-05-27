function Login() {
	var username = $("#user").val();
	var password = $("#pass").val();
	$.ajax({
		type:'GET',
		data:{"username":username,"password":password},
		url:'/ajax/login',
		dataType:'json',
		success:function (result) {
			if (result['state']=="true") {
				alert(result['text']);
			}
			else{
				alert(result['text']);
			}
		}
	});
}