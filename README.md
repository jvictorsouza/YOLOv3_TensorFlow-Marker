## Yolo marker

![screenshot](./screen.png)

### Install virtualenv via pip:
pip install virtualenv

### Test your installation
virtualenv --version



### Create the virtualenv for the project
cd yolo-marker\
virtualenv .env -p python3 --no-site-packages

### To begin using the virtual environment, it needs to be activated:
. .env/bin/activate

### Intall the packages
pip install -r requirements.txt

### Run the application
python3 marker.py -p "PATH_WITH_IMGS/*EXTENSION\" -d WIDTH HEIGHT\ -m MERGE_FLAG-TXT_IMAGES(OPTIONAL)
Eg.:  python3 marker.py -p "demo/train/*.jpg" -d 1920 1080 -m true

#### If you are done working in the virtual environment for the moment, you can deactivate it:
deactivate


## .txt files for Yolo train

### Run the script to generate the txt files
#### write_img_names - the images' path will be data/img
python write_img_names.py -p \"PATH_WITH_IMGS/*EXTENSION\" -ptrain [0..1] [-v]\
Eg1.: python write_img_names.py -p \"/Users/leandrobmarinho/img/\*.png\" -ptrain .95 -v\
Eg2.: python write_img_names.py -p \"/Users/leandrobmarinho/img/\*.png\" -ptrain .95

#### write_img_names_2 - the images' path will be the absolute path, and if there is not marked images, they will not be counted to the train and test files
python write_img_names_2.py -p \"PATH_WITH_IMGS/*EXTENSION\" -ptrain [0..1] [-v]\
Eg1.: python write_img_names_2.py -p \"/Users/leandrobmarinho/img/\*.png\" -ptrain .95 -v\
