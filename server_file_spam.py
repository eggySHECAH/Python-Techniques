# A file spammer
class Filegen:
  def __init__(self, file: int):
    self.text = file
    self.file = open(self.text, 'w')
    self.file.write("Hello!")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ә', 'б', 'в', 'г', 'ғ', 'д', 'ё', 'ж', 'з', 'и', 'й', 'к', 'қ', 'л', 'м', 'н']
for letter in letters:
    try:
      text = letter
      while True:
        fg = Filegen(text)
        text += letter
        print(letter)
    except:
      continue
