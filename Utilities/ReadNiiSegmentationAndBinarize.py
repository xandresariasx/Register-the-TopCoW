import nibabel as nib
import numpy as np
import argparse

# Load the NIfTI file
def load_nifti(file_path):
    nifti_img = nib.load(file_path)      # Load the .nii.gz file
    nifti_data = nifti_img.get_fdata()   # Get the image data as a numpy array
    affine = nifti_img.affine            # Get the affine transformation matrix
    header = nifti_img.header            # Get the header information
    return nifti_data, affine, header
    
# Save the segmentation result as a new NIfTI file
def save_nifti(segmentation_data, affine, header, output_path):
    # Create a new Nifti1Image object
    nifti_img = nib.Nifti1Image(segmentation_data, affine, header)
    # Save the NIfTI image to the specified output path
    nib.save(nifti_img, output_path)
    print(f"Segmentation saved to {output_path}")    

# Visualize a specific slice
def plot_slice(nifti_data, slice_idx, axis=2):
    # Choose which axis to slice (0: Sagittal, 1: Coronal, 2: Axial)
    if axis == 0:
        slice_data = nifti_data[slice_idx, :, :]
    elif axis == 1:
        slice_data = nifti_data[:, slice_idx, :]
    else:
        slice_data = nifti_data[:, :, slice_idx]
    
    plt.imshow(np.rot90(slice_data), cmap='gray')
    plt.axis('off')
    plt.show()

# Main function that accepts file_path, slice_idx, and axis
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Visualize a slice from a NIfTI (.nii.gz) file")
    parser.add_argument('file_path', type=str, help='Path to the .nii.gz file')
    # parser.add_argument('slice_idx', type=int, help='Index of the slice to visualize')
    # parser.add_argument('--axis', type=int, default=2, choices=[0, 1, 2], help='Axis for the slice (0: Sagittal, 1: Coronal, 2: Axial)')
    parser.add_argument('--output', type=str, default=None, help='Path to save the segmentation .nii.gz file')


    args = parser.parse_args()

    # Load the NIfTI file
    nifti_data, affine, header = load_nifti(args.file_path)

   
    # Plot the selected slice
    # plot_slice(nifti_data, args.slice_idx, args.axis)
    
    nifti_segmentation = (nifti_data > 0).astype(np.uint8)
    #plot_slice(nifti_segmentation, 115, 2)
    
    # Save the segmentation result if output path is provided
    if args.output:
        save_nifti(nifti_segmentation, affine, header, args.output)

# Entry point
if __name__ == "__main__":
    main()
