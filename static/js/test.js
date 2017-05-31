function AddFavorite(sURL, sTitle)
{
	try
	{
		window.external.addFavorite(sURL, sTitle);
	}
	catch(e)
	{
		try
		{
			window.sidebar.addPanel(sTitle, sURL, "");
		}
			catch (e)
		{
			alert("加入收藏失败，请使用Ctrl+D进行添加");
		}
	}
}
function moves() {
	var name = $("#information").val();
	var a;
	a = document.URL.replace(window.location.pathname,'/filter');
	if(a.indexOf("?") == 0 ){
	window.open(a+'&itemid='+name);
	} else{
		window.open(a+'?&itemid='+name);
		
	}

	
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
				location.href = '/login';
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
				 location.href="/shop?user="+username;
			}
			else{
				alert(result['text']);
			}
		}
	});
}
function changeUrlArg(arg, val){
	url=document.URL;
    var pattern = arg+'=([^&]*)';
    var replaceText = arg+'='+val;
    return url.match(pattern) ? url.replace(eval('/('+ arg+'=)([^&]*)/gi'), replaceText) : (url.match('[\?]') ? url+'&'+replaceText : url+'?'+replaceText);
}


function GetQueryString(arg)
{
    var reg = new RegExp("(^|&)" + arg + "=([^&]*)(&|$)", "i");  
    var l = decodeURI(window.location.search);  
    var r = l.substr(1).match(reg);  
    if (r != null) return unescape(r[2]);  
    return null;  
}
function loader(){
		if(GetQueryString("user")!=null) {
			document.getElementById("login").style.display="none";
			document.getElementById("register").style.display="none";
		}
	}

	
