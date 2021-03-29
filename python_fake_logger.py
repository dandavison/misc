class logging:
    def getLogger(*args):
        return logger


class logger:
    def info(*args):
        print("INFO", *args)

    def error(*args):
        print("ERROR", *args)
