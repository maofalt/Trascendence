import '@css/style.css'
// import 'bootstrap/dist/css/bootstrap.min.css';
// import 'bootstrap';
// import javascriptLogo from '/javascript.svg';
// import viteLogo from '/vite.svg';
// import { setupCounter } from '@utils/counter.js';
import Home from '@views/Home.js';
import Tournament from '@views/Tournament.js';
import Options from '@views/Options.js';
import Game from '@views/Game.js';
import Login from '@views/Login.js';
import NotFound from '@views/NotFound.js';

const routes = {
	'/': {
		path: '/',
		view: Home,
		title: 'Pongiverse',
		buttonText: 'Home'
	},
	'/play': {
		path: '/play',
		view: Game,
		title: 'Game',
		buttonText: 'Play'
	},
	'/game': {
		path: '/game',
		view: Game,
		title: 'Game',
		buttonText: 'Play'
	},
	'/tournament': {
		path: '/tournament',
		view: Tournament,
		title: 'Tournament',
		buttonText: 'Tournament'
	},
	'/options': {
		path: '/options',
		view: Options,
		title: 'Options',
		buttonText: 'Options'
	},
	'/login': {
		path: '/login',
		view: Login,
		title: 'Login',
		buttonText: 'Login'
	},
	'/404': {
		path: '/404',
		view: NotFound,
		title: '404 Not Found',
		buttonText: 'Not Found Page'
	}
};

const navigateTo = (url) => {
	history.pushState(null, null, url);
	router();
}

let currentView = null;

const router = async () => {
	const path = window.location.pathname; // get the current path
<<<<<<< HEAD
	const match = routes[path] || routes['/404']; // find the matching route or use the 404 route
	
=======
	const match = routes[Object.keys(routes).find(route => route == path)] || routes['/404']; // find the matching route or use the 404 route

>>>>>>> 18e9b5ffa1150d3841e7ce8cb63b25498b2a5c6c
	// if view has a destroy function, call it
	if (currentView && currentView.destroy && currentView != match.view) {
		currentView.destroy();
		//console.log("destroying view" + currentView);
	}
	// create a new view
	const view = new match.view();
	currentView = view;

	// set the html of the view element to the html of the view
	document.querySelector('#view').innerHTML = await view.getHtml();
	document.title = match.title; // set the title of the page
	
	// if the view has an init function, call it
	if (view.init)
		view.init();

	// document.querySelector('#counter').innerHTML = path;
};

// listen for back and forward button clicks and route to the correct page
window.addEventListener("popstate", router);

document.addEventListener('DOMContentLoaded', () => {
	// listen for clicks on html elements with nav-link property and navigate to them without refreshing
	document.body.addEventListener('click', event => {
		if (event.target.matches('[nav-link]')) {
			event.preventDefault(); // prevent page refresh
			if (event.target.href != document.URL) // only navigate if it goes to a new page
				navigateTo(event.target.href);
		}
	});
	router(); // route to page on load
});

// Create a parent element
const parentElement = document.querySelector('#app');

const elems = [];

const validRoutes = ['/', '/play', '/tournament', '/options', '/login'];
Object.entries(routes).forEach(([route, view]) => {
	if (validRoutes.includes(route)) {
		const link = document.createElement('a');
		link.href = view.path;
		link.classList.add('nav-link');
		link.setAttribute('nav-link', '');
		link.textContent = view.buttonText;
		elems.push(link);
	}
});

elems.forEach(elem => parentElement.insertBefore(elem, parentElement.querySelector('#view')));


// elems.push(document.querySelector('#counter'));


// setupCounter(document.querySelector('#counter'))
