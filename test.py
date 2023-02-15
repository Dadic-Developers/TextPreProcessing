
from Normalizers.dadmatic_Normalizer import DadMatNormalizer
from Normalizers.parsivar_normalizer import ParivarNormalizer
from Normalizers.removeDupChar import Remover
from SpellChecker.Parsiver_SpellChecker import SpellChecker
from printPersianText import Converter

tmp_text = "به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و سنعت ایران آغاز به کار کرد. این صمیناررر  تا ۱۳ شهرییییییور ادامه می یابد."

# نمایش خروجی فارسی در ترمینال
converter= Converter()

# نرمال سازی با دادماتیک
norm_dadmatic= DadMatNormalizer()
new_text=norm_dadmatic.normalize_characters(tmp_text)
print("normalize with dadmatic:",converter.showText(new_text))


# نرمال سازی با پاسی ور

norm_parsivar=ParivarNormalizer()
new_text=norm_parsivar.normalize_characters(new_text)
print("normalize with dadmatic and then parsivar:",converter.showText(new_text))


# حذف کاراکترهای که اضافی ایجاد شده اند
rmv=Remover()
new_text=rmv.removeDupWithOrder(new_text)
print("text after deleting extra double char:",converter.showText(new_text))


# غلط املایی

spellchecker=SpellChecker()
new_text=spellchecker.spell_correcter(new_text)
print("text after spell checker:",converter.showText(new_text))
