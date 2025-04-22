 import datetime

class Logger:
    LEVELS = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']

    def __init__(self, level='INFO'):
        if level not in self.LEVELS:
            raise ValueError("Invalid logging level")
        self.level = level

    def log(self, level, message):
        # Ensure the level is one of the defined levels
        if level not in self.LEVELS:
            raise ValueError("Invalid log level")
        
        # Only print messages of the correct level or higher
        if self.LEVELS.index(level) >= self.LEVELS.index(self.level):
            print(f"{datetime.datetime.now()} - {level} - {message}")

    def debug(self, message):
        self.log('DEBUG', message)

    def info(self, message):
        self.log('INFO', message)

    def warn(self, message):
        self.log('WARN', message)

    def error(self, message):
        self.log('ERROR', message)

    def fatal(self, message):
        self.log('FATAL', message)
