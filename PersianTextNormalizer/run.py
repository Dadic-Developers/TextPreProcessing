
# -*- coding: utf-8 -*-
from FA_Normalizer_V2 import Normalizer

# input_text = input('Enter input: ')
input_text="هیأت وزیران در جلسه مورخ 9/1/1383 بنا به پیشنهاد مشترک " \
           "وزارت خانه های صنایع ومعادن، امور اقتصادی ودارایی وسازمان مدیریت وبرنامه ریزی کشور به استناد ماده  22  " \
           "قانون تنظیم بخشی از مقررات تسهیل نوسازی صنایع کشور واصلاح ماده  113  قانون برنامه سوم توسعه اقتصادی، اجتماعی " \
           "و فرهنگی جمهوری اسلامی ایران – مصوب 1382- آئین نامه اجرایی ماده  4  قانون یاد شده را به شرح زیر تصویب نمود:"

print(input_text)

norm = Normalizer()
text = norm.clean_characters(input_text)
text = norm.remove_entities(text, remove_numbers=False, remove_punctuation=False)

print("result =>",text)



