
var xhr;
$(document).ready(function(){

	$("#follow").keyup(function(){
		if( $("#follow").val() != ''){
			
			load_Follow($("#follow").val());			
			}
		else{
			$('#follow_here').empty();
		}
	});

	
	

});

function load_Follow(follow) {
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