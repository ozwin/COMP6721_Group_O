import splitfolders
from pathlib import Path
inputFolder = "C:\\Personal\\Snake_Species_Recognition\\Dataset\\35-classes\\dataset"
splitfolders.ratio(inputFolder,output="C:\\Personal\\Snake_Species_Recognition\\Dataset\\35-classes\\dataset\\data",seed=44,ratio=(0.7,0.2,0.1), group_prefix=None)



