var initial1 = 0;
var initial2 = 0;
var amount1 = 100;
var amount2 = 10;

carousel();
function carousel(){
	initial1 -= amount1;
	initial2 += amount2;
	if(initial2 >= 60){
		initial1 = 0;
		initial2 = 0;
	}
	document.getElementById("test").style.transform = "translateX(calc(" + initial1 + "% - " + initial2 + "px))"
	setTimeout(carousel, 2000);
}

function DisplayMenu(){
	var x = document.getElementById("menu");
	// x.classList.add('menu-showing');
	if(x.classList.contains("menu-showing")){
		x.classList.remove("menu-showing");
	} else {
		x.classList.add("menu-showing");
	}
}
