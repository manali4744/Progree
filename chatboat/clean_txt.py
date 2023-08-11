# Read the input file
with open('output.txt', 'r') as file:
    lines = file.readlines()

# Remove duplicates while maintaining order
unique_lines = list(dict.fromkeys(lines))

# Write the unique lines back to the file
with open('input.txt', 'w') as file:
    file.writelines(unique_lines)
