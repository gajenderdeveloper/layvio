AOS.init({
	duration: 800,
	easing: 'slide',
	once: true
});

jQuery(document).ready(function ($) {

	"use strict";


	var siteMenuClone = function () {

		$('.js-clone-nav').each(function () {
			var $this = $(this);
			$this.clone().attr('class', 'site-nav-wrap').appendTo('.site-mobile-menu-body');
		});


		setTimeout(function () {

			var counter = 0;
			$('.site-mobile-menu .has-children').each(function () {
				var $this = $(this);

				$this.prepend('<span class="arrow-collapse collapsed">');

				$this.find('.arrow-collapse').attr({
					'data-toggle': 'collapse',
					'data-target': '#collapseItem' + counter,
				});

				$this.find('> ul').attr({
					'class': 'collapse',
					'id': 'collapseItem' + counter,
				});

				counter++;

			});

		}, 1000);

		$('body').on('click', '.arrow-collapse', function (e) {
			var $this = $(this);
			if ($this.closest('li').find('.collapse').hasClass('show')) {
				$this.removeClass('active');
			} else {
				$this.addClass('active');
			}
			e.preventDefault();

		});

		$(window).resize(function () {
			var $this = $(this),
				w = $this.width();

			if (w > 768) {
				if ($('body').hasClass('offcanvas-menu')) {
					$('body').removeClass('offcanvas-menu');
				}
			}
		})

		$('body').on('click', '.js-menu-toggle', function (e) {
			var $this = $(this);
			e.preventDefault();

			if ($('body').hasClass('offcanvas-menu')) {
				$('body').removeClass('offcanvas-menu');
				$this.removeClass('active');
			} else {
				$('body').addClass('offcanvas-menu');
				$this.addClass('active');
			}
		})

		// click outisde offcanvas
		$(document).mouseup(function (e) {
			var container = $(".site-mobile-menu");
			if (!container.is(e.target) && container.has(e.target).length === 0) {
				if ($('body').hasClass('offcanvas-menu')) {
					$('body').removeClass('offcanvas-menu');
				}
			}
		});
	};
	siteMenuClone();


	var sitePlusMinus = function () {
		$('.js-btn-minus').on('click', function (e) {
			e.preventDefault();
			if ($(this).closest('.input-group').find('.form-control').val() != 0) {
				$(this).closest('.input-group').find('.form-control').val(parseInt($(this).closest('.input-group').find('.form-control').val()) - 1);
			} else {
				$(this).closest('.input-group').find('.form-control').val(parseInt(0));
			}
		});
		$('.js-btn-plus').on('click', function (e) {
			e.preventDefault();
			$(this).closest('.input-group').find('.form-control').val(parseInt($(this).closest('.input-group').find('.form-control').val()) + 1);
		});
	};
	// sitePlusMinus();


	var siteSliderRange = function () {
		$("#slider-range").slider({
			range: true,
			min: 0,
			max: 500,
			values: [75, 300],
			slide: function (event, ui) {
				$("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
			}
		});
		$("#amount").val("$" + $("#slider-range").slider("values", 0) +
			" - $" + $("#slider-range").slider("values", 1));
	};
	// siteSliderRange();


	var siteMagnificPopup = function () {
		$('.image-popup').magnificPopup({
			type: 'image',
			closeOnContentClick: true,
			closeBtnInside: false,
			fixedContentPos: true,
			mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
			gallery: {
				enabled: true,
				navigateByImgClick: true,
				preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
			},
			image: {
				verticalFit: true
			},
			zoom: {
				enabled: true,
				duration: 300 // don't foget to change the duration also in CSS
			}
		});

		$('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
			disableOn: 700,
			type: 'iframe',
			mainClass: 'mfp-fade',
			removalDelay: 160,
			preloader: false,

			fixedContentPos: false
		});
	};
	siteMagnificPopup();


	var siteCarousel = function () {
		if ($('.nonloop-block-13').length > 0) {
			$('.nonloop-block-13').owlCarousel({
				center: false,
				items: 1,
				loop: true,
				stagePadding: 0,
				margin: 0,
				autoplay: true,
				nav: true,
				navText: ['<span class="icon-arrow_back">', '<span class="icon-arrow_forward">'],
				responsive: {
					600: {
						margin: 0,
						nav: true,
						items: 2
					},
					1000: {
						margin: 0,
						stagePadding: 0,
						nav: true,
						items: 3
					},
					1200: {
						margin: 0,
						stagePadding: 0,
						nav: true,
						items: 4
					}
				}
			});
		}

		$('.slide-one-item').owlCarousel({
			center: false,
			items: 1,
			loop: true,
			stagePadding: 0,
			margin: 0,
			autoplay: true,
			pauseOnHover: false,
			nav: true,
			navText: ['<span class="icon-keyboard_arrow_left">', '<span class="icon-keyboard_arrow_right">']
		});
	};
	siteCarousel();

	var siteStellar = function () {
		$(window).stellar({
			responsive: false,
			parallaxBackgrounds: true,
			parallaxElements: true,
			horizontalScrolling: false,
			hideDistantElements: false,
			scrollProperty: 'scroll'
		});
	};
	siteStellar();

	var siteCountDown = function () {

		$('#date-countdown').countdown('2020/10/10', function (event) {
			var $this = $(this).html(event.strftime(''
				+ '<span class="countdown-block"><span class="label">%w</span> weeks </span>'
				+ '<span class="countdown-block"><span class="label">%d</span> days </span>'
				+ '<span class="countdown-block"><span class="label">%H</span> hr </span>'
				+ '<span class="countdown-block"><span class="label">%M</span> min </span>'
				+ '<span class="countdown-block"><span class="label">%S</span> sec</span>'));
		});

	};
	siteCountDown();

	var siteDatePicker = function () {

		if ($('.datepicker').length > 0) {
			$('.datepicker').datepicker();
		}

	};
	siteDatePicker();

});

/*testimonial sliadert*/
$(document).ready(function() {
	//Set the carousel options
	$('#quote-carousel').carousel({
	  pause: true,
	  interval: 4000,
	});
  });   

  /*for review rating */

  const allStar = document.querySelectorAll('.rating .star')
const ratingValue = document.querySelector('.rating input')

allStar.forEach((item, idx)=> {
	item.addEventListener('click', function () {
		let click = 0
		ratingValue.value = idx + 1

		allStar.forEach(i=> {
			i.classList.replace('bxs-star', 'bx-star')
			i.classList.remove('active')
		})
		for(let i=0; i<allStar.length; i++) {
			if(i <= idx) {
				allStar[i].classList.replace('bx-star', 'bxs-star')
				allStar[i].classList.add('active')
			} else {
				allStar[i].style.setProperty('--i', click)
				click++
			}
		}
	})
})
/* swiper  slidesPerView: 6*/


var swiper = new Swiper('.swiper-container', {
	slidesPerView: 6,
	spaceBetween: 20,
	slidesPerGroup: 6,
	loop: true,

	loopFillGroupWithBlank: true,
	pagination: {
		el: '.swiper-pagination',
		clickable: true,
	},
	navigation: {
		nextEl: '.swiper-button-next',
		prevEl: '.swiper-button-prev',
	},
});


var swiper = new Swiper('.swiper-second-container', {
	slidesPerView: 3,
	spaceBetween: 20,
	slidesPerGroup: 3,
	loop: false,

	loopFillGroupWithBlank: true,
	pagination: {
		el: '.swiper-pagination',
		clickable: true,
	},
	navigation: {
		nextEl: '.swiper-button-next-two',
		prevEl: '.swiper-button-prev-two',
	},
});


/* scrollToAnchor( */

function scrollToAnchor(aid) {
	var aTag = $("a[name='" + aid + "']");
	$('html,body').animate({ scrollTop: aTag.offset().top }, 'slow');
}

$("#why-choose-us").click(function () {
	scrollToAnchor('why-choose-us');
});
function scrollToAnchor(aid) {
	var aTag = $("a[name='" + aid + "']");
	$('html,body').animate({ scrollTop: aTag.offset().top }, 'slow');
}

$("#let-just-2").click(function () {
	scrollToAnchor('let-just-2');
});
function scrollToAnchor(aid) {
	var aTag = $("a[name='" + aid + "']");
	$('html,body').animate({ scrollTop: aTag.offset().top }, 'slow');
}

$("#let-just").click(function () {
	scrollToAnchor('let-just');
});



(function ($) {
	"use strict"; $('.input100').each(function () {
		$(this).on('blur', function () {
			if ($(this).val().trim() != "") { $(this).addClass('has-val'); }
			else { $(this).removeClass('has-val'); }
		})
	})
	var input = $('.validate-input .input100'); $('.validate-form').on('submit', function () {
		var check = true; for (var i = 0; i < input.length; i++) { if (validate(input[i]) == false) { showValidate(input[i]); check = false; } }
		return check;
	}); $('.validate-form .input100').each(function () { $(this).focus(function () { hideValidate(this); }); }); function validate(input) {
		if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') { if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) { return false; } }
		else { if ($(input).val().trim() == '') { return false; } }
	}
	function showValidate(input) { var thisAlert = $(input).parent(); $(thisAlert).addClass('alert-validate'); }
	function hideValidate(input) { var thisAlert = $(input).parent(); $(thisAlert).removeClass('alert-validate'); }
})(jQuery);

//----- for profile ------//

$('#myTab a').on('click', function(e) {
    e.preventDefault()
    $(this).tab('show')
});

/**
 * Datatable call
 */
$(document).ready(function() {
    $('#my-orders-table').DataTable();
});

/**
 * My account nav click
 */
$(document).ready(function() {
    $('.tg-tabs-content-wrapp .my-account-dashboard .card').click(function() {

        var ariaClick = $(this).attr('area-toggle');
        $('.tg-account .account-banner .nav-area  a#' + ariaClick).click();
    });
});

// ===== Scroll to Top ==== 



$(window).scroll(function() {
    if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
        $('#return-to-top').fadeIn(200);    // Fade in the arrow
    } else {
        $('#return-to-top').fadeOut(200);   // Else fade out the arrow
    }
});
$('#return-to-top').click(function() {      // When arrow is clicked
    $('body,html').animate({
        scrollTop : 0                       // Scroll to top of body
    }, 500);
});

// ===== hide button  ==== 

$(document).ready(function () {
	$(".req-temp").click(function () {
		$(".custom-req").show();
	});
	$(".req-temp-2").click(function () {
		$(".custom-req").hide();
	});
});