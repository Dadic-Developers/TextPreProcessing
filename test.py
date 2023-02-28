
from KeyPhrase.KeyPhraseFa import KeyPhrases
from Normalizers.dadmatic_Normalizer import DadMatNormalizer
from Normalizers.parsivar_normalizer import ParivarNormalizer
from Normalizers.removeDupChar import Remover
from SpellChecker.Parsiver_SpellChecker import SpellChecker
from PersianTextNormalizer.FA_Normalizer_V2 import Normalizer as Normalizer_V2
from IO.sysIO import sysIO


from hazm import Normalizer as norm_hazm
from negar.virastar import PersianEditor

# نمایش خروجی فارسی در ترمینال

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
custom_pos_tagger=[]
dic={}
docs=[]
i=0
for item  in data:
    i+=1
    subject=item['subject']
    text=item['text']
    print('subject:', subject)
    # print('text:', converter.showText(text))
   
    
# #     # نرمال سازی با پاسی ور

    subject=norm_parsivar.normalize_characters(subject)
    # print("normalize with  parsivar step-1:",subject)
    text=norm_parsivar.normalize_characters(text)
    # print("normalize with parsivar step-1:",text)

# #   
#     # نرمال سازی با دادماتیک

    subject=norm_dadmatic.normalize_characters(subject)
    # print("normalize with dadmatic:",subject)
    text=norm_dadmatic.normalize_characters(text)
    # print("normalize with dadmatic:",text)


    # حذف کاراکترهای که اضافی ایجاد شده اند
    # subject=rmv.removeDupWithOrder(subject)
    # print("text after deleting extra double char:",subject)
    # text=rmv.removeDupWithOrder(text)
    # print("text after deleting extra double char:",text)

    # # غلط املایی
    # subject=spellchecker.spell_Doc(subject)
    # print("text after spell checker:",subject)
    # text=spellchecker.spell_Doc(text)
    # print("normalize with dadmatic:",(text))

    # subject=spellchecker.spell_correcter(subject)
    # # print("text after spell checker:",subject)
    # text=spellchecker.spell_correcter(text)
    
    #  spell cheaker
    subject=str(PersianEditor(subject))
    
    print("subject after negar:",subject)
    text=str(PersianEditor(text))
    print("text after negar:",text)
    


     # غلط املایی
    # subject=spellchecker.spell_correcter(subject)
    # print("text after spell checker:",converter.showText(subject))
    # text=spellchecker.spell_correcter(text)
    # print("normalize with dadmatic:",converter.showText(text))
  
    # #Normalizer HAZM
    
    normalizer = norm_hazm()
    subject=normalizer.normalize(subject)
    text = normalizer.normalize(text)
    # print('new subject:', converter.showText(subject))
    
    # print('new text:', converter.showText(text))
    norm = Normalizer_V2()
    subject = norm.clean_characters(subject)
    subject = norm.remove_entities(subject)
    text = norm.clean_characters(text)
    text = norm.remove_entities(text)

    # print("text after spell checker:",new_text)
    new_data.append(dict(subject=subject, text=text))
    if (i>=4):
        break
    # print('new subject:', subject)
    
    #  print('new text:', text)
    
    
# print (custom_pos_tagger)

io.writeFile(new_data,fileName='/media/daadik/Local Disk/backend/TextPreProcessing/Data/outFile.json')
exit()
#  find keyphrase
docs=[]
listfile=[]
data=io.readFile('/media/daadik/Local Disk/backend/TextPreProcessing/Data/outFile.json')
i=0
for item  in data:
    try:
        i+=1
        docs=[]
        subject=item['subject']
        text=item['text']
        docs.append(subject)
        # print(text.split('.'))
        docs=docs+text.split('.')
        # print(docs)
        # print('start ...')
        keyphrase=KeyPhrases()
        keywords=keyphrase.findKeyPhrase(docs=docs,pos_pattern="<ADJ.*>*<N.*>+")
        # print(keywords)
        dic={}
        listfile.append(dict(keyphrase=keywords.tolist(), sentences=docs))
    except:
        print('error in docs:',i)  
        
        
    
print(listfile)
io.writeFile(listfile,fileName='/media/daadik/Local Disk/backend/TextPreProcessing/Data/outFilekeyPhrase.json')

# io.writeFile(listfile,fileName='/media/daadik/Local Disk/backend/TextPreProcessing/Data/outFilekeyPhrase.json')
# print (docs)  
    
print('Done....')