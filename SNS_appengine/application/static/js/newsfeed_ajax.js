var last = false;
var running = false;
var num = 0;

$(document).ready(function(){
	$(window).scroll(function () {
		if (last == false) {
			if ($(window).scrollTop() == ( $(document).height() - $(window).height())) {
				loadData();
				console.log(num);
			}
		}
	});
});

function loadData() {
	if(!running) {
		running = true;
		$.ajax({
			url: '/load_newsfeed',
			type: 'POST',
			data:{"num":num},

			success:function(response){
				$('#newsfeed_here').append(response);
				num = num+5;
				running = false;
				if (response.trim() ==''){
					last = true;
				}
			},
			error: function(){
				console.log('error');
			},
			complete:function(){
				console.log('complete')
			}
			});
	}
}
