class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = False if self.is_on else True

    def install(self, app, memory):
        message = ""
        if self.memory >= memory and self.is_on:
            self.apps.append(app)
            self.memory -= memory
            message = f"Installing {app}"
        elif self.memory >= memory and not self.is_on:
            message = f"Turn on your phone to install {app}"
        else:
            message = f"Not enough memory to install {app}"
        return message

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
