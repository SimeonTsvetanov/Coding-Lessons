function solve() {
    // Get the sections:
    let addTaskSection = document.querySelectorAll('section')[0].lastElementChild // Add Task
    let openTaskSection = document.querySelectorAll('section')[1].lastElementChild // Open Task
    let inProgressTaskSection = document.querySelectorAll('section')[2].lastElementChild // In Progress
    let completeTaskSection = document.querySelectorAll('section')[3].lastElementChild // Complete

    // Get the Task Input
    let taskNameField = document.querySelector('#task');
    let taskDecrField = document.querySelector('#description');
    let taskDateField = document.querySelector('#date');

    // Get the Add button:
    let addButton = document.querySelector("#add");

    // Create the Element when add is clicked:
    addButton.addEventListener('click', addTask);

    function addTask(e) {
        // Stop if from Reloading:
        e.preventDefault();

        // Validate the input:
        if (!(taskNameField.value && taskDecrField.value && taskDateField.value)) { return; }

        // Create the Element
        let article = l('article', [
            l('h3', taskNameField.value),
            l('p', `Description: ${taskDecrField.value}`),
            l('p', `Due Date: ${taskDateField.value}`),
            l('div', [
                l('button', 'Start', {class: 'green'}),
                l('button', 'Delete', {class: 'red'}),
            ], {class: 'flex'})
        ]);

        // Add the Event Listener on the Task:
        article.addEventListener('click', workOnArticle);

        // Append the Article to the Open Section:
        openTaskSection.appendChild(article);

        // Clear the input fields:
        taskNameField.value = ''; taskDecrField.value = ''; taskDateField.value = '';
    }

    function workOnArticle(e) {
        if (e.target.className === 'green') {
            // Clicked on start
            startTask(e);
        } else if (e.target.className === 'red') {
            // Clicked on Delete
            deleteTask(e);
        } else if (e.target.className === 'orange') {
            // Clicked on Finish
            finishTask(e);
        }
    }

    function startTask(e) {
        let task = e.target.parentElement.parentElement;

        // Change the Section
        inProgressTaskSection.appendChild(task);
        // Remove the Start Button
        let buttons = e.target.parentElement;
        let startButton = e.target.parentElement.firstElementChild;
        buttons.removeChild(startButton);

        // Add the Finish Button
        let finishButton = l('button', 'Finish', {class: 'orange'});
        buttons.appendChild(finishButton);
    }

    function deleteTask(e) {
        let section = e.target.parentElement.parentElement.parentElement;
        let task = e.target.parentElement.parentElement;
        section.removeChild(task);
    }

    function finishTask(e) {
        let task = e.target.parentElement.parentElement;
        completeTaskSection.appendChild(task);
        let buttons = e.target.parentElement;
        task.removeChild(buttons);
    }

    function l(type, content, ...attr) {
        // 'Type', 'content' / ['content', l(another)], - [{className: 'className', {id: 'idName'}]
        const r = document.createElement(type);
        attr !== undefined ? attr.forEach(x => {
            r.setAttribute(Object.keys(x)[0], Object.values(x)[0]);
        }) : 'pass';
        Array.isArray(content) ? content.forEach(append) : append(content);
        function append(node) {
            typeof node === 'string' ? node = document.createTextNode(node) : 'do nothing';
            r.appendChild(node);
        }
        return r
    }
}


