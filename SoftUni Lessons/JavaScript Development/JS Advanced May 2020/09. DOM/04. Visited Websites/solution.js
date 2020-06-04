function solve() {
    // Collect all the Links in one place:
    let links = document.querySelectorAll('.link-1');

    // Iterate the links when the click event is triggered: 
    for (let i = 0; i < links.length; i++) {
        // Send the clicked link to our function:
        links[i].addEventListener("click", function() {
            countClicks(links[i]);
        })
    }

    function countClicks(link) {
        // Get the p element:
        let p = link.lastElementChild;
        // Increment its value with 1:
        p.innerText = `visited ${Number(p.innerText[8]) + 1} times`;
    }
}
