function createArticle() {
	// Get the Input Fields
	const heading = document.getElementById('createTitle');
	const text = document.getElementById('createContent');
	
	// Get the Are to Display the Articles:
	const articles = document.getElementById('articles');

	// Create the new Elements that we are going to add in the future:
	const article = document.createElement('article');
	const h3 = document.createElement('h3');
	const p = document.createElement('p');
	
	// Check if we have input:
	if (heading.value !== '' && text.value !== '') {
		// If we do we will assighn the value to the new elements
		h3.innerText = heading.value;
		p.innerText = text.value;

		// Append the heading and the paragraph t the article:
		article.appendChild(h3);
		article.appendChild(p);

		// Append the article to the articles Section:
		articles.appendChild(article);
	}

	// Clear the values of the input fields:
	heading.value = '';
	text.value = '';
}
