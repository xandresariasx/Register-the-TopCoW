import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_path1', type=str)
args = parser.parse_args()
file_path = args.file_path1


# Input and output file paths
input_file = file_path
output_file = file_path

# Define the line to replace and the replacement
# old_line = '(Metric "AdvancedMattesMutualInformation")'
# new_line = '(Metric "DisplacementMagnitudePenalty")'

metric_prefix='(Metric '
metric_line='(Metric "DisplacementMagnitudePenalty")'

resolution_prefix='(NumberOfResolutions '
resolution_line='(NumberOfResolutions 20)'

pyramid_prefix='(ImagePyramidSchedule '
pyramid_line='//(ImagePyramidSchedule 4 4 4 2 2 2 1 1 1)'

# Open the file, read, modify, and write back
with open(input_file, 'r') as infile:
    lines = infile.readlines()

# Replace the line
with open(output_file, 'w') as outfile:
    for line in lines:
        # if old_line in line:
            # line = line.replace(old_line, new_line)
        # outfile.write(line)        
        if line.strip().startswith(metric_prefix):  
            line = metric_line + "\n"
        if line.strip().startswith(resolution_prefix):
            line = resolution_line + "\n"
        if line.strip().startswith(pyramid_prefix):
            line = pyramid_line + "\n"
        outfile.write(line)
