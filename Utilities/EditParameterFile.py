# Define the file path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_path1', type=str)
args = parser.parse_args()
file_path = args.file_path1

# Read the content of the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Modify the last line if it matches the target string
if lines[-1].strip() == '(ResultImageFormat "mha")':
    lines[-1] = '(ResultImageFormat "nii.gz")\n'

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.writelines(lines)

