
import re


EXTRA_SPACE = [(r' +', ' '), (r'\n\n+', '\n\n'), (r'[ـ\r]', ''),]
punc_after, punc_before = r'\.:!،؛؟»\]\)\}', r'«\[\(\{'
PUNCTUATION_SPACE = [
                    ('" ([^\n"]+) "', r'"\1"'),  # remove space before and after quotation
                    (' ([' + punc_after + '])', r'\1'),  # remove space before
                    ('([' + punc_before + ']) ', r'\1'),  # remove space after
                    ('([' + punc_after[:3] + '])([^ \d' + punc_after + '])', r'\1 \2'),  # put space after . and :
                    ('([' + punc_after[3:] + '])([^ ' + punc_after + '])', r'\1 \2'),  # put space after
                    ('([^ ' + punc_before + '])([' + punc_before + '])', r'\1 \2'),  # put space before
                    ]

PUNCTUATION_CHARS = re.compile(r'[!"#\$%&\'\(\)\*\+\,\-./:;<=>\?@\[\]\^_`\{\|\}~،؛«»]')
HTML_TAGS = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

URL_REGEX = re.compile(
    r"(?:^|(?<![\w\/\.]))"
    r"(?:(?:https?:\/\/|ftp:\/\/|www\d{0,3}\.))"
    r"(?:\S+(?::\S*)?@)?" r"(?:"
    r"(?!(?:10|127)(?:\.\d{1,3}){3})"
    r"(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})"
    r"(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})"
    r"(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])"
    r"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}"
    r"(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))"
    r"|"
    r"(?:(?:[a-z\\u00a1-\\uffff0-9]-?)*[a-z\\u00a1-\\uffff0-9]+)"
    r"(?:\.(?:[a-z\\u00a1-\\uffff0-9]-?)*[a-z\\u00a1-\\uffff0-9]+)*"
    r"(?:\.(?:[a-z\\u00a1-\\uffff]{2,}))" r"|" r"(?:(localhost))" r")"
    r"(?::\d{2,5})?"
    r"(?:\/[^\)\]\}\s]*)?",
    flags=re.UNICODE | re.IGNORECASE,
)

HOME_PHONE_REGEX = re.compile(r"(\d{8})|(0\d{2}[-]?\d{8})")
MOBILE_PHONE_REGEX = re.compile(r"((098|\+98)?(0)?9\d{9})")