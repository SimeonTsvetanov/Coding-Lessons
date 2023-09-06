function browserHistory (object, commands) {
    // MasK --> First Solution using Class. Second solution is down below !
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


function mask (browser, commands) {
    // MASK -> Second Solution. Short but ugly!

    commands.forEach(data => {
        data = data.split(' ');
        let command = data.shift();
        let tab = data.join(' ');
        if (command === 'Open') {
            // Open tab
            browser["Open Tabs"].push(tab);
            browser["Browser Logs"].push(`Open ${tab}`);
        } else if (command === 'Close') {
            // Close tab
            if (browser["Open Tabs"].includes(tab)) {
                let tabIndex = browser["Open Tabs"].indexOf(tab);
                browser["Open Tabs"].splice(tabIndex, 1);
                browser["Recently Closed"].push(tab);
                browser["Browser Logs"].push(`Close ${tab}`);
            }
        } else if (command === 'Clear') {
            // Clear History and Cache
            browser["Open Tabs"] = [];
            browser["Recently Closed"] = [];
            browser["Browser Logs"] = [];
        }
    });

    console.log(browser["Browser Name"]);
    console.log(`Open Tabs: ${browser["Open Tabs"].join(', ')}`);
    console.log(`Recently Closed: ${browser["Recently Closed"].join(', ')}`);
    console.log(`Browser Logs: ${browser["Browser Logs"].join(', ')}`);
}

mask({"Browser Name":"Google Chrome","Open Tabs":["Facebook","YouTube","Google Translate"],
 "Recently Closed":["Yahoo","Gmail"],
 "Browser Logs":["Open YouTube","Open Yahoo","Open Google Translate","Close Yahoo","Open Gmail","Close Gmail","Open Facebook"]},
    ["Close Facebook", "Open StackOverFlow", "Open Google"]);
// Google Chrome
// Open Tabs: YouTube, Google Translate,
// StackOverFlow, Google
// Recently Closed: Yahoo, Gmail, Facebook
// Browser Logs: Open YouTube, Open Yahoo,
// Open Google Translate, Close Yahoo, Open
// Gmail, Close Gmail, Open Facebook, Close
// Facebook, Open StackOverFlow, Open Google

console.log('-------------------------------------');

mask({"Browser Name":"Mozilla Firefox",
 "Open Tabs":["YouTube"],
 "Recently Closed":["Gmail", "Dropbox"],
 "Browser Logs":["Open Gmail", "Close Gmail", "Open Dropbox", "Open YouTube", "Close Dropbox"]},
 ["Open Wikipedia", "Clear History and Cache", "Open Twitter"]);
// Mozilla Firefox
// Open Tabs: Twitter
// Recently Closed:
// Browser Logs: Open Twitter
