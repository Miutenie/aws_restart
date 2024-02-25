# read file content
with open("preproinsulin-seq.txt", "r") as input_file:
    content =input_file.readlines()
    
print(content)

# delete the first and last lines
remaining_lines = content[1:-1]
print(remaining_lines)

#remove the spaces and last lines
processed_lines = []
for line in remaining_lines:
    line = line.replace('','')
    line = line.replace('\n','')
    processed_lines.append(line.lstrip('123456789'))
    
print(processed_lines)

# write the result in a new line
with open("preproinsulin-processed.txt", 'w') as output_file:
    output_file.writelines(processed_lines)
    
# print the number of lower characters save in the processed file    
lowercase_count = 0
with open("preproinsulin-processed.txt", 'r') as output_file:
    content = file.read()
    for char in content:
    if (char.islower()):
           lowercase_count += 1

print(lowercase_count)

# function that reads the amino accids and write the amino accids corresponding to a given range in a specific file
def extract_and_save_animo_acids(input_file, start, end, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
# extract the sequence of amino accids which corresponds to a given range
amino_acids_sequence = content[start-1:end]

with open(output_file, 'w') as file:
    file.write(amino_acids_sequence)
    
print(f'The file named {output_file} contains {len(amino_acids_sequence)} characters')    


#extract_and_save_animo_acids('preproinsulin_processed.txt', 1, 24, "lsinsulin-seq-clean.txt")