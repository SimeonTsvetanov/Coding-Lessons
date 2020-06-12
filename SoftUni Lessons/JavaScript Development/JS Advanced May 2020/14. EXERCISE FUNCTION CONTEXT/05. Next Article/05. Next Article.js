function getArticleGenerator(articles) {
    const content = document.querySelector('#content');
    
    function showNext() {
        const article = document.createElement('article');
        if (articles.length === 0) { return; }
        article.textContent = articles.shift();
        content.appendChild(article);
    }

    return showNext; 
}