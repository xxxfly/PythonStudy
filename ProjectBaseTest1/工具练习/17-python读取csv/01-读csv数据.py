# -*- coding: utf-8 -*-
import csv
import io

base_file='File/test4.csv'


def redCsvFile(filePath):
    with open(filePath,'r',encoding='utf-8') as f:
        csv_file=csv.reader(f)
        dat_index=289
        count=0
        content='' 
        for item in csv_file:
            try:
                userid=item[1]+"$"   
            except Exception as ex:
                print(ex)
            content=content+userid+'\n'            
            count=count+1        
            if count>=5000:                
                fileName='File/data'+str(dat_index)+'.dat'
                print('生成文件：'+fileName)
                with open(fileName,'w',encoding='utf-8') as fw:
                    fw.write(content)
                content=''
                count=0
                dat_index=dat_index+1
        fileName='File/data'+str(dat_index)+'.dat'
        print('生成文件：'+fileName)
        with open(fileName,'w',encoding='utf-8') as fw:
            fw.write(content)
        
        print('完成操作')
                            
                
        
if __name__ == "__main__":
    redCsvFile(base_file)