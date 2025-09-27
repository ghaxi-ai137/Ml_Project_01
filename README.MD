# created a ML project folder
# Creating a virtual environment in windows
python --version to check python version
To clear the terminal we use "clear" command
python -m ven ven_name
python -m venv mlpro to create a virtual environment
# Action the virtual environment
<!-- ./ven_name/Scripts/activate -->
./mlpro/Scripts/activate
# incase you get an error while activating virtual environment
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

pwd - present working directory
cd - to move a specific directory
ls - to list all files

# to install all libraries from requirements file
cd backend
pip install -r requirements.txt
cd .. #come out of backend

# git init
# git add backend/ frontend/ README.MD
# git commit -m "v1"

git remote add origin https://github.com/mujeebr/Ml_Project_Bidar.git
git branch -M main
git push -u origin main


# from second time

git add modified files
# git commit -m "v1"
git push -u origin main