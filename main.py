import re

# Function to extract [[]] words from text
def extract_double_brackets(text):
    pattern = r'\[\[(.*?)\]\]'  # Regular expression pattern to match [[]] words
    matches = re.findall(pattern, text)  # Find all matches in the text
    return matches

# Function to save extracted words to a plain text file
def save_to_text_file(words, filename):
    with open(filename, 'a') as file:  # Use 'a' to append to the file instead of overwriting
        for word in words:
            file.write(word + '\n')

# Define the XML file path
xml_file = './enwiki-latest-pages-articles.xml'

# Define the chunk size (adjust as per your system's memory limitations)
chunk_size = 1000000  # Adjust the chunk size as needed

# Open the XML file and process it in chunks
with open(xml_file, 'r') as file:
    buffer = ''  # Buffer to store the partial XML content

    while True:
        chunk = file.read(chunk_size)  # Read a chunk from the file

        if not chunk:  # If no more content, exit the loop
            break

        buffer += chunk  # Add the chunk to the buffer

        # Process the buffer and extract [[]] words
        while True:
            match = re.search(r'<page>(.*?)</page>', buffer, re.DOTALL)  # Match <page>...</page> tags
            if not match:  # If no more matches, break the inner loop
                break

            page_content = match.group(1)  # Get the content within <page>...</page> tags
            words = extract_double_brackets(page_content)  # Extract [[]] words from the content
            save_to_text_file(words, 'extracted_words.txt')  # Save the extracted words to a file

            buffer = buffer[match.end():]  # Remove the processed content from the buffer

        # Move the remaining content to the beginning of the buffer
        buffer = buffer[-len('</page>') :]
