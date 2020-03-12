from analyzer import Analyzer
import sys

filePath = None

try:
    filePath = sys.argv[1]
except IndexError:
    print("Please enter the file path ex. python main.py 'test.c'")
    quit()

with open(filePath, 'r') as file:
    data = file.read()

analyzer = Analyzer()
tokens = analyzer.compile(data)
strTokens = ""

for token in tokens:
    strTokens += token.__str__() +"\n"



with open("o.txt", 'w') as file:
    data = file.write(strTokens)
print(strTokens)

