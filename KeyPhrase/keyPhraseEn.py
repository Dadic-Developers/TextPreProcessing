from typing import List
import flair
import numpy
from flair.models import SequenceTagger
from flair.tokenization import SegtokSentenceSplitter
from postagger_persian import POSTager
from postag import POSTag

persian_stop_words = numpy.loadtxt('/media/daadik/Local Disk/backend/TextPreProcessing/Data/stopwords.dat', dtype=str)



# define flair POS-tagger and splitter
tagger = SequenceTagger.load('hamedkhaledi/persain-flair-upos')#hamedkhaledi/persain-flair-pos
splitter = SegtokSentenceSplitter()

# define custom POS-tagger function using flair
def custom_pos_taggerm(raw_documents: List[str], tagger: flair.models.SequenceTagger = tagger, splitter: flair.tokenization.SegtokSentenceSplitter = splitter)->List[tuple]:
    """
    
    """ 
   
    postag= POSTager()
    custom_pos_taggers=(postag.findPostagger(raw_documents))
    return (custom_pos_taggers)


docs=[".به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و صنعت ایران آغاز به کار کرد","تمام ایران یک تابستان تنوری را تجربه میکند ."]

# check that the custom POS-tagger function returns a list of (word token, POS-tag) tuples
# print(custom_pos_taggerm(raw_documents=docs))

   

from keyphrase_vectorizers import KeyphraseCountVectorizer

# use custom POS-tagger with KeyphraseVectorizers
vectorizer = KeyphraseCountVectorizer(custom_pos_tagger=custom_pos_taggerm(docs),pos_pattern='<ADJ.*>*<N.*>+', stop_words=persian_stop_words)
vectorizer.fit(docs)
keyphrases = vectorizer.get_feature_names_out()
print(keyphrases)

