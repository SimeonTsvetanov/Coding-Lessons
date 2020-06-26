// First is the short version and second is the same task but easier on the eyes:
// Short link: https://git.io/Jfjje
function solve() {
    let openMenu = document.querySelectorAll('section').item(1).lastElementChild;
    let inProgressMenu = document.querySelectorAll('section').item(2).lastElementChild;
    let completeMenu = document.querySelectorAll('section').item(3).lastElementChild;
    document.querySelector('#add').addEventListener('click', mask);
    function mask(e) {
        e.preventDefault();
        let titleField = document.querySelector("#task");
        let descField = document.querySelector('#description');
        let dateField = document.querySelector('#date');
        let title = titleField.value; let desc = descField.value; let date = dateField.value;
        if (!(title && desc && date)) { return; }
        let task = document.createElement('article');
        task.innerHTML = `<h3>${title}</h3><p>Description: ${desc}</p><p>Due Date: ${date}</p><div class="flex"><button class="green">Start</button><button class="red">Delete</button></div>`;
        task.addEventListener('click', (e) => {
            if (e.target.textContent === 'Start') {
                task.querySelector('.flex').removeChild(task.querySelector('.green'));
                let finishBtn = document.createElement('button');
                finishBtn.classList.add('orange');
                finishBtn.textContent = 'Finish';
                task.querySelector('.flex').appendChild(finishBtn);
                inProgressMenu.appendChild(task);
            } else if (e.target.textContent === 'Delete') {
                task.parentElement.removeChild(task);
            } else if (e.target.textContent === 'Finish') {
                task.removeChild(task.lastElementChild);
                completeMenu.appendChild(task);
            }
        });
        openMenu.appendChild(task);
        titleField.value = ''; descField.value = ''; dateField.value = '';
    }
}


function solveLongerButBetterVersion() {
    // Get the Add button;
    let addButton = document.getElementById('add');

    // Add the event listener to the Add Button:
    addButton.addEventListener("click", add);

    function add(e) {
        e.preventDefault();  // needed for easy debugging
        let addMenu = e.target.parentElement;  // Get the Parent Element;
        let task = document.querySelector('#task');  // Task Input Area
        let description = document.querySelector('#description');  // Dec. input Area
        let date = document.querySelector('#date');  // Date Input Area
        // If any of the input fields is empty, the function doesn’t make anything
        if (!(task.value && description.value && date.value)) {
            return;
        }

        /*
        We can do the next part using Inner HTML But the eventListeners will be hard to apply:
        newTask.innerHTML = `<h3>${task.value}</h3><p>Description: ${description.value}</p><p>Due Date: ${date.value}</p><div class="flex"><button class="green">Start</button><button class="red">Delete</button></div>`;
        If we add it in ths way we will need to set event listeners in a diff. way.
        */

        // Lets Create the task:
        let article = document.createElement('article');
        // Create All the Features for the article.
        // Title
        let h3Task = document.createElement('h3');
        h3Task.textContent = task.value;
        // Description
        let pDescription = document.createElement('p');
        pDescription.textContent = `Description: ${description.value}`;
        // Date
        let pDate = document.createElement('p');
        pDate.textContent = `Due Date: ${date.value}`;
        // Div for the buttons
        let divButtons = document.createElement('div');
        divButtons.classList.add('flex');
        // Start Button
        let startButton = document.createElement("button");
        startButton.classList.add('green');
        startButton.textContent = 'Start';
        startButton.addEventListener('click', start);
        // Delete Button
        let deleteButton = document.createElement('button');
        deleteButton.classList.add('red');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', del);

        // Add All the features to the Article:
        divButtons.appendChild(startButton);
        divButtons.appendChild(deleteButton);
        article.appendChild(h3Task);
        article.appendChild(pDescription);
        article.appendChild(pDate);
        article.appendChild(divButtons);

        // Get the Open tasks menu:
        let openTasksMenu = document.querySelectorAll("section")[1].children[1];
        // And Append it to the OpenTaskMenuMenu:
        openTasksMenu.appendChild(article);
        // Clear the Add menu Data:
        task.value = ''; description.value = ''; date.value = '';
    }

    function start(e) {
        let inProgressMenu = document.querySelectorAll("section")[2].children[1]; // Get the whole menu
        let wholeArticle = e.target.parentNode.parentNode;  // Get the selected Article
        wholeArticle.querySelector("button").remove();  // Remove the Start Button

        let finishButton = document.createElement("button");  // Crete the finish button
        finishButton.classList.add("orange");  // Add the class orange to it
        finishButton.textContent = "Finish";  // Add the text Finish
        finishButton.addEventListener("click", finish);  // set the onclick function
        wholeArticle.querySelector(".flex").appendChild(finishButton); // add the button to the article
        inProgressMenu.appendChild(wholeArticle);  // ad the article to the menu
    }

    function del(e) {
        let wholeArticle = e.target.parentNode.parentNode;  // Get the selected article
        wholeArticle.remove(); // And Remove it.
    }

    function finish(e) {
        let wholeArticle = e.target.parentNode.parentNode; // Get the selected Article
        let completeMenu = document.querySelectorAll("section")[3].children[1];  // Get the menu
        wholeArticle.querySelector("button").parentElement.remove();  // Remove the buttons
        wholeArticle.remove();  // Remove the article from the current position
        completeMenu.appendChild(wholeArticle); // Place it in the Finish area
    }
}
