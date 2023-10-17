from collections import defaultdict

# Define the input text file path
input_file = 'lowercase_words.txt'
output_file = 'sorted_words.txt'

# Create a dictionary to store word counts
word_counts = defaultdict(int)

# Specify the excluded prefixes or keywords
excluded_prefixes = ['wikipedia:', 'category:', 'user:', 'wp:', 'en:', 'hispanic', 'latino']

# Process the input file and count word occurrences
with open(input_file, 'r') as file:
    for line in file:
        word, count = line.strip().split(': ')
        if not any(word.startswith(prefix) for prefix in excluded_prefixes):
            word_counts[word] = int(count)

# Sort the words by their counts in descending order
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Save the sorted words and their counts to a text file
with open(output_file, 'w') as file:
    for word, count in sorted_words:
        file.write(f"{word}: {count}\n")

# Print the top 10 most frequent words
print("Top 10 most frequent words:")
for word, count in sorted_words[:10]:
    print(f"{word}: {count}")