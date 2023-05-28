import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk import pos_tag
from nltk.corpus import stopwords
from bidi.algorithm import get_display
import arabic_reshaper

# Read the words from the CSV file with UTF-8 encoding
words_file_path = 'AM.csv'
words_df = pd.read_csv(words_file_path, encoding='utf-8')

# Read the custom stopwords from the CSV file with UTF-8 encoding
stopwords_file_path = 'stopwords.csv'
stopwords_df = pd.read_csv(stopwords_file_path, encoding='utf-8')

# Extract the words and stopwords as lists
words = words_df['Token'].tolist()
stopwords = stopwords_df['stopword'].tolist()

# Function to filter words based on POS tags (exclude verbs and include only names)
def filter_words(word_list):
    tagged_words = pos_tag(word_list)
    filtered_words = [word for word, pos in tagged_words if pos.startswith('NN')]
    return filtered_words

# Filter the words based on POS tags
filtered_words = filter_words(words)

# Remove stopwords
filtered_words = [word for word in filtered_words if word not in stopwords]

# Create a custom WordCloud object with the provided stopwords and font path for Arabic text
wordcloud = WordCloud(stopwords=[], font_path='Amiri-Regular.ttf')

# Generate the word cloud with reshaped Arabic text
reshaped_text = arabic_reshaper.reshape(' '.join(filtered_words))
text = get_display(reshaped_text)
wordcloud.generate(text)

# Save the word cloud as SVG
output_file_path = 'AM.svg'
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig(output_file_path, format='svg')

# Display the word cloud
plt.show()
