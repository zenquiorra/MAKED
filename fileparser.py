import os
class Parse:
    '''Intialize article json'''
    def __init__(self, article):
        self.article = article
        
    def get_title(self):
        try:
            return self.article['title']
        except:
            return []
    
    def get_date(self):
        try:
            return self.article['date']
        except:
            return []
        
    def get_url(self):
        try:
            return self.article['url']
        except:
            return []
    
    def get_summary(self):
        try:
            return self.article['summary']
        except:
            return []
    
    def get_text(self):
        '''Gets ALL the text in our article'''
        
        text = ''   
        for element in self.article:
            # check subheading
            try:
                # subheading comes under a number so conversion to integer is possible
                int(element)
                
                text += ''.join(self.article[element]['para']) + '\n'
                
            except:
                pass
            
        return text
    
    def get_textall(self):
        "gets all the text , treats subheadings as a part of the text"
        text = ''   
        for element in self.article:
            # check subheading
            try:
                # subhead or text comes under a number so conversion to integer is possible
                int(element)
                try:
                    text += self.article[element]['subheading'] + '\n'
                    text += ''.join(self.article[element]['para']) + '\n'
                except:
                    text += ''.join(self.article[element]['para']) + '\n'
            except:
                pass
            
        return text
    
    
    def get_subheading(self):
        'Returns a list all the subheadings'
        subheadings = []
        for element in self.article:
            try:
                int(element)
                if int(element) == 0:
                    pass
                else:
                    subheadings.append(self.article[element]['subheading'])
                    
            except:
                pass
            
        return subheadings
    
    
    def get_images(self, path):
        'Returns a list of tuples of all image names inside our article along with their captions'
        images = []
        for element in self.article:
            try:
                int(element)
                if 'images' in self.article[element]:
                    images.extend(self.article[element]['images'])
                    
            except:
                pass
        
        all_im = os.listdir(path)
        filter_images = []
        
        # Instead of checking like this, create a dictionary of article-images using this method and read image from that file directly 
        
        for i in images:
            if i[0] in all_im and i not in filter_images:
                filter_images.append(i)
            
        
        return filter_images
        
    def get_keywords(self):
        'Returns a list of all keywords'
        try:
            return self.article['keyword']
        except:
            return []
    
    def get_related(self):
        'Returns a list of URLs all related articles'
        try:
            return self.article['related']
        except:
            return []
        
    def get_en_url(self):
        'Returns the parallel English URL for cross-lingual data'
        try:
            return self.article['english_url']
        except:
            return ''
                
                
