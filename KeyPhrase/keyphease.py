from keyphrase_vectorizers import KeyphraseCountVectorizer
import numpy

from printPersianText import Converter
persian_stop_words = numpy.loadtxt('/media/daadik/Local Disk/backend/TextPreProcessing/Data/stopwords.dat', dtype=str, delimiter='\n')


# docs = ["""Supervised learning is the machine learning task of learning a function that
#          maps an input to an output based on example input-output pairs. It infers a
#          function from labeled training data consisting of a set of training examples.
#          In supervised learning, each example is a pair consisting of an input object
#          (typically a vector) and a desired output value (also called the supervisory signal). 
#          A supervised learning algorithm analyzes the training data and produces an inferred function, 
#          which can be used for mapping new examples. An optimal scenario will allow for the 
#          algorithm to correctly determine the class labels for unseen instances. This requires 
#          the learning algorithm to generalize from the training data to unseen situations in a 
#          'reasonable' way (see inductive bias).""", 
             
#         """Keywords are defined as phrases that capture the main topics discussed in a document. 
#         As they offer a brief yet precise summary of document content, they can be utilized for various applications. 
#         In an information retrieval environment, they serve as an indication of document relevance for users, as the list 
#         of keywords can quickly help to determine whether a given document is relevant to their interest. 
#         As keywords reflect a document's main topics, they can be utilized to classify documents into groups 
#         by measuring the overlap between the keywords assigned to them. Keywords are also used proactively 
#         in information retrieval."""]

        



class KeyPhrase:
    
        
    def findKeyPhrase(self,docs):
       # Init default vectorizer.

        vectorizer = KeyphraseCountVectorizer( pos_pattern='<ADJ.*>*<N.*>+', stop_words=persian_stop_words)
        # Print parameters
        print(vectorizer.get_params())
        # After initializing the vectorizer, it can be fitted
        # to learn the keyphrases from the text documents.
        vectorizer.fit(docs)
        # After learning the keyphrases, they can be returned.
        keyphrases = vectorizer.get_feature_names_out()
        return keyphrases

        
# Driver program
if __name__ == "__main__":
    converter= Converter()
    keyphrase=KeyPhrase()
    docs = ["به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و صنعت ایران آغاز به کار کرد. این صمینار  تا ۱۳ شهریور ادامه می یابد."]
    print(converter.showText("\n".join(keyphrase.findKeyPhrase(docs)) ))