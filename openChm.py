#本脚本用于解压chm帮助文档的内容
import os
original_chm = r'C:\Users\Administrator\Desktop\大漠插件接口说明.chm'
root_dir = r'C:\Users\Administrator\Desktop\dm'
seperator = os.sep
#    HH.EXE -decompile <输出路径> <目标chm文件>
decomplile_cmd = 'HH.EXE -decompile %s %s' % (root_dir, original_chm)
os.system(decomplile_cmd)
