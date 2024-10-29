# Register-the-TopCoW
DOS Batch script to register the brain CT and MRI images from the TopCoW challenge (https://topcow24.grand-challenge.org/).

In this challenge, images are not aligned, then if both images need to be pixel-wise comparable for further combined CT-MRI analysis, then registration is needed.

CT images are aligned to MRI images as they have better quality. Registrations are done using Elastix tool using the parameters described in "http://37-97-228-132.colo.transip.net/modelzoo/par0035/" for CT and MRI registration.

Execute RegisterTopCow.bat, then in the command prompt you will be asked to input the data folder.

The script will download the raw data and several tools such as Elastix. Then each CT image from folder imagesTr is register to the MRI image with the same number. 

At the end, 165 registered CT to MRI images are obtained in the Results folder given by the files result.0.nii.gz.

![CT](https://github.com/user-attachments/assets/69ed649d-67a8-4f36-b321-afe142c5b012)

![MR](https://github.com/user-attachments/assets/f0df2a80-d66e-4b34-85ea-c3ab63ee8e80)


![CTtoMR](https://github.com/user-attachments/assets/32b03bef-3d3f-4257-b04d-df6184951cab)
