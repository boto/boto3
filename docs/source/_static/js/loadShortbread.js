// Load shortbread
document.addEventListener('DOMContentLoaded', function() {

	document.body.dataset.theme = localStorage.getItem("theme") || "auto";

	if (typeof AWSCShortbread !== 'undefined') {
		const shortbread = AWSCShortbread({
        // domain: ".amazonaws.com"
        domain: "d3o2vvnrhogbwx.cloudfront.net"
    	});

	    // Check for cookie consent
	    shortbread.checkForCookieConsent();

	    // Add event listener for 'Cookie preferences' link read from page.html
	    const cookiePreferencesLink = document.getElementById('cookie-button-link');
	    if (cookiePreferencesLink) {
	        cookiePreferencesLink.addEventListener('click', function(event) {
	            event.preventDefault();
	            shortbread.customizeCookies();
	        });
	    }
	    console.log("AWSCShortbread loaded successfully loaded!!!")
	} else {
		console.error("AWSCShortbread failed to load!!!")
	}
});
