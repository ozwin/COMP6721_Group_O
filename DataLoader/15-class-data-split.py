import splitfolders
from pathlib import Path
inputFolder = "C:\\Personal\\Snake_Species_Recognition\\Dataset\\15-classes\\train"
splitfolders.ratio(inputFolder,output="C:\\Personal\\Snake_Species_Recognition\\Dataset\\15-classes\\data",seed=44,ratio=(0.9,0.1), group_prefix=None)



