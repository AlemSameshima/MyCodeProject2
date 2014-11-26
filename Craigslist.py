# importing random for use picking an option from the list of words
import random

# reads the file and enters the text from the file in the fileString string var
# the default file is C:\Python34\test.txt but can be overridden by providing a path when calling read_file
def read_file(path='craigslist.txt'): 
    global fileString      
    source = open(path,'r')
    fileString = source.read()

# execute the read_file function and set some defaults
read_file()
outputString = str()
startIndex = 0

# read from the start to the end of the file looking for the tags.
while startIndex < len(fileString):
    startOptions = 0
    endOptions = 0
    holderString = str()
    randomOption = str ()

# if a tag is found, set startTag to the beginning of the first tag
# if a tag is found, set startOptions to the first character of the list
# if a tag is found, set endOptions to the character just before the end tag            
    startTag = fileString.find('<select>',startIndex,len(fileString))
    startOptions = startTag + 8
    endOptions = fileString.find('</select>',startIndex,len(fileString))

# if something exists for startTag, it means a tag was found
# pull out the list and choose an option to add to the output string
    if startTag != -1:
        outputString += fileString[startIndex:startTag]
        optionsList = []
        del optionsList[:]
        startIndex2 = 0
        listIndex = 0
        barSymbol = -1
        holderString = fileString[startOptions:endOptions]
        holderStringLen = len(holderString)
        while startIndex2 < holderStringLen:
            barSymbol = holderString.find('|',startIndex2,holderStringLen)
            if barSymbol != -1:
                optionsList.insert(listIndex,holderString[startIndex2:barSymbol])
                startIndex2 = barSymbol +1
            else:
                optionsList.insert(listIndex,holderString[startIndex2:holderStringLen])
                startIndex2 = holderStringLen        
            listIndex += 1
        startIndex = endOptions + 9
        randomOption = random.choice(optionsList)
        outputString += randomOption

# if startTag is -1, there are no tags found. Output the rest of the file.    
    if startTag == -1:
        outputString += fileString[startIndex:len(fileString)]
        startIndex = len(fileString)

# write file to output finished document
saveFile = open('CraigslistFinished.txt','w')
saveFile.write(outputString)
saveFile.close()



