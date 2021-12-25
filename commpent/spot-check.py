import sys
import tqdm
import random

def sample():
    with open(sys.argv[2],"r",encoding="utf8")as fr:
        with open(sys.argv[3], "w+", encoding="utf8") as fw1:
            with open(sys.argv[4], "w+", encoding="utf8") as fw2:
                datalines=fr.readlines()
                randomlist = random.sample(range(0, len(datalines)),k=1000)
                for linenum in tqdm.tqdm(randomlist):
                   fw1.write(datalines[linenum].strip()+"\n")
                   fw2.write(datalines[linenum].split("\t")[0]+"\n")





def compare():
    counter=0
    total=0
    errdict={}
    logfile = (open(sys.argv[4], 'w+', encoding='utf8'))
    with open(sys.argv[2],"r",encoding="utf8")as fr1:
        with open(sys.argv[3], "r", encoding="utf8") as fr2:
               fr1lines=fr1.readlines()
               fr2lines=fr2.readlines()
               try:
                   assert  len(fr1lines)==len(fr2lines)
               except:
                   print(len(fr1lines),len(fr2lines))
                   print(fr1lines)
                   print(fr2lines)
                   exit(0)
               for num in range(len(fr1lines)):
                   phonelist1=fr1lines[num].split("\t")[1].split()
                   phonelist2=fr2lines[num].split("\t")[1].split()
                   try:
                       assert len(phonelist1) == len(phonelist2)
                   except:
                       print(len(phonelist1), len(phonelist2))
                       print(fr1lines[num])
                       print(phonelist1)
                       print(phonelist2)
                       exit(0)
                   for   i in range(len(phonelist2)):
                       total+=1
                       if phonelist1[i].strip()==phonelist2[i].strip():
                           continue
                       else:
                           counter+=1
                           if errdict.get(phonelist1[i].strip())is None:
                              errdict[phonelist1[i].strip()]=0
                              errdict[phonelist1[i].strip()]+=1
    error_number = sum(errdict.values())
    correct_number = total - error_number
    accuracy = correct_number / total
    print("details:   error_dict:{}  total_number:{}".format(errdict, total))
    print("accuracy:error_number:{} total_number:{} accuracy:{}".format(error_number, total, accuracy))

    logfile.write("details:   error_dict:{}  total_number:{}".format(errdict, total) +"\n")
    logfile.write("accuracy:error_number:{} total_number:{} accuracy:{}".format(error_number, total, accuracy)+ "\n")

    logfile.close()

if __name__=="__main__":
    #sample()
    funcname=sys.argv[1]
    assert  funcname in ["sample","compare"]
    print("will call  function "+funcname)
    eval(funcname+"()")


# a=['shi2', 'ge2', 'duo1', 'nian2', 'hou4', 'zhu1', 'jiong3', 'ceng2', 'tou4', 'lu4', 'zhe4', 'ci4', 'shang1', 'bing4', 'qi2', 'shi2', 'shi4', 'yi1', 'ci4', 'wu4', 'zhen3', '^', 'jie2', 'guo3', 'tuo1', 'yan2', 'le5', 'zhi4', 'liao2', 'shi2', 'ji1', '^', 'zao4', 'cheng2', 'shi2', 'zi4', 'ren4', 'dai4', 'wei1', 'suo1', '^']
# b=['shi2', 'ge2', 'duo1', 'nian2', 'hou4', 'zhu1', 'jiong3', 'ceng2', 'tou4', 'lu4', 'zhe4', 'ci4', 'shang1', 'bing4', 'qi2', 'shi2', 'shi4', 'yi1', 'ci4', 'wu4', 'zhen3', '^', 'jie2', 'guo3', 'tuo1', 'yan2', 'le5', 'zhi4', 'liao2', 'shi2', 'ji1', '^', 'zao4', 'cheng2', 'shi2', 'zi4', 'ren4', 'dai4', 'suo1', '^']
# print(len(a),len(b))

# python spot-check.py  compare dataset/train.dict  dataset/train-ground.dict  dataset/train-test.dict


#python spot-check.py compare  dataset/train-ground.dict  dataset/train-test.out.dict  dataset/log.txt