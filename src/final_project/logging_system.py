from abc import ABC, abstractmethod
from datetime import datetime


class Handler(ABC):
    @abstractmethod
    def emit(self, message: str):
        pass


class ConsoleHandler(Handler):
    def emit(self, message: str):
        print(message)


class FileHandler(Handler):
    def emit(self, message: str):
        return f"Запись в файл: {message}"


class TimeMixin:
    def format_with_timestamp(self, message: str):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"[{now}] [{message}]"


class Logger(TimeMixin):
    def __init__(self, handlers: list):
        self._handlers = handlers

    def log(self, message: str):
        formated_message = self.format_with_timestamp(message)
        for handler in self._handlers:
            handler.emit(formated_message)

    def __call__(self, message: str):
        self.log(message)
