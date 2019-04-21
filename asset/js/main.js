$(document).ready(function(){
		var controller = new ScrollMagic.Controller();	
	$('.describe').each(function(){


		var ourScene= new ScrollMagic.Scene({
			triggerElement: this,
			triggerHook:0.9,
			reverse:false
		})

		.setClassToggle(this, 'fade-in')
		// .addIndicators({
		// 	name:'fade scene',
		// 	colorTrigger:'black',
		// 	colorStart:'green'
		// })		
		.addTo(controller);


	});
	// var pin = new ScrollMagic.Scene({
 //      triggerElement: '#nav',
 //      triggerHook:'onLeave'
 //  	})
 //  	.setPin('#nav', {pushFollowers: true})
 //  	.addTo(controller);

var butscene = new ScrollMagic.Scene({
	triggerElement:'.moveUp',
	triggerHook:0.9
	
})
.setClassToggle('.moveUp', 'move')
.addTo(controller);

});


var contentid = document.getElementById("contentid");

contentid.onclick = function() {
  TweenLite.to(window, 1, {scrollTo:{y:"#contents", offsetY:70, autoKill:false}});
}

