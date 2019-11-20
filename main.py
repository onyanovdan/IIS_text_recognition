import os
import process as P

folder = "texts"
for file in os.listdir(os.path.join(folder)):
    fileName = os.path.join(folder, file)
    # print(os.path.basename(fileName))
    # print(os.path.dirname(fileName))
    P.runImagesFuller(fileName)
