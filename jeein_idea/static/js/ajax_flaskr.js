$(document).ready(function(){
	$('#email').change(function(){
		var email = $('#email').val();

		$.ajax({
			url: '/email_check',
			type: 'POST',
			data:{"email" : email},
			success:function(response){
				//do something
				var result = $.parseJSON(response);
				if ($("#email").val().match(/[\w_]+@\w+(\.com|\.net|\.ac\.kr)/)){
					if (result['message'] == 'used'){
						$("#email_check").show();
					}
				  else {
						$("#email_check").hide();
					}	
					
			},
			error: function(){
				console.log('error');
			},
			complete:function(){
				console.log('complete')
			}

		});
	});
});