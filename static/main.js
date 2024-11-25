

/*
	Miniport by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/





(function($) {

	var	$window = $(window),
		$body = $('body'),
		$nav = $('#nav');

	// Breakpoints.
		breakpoints({
			xlarge:  [ '1281px',  '1680px' ],
			large:   [ '981px',   '1280px' ],
			medium:  [ '737px',   '980px'  ],
			small:   [ null,      '736px'  ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Scrolly.
		$('#nav a, .scrolly').scrolly({
			speed: 1000,
			offset: function() { return $nav.height(); }
		});

})(jQuery);


var c1 = document.getElementsByClassName("col-12")[2]
var c2 = c1.getElementsByTagName("li")[0]
c2.onclick = function() {
	alert("Confirm Sumbit")
}

// var colourChanger = document.getElementById("top")
// var colours = ["Red", "Blue", "Green", "Pink"]
// var counter = 0

// function changeColour() {
//     if (counter >= colours.length){
//         counter = 0
//     }
//     colourChanger.style.background = colours[counter]
//     counter ++
// }

var myTime = setInterval(changeColour, 1000)
