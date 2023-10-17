# Function to clean the extracted words
def clean_words(words):
    cleaned_words = [word.lower() for word in words]
    return cleaned_words

# Function to save cleaned words to a plain text file
def save_to_text_file(words, filename):
    with open(filename, 'a') as file:
        for word in words:
            file.write(word + '\n')

# Define the input text file path
input_file = 'cleaned_words.txt'

# Define the chunk size (adjust as needed)
chunk_size = 100000  # Read 100,000 lines at a time

# Open the output file in write mode (create a new file)
with open('lowercase_words.txt', 'w') as output_file:
    pass  # Create an empty file

# Process the input file in chunks
with open(input_file, 'r') as file:
    chunk = []
    for line in file:
        line = line.strip()
        chunk.append(line)

        if len(chunk) >= chunk_size:
            cleaned_words = clean_words(chunk)
            save_to_text_file(cleaned_words, 'lowercase_words.txt')
            chunk = []

    # Process the remaining lines (last chunk)
    if chunk:
        cleaned_words = clean_words(chunk)
        save_to_text_file(cleaned_words, 'lowercase_words.txt')