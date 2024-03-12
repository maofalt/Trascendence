import { createElement } from "@utils/createElement";
import { htmlToElement } from "@utils/htmlToElement";
import styles from '@css/InputAugmented.css?raw';
import AbstractComponent from '@components/AbstractComponent';
import WarnIndicator from "./WarnIndicator";
import InputField from "./InputField";
import CustomButton from "./CustomButton";

export default class InputAugmented extends AbstractComponent {
	constructor(options = {}) {
		super();

		const styleEl = document.createElement('style');
		styleEl.textContent = styles;

		this.shadowRoot.appendChild(styleEl);

		// let	indicators = [];
		const title = document.createElement('p');
		title.id = "input-title";
		title.textContent = options.title ? options.title : "Input title";
		title.style.setProperty("font-family", "tk-421, Anta, sans-serif");
		title.style.setProperty("font-size", "26px");
		title.style.setProperty("margin", "0px 0px 10px 0px");
		this.shadowRoot.appendChild(title);
		
		this.input = new InputField({type: options.type, content: options.content});
		this.input.id = "input-field";
		this.input.style.setProperty("marin-bottom", "0px");
		this.shadowRoot.appendChild(this.input);
		
		let indicatorsBox = document.createElement('div');
		indicatorsBox.id = "indicators-box";
		indicatorsBox.style.setProperty("display", "flex");
		indicatorsBox.style.setProperty("flex-direction", "column");
		indicatorsBox.style.setProperty("align-items", "flex-start");
		indicatorsBox.style.setProperty("width", "100%");
		indicatorsBox.style.setProperty("height", "50px");
		
		this.indicators = {};
		if (options.indicators) {
			Object.entries(options.indicators).forEach(([key, value]) => {
				let indicator = new WarnIndicator({content: value});
				indicator.id = value.replaceAll(' ', '-');
				// indicators.push(indicator);
				this.indicators[key] = indicator;
				indicatorsBox.appendChild(indicator);
			});
			this.shadowRoot.appendChild(indicatorsBox);
		}

		if (options.description) {
			this.description = document.createElement("p");
			this.description.textContent = options.description;
			this.description.style.setProperty("font-family", "Anta, sans-serif");
			this.description.style.setProperty("font-size", "14px");
			this.description.style.setProperty("margin-top", "-3px");
			this.shadowRoot.appendChild(this.description);
		}

		if (options.button) {
			this.button = new CustomButton({content : options.button.content, action: options.button.action});
			this.shadowRoot.appendChild(this.button);
		}
		
		this.style.setProperty("height", "145px");
		this.style.setProperty("margin", "0px 0px 20px 0px");
		if (options.style) {
			for (const [key, value] of Object.entries(options.style)) {
				console.log(key);
				console.log(value);
				this.shadowRoot.host.style.setProperty(key, value);
			}
		}

	}

	// Implement other methods or properties as needed
}

customElements.define('input-augmented', InputAugmented);