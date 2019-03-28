#-*-coding:utf-8-*-
import os
import xml.etree.ElementTree as ET

dirPath='file/'

# 读取目录下的所有xml 文件，并逐一解析
def ReadXmlFile(dirPath):
    list=os.listdir(dirPath)
    fileList=[]
    for file in list:
        if file.find(".xml")>-1:
            fileList.append(os.path.join(dirPath,file))
    for file in  fileList:
        ReadXmlContent(file)
# 解析xml 文件内容
def ReadXmlContent(filePath):
    tree=ET.ElementTree(file=filePath)
    for node in tree.iter(tag='productlist'):
        strText="%s\t%s"%(node.attrib['AreaCode'],node.attrib['Desciption'])
        SaveToTxt(strText)
# 保存txt 文件
def SaveToTxt(strText):
    with open(os.path.join(dirPath,'result.txt'),'a',encoding='utf-8') as f:
        f.writelines(strText+'\n')

if __name__ == "__main__":
    ReadXmlFile(dirPath)