import numpy as np
import nibabel as nib
import argparse

# Function to read the ROI from the text file
def read_roi_info(roi_file_path):
    with open(roi_file_path, 'r') as file:
        lines = file.readlines()
    
    # Parse size and location of ROI
    size_line = lines[1].strip()
    location_line = lines[2].strip()
    
    # Extract ROI size and location (convert to integers)
    size = tuple(map(int, size_line.split(':')[-1].strip().split()))
    location = tuple(map(int, location_line.split(':')[-1].strip().split()))
    
    return size, location

# Function to compute Dice similarity coefficient within an ROI
def dice_coefficient_roi(seg1, seg2, roi_size, roi_origin):
    # Extract the ROI from both segmentation arrays
    x, y, z = roi_origin
    dx, dy, dz = roi_size
    roi_seg1 = seg1[x:x+dx, y:y+dy, z:z+dz]
    roi_seg2 = seg2[x:x+dx, y:y+dy, z:z+dz]

    # Ensure both ROIs are binary (0 and 1)
    roi_seg1 = (roi_seg1 > 0).astype(np.bool_)
    roi_seg2 = (roi_seg2 > 0).astype(np.bool_)

    # Calculate intersection and sums within the ROI
    intersection = np.logical_and(roi_seg1, roi_seg2).sum()
    seg1_sum = roi_seg1.sum()
    seg2_sum = roi_seg2.sum()

    # Handle edge case where both segmentations are empty in the ROI
    if seg1_sum + seg2_sum == 0:
        return 1.0

    # Compute Dice coefficient
    dice = 2. * intersection / (seg1_sum + seg2_sum)
    return dice
 
 
# Load the NIfTI file
def load_nifti(file_path):
    nifti_img = nib.load(file_path)      # Load the .nii.gz file
    nifti_data = nifti_img.get_fdata()   # Get the image data as a numpy array
    affine = nifti_img.affine            # Get the affine transformation matrix
    header = nifti_img.header            # Get the header information
    return nifti_data, affine, header    
    
# Function to save the Dice coefficient to a text file
def save_dice_to_file(dice_value, FileNumber, output_path):
    with open(output_path, 'a') as file:
        file.write(f"Dice Similarity Coefficient({FileNumber}): {dice_value:.4f}\n")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Compute Dice from two NIfTI (.nii.gz) files")
    parser.add_argument('file_path1', type=str, help='Path to the .nii.gz file')
    parser.add_argument('file_path2', type=str, help='Path to the .nii.gz file')
    parser.add_argument('file_pathROI', type=str, help='Path to the ROI file')
    parser.add_argument('FileNumber', type=str, help='File number')
    parser.add_argument('Outfile_path', type=str, help='Path to the .nii.gz file')
    
    args = parser.parse_args()

    # Load the NIfTI file1
    nifti_data1, affine1, header1 = load_nifti(args.file_path1)
    
    # Load the NIfTI file2
    nifti_data2, affine2, header2 = load_nifti(args.file_path2)   

    # Read ROI information
    roi_size, roi_origin = read_roi_info(args.file_pathROI)    

    # Compute Dice coefficient within the specified ROI
    dice_value = dice_coefficient_roi(nifti_data1, nifti_data2, roi_size, roi_origin)
    print(dice_value)
    
    # Save the Dice coefficient to a text file
    save_dice_to_file(dice_value, args.FileNumber, args.Outfile_path)
   

# Entry point
if __name__ == "__main__":
    main()