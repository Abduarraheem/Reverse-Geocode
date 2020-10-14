// variable which checks if the switch has been checked 
const pressSwitch = document.querySelector('.switch input[type="checkbox"]');

function switchBtn(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-mode', 'dark'); // set the attibute to dark
        localStorage.setItem('mode', 'dark'); // set the mode to document storage so we can use it if the user refreshes
    }
    else {
        document.documentElement.setAttribute('data-mode', 'light');  // set the attibute to light
        localStorage.setItem('mode', 'light'); // set the mode to document storage so we can use it if the user refreshes
    }    
}

/* 
listener that waits and checks for the switch to be pressed
if pressed then the mode will be switched.
*/
pressSwitch.addEventListener('change', switchBtn, false); 

// get the current mode from localStorage
const currentMode = localStorage.getItem('mode') ? localStorage.getItem('mode') : null;

/* 
Gets the current mode from localStorage and sets that mode and if it is dark mode
it make it so that the switch is checked.
*/

if (currentMode) {
    document.documentElement.setAttribute('data-mode', currentMode);
    if (currentMode === 'dark') {
        pressSwitch.checked = true;
    }
}


/*Nav menu button*/
const navBtn = document.querySelector('.nav-menu'); 
const navBar = document.querySelector('.top-nav');
const navList = document.querySelector('.nav-list');
navBtn.addEventListener('click',()=>{
    navBtn.classList.toggle("open");
    navBar.classList.toggle("open");
    navList.classList.toggle("open");
});