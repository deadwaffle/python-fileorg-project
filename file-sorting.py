import os
import shutil
from os import path
from datetime import datetime

# function that returns file extension 
def get_extension(str):
    temp = ''
    for each in reversed(str):
        temp += each 
        if each == '.':
            break
    return temp[::-1]

#function that returns a dictionary of extentions and counts of the files in given folder.
def get_ext_dic(str):
    ls = os.listdir(str)
    dic = {}
    for each in ls:
        if path.isdir(path.join(str,each)):
            if 'dir' not in dic.keys():
                dic['dir'] = 1
            else: 
                dic['dir'] += 1
        else:
            ext = get_extension(each)
            if ext not in dic.keys():
                dic[ext] = 1
            else:
                dic[ext] += 1
    return dic

# file formats
folder_dic = {
    'Music':['.mp3','.wav','.MP3','.WAV'],
    'Videos':['.mp4','.mkv','.avi','.webm','.MP4','.MKV','.AVI','.WEBM'],
    'Zips and Torrents':['.torrent','.TORRENT','.zip','.ZIP','.rar','.RAR','.tar','.TAR','.gz','.GZ'],
    'Images':['.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp','.png', '.gif', '.webp', '.svg', '.apng', '.avif'],
    'Documents':['.PDF','.pdf','.DOC','.DOCX','.doc','.docx','.ppt','.pptx','.PPT','.PPTX','.txt','.TXT'],
    'Programs':['.exe','.EXE','.msi','.MSI']
}
exceptions = ['Music','Videos','Zips and Torrents','Programs','Images','Folders','Documents','Others','logs.txt']

# creating required folders and log file
def init(path_str):
    for each in exceptions:
        full_path = path.join(path_str,each)
        if not path.exists(full_path):
            if '.' not in each:
                os.mkdir(full_path)
    if not path.exists(path.join(path_str,'logs.txt')):
        log_file = open(path.join(path_str,'logs.txt'),'w')
        log_file.write('<< log file created by file-sorting.py *Original code created by sahankj2000 >>\n')
        log_file.close()
      
# function that starts organizing
def start(path_str):
    init(path_str)
    ls = os.listdir(path_str)
    log_file = open(path.join(path_str,'logs.txt'),'a')
    log_file.write('\n<< New Session Started at \"'+path_str+'\" on \"'+str(datetime.now())[:19:]+'\">>\n')
    for each in ls:
        ls = ''
        if each not in exceptions:
            full_path = path.join(path_str,each)
            log_str = '\"'+each+'\" moved to '
            if path.isdir(full_path):
                shutil.move(full_path,path.join(path_str,'Folders',each))
                log_str += 'Folders on \"'+str(datetime.now())[:19:]+'\"'
            else:
                ext = get_extension(each)
                found = False
                for key in folder_dic.keys():
                    if ext in folder_dic[key]:
                        shutil.move(full_path,path.join(path_str,key,each))
                        log_str += key+' on \"'+str(datetime.now())[:19:]+'\"'
                        found = True
                        break
                if not found:
                    shutil.move(full_path,path.join(path_str,'Others',each))
                    log_str += 'Others on \"'+str(datetime.now())[:19:]+'\"'
            log_file.write(log_str+'\n')
            print(log_str)
    log_file.write('<< Session ended on \"'+str(datetime.now())[:19:]+'\" >>\n')
    log_file.close()

# organizes the folder its in
current_path = os.getcwd()

# uncomment the below line and add your path to give a custom path
# current_path = "ex: C:/Users/User1/Downloads"

start(current_path)  