from Lexer.readfile import read_file
from Lexer.lexer import getWords, get_tokens
  
file = read_file("code.jp")
# print(file)
words = getWords(file)
# print(words)
tokens = get_tokens(words)
for token in tokens:
    print(token)

