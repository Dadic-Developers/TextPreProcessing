from flair.data import Sentence
from flair.models import SequenceTagger
from typing import List


class POSTager:
    def __init__(self):
         self.__tagger = SequenceTagger.load("hamedkhaledi/persain-flair-upos")
    def findPostagger(self,docs):
        # load tagger
       
        custom_pos_tagger=[]
        # make example sentence
        for doc in docs:
            sentence = Sentence(doc)

            self.__tagger.predict(sentence)
            new_sentence=(sentence.to_tagged_string().split('→')[1])
            new_sentence=new_sentence.replace("[","").replace(']','')
            new_sentence=new_sentence.split(",")
            
            # print(new_sentence.split(","))
            # #print result
            # # print(sentence.to_tagged_string().split('→')[1])
            # pos_list=list(sentence.to_tagged_string().split('→')[1])
            # print(pos_list) 
            for items in new_sentence:
                item=items.replace("\"","")
                # print(items.replace("\"",""))
                custom_pos_tagger.append((item.split('/')[0], item.split('/')[1]))
            # #     # pos.append(zip(item.split('/')[0], item.split('/')[1]))
            return(custom_pos_tagger)
# Driver program
if __name__ == "__main__":
    docs=[
    "آئین نامه اجرایی بند الف و ب ماده ۴۹ برنامه سوم و تعریف کارفرما و نیروی کار جدید و معافیت‌های بیمه و مالیات حقوق",
    "هیات وزیران در جلسه مورخ ۱۵ / ۲ / ۱۳۸۱ بنا به پیشنهاد مشترک وزارت خانه‌های کار و امور اجتماعی، وزارت تعاون، سازمان مدیریت و برنامه‌ریزی کشور وسازمان تامین اجتماعی و به استناد ماده (۴۹) قانون برنامه سوم توسعه اقتصادی، اجتماعی و فرهنگی جمهوری اسلامی ایران مصوب ۱۳۷۹ - آئین نامه اجرایی بندهای (الف) و (ب) ماده یادشده‌را به شرح زیر تصویب نمود: ((آئین نامه اجرایی بندهای (الف) و (ب) ماده (۴۹) قانون برنامه سوم توسعه اقتصادی، اجتماعی و فرهنگی جمهوری اسلامی ایران)) ماده ۱ - تعاریف: الف - کارفرما شخصی است که در ماده (۳) قانون کار جمهوری اسلامی ایران تعریف‌شده‌و اداره کارگاه‌ها و موسسات موضوع این آئین نامه را بر عهده دارد",
    " ب - نیروی کار جدید به کسی اطلاق می‌شود که کار فرما علاوه بر نیروی کار موجود، از بیکاران ثبت نام‌شده نزد ادارات کار و امور اجتماعی است خدام نماید",
    " تبصره در مواردی که نیروی کار جدید به جای نیروی کار موجود که اخراج، مستعفی را ترک کار نموده‌اند در کارگاه‌های موضوع‌بند (ج) ماده (۱) آئین نامه به کار گمارده شوند، کارفرما مشمول استفاده از تخفیفات مندرج در این آئین نامه نخواهدبود",
    " ح - کارگاه‌ها و موسسات مشمول این آئین نامه، کارگاه‌های خصوصی و تعاونی دایر موضوع ماده (۴) قانون کار و یا کارگاه‌هایی که از مراجع رسمی دارای مجوز فعالیت هستند می‌باشند",
    " ماده ۲ - کارفرمایان کارگاه‌ها و موسسات موضوع‌بند (ج) ماده (۱) این آئین نامه که پس از اعلام نیاز به ادارات کار و امور اجتماعی، فرد یا افراد مورد نظر را از بین نیروهای کار ثبت نام‌شده ادارات کار و امور اجتماعی انتخاب و به کار گمارند، برای استفاده از تخفیفات موضوع این آئین نامه مکلفند مراتب به کار آماری Merg"
    ]
    # docs=[".به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و صنعت ایران آغاز به کار کرد","تمام ایران یک تابستان تنوری را تجربه میکند ."]
    # pos tagger 
    postag= POSTager()
    custom_pos_tagger=(postag.findPostagger(docs))
   

    print(custom_pos_tagger)




