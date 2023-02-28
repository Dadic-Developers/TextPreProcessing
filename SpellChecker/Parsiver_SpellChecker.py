from parsivar import SpellCheck

from IO.printPersianText import Converter


class SpellChecker:
    def __init__(self):
        # self.__converter=Converter()
        self.__spell_checker=SpellCheck()
    def spell_Doc(self, doc):
        newDoc=""
        for sentence in doc.split('.'):
            newDoc += self.spell_correcter(sentence)
        return newDoc
    def spell_correcter(self,str):

        new_str = self.__spell_checker.spell_corrector(str)
        # print(self.__converter.showText(new_str))
        return new_str
# Driver program
if __name__ == "__main__":
    converter= Converter()
    spell=SpellChecker()
    doc = """
            هیأت وزیران در جلسه مورخ 15/2/1381 بنا به پیشنهاد مشترک وزارت خانه های کار وامور اجتماعی، وزارت تعاون، سازمان مدیریت وبرنامه ریزی کشوروسازمان تأمین اجتماعی وبه استناد ماده (49) قانون برنامه سوم توسعه اقتصادی، اجتماعی وفرهنگی جمهوری اسلامی ایران – مصوب 1379- آئین نامه اجرایی بندهای (الف) و(ب) ماده یاد شده را به شرح زیر تصویب نمود:




            ((آئین نامه اجرایی بندهای (الف) و(ب) ماده (49) قانون برنامه سوم توسعه
            اقتصادی، اجتماعی وفرهنگی جمهوری اسلامی ایران))

            ماده 1- تعاریف:
            الف- کارفرما شخصی است که در ماده (3) قانون کار جمهوری اسلامی ایران تعریف شده واداره کارگاه ها وموسسات موضوع این آئین نامه را بر عهده دارد.
            ب- نیروی کار جدید به کسی اطلاق می شود که کار فرما علاوه بر نیروی کار موجود، از بیکاران ثبت نام شده نزد ادارات کار وامور اجتماعی استخدام نماید.
            تبصره – در مواردی که نیروی کار جدید به جای نیروی کار موجود که اخراج، مستعفی یا ترک کار  نموده اند در کارگاه های موضوع بند (ج) ماده (1) آئین نامه به کار گمارده شوند، کارفرما مشمول استفاده از تخفیفات مندرج دراین آئین نامه نخواهد بود.
            ح- کارگاه ها وموسسات مشمول این آئین نامه، کارگاه های خصوصی وتعاونی دایر موضوع ماده (4) قانون کار ویا کارگاه هایی که از مراجع رسمی دارای مجوز فعالیت هستند می باشند.
            ماده 2- کارفرمایان کارگاه ها وموسسات موضوع بند (ج) ماده (1) این آئین نامه که پس از اعلام نیاز به ادارات کار وامور اجتماعی، فرد یا افراد مورد نظر را از بین نیروهای کار ثبت نام شده ادارات کار وامور اجتماعی انتخاب وبه کار گمارند، برای استفاده از تخفیفات موضوع این آئین نامه مکلفند مراتب به کار گماری آنا ن را به ادارات کار وامور اجتماعی اعلام نمایند.
            ماده 3- کلیه کارفرمایان پس از کسب تأییدیه استخدام نیروی کار جدید از سوی ادارات کار وامور اجتماعی وارائه آن به همراه صورت مزد وحقوق با رعایت تبصره بند (ب) ماده (1)، مشمول استفاده از تخفیفات موضوع ماده (4) این آئین نامه خواهند بود.
            ماده 4- کلیه کار فرمایان کارگاه ها وموسسات موضوع بند (ج) ماده (1) این آئین نامه از پرداخت مالیات بر حقوق کارکنان جدید الاستخدام علاوه بر نیروهای موجود و پرداخت حق بیمه سهم کار فرمای موضوع ماده (28) قانون تأمین اجتماعی بابت کارکنان مزبور، به میزان صددرصد (100%) معاف می باشند.
            تبصره 1- تخفیف حق بیمه موضوع این ماده شامل کارگاه های مشمول قانون معافیت از پرداخت حق بیمه سهم کارفرما تا میزان پنج نفر کارگر، موضوع تصویب نامه شماره 106254/ت /23/هـ مورخ 12/2/1369 هیأت وزیران نمی گردد وکارگاه های مذکور منحصرا از معافیت قانون مزبور برخوردار خواهند بود. اگر واحدهای مشمول    تصویب نامه مذکور نیروی کار جدید با رعایت سایر شرایط مندرج دراین آئین نامه به کار گیرند، می توانند از مزایای این آئین نامه برخوردار شوند.
            تبصره 2- مبنای تعیین تعداد نیروی کار موجود در کارگاه های دایر، تعداد بیمه شدگان آنها طبق صورت مزد وحقوق ارسالی توسط کارفرما در اسفند ماه 1380 به سازمان تأمین اجتماعی می باشد.
            تبصره 3- اعمال تخفیف موضوع این ماده در مورد افراد به کار گمارده شده جدید با رعایت تبصره (2) این ماده ومنوط به ارائه تأییدیه موضوع ماده (3) وارسال صورت مزد وحقوق کلیه کارکنان در مهلت مقرر به شعب سازمان تأمین اجتماعی وادارات امور اقتصادی ودارایی ذیربط می باشد.
            ماده 5- سازمان مدیریت وبرنامه ریزی کشور مکلف است اعتبار لازم برای اعمال تخفیفات حق بیمه سهم کارفرما برای سال های اجرای برنامه سوم توسعه به ازای فرصت های شغلی ایجاد شده در رابطه با این تصویب نامه را ازطریق منظور دادن در لوایح بودجه سنواتی تأمین وبه سازمان تأمین اجتماعی پرداخت نماید.
            تبصره 1- ادارات کل تأمین اجتماعی استان ها مکلفند در پایان هر ماه گزارش عملکرد شعب خودرا در زمینه به کار گماری نیروهای جدید موضوع این آئین نامه به ادارات کل کار وامور اجتماعی استان مربوط اعلام نمایند.
            تبصره 2- سازمان تأمین اجتماعی مکلف است هر سه ماه یکبار میزان تخفیف حق بیمه وتعداد افراد برخوردار شده از تخفیف را به سازمان مدیریت وبرنامه ریزی کشور، وزارت کار وامور اجتماعی ووزارت امور اقتصادی ودارایی اعلام نماید.
            ماده 6- اگر به طریقی محرز گردد که نیروی کار جدید معرفی شده خارج از طریق ادارات کار وامور اجتماعی در واحد مورد نظر فعالیت داشته یا در زمان استفاده از مزایای این آئینامه اشتغال به کار نداشته است، کارگاه برای همیشه از تسهیلات این آئین نامه محروم ووزارت کار وامور اجتماعی وسازما ن تأمین اجتماعی ووزارت امور اقتصادی ودارایی مجاز خواهند بودکار فرمای مربوط را تحت پیگرد قانونی قرار دهند وضرر وزیان واردشده را از وی مطالبه ووصول نمایند.
            ماده 7- کارگاه های مشمول این آئین نامه می توانند ضمن استفاده از مزایای این آئین نامه تواما از تسهیلات ماده (56) قانون برنامه سوم توسعه و آئین نامه اجرایی مربوط استفاده نمایند.
            ماده 8- از تـاریـخ تصـویب و ابـلاغ ایـن آئـیـن نـامه تـصویـب نـامه هـای شـماره 56901/ت 23995هـ مـورخ 10/12/1379 و40152/ت 25589هــ مـورخ 3/9/1380 هیأت وزیران ملغی الاثر خواهند بود. 
    """
    print(spell.spell_Doc(doc))




