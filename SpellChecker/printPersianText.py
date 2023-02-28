import arabic_reshaper
from bidi.algorithm import get_display

class Converter:

    def showText(self,text):
        reshaped_text = arabic_reshaper.reshape(text)
        converted = get_display(reshaped_text)
        return converted
# Driver program
if __name__ == "__main__":
    converter= Converter()
    sentence = "این سمینار تا ۱۲ شهرییییور ادامه می یابد"
    print(sentence)