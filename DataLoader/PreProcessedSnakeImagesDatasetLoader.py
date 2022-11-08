# Reference for train test and val split https://www.youtube.com/watch?v=C6wbr1jJvVs
#run pip install split-folders
import splitfolders
from pathlib import Path
inputFolder = Path('C:\\Personal\\Snake_Species_Recognition\\Dataset\\5-class\\preprocessed-cleaned-set\\train')
splitfolders.ratio(inputFolder,output="C:\\Personal\\Snake_Species_Recognition\\Dataset\\5-class\\preprocessed-cleaned-set\\data",seed=42,ratio=(0.7,0.2,0.1), group_prefix=None)