:: Read user data and initialize variables
set SoftwareFolder=%CD%\
set ElastixFolder=elastix-5.2.0-win64\
set /p DataFolder=Enter Data folder (Ex: Data\): 
set OutDirectory=%DataFolder%Results\

:: Install and download data
set PYTHON_VERSION=3.10.8
set INSTALL_PATH=C:\Python310
set INSTALLER=python-installer.exe
curl -o %INSTALLER% https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
%INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 TargetDir=%INSTALL_PATH%
del %INSTALLER%
pip install nibabel
set output_file=downloaded_file.zip
curl -o %output_file% https://drive.switch.ch/index.php/s/rkqOO3adjmJVlMz/download
mkdir "%DataFolder%"
tar -xf %output_file% -C %DataFolder%
del downloaded_file.zip
curl -L -o elastix-5.2.0-win64.zip https://github.com/SuperElastix/elastix/releases/download/5.2.0/elastix-5.2.0-win64.zip
mkdir %SoftwareFolder%%ElastixFolder%
tar -xf elastix-5.2.0-win64.zip -C %SoftwareFolder%%ElastixFolder%
del elastix-5.2.0-win64.zip
curl -L -o Par0035.RIRE.MI.ri.ASGDPrime.txt https://raw.githubusercontent.com/SuperElastix/ElastixModelZoo/master/models/Par0035/Par0035.RIRE.MI.ri.ASGDPrime.txt
move Par0035.RIRE.MI.ri.ASGDPrime.txt %SoftwareFolder%%ElastixFolder%

:: Preparation
set DataFolder=%DataFolder%\TopCoW2024_Data_Release\
set ParameterFile1=%SoftwareFolder%%ElastixFolder%Par0035.RIRE.MI.ri.ASGDPrime.txt
python %SoftwareFolder%Utilities\EditParameterFile.py %ParameterFile1%
if exist "%OutDirectory%" (
    :: Remove the folder and its contents
    rd /s /q "%OutDirectory%"
)
mkdir "%OutDirectory%"
copy %ParameterFile1% %OutDirectory%

:: Computation
setlocal enabledelayedexpansion
for /L %%i in (1, 1, 165) do (
	set "num=00%%i"
    set "num=!num:~-3!"
	mkdir "%OutDirectory%Out!num!\"	
	%SoftwareFolder%%ElastixFolder%elastix -f %DataFolder%\imagesTr\topcow_mr_!num!_0000.nii.gz -m %DataFolder%\imagesTr\topcow_ct_!num!_0000.nii.gz ^
		-out %OutDirectory%Out!num!\ -p %ParameterFile1% 
	%SoftwareFolder%%ElastixFolder%transformix -in %DataFolder%\cow_seg_labelsTr\topcow_ct_!num!.nii.gz -out %OutDirectory%Out!num!\ ^
		-tp %OutDirectory%Out!num!\TransformParameters.0.txt	
	python %SoftwareFolder%Utilities\ReadNiiSegmentationAndBinarize.py %OutDirectory%Out!num!\result.nii.gz ^
		--output %OutDirectory%Out!num!\SegmentationCTtoMRI.nii.gz
	python %SoftwareFolder%Utilities\ReadNiiSegmentationAndBinarize.py %DataFolder%\cow_seg_labelsTr\topcow_mr_!num!.nii.gz ^
		--output %OutDirectory%Out!num!\SegmentationMRI.nii.gz
	python %SoftwareFolder%Utilities\ComputeDiceV2.py %OutDirectory%Out!num!\SegmentationCTtoMRI.nii.gz %OutDirectory%Out!num!\SegmentationMRI.nii.gz ^
		%DataFolder%\roi_loc_labelsTr\topcow_mr_!num!.txt !num! %OutDirectory%Dices.txt
)
