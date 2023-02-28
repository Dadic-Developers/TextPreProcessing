from parsivar import POSTagger
from parsivar import Tokenizer
from flair.data import Sentence
from flair.models import SequenceTagger


class POSTag:
    
    def findPostagger(self,text):


        # # load tagger
        
        tokenizer = Tokenizer()
        tagger = POSTagger(tagging_model="stanford")  # tagging_model = "wapiti" or "stanford". "wapiti" is faster than "stanford"
        text_tags = tagger.parse(tokenizer.tokenize_words(text))
        # print(text_tags)
        return (text_tags)
# Driver program
if __name__ == "__main__":
    sentence = "به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و صنعت ایران آغاز به کار کرد. این صمینار  تا ۱۳ شهریور ادامه می یابد."
    # pos tagger 
    postag= POSTag()
    custom_pos_tagger=(postag.findPostagger(sentence))
   

    print(custom_pos_tagger)
    # print(converter.showText(pos.findPostagger(sentence)))