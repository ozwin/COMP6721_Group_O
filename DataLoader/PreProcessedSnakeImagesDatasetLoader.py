# Reference for train test and val split https://www.youtube.com/watch?v=C6wbr1jJvVs
#run pip install split-folders
import splitfolders
inputFolder = '/home/keena/PycharmProjects/SnakeSpeciesDetection/DataSets/preprocessed-cleaned-set/train'
splitfolders.ratio(inputFolder,output="/home/keena/PycharmProjects/SnakeSpeciesDetection/DataSets/preprocessed-cleaned-set/preprocessedSnake",seed=42,ratio=(0.7,0.2,0.1), group_prefix=None)