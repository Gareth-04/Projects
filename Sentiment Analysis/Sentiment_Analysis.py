# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 09:38:02 2025

@author: 25646648 and 25709054
"""
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import pos_tag
from nltk import bigrams
import operator
from collections import defaultdict

import nltk
nltk.download('stopwords')
import csv
nltk.download('punkt')


# Calculation of Sentiment 
def get_sentiment(text): #TEXTBLOB, 2025. Tutorial: Quickstart [online]. Available from: https://textblob.readthedocs.io/en/dev/quickstart.html [Accessed 10 March 2025].
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Applying labels to sentiment Takes Polarity from get_sentiment and passes it through to check what value it should be assigned.
def sentiment_label(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral' #=0

# Arrays to Store output values. 
sentiment_values = []
sentiment_labels = []
review_texts = []

# STACKOVERFLOW, 2023. Effective Approaches for Optimizing Performance with Large Datasets in Python? [online]. Available from: https://stackoverflow.com/questions/76318762/effective-approaches-for-optimizing-performance-with-large-datasets-in-python [Accessed 10 March 2025].
chunksize = 1000  # Process 1000 rows at a time. Using this method helps optimise performance and limits the chances of crashes happening midway through the process.
for chunk in pd.read_csv('Movie_reviews_CW2 Data.csv', 
                         header=None, #No header rows Some CSV files have a header explaining what each value is. E.G ReviewID, MovieID, ReviewText. GEEKS FOR GEEKS, 2021. How to read csv file with Pandas without header? [online]. Available from: https://www.geeksforgeeks.org/how-to-read-csv-file-with-pandas-without-header/ [Accessed 10 March 2025]. 
                         delimiter='\t', #columns are seperated by tab spaces instead of the normal columns. GEEKS FOR GEEKS, 2024. How to convert tab-seperated file into a dataframe using Python [online]. Available from: https://www.geeksforgeeks.org/how-to-convert-tab-separated-file-into-a-dataframe-using-python/ [Accessed 10 March 2025]. 
                         on_bad_lines='skip', #SATURNCLOUD, 2023. How to Fix Python Pandas Error Tokenizing Data [online]. Available from: https://saturncloud.io/blog/how-to-fix-python-pandas-error-tokenizing-data/#:~:text=For%20example%3A,the%20rest%20of%20the%20file. [Accessed 10 March 2025].
                         quotechar="'", #ensures that the delimter is split correctly by ensuring it is not read as a single column. 
                         chunksize=chunksize): #chunksize=chunksize ensures the file is read in chunks of 1000.     
    
  
    # This Manually assigns columns to the dataset. In this case ReviewID, MovieID and ReviewText
    chunk.columns = ['ReviewID', 'MovieID', 'ReviewText'] #GEEKS FOR GEEKS, 2024. Pandas DataFrame.columns [online]. Available from: https://www.geeksforgeeks.org/python-pandas-dataframe-columns/ [Accessed 10 March 2025].
    
    
    # This gathers the chunk and gets the Sentiment Value by gathering the Review Text and running it through the TextBlob get_sentiment function.
    chunk['Sentiment_Value'] = chunk['ReviewText'].apply(get_sentiment)
    
    # This takes the value from the above calculation and applies a label (positive, neutral and negative) by checking the value.
    chunk['Sentiment_Label'] = chunk['Sentiment_Value'].apply(sentiment_label)
    
    # Add all results to the pre-established arrays. .extend adds elements to the lists and .tolist() converts the above sentiment value and label to list values so they can be added to the lists easily. 
    sentiment_values.extend(chunk['Sentiment_Value'].tolist()) #GEEKS FOR GEEKS, 2018. Python | Pandas Series.tolist() [online]. Available from: https://www.geeksforgeeks.org/python-pandas-series-tolist/ [Accessed 10 March 2025].
    sentiment_labels.extend(chunk['Sentiment_Label'].tolist()) #W3 Schools, 2025. Python List extend() Method [online]. Available from: https://www.w3schools.com/python/ref_list_extend.asp [Accessed 10 March 2025].
    review_texts.extend(chunk['ReviewText'].tolist())
    
    #Prints the head of all chunks to help show that the chunks are being processed. This allows a breif view of the process. 
    print(chunk[['ReviewText', 'Sentiment_Label']].head())


# Create a DataFrame from the data. Assigning the column values generated above.
final_df = pd.DataFrame({ #Assigns names and then gathers the values from the columns. Eg ReviewText is the column name and has the values gathered from the review_texts array
    'ReviewText': review_texts,
    'Sentiment_Value': sentiment_values,
    'Sentiment_Label': sentiment_labels
})

print(final_df['Sentiment_Label'].value_counts()) #SATURNCLOUD, 2023. Python Pandas Convert valuecounts Output to Dataframe [online]. Available from: https://saturncloud.io/blog/python-pandas-convert-valuecounts-output-to-dataframe/#:~:text=value_counts()%20method%20is%20a,count%20is%20the%20corresponding%20value.&text=As%20you%20can%20see%2C%20the%20output%20of%20. [Accessed 10 March 2025].

#Visualisation of Results 
#Bar Chart

df= pd.read_csv('Movie_reviews_CW2 Data.csv', header = None, names=['ReviewID', 'MovieID','ReviewText'], low_memory=False)
sentiment_counts = final_df['Sentiment_Label'].value_counts()
plt.figure(figsize=(10,5))
plt.bar(sentiment_counts.index, sentiment_counts.values, color=['purple','blue','green'])

plt.title('The sentiment analysis based on the number of reviews')
plt.xlabel('Sentiment results')
plt.ylabel('The amount of reviews')
plt.show()

#Scatter Graph 
df = pd.read_csv('Movie_reviews_CW2 Data.csv', header = None, names=['ReviewID','MovieID','ReviewText'], low_memory=False)
sentiment_counts = final_df['Sentiment_Label'].value_counts()

plt.scatter(sentiment_counts.index, sentiment_counts.values, color = 'red',)
plt.xlabel("Sentiment cateogry")
plt.ylabel("the amount of reviews")
plt.title("The amount of reviews based upon sentiment category")

plt.show()

#Pie Chart
df = pd.read_csv('Movie_reviews_CW2 Data.csv', header = None, names=['ReviewID','MovieID','ReviewText'], low_memory=False)
sentiment_counts = final_df['Sentiment_Label'].value_counts()
plt.pie(sentiment_counts.values, labels=sentiment_counts.index,colors=['orange','blue','green'], autopct = '%1.1f%%') #GEEKS FOR GEEKS, 2025.  plot a pie chart in python using Matplotlib [online]. Available from: https://www.geeksforgeeks.org/plot-a-pie-chart-in-python-using-matplotlib/ [Accessed 25 April 2025].  
plt.title('Sentiment category of movie reviews')
plt.axis('equal')
plt.show()

# Collocation Extraction 

# Extracting Positive and Negative Reviews 

positive_review_texts = final_df[final_df['Sentiment_Label'] == 'Positive']['ReviewText'] # Single out positive and negative reviews.
negative_review_texts = final_df[final_df['Sentiment_Label'] == 'Negative']['ReviewText']

file_path = 'Movie_reviews_CW2 Data.csv'
df = pd.read_csv('Movie_reviews_CW2 Data.csv', sep='\t', header = None , engine = 'python', quoting=csv.QUOTE_NONE,)


#defining the key variables
bigrams_with_frequencies = defaultdict(int) #REAL PYTHON, 2024. Dictionaries in Python [online]. Available from: https://realpython.com/python-dicts/ [Accessed 24 April 2025].
bigrams_with_frequencies_unfiltered = defaultdict(int)


#for positive reviews
for text in positive_review_texts:
        tokens = word_tokenize(text)
        #filters tokens
        filtered_tokens = [word.lower() for word in tokens if word.isalpha()]
        
        # Generating bigrams that are filtered
        bigram_list_filtered = list(bigrams(filtered_tokens))
        
        # Counting bigram frequencies
        for bigram_pair in bigram_list_filtered:
            bigrams_with_frequencies[bigram_pair] += 1

        #Generating bigrams for tokens that are unfiltered
        bigram_list_unfiltered = list(bigrams(tokens))

        #Counting bigram frequencies for unfiltered tokens
        for bigram_pair in bigram_list_unfiltered:
            bigrams_with_frequencies_unfiltered[bigram_pair]+= 1


sorted_bigrams_filtered = sorted(bigrams_with_frequencies.items(), key=lambda x: x[1], reverse=True)
sorted_bigrams_unfiltered = sorted(bigrams_with_frequencies_unfiltered.items(), key=lambda x: x[1], reverse=True)


#outputting the results for filtered tokens
print("Top 40 filtered bigrams for Positive Reviews ")
for bigram, freq in sorted_bigrams_filtered[:40]:
    print(f"{bigram}: {freq}")

#unfiltered
print("Top 40 unfiltered bigrams for Positive Reviews ")
for bigram, freq in sorted_bigrams_unfiltered[:40]:
    print(f"{bigram}: {freq}")

#negative reviews 

for text in negative_review_texts:
    tokens = word_tokenize(text)
    unfiltered_tokens = tokens
    filtered_tokens = [word.lower() for word in tokens if word.isalpha()]

    # Generating bigrams that are filtered
    bigram_list_filtered = list(bigrams(filtered_tokens))

    # Counting bigram frequencies
    for bigram_pair in bigram_list_filtered:
        bigrams_with_frequencies[bigram_pair] += 1

    # Generating bigrams for tokens that are unfiltered
    bigram_list_unfiltered = list(bigrams(unfiltered_tokens))

    # Counting bigram frequencies for unfiltered tokens
    for bigram_pair in bigram_list_unfiltered:
        bigrams_with_frequencies_unfiltered[bigram_pair] += 1

    #Generating bigrams for tokens that are unfiltered
    bigram_list_unfiltered = list(bigrams(tokens))

    #counting bigram frequencies for unfiltered tokens
    for bigram_pair in bigram_list_unfiltered:
        bigrams_with_frequencies_unfiltered[bigram_pair]+= 1


sorted_bigrams_filtered = sorted(bigrams_with_frequencies.items(), key=lambda x: x[1], reverse=True)
sorted_bigrams_unfiltered = sorted(bigrams_with_frequencies_unfiltered.items(), key=lambda x: x[1], reverse=True)


# outputting the results for filtered tokens
print("Top 40 filtered bigrams for Negative Reviews ")
for bigram, freq in sorted_bigrams_filtered[:40]:
    print(f"{bigram}: {freq}")

#unfiltered 
print("Top 40 unfiltered bigrams for Negative Reviews ")
for bigram, freq in sorted_bigrams_unfiltered[:40]:
    print(f"{bigram}: {freq}")


def compute_frequency_of_bigrams_in_positive_review_with_pos_tag(positive_review_texts):
    bigrams_with_frequencies = defaultdict(int)
    
    stop_words = set(stopwords.words('english')) #CHOUBEY,V, 2022. Text Processing in Python: Steps and Implementation [online]. Available from: https://vijay-choubey.medium.com/text-preprocessing-in-python-steps-and-implementation-c2012f4e368a [Accessed 31 March 2025].
    
    for review in positive_review_texts:
        words = word_tokenize(review.lower()) #LANE,K, 2021. Tokenization with NLTK [online]. Available from:https://medium.com/@kelsklane/tokenization-with-nltk-52cd7b88c7d [Accessed 31 March 2025].
        
        pos_tagged_words = pos_tag(words) #JAIN,Y, 2022. POS Tagging [NLP,Python] [online]. Available from:https://medium.com/@yashj302/pos-tagging-nlp-python-41df5243da78 [Accessed 31 March 2025].
        
        filtered_words = [(word, tag) for word, tag in pos_tagged_words if word.isalpha() and word not in stop_words]
    
        bigram_list = list(bigrams(filtered_words))
    
        for bigram_pair in bigram_list:
            bigrams_with_frequencies[bigram_pair] += 1 #+=1 increments the value until their is no occurences of the pair left. 
        
    return bigrams_with_frequencies

# Calculate frequency of Pairs
bigram_frequencies = compute_frequency_of_bigrams_in_positive_review_with_pos_tag(positive_review_texts)
sorted_bigrams = sorted(bigram_frequencies.items(), key=operator.itemgetter(1), reverse=True)

# Print 40 most frequent bigrams
print("Top 40 most frequent bigrams in positive reviews with pos tag:")
for bigram, freq in sorted_bigrams[:40]:
    print(f"{bigram}: {freq}")
    
    
def compute_frequency_of_bigrams_in_positive_reviews_with_noun_and_noun_pos_tag(positive_review_texts):
    bigrams_with_frequencies = defaultdict(int)
    
    stop_words = set(stopwords.words('english')) #CHOUBEY,V, 2022. Text Processing in Python: Steps and Implementation [online]. Available from: https://vijay-choubey.medium.com/text-preprocessing-in-python-steps-and-implementation-c2012f4e368a [Accessed 31 March 2025].
    
    for review in positive_review_texts:
        words = word_tokenize(review.lower()) #LANE,K, 2021. Tokenization with NLTK [online]. Available from:https://medium.com/@kelsklane/tokenization-with-nltk-52cd7b88c7d [Accessed 31 March 2025].
        
        pos_tagged_words = pos_tag(words) #JAIN,Y, 2022. POS Tagging [NLP,Python] [online]. Available from:https://medium.com/@yashj302/pos-tagging-nlp-python-41df5243da78 [Accessed 31 March 2025].
        
        filtered_words = [(word, tag) for word, tag in pos_tagged_words if word.isalpha() and word not in stop_words and tag.startswith('NN')]
    
        bigram_list = list(bigrams(filtered_words))
    
        for bigram_pair in bigram_list:
            bigrams_with_frequencies[bigram_pair] += 1 #+=1 increments the value until their is no occurences of the pair left. 
        
    return bigrams_with_frequencies

# Calculate frequency of Pairs
bigram_frequencies = compute_frequency_of_bigrams_in_positive_reviews_with_noun_and_noun_pos_tag(positive_review_texts)
sorted_bigrams = sorted(bigram_frequencies.items(), key=operator.itemgetter(1), reverse=True)

# Print 40 most frequent bigrams
print("Top 40 most frequent bigrams in positive reviews with NN pos tag:")
for bigram, freq in sorted_bigrams[:40]:
    print(f"{bigram}: {freq}")
    
    
def compute_frequency_of_bigrams_in_negative_review_with_pos_tag(negative_review_texts):
    bigrams_with_frequencies = defaultdict(int) #used to count the frequency of bigrams. 
    
    stop_words = set(stopwords.words('english')) #CHOUBEY,V, 2022. Text Processing in Python: Steps and Implementation [online]. Available from: https://vijay-choubey.medium.com/text-preprocessing-in-python-steps-and-implementation-c2012f4e368a [Accessed 31 March 2025].
    
    for review in negative_review_texts:
        words = word_tokenize(review.lower()) #LANE,K, 2021. Tokenization with NLTK [online]. Available from:https://medium.com/@kelsklane/tokenization-with-nltk-52cd7b88c7d [Accessed 31 March 2025].
        
        pos_tagged_words = pos_tag(words) #JAIN,Y, 2022. POS Tagging [NLP,Python] [online]. Available from:https://medium.com/@yashj302/pos-tagging-nlp-python-41df5243da78 [Accessed 31 March 2025].
        
        filtered_words = [(word, tag) for word, tag in pos_tagged_words if word.isalpha() and word not in stop_words]
    
        bigram_list = list(bigrams(filtered_words))
    
        for bigram_pair in bigram_list:
            bigrams_with_frequencies[bigram_pair] += 1
        
    return bigrams_with_frequencies

# Calculate frequency of Pairs
bigram_frequencies = compute_frequency_of_bigrams_in_negative_review_with_pos_tag(negative_review_texts)
sorted_bigrams = sorted(bigram_frequencies.items(), key=operator.itemgetter(1), reverse=True)

# Print 40 most frequent bigrams
print("Top 40 most frequent bigrams in negative reviews with pos tag:")
for bigram, freq in sorted_bigrams[:40]:
    print(f"{bigram}: {freq}")
    

def compute_frequency_of_bigrams_in_negative_reviews_with_noun_and_noun_pos_tag(negative_review_texts):
    bigrams_with_frequencies = defaultdict(int)
    
    stop_words = set(stopwords.words('english')) #CHOUBEY,V, 2022. Text Processing in Python: Steps and Implementation [online]. Available from: https://vijay-choubey.medium.com/text-preprocessing-in-python-steps-and-implementation-c2012f4e368a [Accessed 31 March 2025].
    
    for review in negative_review_texts:
        words = word_tokenize(review.lower()) #LANE,K, 2021. Tokenization with NLTK [online]. Available from:https://medium.com/@kelsklane/tokenization-with-nltk-52cd7b88c7d [Accessed 31 March 2025].
        
        pos_tagged_words = pos_tag(words) #JAIN,Y, 2022. POS Tagging [NLP,Python] [online]. Available from:https://medium.com/@yashj302/pos-tagging-nlp-python-41df5243da78 [Accessed 31 March 2025].
        
        filtered_words = [(word, tag) for word, tag in pos_tagged_words if word.isalpha() and word not in stop_words and tag.startswith('NN')]
    
        bigram_list = list(bigrams(filtered_words))
    
        for bigram_pair in bigram_list:
            bigrams_with_frequencies[bigram_pair] += 1 #+=1 increments the value until their is no occurences of the pair left. 
        
    return bigrams_with_frequencies

# Calculate frequency of Pairs
bigram_frequencies = compute_frequency_of_bigrams_in_negative_reviews_with_noun_and_noun_pos_tag(negative_review_texts)
sorted_bigrams = sorted(bigram_frequencies.items(), key=operator.itemgetter(1), reverse=True)

# Print 40 most frequent bigrams
print("Top 40 most frequent bigrams in negative reviews with NN pos tag:")
for bigram, freq in sorted_bigrams[:40]:
    print(f"{bigram}: {freq}")

