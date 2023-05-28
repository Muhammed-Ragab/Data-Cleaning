import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import string
import glob

# Download the NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Ask for the stopwords CSV file path
stopwords_path = input("Enter the path to the stopwords CSV file: ")

# Read the stopwords CSV file
with open(stopwords_path, 'r', encoding='utf-8') as stopwords_file:
    stopwords_list = [word.strip() for word in stopwords_file]

# Get a list of TXT files in the current directory
txt_files = glob.glob('*.txt')

# Tokenize each TXT file and save the tokenized data to a CSV file
for txt_file in txt_files:
    # Read the TXT file
    with open(txt_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text and exclude stopwords, verbs, punctuation marks, and numbers
    tokens = word_tokenize(text)
    punctuations = string.punctuation + 'ـ'
    filtered_tokens = [token for token in tokens if token not in stopwords_list and nltk.pos_tag([token])[0][1] not in ['VB', 'RB']
                       and not token.isdigit() and token not in punctuations]

    # Save the filtered tokens to a CSV file with the same name as the TXT file
    output_file_path = f"{txt_file.split('.')[0]}.csv"
    with open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Token'])  # Write header row
        writer.writerows(zip(filtered_tokens))  # Write filtered tokens

    print(f"Tokenized data for {txt_file} saved to CSV successfully.")
