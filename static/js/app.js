
var init1 = 0;
var init2 = 0;
var amount1 = 100;
var amount2 = 10;
var next1;
var next2;
var current = 0;
var  slider = $('.slider');

carousel();
function carousel(){
	init1 = current*(-100);
	init2 = current*(10);
	if(current >= 16){
		init1 = 0;
		init2 = 0;
		current = 0;
	}
	++current;
	slider.css('transform', "translateX(calc(" + init1 + "% - " + init2 + "px))");
	console.log(current);
	setTimeout(carousel, 1000);
}

$('.gallery_btn_wrapper').show().find('.gallery_btn').on('click', function() {
	var direction = $(this).data('dir')
	if(direction === 'next'){
		++current;
	} else {
		--current;
	}
	if (current >= 16) {current = 0}
	transition(direction,slider, current)
});

function transition(direction, container, current){
	var a,b,c = -100, d = 10;
	if(direction === 'next'){
		a = current*(-100);
		b = current*(10);
	} else {
		a += 100;
		b -= 10;
	}
	slider.css('transform', "translateX(calc(" + a + "% - " + b + "px))");
}

function DisplayMenu(){
	var x = document.getElementById("menu");
	var y = document.getElementById("show-x");
	if(x.classList.contains("menu-showing")){
		x.classList.remove("menu-showing");
		y.classList.remove("menu-showing");
	} else {
		x.classList.add("menu-showing");
		y.classList.add("menu-showing");
	}
}


function initMap(){
	var location = {lat: -25.363, lng: 131.044};
	var map = new google.maps.Map(document.getElementById("map"),{
		zoom: 4,
		center: location
	});
}