import os
import glob

# specify the path of your cloned repository
repo_path = '/mnt/c/Users/Rishabh/OneDrive/Desktop/github/next13-ai-saas-master'

# find all .tsx files in the repository
tsx_files = glob.glob(os.path.join(repo_path, '**/*.tsx'), recursive=True)

print(f"Found {len(tsx_files)} .tsx files.")

# specify the output file where all .tsx files content will be written
output_file = 'output.tsx'

# open the output file in write mode
with open(output_file, 'w', encoding='utf-8') as outfile:
    # iterate through each .tsx file
    for file in tsx_files:
        print(f"Processing: {file}")
        # open each .tsx file in read mode
        with open(file, 'r', encoding='utf-8') as infile:
            # write the relative path of the file as a comment
            relative_path = os.path.relpath(file, repo_path)
            outfile.write('// File: ' + relative_path + '\n')
            # read the contents of the file
            file_contents = infile.read()
            # write the contents to the output file
            outfile.write(file_contents)
            # write a newline character to separate the contents of different files
            outfile.write('\n')
