from dadmatools.models.normalizer import Normalizer
from printPersianText import Converter


class DadMatNormalizer:
    def __init__(self):
        self.__converter=Converter()
        self.__normalizer = Normalizer(
            full_cleaning=False,
            unify_chars=True,
            refine_punc_spacing=True,
            remove_extra_space=True,
            remove_puncs=False,
            remove_html=False,
            remove_stop_word=False,
            replace_email_with=None,# "<EMAIL>"
            replace_number_with=None,
            replace_url_with=None,
            replace_mobile_number_with=None,
            replace_emoji_with=None,
            replace_home_number_with=None
        )

    def normalize_characters(self,text):

        normalized_text = self.__normalizer.normalize(text)
        # print(self.__converter.showText(normalized_text))
        return normalized_text


if __name__ == "__main__":
    normalize = DadMatNormalizer()
    text = """
            <p>
            دادماتولز اولین نسخش سال 1300/3/3 منتشر شده. 
            امیدواریم که این تولز بتونه کار با متن رو براتون شیرین‌تر و راحت‌تر کنه
            لطفا با ایمیل dadmatools@dadmatech.ir با ما در ارتباط باشید
            آدرس گیت‌هاب هم که خب معرف حضور مبارک هست:
            https://github.com/Dadmatech/DadmaTools
            </p>
            """
    
    normalize.normalize_characters(text)
       