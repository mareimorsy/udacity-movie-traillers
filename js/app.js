$(document).ready(function(){

	// boxes
	$('.movie-wrapper').hover(function(){
		$(".boxcaption", this).stop().animate({top:'0'},{queue:false,duration:300});
		$(".boxcaption").css("cursor", "pointer")
	}, function() {
		height = $(".movie-box").height();
		$(".boxcaption", this).stop().animate({top:(height-61)+'px'},{queue:false,duration:300});
	});

	// Animate in the movies when the page loads
	$('.movie-box').hide().first().show("fast", function showNext() {
		$(this).next("div").show("fast", showNext);
	});

});

$(window).on('resize', function(){
	height = $(".movie-box").height();
	$(".boxcaption", ".movie-box").stop().animate({top:(height-61)+'px'},{queue:false,duration:300});
});

// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});
// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-box', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
      'id': 'trailer-video',
      'type': 'text-html',
      'src': sourceUrl,
      'frameborder': 0
    }));
});