
try :
    word = open('hell.txt',"r")
    hello=word.read()
    print(hello)
    word.close()
except:
    print("File not found")


