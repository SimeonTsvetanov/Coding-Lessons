function browserHistory (object, commands) {
    // MasK - I don't think that comments are needed here!

    class Browser {
        constructor(name, openTabs, recentlyClosed, browserLogs) {
            this.name = name
            this.openTabs = openTabs;
            this.recentlyClosed = recentlyClosed;
            this.browserLogs = browserLogs;
        }

        openTab(tabName) {
            this.openTabs.push(tabName);
            this.browserLogs.push(`Open ${tabName}`);
        }

        closeTab(tabName) {
            if (this.openTabs.includes(tabName)) {
                this.openTabs.splice(this.openTabs.indexOf(tabName), 1);
                this.recentlyClosed.push(tabName);
                this.browserLogs.push(`Close ${tabName}`);
            }
        }

        clearHistory() {
            this.openTabs = [];
            this.recentlyClosed = [];
            this.browserLogs = [];
        }

        print() {
            let result = '';

            result += `${this.name}\n`;
            result += `Open Tabs: ${this.openTabs.join(', ')}\n`;
            result += `Recently Closed: ${this.recentlyClosed.join(', ')}\n`;
            result += `Browser Logs: ${this.browserLogs.join(', ')}\n`;

            return result
        }
    }

    let browser = new Browser(object['Browser Name'], object['Open Tabs'], object['Recently Closed'], object['Browser Logs']);

    commands.forEach(command => {
        let action = command.split(' ')[0];
        let tab = command.split(' ')[1];

        if (command === 'Clear History and Cache') {
            browser.clearHistory();
        } else if (action === 'Open') {
            browser.openTab(tab);
        } else if (action === 'Close') {
            browser.closeTab(tab);
        }
    });

    console.log(browser.print());
}

browserHistory({"Browser Name":"Google Chrome","Open Tabs":["Facebook","YouTube","Google Translate"],
        "Recently Closed":["Yahoo","Gmail"],
        "Browser Logs":["Open YouTube","Open Yahoo","Open Google Translate","Close Yahoo","Open Gmail","Close Gmail","Open Facebook"]},
    ["Close Facebook", "Open StackOverFlow", "Open Google"]
);

// Google Chrome
// Open Tabs: YouTube, Google Translate, StackOverFlow, Google
// Recently Closed: Yahoo, Gmail, Facebook
// Browser Logs: Open YouTube, Open Yahoo, Open Google Translate, Close Yahoo, Open Gmail, Close Gmail, Open Facebook, Close Facebook, Open StackOverFlow, Open Google
