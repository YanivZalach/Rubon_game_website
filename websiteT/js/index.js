// Getting the element for the feedback rotation
const feedbackUl = document.querySelector('#IndexFeedbackUl');

// Starting number of element
let element_num = 0;

// Li list
const li_list = [...feedbackUl.children];

// Setting the feedback interval
const feedback_interval = 4000;

// Setting the interval
const interval = setInterval(move_feedback,feedback_interval);


function move_feedback(){
	// Making the currant element to disappear
	li_list[element_num].style.display = 'none';
	// The next element
	element_num = (element_num + 1) % li_list.length;
	// Making it to appear
	li_list[element_num].style.display = 'block';
}

