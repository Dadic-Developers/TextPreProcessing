import re

class Remover:
    def __init__(self) -> None:

        pass
    def removeDupWithOrder(self,str): 
        DuplicatCharRegex = re.compile(r'[^\w\s\!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]|(.)(?=\1)')
        new_str = re.sub(DuplicatCharRegex,'',str) 
        # print(showText(new_str))
        return(new_str)

# Driver program
if __name__ == "__main__":
    removeChar= Remover()
    sentence = "این سمینار تا 1200/2/2 شهرییییور ادامه می یابد"
    print(removeChar.removeDupWithOrder(sentence))
