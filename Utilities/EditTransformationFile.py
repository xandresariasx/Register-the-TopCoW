import argparse

parser = argparse.ArgumentParser(description="Edit transformation file to do the inverse")
parser.add_argument('file_path1', type=str, help='Path to Inverse file')
parser.add_argument('file_path2', type=str, help='Path to direct file')  
args = parser.parse_args()

# Input and output file paths
inverse_file = args.file_path1
direct_file = args.file_path2

# Extract the Spacing line from the source file
spacing_prefix = "(Spacing "

with open(direct_file, 'r') as src:
    spacing_line = None
    for line in src:
        if line.strip().startswith(spacing_prefix):
            spacing_line = line.strip()
            break
            
# Extract the Size line from the source file
size_prefix = "(Size "

with open(direct_file, 'r') as src:
    size_line = None
    for line in src:
        if line.strip().startswith(size_prefix):
            size_line = line.strip()
            break            
           
# Define the line prefix to match and the replacement
line_prefix = "(InitialTransformParameterFileName "
replacement_line = '(InitialTransformParameterFileName "NoInitialTransform")'

# Read the file and replace the matching line
with open(inverse_file, 'r') as infile:
    lines = infile.readlines()

# Process lines and replace the matching one
with open(inverse_file, 'w') as outfile:
    for line in lines:
        if line.strip().startswith(line_prefix):  
            line = replacement_line + "\n"
        if line.strip().startswith(spacing_prefix):
            line = spacing_line + "\n"
        if line.strip().startswith(size_prefix):
            line = size_line + "\n"     
        outfile.write(line)



