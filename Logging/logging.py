# Suppose you're building a logging library for a web application that needs to keep track of all requests and
# responses. You want to use the Singleton pattern to ensure that there's only one instance of the logger class
# throughout the application.


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        print("Logging", message)


class IncorrectLogger:
    def log(self, message):
        print("Incorrect Logging", message)


logger1 = Logger()
logger1.log("Request 1")
logger2 = Logger()
logger2.log("Request 2")
logger3 = IncorrectLogger()
logger3.log("Request 3")
logger4 = IncorrectLogger()
logger4.log("Request 4")

print(logger1 is logger2)
print(logger3 is logger4)
