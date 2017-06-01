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
