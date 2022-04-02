import os


def afficherTableau(tableau):
    for i in range(len(tableau)):
        print(tableau[i], end="\n")


folders = os.listdir("./images/")

for folder in folders:
    files = os.listdir("./images/"+folder)
    for file in files:
        # os.remove("./images/"+folder+"/"+file)
        os.rename("./images/"+folder+"/"+file,
                  "./images/"+folder+"/"+file.replace(" ", "_"))
