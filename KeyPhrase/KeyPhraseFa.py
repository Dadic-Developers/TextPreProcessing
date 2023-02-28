from typing import List
import flair
import numpy
from flair.models import SequenceTagger
from flair.tokenization import SegtokSentenceSplitter
from keyphrase_vectorizers import KeyphraseCountVectorizer

from KeyPhrase.postagger_persian import POSTager

tagger = SequenceTagger.load('hamedkhaledi/persain-flair-upos')#hamedkhaledi/persain-flair-pos
splitter = SegtokSentenceSplitter()
class KeyPhrases:
    
    def __init__(self):
        
        self.__persian_stop_words=numpy.loadtxt('/media/daadik/Local Disk/backend/TextPreProcessing/Data/stopwords.dat', dtype=str)
                # define flair POS-tagger and splitter
        

    def findKeyPhrase(self,docs,pos_pattern="<ADJ.*>*<N.*>+"):
    
        # define custom POS-tagger function using flair
        def custom_pos_taggers(raw_documents: List[str], tagger: flair.models.SequenceTagger = tagger, splitter: flair.tokenization.SegtokSentenceSplitter = splitter)->List[tuple]:
             
            # check that the custom POS-tagger function returns a list of (word token, POS-tag) tuples
            postag= POSTager()
            custom_pos_tagger=(postag.findPostagger(docs))
            return custom_pos_tagger
        print (custom_pos_taggers(raw_documents=docs))
        
        # use custom POS-tagger with KeyphraseVectorizers
        vectorizer = KeyphraseCountVectorizer(custom_pos_tagger= custom_pos_taggers,pos_pattern=pos_pattern, stop_words=self.__persian_stop_words)
        vectorizer.fit(docs)
        keyphrases = vectorizer.get_feature_names_out()
        return(keyphrases)


    



if __name__ == "__main__":
    docs=[
    "آئین نامه اجرایی بند الف و ب ماده ۴۹ برنامه سوم و تعریف کارفرما و نیروی کار جدید و معافیت‌های بیمه و مالیات حقوق",
    "هیات وزیران در جلسه مورخ ۱۵ / ۲ / ۱۳۸۱ بنا به پیشنهاد مشترک وزارت خانه‌های کار و امور اجتماعی، وزارت تعاون، سازمان مدیریت و برنامه‌ریزی کشور وسازمان تامین اجتماعی و به استناد ماده (۴۹) قانون برنامه سوم توسعه اقتصادی، اجتماعی و فرهنگی جمهوری اسلامی ایران مصوب ۱۳۷۹ - آئین نامه اجرایی بندهای (الف) و (ب) ماده یادشده‌را به شرح زیر تصویب نمود: ((آئین نامه اجرایی بندهای (الف) و (ب) ماده (۴۹) قانون برنامه سوم توسعه اقتصادی، اجتماعی و فرهنگی جمهوری اسلامی ایران)) ماده ۱ - تعاریف: الف - کارفرما شخصی است که در ماده (۳) قانون کار جمهوری اسلامی ایران تعریف‌شده‌و اداره کارگاه‌ها و موسسات موضوع این آئین نامه را بر عهده دارد",
    " ب - نیروی کار جدید به کسی اطلاق می‌شود که کار فرما علاوه بر نیروی کار موجود، از بیکاران ثبت نام‌شده نزد ادارات کار و امور اجتماعی است خدام نماید",
    " تبصره در مواردی که نیروی کار جدید به جای نیروی کار موجود که اخراج، مستعفی را ترک کار نموده‌اند در کارگاه‌های موضوع‌بند (ج) ماده (۱) آئین نامه به کار گمارده شوند، کارفرما مشمول استفاده از تخفیفات مندرج در این آئین نامه نخواهدبود",
    " ح - کارگاه‌ها و موسسات مشمول این آئین نامه، کارگاه‌های خصوصی و تعاونی دایر موضوع ماده (۴) قانون کار و یا کارگاه‌هایی که از مراجع رسمی دارای مجوز فعالیت هستند می‌باشند",
    " ماده ۲ - کارفرمایان کارگاه‌ها و موسسات موضوع‌بند (ج) ماده (۱) این آئین نامه که پس از اعلام نیاز به ادارات کار و امور اجتماعی، فرد یا افراد مورد نظر را از بین نیروهای کار ثبت نام‌شده ادارات کار و امور اجتماعی انتخاب و به کار گمارند، برای استفاده از تخفیفات موضوع این آئین نامه مکلفند مراتب به کار آماری Merg"
    ]
    # docs=[".به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و صنعت ایران آغاز به کا  کرد","تمام ایران یک تابستان تنوری را تجربه میکند ."]
    # key Phrase
    keyphrase=KeyPhrases()
    keywords=keyphrase.findKeyPhrase(docs=docs,pos_pattern="<ADJ.*>*<N.*>+")
    print(keywords)


   





