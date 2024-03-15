// Router.js
import Home from '@views/Home.js';
import Tournament from '@views/Tournament.js';
import Options from '@views/Options.js';
import Game from '@views/Game.js';
import Login from '@views/Login.js';
import NotFound from '@views/NotFound.js';
import CreateTournament from '@views/CreateTournament.js';
import ProfilePage from '@components/ProfilePage.js';
import SpaceBackground from '../components/SpaceBackground';
import User from '@views/User';
import Design from '@views/Design.js';
import BasicGame from '@views/BasicGame.js';
import TwoFactorAuth from '@views/2fa';
import Signup from '@views/Signup.js';
import EditProfile from '@components/EditProfile';
import LoginUserProfile from '@views/LoginUserProfile';

export const routes = {
	'/': {
		path: '/',
		component: 'home-page',
		title: 'Pongiverse',
		buttonText: 'Home'
	},
	'/space-background': {
		path: '/space-background',
		component: 'space-background',
		title: 'Space Background',
		buttonText: 'Space Background'
	},
	'/play': {
		path: '/play',
		view: Game,
		title: 'Game',
		buttonText: 'Play'
	},
	'/game': {
		path: '/game',
		component: 'play-menu',
		title: 'Game',
		buttonText: 'Game'
	},
	'/profile': {
		path: '/profile',
		component: 'profile-page',
		title: 'Profile',
		buttonText: 'Profile',
	},
	'/edit-profile': {
		path: '/edit-profile',
		component: 'edit-profile',
		title: 'Edit Profile',
		buttonText: 'Edit Profile',
	},
	'/tournament': {
		path: '/tournament',
		view: Tournament,
		title: 'Tournament',
		buttonText: 'Tournament'
	},
	'/create-tournament': {
		path: '/create-tournament',
		view: CreateTournament,
		title: 'Tournament Creation',
		buttonText: 'Create Tournament'
	},
	'/options': {
		path: '/options',
		view: Options,
		title: 'Options',
		buttonText: 'Options'
	},
	'/login': {
		path: '/login',
		component: 'login-page-v2',
		title: 'Login',
		buttonText: 'Login'
	},
	'/signup-old': {
		path: '/signup-old',
		component: 'signup-page-v2',
		title: 'Signup',
		buttonText: 'Signup'
	},
	'/signup': {
		path: '/signup',
		component: 'signup-page',
		title: 'Signup',
		buttonText: 'Signup'
	},
	'/forgot_password': {
		path: '/forgot_password',
		component: 'forgot-password',
		title: 'Forgot Password',
		buttonText: 'Forgot Password'
	},
	'/2fa': {
		path: '/2fa',
		component: 'two-factor-auth',
		title: 'Two Factor Authentication',
		buttonText: '2FA'
	},
	'/user': {
		path: '/user',
		view: User,
		title: 'Profile Page',
		buttonText: 'Profile'
	},
	'/design': {
		path: '/design',
		view: Design,
		title: 'Design',
		buttonText: 'Design',
		component: 'design-page'
	},
	'/basic': {
		path: '/basic',
		view: BasicGame,
		title: 'Basic Game',
		buttonText: 'Basic',
		component: 'basic-game'
	},
	'/404': {
		path: '/404',
		view: NotFound,
		title: '404 Not Found',
		buttonText: 'Not Found Page'
	}
	// '/profile': {
	// 	path: '/profile',
	// 	component: 'profile-page',
	// 	title: 'ProfilePage',
	// }
};

let currentView = null;

export const navigateTo = (url) => {
  history.pushState(null, null, url);
  console.log('url: ', url);
  router();
};

const router = async () => {
  const path = window.location.pathname;
  const View = routes[path] || routes['/404'];
  const viewContainer = document.querySelector('#view');

  if (View.component) {
	viewContainer.innerHTML = `
		<${View.component}></${View.component}>`;
  } else {
	console.log('path: ', path);

	if (currentView && currentView.destroy && currentView !== View) {
		currentView.destroy();
	}

	currentView = new View.view();

	document.querySelector('#view').innerHTML = await currentView.getHtml();
	document.title = View.title;
    if (currentView.init) {
        currentView.init();
    }
  }
};

window.addEventListener("popstate", router);

document.addEventListener('DOMContentLoaded', () => {
  router();
});

// const background = new SpaceBackground();

// document.querySelector('#app').appendChild(background);
// background.shadowRoot.style.setProperty("position", "absolute");
// background.shadowRoot.style.setProperty("top", "0px");
// background.shadowRoot.style.setProperty("left", "0px");
// background.shadowRoot.style.setProperty("border", "3px red solid");

export default { routes, navigateTo, router };
