import datetime

class Logger:
    LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    def __init__(self, level='INFO'):
        if level not in self.LEVELS:
            raise ValueError("Invalid logging level")
        self.level = level

    def log(self, level, message):
        if self.LEVELS.index(level) >= self.LEVELS.index(self.level):
            print(f"{datetime.datetime.now()} - {level} - {message}")

    def debug(self, message):
        self.log('DEBUG', message)

    def info(self, message):
        self.log('INFO', message)

    def warning(self, message):
        self.log('WARNING', message)

    def error(self, message):
        self.log('ERROR', message)

    def critical(self, message):
        self.log('CRITICAL', message)
