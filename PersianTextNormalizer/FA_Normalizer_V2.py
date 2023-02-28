# -*- coding: utf-8 -*-
# ==============================================================================
# %% functions
# ==============================================================================

from PersianTextNormalizer.RegexConstant import *

class Normalizer:

    def __init__(self):
        replace = lambda A, B: dict((ord(a), b) for a, b in zip(A, B))
        FA_DIGITS = '۰۱۲۳۴۵۶۷۸۹'
        AR_DIGITS = '٠١٢٣٤٥٦٧٨٩'
        EN_DIGITS = '0123456789'
        self.__NUMBERS = re.compile(r'\d+')
        self.__FA_DIGITS = replace(FA_DIGITS, EN_DIGITS)
        self.__AR_DIGITS = replace(AR_DIGITS, EN_DIGITS)
        self.__DIACRITIC = re.compile('[\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652]')
        self.__DAL = re.compile('[دڈډڊڋڌڍڎڏڐ]')  # ڐ
        self.__REH = re.compile('[رڑڒړڔڕږڗ]')  # ڗ
        self.__SEEN = re.compile('[سڛښ]')  # ښ
        self.__YEH = re.compile('[یيىئؠؽؾؿٸ]')  # ٸ
        self.__KAF = re.compile('[كکػؼڪګڬڭڮ]')  # ڮ
        self.__GAF = re.compile('[گڰڱڲڳڴ]')  # ڴ
        self.__LAM = re.compile('[لڵڶڷڸ]')  # ب
        self.__ALEF = re.compile('[اأآأإٱٲٳ]')  # ٳ
        self.__NOON = re.compile('[نڹںڻڼڽ]')  # ڽ
        self.__HAH = re.compile('[حځڂ]')  # ڂ
        self.__WAW = re.compile('[وؤٶۄۊۏ]')  # ۏ
        self.__HAMZA = u'\u0621'  #
        self.__HEH = re.compile('[هة]')  # HEH=> ه
        self.__SPACE = re.compile('[           ]')  # SPACE
        self.__ZWNJ = re.compile('\u2008|\u200A|\u200C')  # نیم فاصله
        self.__DASH = re.compile('[‒–—‐‑]')
        self.__QUOT = re.compile('[”“]')
        self.__FA_PUNCT = replace("?⁒", "?%")
        compile_patterns = lambda patterns: [(re.compile(pattern), repl) for pattern, repl in patterns]
        self.__PUNCTUATION_SPACE = compile_patterns(PUNCTUATION_SPACE)
        self.__EXTRA_SPACE = compile_patterns(EXTRA_SPACE)


    def clean_characters(self, text, zwnj=True, digit=True, hamza=True):
        if not text:
            return ""
        if zwnj:
            text = re.sub(self.__ZWNJ, ' ', text)
        if digit:
            text = text.translate(self.__FA_DIGITS)
            text = text.translate(self.__AR_DIGITS)
        if hamza:
            text = text.replace(self.__HAMZA, '')
        text = text.translate(self.__FA_PUNCT)
        text = re.sub(self.__DIACRITIC, '', text)
        text = re.sub(self.__QUOT, '"', text)
        text = re.sub(self.__DASH, '-', text)
        text = re.sub(self.__SPACE, ' ', text)
        text = re.sub(self.__DAL, 'د', text)
        text = re.sub(self.__REH, 'ر', text)
        text = re.sub(self.__SEEN, 'س', text)
        text = re.sub(self.__YEH, 'ی', text)
        text = re.sub(self.__KAF, 'ک', text)
        text = re.sub(self.__GAF, 'گ', text)
        text = re.sub(self.__LAM, 'ل', text)
        text = re.sub(self.__ALEF, 'ا', text)
        text = re.sub(self.__NOON, 'ن', text)
        text = re.sub(self.__HAH, 'ح', text)
        text = re.sub(self.__WAW, 'و', text)
        text = re.sub(self.__HEH, 'ه', text)
        return text



    def remove_entities(self, text,
                        removed_html=False,
                        remove_extra_spaces=True,
                        punctuation_spacing=False,
                        remove_punctuation=False,
                        remove_url=False,
                        remove_mobile_number=False,
                        remove_home_number=False,
                        remove_numbers=False):
        patterns = []
        patterns_replacement = []
        if remove_url:
            patterns.append(URL_REGEX)
        if remove_mobile_number:
            patterns.append(MOBILE_PHONE_REGEX)
        if remove_home_number:
            patterns.append(HOME_PHONE_REGEX)
        if remove_extra_spaces:
            patterns_replacement.extend(self.__EXTRA_SPACE)
        if removed_html:
            patterns.append(HTML_TAGS)
        if punctuation_spacing:
            patterns_replacement.extend(self.__PUNCTUATION_SPACE)
        if remove_punctuation:
            patterns.append(PUNCTUATION_CHARS)
        if remove_numbers:
            patterns.append(self.__NUMBERS)
        for ptn in patterns:
            text = ptn.sub(' ', text)
        for ptn, repl in patterns_replacement:
            text = ptn.sub(repl, text)
        return text


