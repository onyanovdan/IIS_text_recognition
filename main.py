import os
import process as P

folder = "texts"
for file in os.listdir(os.path.join(folder)):
    if os.path.splitext(file)[1] == '.txt':
        fileName = os.path.join(folder, file)
        # print(os.path.basename(fileName))
        # print(os.path.dirname(fileName))
        P.runImagesFuller(fileName)
