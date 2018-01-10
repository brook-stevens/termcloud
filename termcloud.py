import nltk

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from wordcloud import WordCloud, STOPWORDS
import io

from os import path

def generate(text, font_path, no_lemmatization, width, height):
    documents = []
    buf = io.StringIO(text)
    for line in buf:
        line = line.rstrip('\n')
        if(line != ''):
            documents.append(line)

    engstopwords = stopwords.words('english')
    engstopwords.append("n't")
    engstopwords.append("ve")

    all_words = []

    for curr_doc_index, val in enumerate(documents):
        tokens = nltk.word_tokenize(documents[curr_doc_index])

        lemmatizer = WordNetLemmatizer()
        tokens_cleaned = []
        for tok in tokens:
            if tok.lower() in no_lemmatization:
                tokens_cleaned.append(lemmatizer.lemmatize(tok))
            else:
                tokens_cleaned.append(tok)

        tokens = tokens_cleaned

        tokens_cleaned = []
        for tok in tokens:
            if tok.lower() not in engstopwords:
                tokens_cleaned.append(tok)
        tokens = tokens_cleaned

        all_words.extend(tokens)


    # Convert all the required text into a single string here
    # and store them in word_string

    # you can specify fonts, stopwords, background color and other options
    all_words_string = ' '.join(str(e) for e in all_words)

    d = path.dirname(__file__)

    def grey_color_func(word, font_size, position, orientation, random_state=None,
                        **kwargs):
        #print "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
        return "hsl(0, 0%, 40%)"

    wordcloud = WordCloud(font_path=font_path,
                            stopwords=STOPWORDS,
                            background_color='white',
                            width=width,
                            height=height,
                            #mask=mask,
                            max_font_size=48,
                          normalize_plurals=False,
                          color_func=grey_color_func
                          ).generate(all_words_string)

    image = wordcloud.to_image()

    return image