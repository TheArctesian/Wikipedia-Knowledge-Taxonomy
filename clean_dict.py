import re

# Regular expression pattern to match Wikipedia meta articles
pattern = r"^wikipedia:|wp:|category:|project:|help:|user:|en:user:|c:"

# Input file path
input_file_path = "sorted_words.txt"

# Output file path
output_file_path = "filtered_file.txt"

# Open input and output files
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    # Iterate over each line in the input file
    for line in input_file:
        # Check if the line matches the pattern
        if not re.search(pattern, line, re.IGNORECASE):
            # Write the line to the output file
            output_file.write(line)