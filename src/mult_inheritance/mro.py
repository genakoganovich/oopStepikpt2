class Radio:
    @staticmethod
    def play():
        return "Радио играет"

class Speaker:
    @staticmethod
    def play():
        return "Колонка играет"

class Boombox(Radio, Speaker):
    pass