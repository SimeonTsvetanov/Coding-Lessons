function focus() {
    document.addEventListener('focus', function (e) {
        e.target.parentNode.className = 'focused';
    }, true);

    document.addEventListener('blur', function (e) {
        e.target.parentNode.className = '';
    }, true);
}
