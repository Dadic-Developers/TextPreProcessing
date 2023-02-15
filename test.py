
from Normalizers.dadmatic_Normalizer import DadMatNormalizer
from Normalizers.parsivar_normalizer import ParivarNormalizer
from Normalizers.removeDupChar import Remover
from SpellChecker.Parsiver_SpellChecker import SpellChecker
from printPersianText import Converter
from IO.sysIO import sysIO

# نمایش خروجی فارسی در ترمینال
converter= Converter()
norm_dadmatic= DadMatNormalizer()
norm_parsivar=ParivarNormalizer()
rmv=Remover()
spellchecker=SpellChecker()
io=sysIO()
data=io.readFile('/media/daadik/Local Disk/backend/TextPreProcessing/Data/TaxRules.json')

# tmp_text = "به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و سنعت ایران آغاز به کار کرد. این صمیناررر  تا ۱۳ شهرییییییور ادامه می یابد."
# Iterating through the json
        # list
print('start...')
new_data=[]
dic={}
for item  in data:
    subject=item['subject']
    text=item['text']
    # print('subject:', converter.showText(subject))
    # print('text:',text)

    # نرمال سازی با دادماتیک

    subject=norm_dadmatic.normalize_characters(subject)
    # print("normalize with dadmatic:",converter.showText(new_text))

    # نرمال سازی با پاسی ور

    subject=norm_parsivar.normalize_characters(subject)
    # print("normalize with dadmatic and then parsivar:",converter.showText(new_text))

    # حذف کاراکترهای که اضافی ایجاد شده اند
    subject=rmv.removeDupWithOrder(subject)
    # print("text after deleting extra double char:",converter.showText(new_text))


    # غلط املایی
    subject=spellchecker.spell_correcter(subject)
    # print("text after spell checker:",converter.showText(new_text))
    
    # نرمال سازی با دادماتیک

    text=norm_dadmatic.normalize_characters(text)
    # print("normalize with dadmatic:",converter.showText(new_text))

    # نرمال سازی با پاسی ور

    text=norm_parsivar.normalize_characters(text)
    # print("normalize with dadmatic and then parsivar:",converter.showText(new_text))

    # حذف کاراکترهای که اضافی ایجاد شده اند
    text=rmv.removeDupWithOrder(text)
    # print("text after deleting extra double char:",converter.showText(new_text))


    # غلط املایی
    text=spellchecker.spell_correcter(text)
    # print("text after spell checker:",converter.showText(new_text))
    new_data.append(dict(subject=subject, text=text))

    # print('new subject:', converter.showText(subject))
    break
    #  print('new text:', text)
   
io.writeFile(new_data,"/media/daadik/Local Disk/backend/TextPreProcessing/Data/outFile.json")

print('Done....')