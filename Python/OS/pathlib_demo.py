from hmac import new
from operator import ne
from pathlib import Path
import os

#Relative path
print("Relative path",Path())

# Get the current working directory
print("Absolute Path",Path().absolute())

#set the path to the current file
print(f"Current File Path:", Path(__file__))

#change current directory to current file path's parent directory
os.chdir(Path(__file__).parent)
print(f"Changed Current Directory: {Path.cwd()}")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(f"BASE_DIR: {BASE_DIR}")


#home directory
print(f"Home Directory: {Path.home()}")


for p in Path().iterdir():
    print(p)
        
        

print(f"File Name: {Path('demo.py').name}")
print(f"File Stem: {Path('demo.py').stem}")
print(f"File Suffix: {Path('demo.py').suffix}")

print(f"File Parent: {Path('demo.py').parent}")
print(f"File Absolute Path: {Path('demo.py').absolute()}")

print(f"File Exists: {Path('demo.py').exists()}")
print(f"File is File: {Path('demo.py').is_file()}")
print(f"File is Directory: {Path('demo.py').is_dir()}")

print(f"Join Path 1: {Path('OS').joinpath('txt1')}")
print(f"Join Path 2: {Path('OS') / 'txt1'}")

os.chdir(BASE_DIR)
print(f"Changed Current Directory: {Path.cwd()}")

for p in Path().rglob('*.txt'):
    print(p)
    
    
new_path= Path()/"Python"/"OS"
os.chdir(new_path)
print(f"Changed Current Directory: {Path.cwd()}")

for p in Path().rglob('*.log'):
    print(p)
    with open(p, 'r') as file:
        print(file.read())
        
        
        
# Create a new directory
new_dir = Path('new_directory')
if not new_dir.exists():
    new_dir.mkdir()
    print(f"Directory {new_dir} created")
    
# Create a new file
new_file = new_dir / 'new_file.txt'
if not new_file.exists():
    Path.touch(new_file)
    print(f"File {new_file} created")
    
multi_lvl_dir = Path('multi_level_dir/sub_dir')
if not multi_lvl_dir.exists():
    multi_lvl_dir.mkdir(parents=True)
    print(f"Multi-level directory {multi_lvl_dir} created")
    
Path(new_file).write_text("Hello, World!")

Path(new_file).replace(new_file.with_stem('renamed_file'))
print(f"File renamed to {new_file.stem}")

# Delete the file
Path(new_file.parent/"renamed_file.txt").unlink()
print(f"File {new_file} deleted")