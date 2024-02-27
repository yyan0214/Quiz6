from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[INFO] {message}")

class FileLogger(Logger):
    def log(self, message):
        with open("app.log", "a") as f:
            f.write(f"[INFO] {message}\n")

class LoggerFactory:
    @staticmethod
    def create_logger(logger_type):
        if logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "file":
            return FileLogger()
        else:
            raise ValueError("Invalid logger type")

class App:
    def __init__(self, logger):
        self.logger = logger

    def do_something(self):
        # Some application logic
        self.logger.log("Doing something...")

def main():
    # Dummy data
    logger_type = "file"

    # Create logger dynamically
    logger = LoggerFactory.create_logger(logger_type)

    # Create application with logger
    app = App(logger)

    # Perform application actions
    app.do_something()

if __name__ == "__main__":
    main()
