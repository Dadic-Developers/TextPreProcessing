from parsivar import Normalizer
from printPersianText import Converter


class ParivarNormalizer:


    def __init__(self) :
        self.__normalizer = Normalizer()
        self.__converter=Converter()
    def normalize_characters(self,str):
        new_text=self.__normalizer.normalize(str)
        # print(self.__converter.showText(new_text))
        return (new_text)
if __name__ == "__main__":
    normalize = ParivarNormalizer()
    text = """
            <p>
            دادماتولز اولین نسخش سال 1400/4/4 منتشر شده. 
            امیدواریم که این تولز بتونه کار با متن رو براتون شیرین‌تر و راحت‌تر کنه
            لطفا با ایمیل dadmatools@dadmatech.ir با ما در ارتباط باشید
            آدرس گیت‌هاب هم که خب معرف حضور مبارک هست:
            https://github.com/Dadmatech/DadmaTools
            </p>
            """
    normalize.normalize_characters(text)