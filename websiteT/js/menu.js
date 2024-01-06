// For smartphone display
function for_smartphone(width) {
	console.log("width limit pased")
	// The changes
	const nav = document.querySelector('nav');
	const navList = document.querySelector('#NavList');
	const navHideButton = document.querySelector('#NavHide');

	if (width.matches) { // If media query matches
		// Not showing the list of locations
		navList.style.display = 'none';

		// Showing the button to use the website
		navHideButton.style.display = 'block';

		// Making the nav to cover the screen when open
		navList.style.height = '100vh'; // Set height to 100% of viewport height 
		// Making the list to appear at the end for seeing all the buttons
		navList.style.order = '1';

		// Making the nav warp
		nav.style.flexWrap = 'wrap';
	}else{
		// Showing the list of locations
		navList.style.display = 'inline-flex';

		// Not showing the button to use the website
		navHideButton.style.display = 'none';

		// Resetting the header hight
		navList.style.height = 'auto'; // Set height to 100% of viewport height 

		// Making the nav to not warp
		nav.style.flexWrap = 'nowrap';
		// Making the list to appear at the original location
		navList.style.order = '0';
	}
}

// Create a MediaQueryList object
const width = window.matchMedia("(max-width: 570px)")

// Call listener function at run time
for_smartphone(width);

// Attach listener function on state changes
width.addEventListener("change", function() {
  for_smartphone(width);
});

// Function to scroll to the top of the page
function scrollToTop() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
}

// Nav toggle menu
// The elements
const toggle_button = document.querySelector('#NavHide');
const nav_list = document.querySelector('#NavList');

// Function to toggle the menu
function toggle_menu() {
	scrollToTop();  // Going to the top of the website for seeing the hole list
    if (window.getComputedStyle(nav_list).display === 'none') {
        nav_list.style.display = 'block';
    } else {
        nav_list.style.display = 'none';
    }
}

