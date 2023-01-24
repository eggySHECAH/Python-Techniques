# spams text onto a specific file
class Spam:
    def __init__(self, file: str, text: str):
        self.f = file
        self.t = text
        self.file = open(self.f, 'w')
        while True:
            self.file.write(self.t)

s = Spam('demo_file.rtf', 'Lorem ipsum sit dolor amet... ')
