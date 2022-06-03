"""
    Author:     Sarvar Azimov
    Telegram:   https://t.me/SarvarAzim
    Facebook:   https://facebook.com/SarvarAzim
    Instagram:  https://instagram.com/SarvarAzim
"""


import re

class GetWordsSimilar2Keyword:
    def __init__(self, keyWord):
        self.key = keyWord.lower() # Convert keyword to lowercase
        self.words = [] # array for similar words
        self.s_words = [] # count all similar words
        
        #Define language of keyword & read compatible words list [EN-RU]
        if ord(self.key[0]) < 123 and ord(self.key[0]) > 96: # check by ASCII code
            self.f = self.readWordsList('en')
        else:
            self.f = self.readWordsList('ru')
        
        self.words = self.getWords(self.f) # get words similar to keyword
        
        print("All similar words count: ", self.s_words)

        # print list all similar words by priority (similarity degree)
        for word in self.words:
            print(word)

    def getWords(self, f):
        words_starts = [] # words list which starts with keyword
        words_ends = [] # words list which ends with keyword
        words_between = [] # words list which contain keyword
        words_similar = [] # words list which differs with only one letter from keyword

        s_starts = 0 # words count which starts with keyword
        s_ends = 0 # words count which ends with keyword
        s_between = 0 # words count which contain keyword
        s_similar = 0 # words count which differs with only one letter from keyword

        for str in f:
            #define words which starts with keyword
            if str.startswith(self.key):
                words_starts.append(str[:-1])
                s_starts += 1
            
            #define words which ends with keyword
            elif str[:-1].endswith(self.key):
                words_ends.append(str[:-1])
                s_ends += 1
            
            #define words which contains keyword
            elif str[:-1].find(self.key) != -1:
                words_between.append(str[:-1])
                s_between += 1
            
            # define words which differs with one letter from keyword (similar words), example: [pain, gain, main, ...]
            elif len(str) - 1 == len(self.key):
                for i in range(len(self.key)):
                    temp_key = self.key.replace(self.key[i], ".")
                    if re.findall(temp_key, str):
                        words_similar.append(str[:-1])
                        s_similar += 1
                        break
        all_words = words_starts + words_ends + words_between + words_similar
        self.s_words = s_starts + s_ends + s_between + s_similar
        return all_words
      
    def readWordsList(self, lang):
        fileName = "words_" + lang + ".txt"
        return open(fileName, "r")


GetWordsSimilar2Keyword(keyWord="Insert your keyword here")