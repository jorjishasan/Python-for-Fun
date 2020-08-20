from textblob import  TextBlob

string='I lve Python'
blob=TextBlob(string)
print(str(blob.correct()))

#after printing
#result:I love Python