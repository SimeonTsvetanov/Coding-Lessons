class Forum {
    constructor() {
        this._users = [];
        this._questions = [];
        this._id = 1;
    }

    register(username, password, repeatPassword, email) {
        if (username === '' || password === '' || repeatPassword === '' || email === '') {
            throw new Error("Input can not be empty");
        } else if (password !== repeatPassword) {
            throw new Error("Passwords do not match");
        } else if (this._users.find(user => user.username === username)) {
            throw new Error("This user already exists!");
        }

        let user = {
            username: username,
            password: password,
            email: email,
            logged: false,
        };

        this._users.push(user);
        return `${username} with ${email} was registered successfully!`;
    }

    login(username, password) {
        let user = this._users.find(x => x.username === username);
        if (!user) { throw new Error("There is no such user"); }

        if (user.password === password) {
            user.logged = true;
            return `Hello! You have logged in successfully`;
        }
    }

    logout(username, password) {
        let user = this._users.find(x => x.username === username);
        if (!user) { throw new Error("There is no such user"); }

        if (user.password === password) {
            user.logged = false;
            return 'You have logged out successfully';
        }
    }

    postQuestion(username, questionContent) {
        let user = this._users.find(x => x.username === username);

        if ((!user) || (user.logged === false)) { throw new Error("You should be logged in to post questions"); }
        if (questionContent === '') { throw new Error("Invalid question"); }

        let question = {
            id: this._id,
            username: username,
            content: questionContent,
            answers: [],
        };

        this._questions.push(question);
        this._id += 1;
        return "Your question has been posted successfully";
    }

    postAnswer(username, questionId, answerContent) {
        let user = this._users.find(x => x.username === username);
        if ((!user) || (user.logged === false)) { throw new Error("You should be logged in to post answers"); }
        if (answerContent === '') { throw new Error("Invalid answer"); }
        let question = this._questions.find(x => x.id === questionId);
        if (!question) { throw new Error("There is no such question"); }

        let answer = {
            username: username,
            content: answerContent,
        };

        question.answers.push(answer);

        return "Your answer has been posted successfully";
    }

    showQuestions() {
        let result = '';
        this._questions.map(question => {
            result += `Question ${question.id} by ${question.username}: ${question.content}\n`;
            question.answers.map(answer => {
                result += `---${answer.username}: ${answer.content}\n`;
            });
        });
        return result.trim();
    }
}

let forum = new Forum();
forum.register('Jonny', '12345', '12345', 'jonny@abv.bg');
forum.register('Peter', '123ab7', '123ab7', 'peter@gmail@.com');
forum.login('Jonny', '12345');
forum.login('Peter', '123ab7');
forum.postQuestion('Jonny', "Do I need glasses for skiing?");
forum.postAnswer('Peter',1, "Yes, I have rented one last year.");
forum.postAnswer('Jonny',1, "What was your budget");
forum.postAnswer('Peter',1, "$50");
forum.postAnswer('Jonny',1, "Thank you :)");
console.log(forum.showQuestions());



