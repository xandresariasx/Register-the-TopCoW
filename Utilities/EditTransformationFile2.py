import argparse

parser = argparse.ArgumentParser(description="Edit transformation file to do the inverse")
parser.add_argument('file_path1', type=str, help='Path to Inverse file')
args = parser.parse_args()

# Input and output file paths
inverse_file = args.file_path1

        
           
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
        outfile.write(line)



