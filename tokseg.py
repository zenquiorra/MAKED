# English word and sentence tokenizer
import syntok.segmenter as segmenter
from syntok.tokenizer import Tokenizer

# Indic Languages
from indicnlp.tokenize import sentence_tokenize
from indicnlp.tokenize import indic_tokenize  

# Japanese tokenizer
from fugashi import Tagger

# Chinese tokenizer 
from chinese import ChineseAnalyzer





class Split:
    
    def tokenize(self, text, lang):
        
        # english and other non indian , indo european languages
        
        if lang == 'ja':
            tagger = Tagger('-Owakati')
            return [str(word) for word in tagger(text)]
    
        # Chinese
        elif lang == 'zh':
            analyzer = ChineseAnalyzer()
            result = analyzer.parse(text)
            return result.tokens()
        
        elif lang == 'es' or lang == 'en' or lang == 'ru' or lang == 'id':
            return [token.value for token in Tokenizer().tokenize(text)]
        
        else:
            return indic_tokenize.trivial_tokenize(text, lang)
                                 
    
    def segment(self, text, lang):
        
        if lang == 'ja':
            tagger = Tagger('-Owakati')
            sentences = []
            sentence = ''
            for word in tagger(text):
#                 print (word)
                if "。" !=  str(word):
                    sentence += str(word)
                else:
                    sentences.append(sentence)
                    sentence = ""
                    
            return sentences
        
        elif lang == 'zh':
            analyzer = ChineseAnalyzer()
            result = analyzer.parse(text)
            sentences = []
            sentence = ''
            for word in result.tokens():
#                 print (word)
                if "。" !=  str(word):
                    sentence += str(word)
                else:
                    sentences.append(sentence)
                    sentence = ""
                    
            return sentences
        
        elif lang == 'es' or lang == 'en' or lang == 'ru':
            return [' '.join([token.value for token in sentence][:-1]) for paragraph in segmenter.process(text) for sentence in paragraph]
        
        
        else:
            return sentence_tokenize.sentence_split(text, lang)
