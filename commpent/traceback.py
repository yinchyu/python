import os
import traceback
import sys
basedir=r"D:\train_dataset\new - 副本"
txtdir=r"D:\train_dataset\new - 副本\txt"
newdir=r"D:\train_dataset\new - 副本\ycy"
counter=0


def removefile():
    global  counter
    for file in os.listdir(txtdir):
        with open(os.path.join(txtdir,file),"r",encoding="gbk") as f:
            for line in f.readlines():
               filename=line.split("\t")[0]
               context=line.split("\t")[1:]
               txtfilename="{}.lab".format(str(counter).zfill(4))
               with open(os.path.join(newdir,txtfilename),"w+",encoding="utf8")as fw:
                   fw.write("".join(context))
               oldwavname=os.path.join(basedir,filename.split("_")[0].upper(),filename.split("_")[0].upper()+filename.split("_")[1]+".pcm.wav")
               newwavname=os.path.join(newdir,"{}.wav".format(str(counter).ljust(4)))
               os.rename(oldwavname,newwavname)
               counter+=1




for filename in os.listdir(newdir):
    cuts=filename.split(" ")
    new=[]
    for i in cuts:
        if i!="":
            new.append(i)
    print(new,filename)
    try:
        newfilename=new[0].zfill(4).strip()+"."+new[1].strip()
        os.rename(os.path.join(newdir,filename),os.path.join(newdir,newfilename))
    except:
        type, value, tracebacks= sys.exc_info()
        traceback.print_exception( type, value, tracebacks)
        # print(traceback.format_exception( type, value, tracebacks))



