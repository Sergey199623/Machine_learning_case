def lem(text):
    punctuations = '''!()-[]{};:'"\''<>/?@#$%^&*_~'''
    import nltk,string
    import re
    import unittest
    from nltk.stem.porter import PorterStemmer
    from nltk.stem.lancaster import LancasterStemmer
    from nltk.stem import SnowballStemmer 
    stemmer = SnowballStemmer('russian')
    stemer = PorterStemmer()
    steme = LancasterStemmer()
    stem=[stemmer.stem(w) for w in text.split()] and [stemer.stem(w) for w in text.split()] and [steme.stem(w) for w in text.split()]
    stem= ' '.join(stem)
    stem1=''
    for p in stem:
        if(p not in punctuations):stem1+=p
    return(stem1)
