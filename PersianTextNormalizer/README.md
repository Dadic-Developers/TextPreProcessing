# PersianTextNormalizer
This module is for normalization of persian text .

Example:
```
from FA_Normalizer_V2 import Normalizer

text_list = ['هیأت وزیران در جلسه مورخ 9/1/1383 پیشنهاد مشترکی را اراءه دادند.', 
             'ماده (2) الحاقی - این ماده حذف شده است.']

norm = Normalizer()
for text in text_list:
    text = norm.clean_characters(text)
    text = norm.remove_entities(text, remove_numbers=True)
    print(text)
```
