
var xhr;
$(document).ready(function(){
	$("#follow").keyup(function(){
		if ($("#follow").val() == ''){
			$('#follow_here').empty();
			if (xhr){
				xhr.abort();
			}
		}
		else{	
			// name edit
			load_follow($("#follow").val());			
		}
	});
});

function load_follow(follow) {
	if (xhr){
		xhr.abort();
	}
	xhr = $.ajax({
		url: '/follow_user',
		type: 'POST',
		data:{"follow":follow},

		success:function(response){
			$('#follow_here').html(response);
		},
		error: function(){
			console.log('error');
		},
		complete:function(){
			console.log('complete');
		}

	});
}