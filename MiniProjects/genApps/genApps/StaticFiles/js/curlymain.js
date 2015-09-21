/*********************** Basic Function *****************/
function show_input(){
    $('.btn1').addClass("zoomOut")
    setTimeout(function() {$('.btn1').hide();$('.btn2').show().addClass("pulse");}, 500);
    
}

function submit_invite(){
    
    $('.btn3').hide().removeClass("pulse");
    var next = $("#inv-email").val();
    if( validateEmail(next) == false){
      $('.btn3').html('<i style="color:#E8B24C"> Please enter valid email id.</i>');  $('.btn3').show().addClass("pulse");return;
    }
    function  before_cb(){  
        $('.btn2').addClass("zoomOut")
        $('.btn3').html('<i style="color:#86F364"> Super!  We received your invitation request! We will get back to you shortly.</i>');
        setTimeout(function() {$('.btn2').hide(); $('.btn3').show().addClass("pulse");}, 1000);
    }
    param ={
        "recipient":"dutta.dipankar08@gmail.com,"+next,
        "subject":"Simple subject",
        "template":"test.html",
        "data":{"a":"aaa","b":"b","res":{"tt":[1,2,3]}}
    }
    //call_backend_api(type,url,param,before_cb,success_cb,error_cb,complete_cb,contentType)
    call_backend_api('POST','/api/email/',param,before_cb,'a','a','a','json')
}

function submit_invite(){
    
    $('.btn3').hide().removeClass("pulse");
    var next = $("#inv-email").val();
    if( validateEmail(next) == false){
      $('.btn3').html('<i style="color:#E8B24C"> Please enter valid email id.</i>');  $('.btn3').show().addClass("pulse");return;
    }
    function  before_cb(){  
        $('.btn2').addClass("zoomOut")
        $('.btn3').html('<i style="color:#86F364"> Super!  We received your invitation request! We will get back to you shortly.</i>');
        setTimeout(function() {$('.btn2').hide(); $('.btn3').show().addClass("pulse");}, 1000);
    }
    param ={
        "recipient":"dutta.dipankar08@gmail.com,"+next,
        "subject":"Simple subject",
        "template":"test.html",
        "data":{"a":"aaa","b":"b","res":{"tt":[1,2,3]}}
    }
    //call_backend_api(type,url,param,before_cb,success_cb,error_cb,complete_cb,contentType)
    call_backend_api('POST','/api/email/',param,before_cb,'a','a','a','json')
}

function submit_contact(){    
    $('.cerror').removeClass("pulse");
    //check
    if($("#cname").val()==''){$('.cerror').html('<i style="color:#E8B24C"> Please enter your name</i>');  $('.cerror').addClass("pulse");return;}
    if( validateEmail($("#cemail").val()) == false){$('.cerror').html('<i style="color:#E8B24C"> Please enter valid email id.</i>');  $('.cerror').addClass("pulse");return;}
    if($("#csub").val()==''){$('.cerror').html('<i style="color:#E8B24C"> Please consider writting some subject</i>');  $('.cerror').addClass("pulse");return;}
    if($("#cmsg").val()==''){$('.cerror').html('<i style="color:#E8B24C"> Please enter some messege</i>');  $('.cerror').addClass("pulse");return;}
    
    
    function  before_cb(){  // we want to fail silently
        $('.cform').addClass("zoomOut")
        $('.cerror').html('<i style="color:#86F364"> Super!  We received your invitation request! We will get back to you shortly.</i>'); $('.cerror').show().addClass("pulse");
    }
    param1 ={
        "name":$("#cname").val(),
        "email":$("#cemail").val(),
        "subject":$("#csub").val(),
        "msg":$("#cmsg").val()
    }
    param ={
        "recipient":"dutta.dipankar08@gmail.com,"+param1.email,
        "subject":"Thank your for your notes!",
        "template":"test.html",
        "data":param1
    }
    //call_backend_api(type,url,param,before_cb,success_cb,error_cb,complete_cb,contentType)
    call_backend_api('POST','/api/ks/peeer_review_form/',param1,before_cb,'a','a','a','json')//store in backend.
    call_backend_api('POST','/api/email/',param,'bc','a','a','a','json');//email send
}

function start_payment(amount){
    amount_inr= amount * 1*100;
    window.r = new Razorpay({
                key: 'rzp_test_x9l3ykmJ0VRznR',
                protocol: 'https',
                hostname: 'api.razorpay.com',
                amount: amount_inr,
                name: 'Peer Review',
                description: 'PeerReview Sample Plan',
                image: 'https://i.imgur.com/3g7nmJC.png',
                prefill: {
                  name: 'Dipankar Dutta',
                  email: 'dutta.dipankar08@gmail.com',
                  contact: '8688204060'
                },
                handler: function (transaction){
                  alert('You have successfully purchased Fine tshirt\ntransaction id: ' + transaction.razorpay_payment_id);
                }
              }).open();
}


/**********************  End of Basic Function *************/


$(document).ready(function() {

  /**
   * Author: Heather Corey
   * jQuery Simple Parallax Plugin
   *
   */
   
  (function($) {
   
      $.fn.parallax = function(options) {
   
          var windowHeight = $(window).height();
   
          // Establish default settings
          var settings = $.extend({
              speed        : 0.15
          }, options);
   
          // Iterate over each object in collection
          return this.each( function() {
   
            // Save a reference to the element
            var $this = $(this);
   
            // Set up Scroll Handler
            $(document).scroll(function(){
   
                  var scrollTop = $(window).scrollTop();
                        var offset = $this.offset().top;
                        var height = $this.outerHeight();
   
            // Check if above or below viewport
        if (offset + height <= scrollTop || offset >= scrollTop + windowHeight) {
          return;
        }
   
        var yBgPosition = Math.round((offset - scrollTop) * settings.speed);
   
                          // Apply the Y Background Position to Set the Parallax Effect
            $this.css('background-position', 'center ' + yBgPosition + 'px');
                  
            });
          });
      }
  }(jQuery));

//Loader
$(window).load(function() {
	$(".loader-overlay").fadeOut("slow");
})
/*
//Counter: http://bfintal.github.io/Counter-Up/demo/demo.html
$('.counter').counterUp({
    delay: 10,
    time: 1000
});
*/


/*
//Ref: http://cornel.bopp-art.com/lightcase/
$('a[data-rel^=lightcase]').lightcase();
*/


/* //ref: https://mixitup.kunkalabs.com/
// Instantiate MixItUp
  $('.portfolio-items').mixItUp({
       animation: {
          duration: 300
      }
  });
*/


// Carousels :http://www.owlcarousel.owlgraphic.com/demos/demos.html ( Responsive)
/*
$('.cl-client-carousel').owlCarousel({
      pagination:true,
      slideSpeed : 300,
      paginationSpeed : 400,
      singleItem:true,
      autoPlay:true,
  }); 
  
  $('.cl-logo-carousel').owlCarousel({
	  items : 6,
      itemsDesktop : [1199,5],
      itemsDesktopSmall : [979,3],
      stopOnHover:true,
      autoPlay:3000,
  });

    $(".header-carousel").owlCarousel({
        pagination:true,
        navigation : true, // Show next and prev buttons
        slideSpeed : 500,
        paginationSpeed : 500,
        singleItem:true,
        autoPlay:true,
    });
*/
// Parallax
$('.parallax-section').parallax({
          speed : .100
        });

// Header Changer on Scroll
$(function() {
    //caches a jQuery object containing the header element
    var header = $(".header-home");
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll >= 100) {
            header.removeClass('header-home').addClass("header-default");
        } else {
            header.removeClass("header-default").addClass('header-home');
        }
    });
});

// Navigation : jquery.nav.js
  $('.nav-container').onePageNav({
    scrollSpeed: 600,
    currentClass: 'current',
    changeHash: true,
    filter: ':not(.external)'
  });

//Header Class Change on Resize
  var $window = $(window);

      // Function to handle changes to style classes based on window width
      function checkWidth() {
      if ($window.width() < 767) {
          $('#top-header').removeClass('header-home').addClass('header-default');
          };

      if ($window.width() >= 767) {
          $('#top-header').removeClass('header-default').addClass('header-home');
      }
  }

  // Execute on load
  checkWidth();

  // Bind event listener
      $(window).resize(checkWidth);

//Google Map
//set your google maps parameters
	var $latitude = 45.537383,
		$longitude = -73.597623,
		$map_zoom = 14;

	//google map custom marker icon - .png fallback for IE11
	var is_internetExplorer11= navigator.userAgent.toLowerCase().indexOf('trident') > -1;
	var $marker_url = ( is_internetExplorer11 ) ? 'http://i.imgur.com/TYdWTLk.png' : 'http://i.imgur.com/TYdWTLk.png';
		
	//define the basic color of your map, plus a value for saturation and brightness
	var	$main_color = '#1abc9c',
		$saturation= -20,
		$brightness= 5;

	//we define here the style of the map
	var style= [ 
		{
			//set saturation for the labels on the map
			elementType: "labels",
			stylers: [
				{saturation: $saturation}
			]
		},  
	    {	//poi stands for point of interest - don't show these lables on the map 
			featureType: "poi",
			elementType: "labels",
			stylers: [
				{visibility: "off"}
			]
		},
		{
			//don't show highways lables on the map
	        featureType: 'road.highway',
	        elementType: 'labels',
	        stylers: [
	            {visibility: "off"}
	        ]
	    }, 
		{ 	
			//don't show local road lables on the map
			featureType: "road.local", 
			elementType: "labels.icon", 
			stylers: [
				{visibility: "off"} 
			] 
		},
		{ 
			//don't show arterial road lables on the map
			featureType: "road.arterial", 
			elementType: "labels.icon", 
			stylers: [
				{visibility: "off"}
			] 
		},
		{
			//don't show road lables on the map
			featureType: "road",
			elementType: "geometry.stroke",
			stylers: [
				{visibility: "off"}
			]
		}, 
		//style different elements on the map
		{ 
			featureType: "transit", 
			elementType: "geometry.fill", 
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
		}, 
		{
			featureType: "poi",
			elementType: "geometry.fill",
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
		},
		{
			featureType: "poi.government",
			elementType: "geometry.fill",
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
		},
		{
			featureType: "poi.sport_complex",
			elementType: "geometry.fill",
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
		},
		{
			featureType: "poi.attraction",
			elementType: "geometry.fill",
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
		},
		{
			featureType: "poi.business",
			elementType: "geometry.fill",
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
		},
		{
			featureType: "transit",
			elementType: "geometry.fill",
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
		},
		{
			featureType: "transit.station",
			elementType: "geometry.fill",
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
		},
		{
			featureType: "landscape",
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
			
		},
		{
			featureType: "road",
			elementType: "geometry.fill",
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
		},
		{
			featureType: "road.highway",
			elementType: "geometry.fill",
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
		}, 
		{
			featureType: "water",
			elementType: "geometry",
			stylers: [
				{ hue: $main_color },
				{ visibility: "on" }, 
				{ lightness: $brightness }, 
				{ saturation: $saturation }
			]
		}
	];
		
	//set google map options
	var map_options = {
      	center: new google.maps.LatLng($latitude, $longitude),
      	zoom: $map_zoom,
      	panControl: false,
      	zoomControl: false,
      	mapTypeControl: false,
      	streetViewControl: false,
      	mapTypeId: google.maps.MapTypeId.ROADMAP,
      	scrollwheel: false,
      	styles: style,
    }
    //inizialize the map
	var map = new google.maps.Map(document.getElementById('google-container'), map_options);
	//add a custom marker to the map				
	var marker = new google.maps.Marker({
	  	position: new google.maps.LatLng($latitude, $longitude),
	    map: map,
	    visible: true,
	 	icon: $marker_url,
	});

	//add custom buttons for the zoom-in/zoom-out on the map
	function CustomZoomControl(controlDiv, map) {
		//grap the zoom elements from the DOM and insert them in the map 
	  	var controlUIzoomIn= document.getElementById('cd-zoom-in'),
	  		controlUIzoomOut= document.getElementById('cd-zoom-out');
	  	controlDiv.appendChild(controlUIzoomIn);
	  	controlDiv.appendChild(controlUIzoomOut);

		// Setup the click event listeners and zoom-in or out according to the clicked element
		google.maps.event.addDomListener(controlUIzoomIn, 'click', function() {
		    map.setZoom(map.getZoom()+1)
		});
		google.maps.event.addDomListener(controlUIzoomOut, 'click', function() {
		    map.setZoom(map.getZoom()-1)
		});
	}

	var zoomControlDiv = document.createElement('div');
 	var zoomControl = new CustomZoomControl(zoomControlDiv, map);

  	//insert the zoom div on the top left of the map
  	map.controls[google.maps.ControlPosition.LEFT_TOP].push(zoomControlDiv);

});
