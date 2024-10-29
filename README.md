# Register-the-TopCoW
DOS Batch script to register the brain CT and MRI images from the TopCoW challenge (https://topcow24.grand-challenge.org/).

In this challenge, images are not aligned, then if both images need to be pixel-wise comparable for further combined CT-MRI analysis, then registration is needed.

CT images are aligned to MRI images as they have better quality. Registrations are done using Elastix tool using the parameters described in "http://37-97-228-132.colo.transip.net/modelzoo/par0035/" for CT and MRI registration.

Execute RegisterTopCow.bat, then in the command prompt you will be asked to input the data folder.

The script will download the raw data and several tools such as Elastix. Then each CT image from folder imagesTr is register to the MRI image with the same number. 

At the end, 165 registered CT to MRI images are obtained in the Results folder given by the files result.0.nii.gz.

Below an example showing the middle slice of the original CT and MRI images, and the resulting registered CT image.

<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/user-attachments/assets/69ed649d-67a8-4f36-b321-afe142c5b012" alt="Image 1" width="200" />
    <img src="https://github.com/user-attachments/assets/f0df2a80-d66e-4b34-85ea-c3ab63ee8e80" alt="Image 2" width="200" />
    <img src="https://github.com/user-attachments/assets/32b03bef-3d3f-4257-b04d-df6184951cab" alt="Image 2" width="200" />
</div>

To evaluate the registration, the script also generates a text file (Results\Dices.txt), with the dice overlap between the registered CT manual segmentations and MRI segmentation of the circle of Willis. The original segmentations for CT and MRI are located in the folder cow_seg_labelsTr, the registered segmentation are in the Results folder by the name SegmentationCTtoMRI.nii.gz.
