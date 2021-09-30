import os, shutil

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
                    print('Removed',i,'\n')
                else:
                    os.rename(textFileName,i)
                
            except Exception as e:
                os.rename(textFileName,i)


folders = os.listdir()
for i in folders:
    if os.path.isdir(i):
        os.chdir(i)
        getFiles()
        os.chdir('..')

for folder in folders: #This removes any folders without .osu files
    if os.path.isdir(folder):
        os.chdir(folder)
        
        files = os.listdir()
        osuFile =  False
        for file in files:
            if '.osu' in file:
                osuFile=True
                break
            
        if osuFile == False:
            print('Removing folder',folder,'as it contains no .osu files\n')
            os.chdir('..')
            shutil.rmtree(folder)
            
        else:
            os.chdir('..')

pause = input('Finished, press enter to close this window')

    
    
