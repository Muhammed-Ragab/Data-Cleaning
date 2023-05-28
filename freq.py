import pandas as pd
from nltk import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# Read the book data from the CSV file
book_data = pd.read_csv('AM.csv', encoding='utf-8')

# Combine all the words into a single string
all_words = ' '.join(book_data['Token'])

# Tokenize the text into individual words
words = all_words.split()

# Read the custom stopwords from the CSV file
stopwords_df = pd.read_csv('stopwords.csv', encoding='utf-8')
custom_stopwords = set(stopwords_df['stopword'].tolist())

# Remove stopwords
stopwords = set(stopwords.words('arabic'))  # Use the appropriate language stopwords
filtered_words = [word for word in words if word.lower() not in stopwords and word.lower() not in custom_stopwords]

# Calculate word frequency
freq_dist = FreqDist(filtered_words)

# Get the most common words and their frequencies
most_common_words = freq_dist.most_common(20)  # Change the number as desired

# Prepare the data for plotting
x = [get_display(reshape(word)) for word, _ in most_common_words]
y = [count for _, count in most_common_words]

# Plot the word frequency distribution
plt.figure(figsize=(12, 6))
plt.bar(x, y)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Word Frequency Distribution')
plt.xticks(rotation=45, ha='right')
plt.show()
