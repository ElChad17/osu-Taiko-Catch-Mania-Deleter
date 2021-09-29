import os

def getFiles():
    files= os.listdir()
    for i in files:
        if '.osu' in i:
            textFileName = i.replace('.osu','.txt')
            os.rename(i,textFileName)
            try:
                text = open(textFileName,'r',errors="ignore").read().splitlines()
                if text[9] != 'Mode: 0':
                    os.remove(textFileName)
                    print('Removed',i)
                else:
                    os.rename(textFileName,i)
                
            except Exception as e:
                print(e)
                os.rename(textFileName,i)
                print(i)
                print()


folders = os.listdir()
for i in folders:
    if os.path.isdir(i):
        os.chdir(i)
        getFiles()
        os.chdir('..')


