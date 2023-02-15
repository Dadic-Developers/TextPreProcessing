from parsivar import SpellCheck

from printPersianText import Converter

class SpellChecker:
    def __init__(self):
        # self.__converter=Converter()
        self.__spell_checker=SpellCheck()
    def spell_correcter(self,str):

        new_str = self.__spell_checker.spell_corrector(str)
        # print(self.__converter.showText(new_str))
        return new_str
# Driver program
if __name__ == "__main__":
    converter= Converter()
    spell=SpellChecker()
    sentence = "این صمینار د ر دانشکاه غلم و سنعت  تا 1400/4/4 شهرییییور ادامه می یابد"
    print(converter.showText(  spell.spell_correcter(sentence)))