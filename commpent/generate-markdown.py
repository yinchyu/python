#!D:\BinConfig\python310\python.exe
# coding=utf-8
import os
from pathlib import Path
from collections import Counter

class DirectionTree(object):
    """生成目录树
    @ pathname: 目标目录
    @ filename: 要保存成文件的名称
    """

    def __init__(self, pathname='.', filename='tree.txt'):
        super(DirectionTree, self).__init__()
        self.pathname = Path(pathname)
        self.filename = filename
        self.tree = ''
        self.filterfile = ["xml", "mod", "sum", "gitignore", "iml", "md", "txt"]
        self.filterpath = [".idea"]
        self.program=[]

    def set_path(self, pathname):
        self.pathname = Path(pathname)

    def set_filename(self, filename):
        self.filename = filename

    def filter(self, name, filetype=True):
        # filetype 表示为文件而不是文件夹
        if filetype:
            for i in self.filterfile:
                if name.endswith(i):
                    return True
            else:
                self.program.append(name.split(".")[-1])
                return False
        else:
            for i in self.filterpath:
                if name.endswith(i):
                    return True
            else:
                return False

    def generate_tree(self, n=0):
        if self.pathname.is_file():
            if not self.filter(self.pathname.name):
                self.tree += '    |' * n + '-' * 4 + self.pathname.name + '\n'
        elif self.pathname.is_dir():
            if not self.filter(self.pathname.name, filetype=False):
                self.tree += '    |' * n + '-' * 4 + \
                             str(self.pathname.relative_to(self.pathname.parent)) + '\\' + '\n'

            for cp in self.pathname.iterdir():
                self.pathname = Path(cp)
                self.generate_tree(n + 1)
    def getprogram(self):
        counter=Counter(self.program)
        ty=counter.most_common(1)[0][0]
        if ty=="py":
            return "python"
        elif ty=="go":
            return "go"
        else:
            return "sh"
    def save_file(self):
        with open(self.filename, 'w', encoding='utf8') as f:
            f.write(self.tree)

    def clear(self):
        self.tree = ""


def getdir(path):
    dirtree = DirectionTree()
    with open(os.path.join(path, "readme.md"), "w+", encoding="utf8") as fw:
        for DIR in os.listdir(path):
            #  去除顶层的文件和隐藏文件夹
            if os.path.isfile(os.path.join(path,DIR)) or DIR.startswith("."):
                continue
            fw.write("#### " + DIR + "\n")
            dirtree.set_path(os.path.join(path, DIR))
            dirtree.generate_tree()
            # 写入文件的类型， 根据文件的后缀进行判断
            fw.write("```" + dirtree.getprogram() + " \n")
            fw.write(dirtree.tree)
            dirtree.clear()
            fw.write("```" + "\n")


def walk():
    for dirpath, dirnames, filenames in os.walk(os.path.join("./")):
        print(dirpath, dirnames, filenames)
        for file in filenames:
            if file.split(".")[-1].strip() in os.listdir("./"):
                continue


if __name__ == '__main__':
    current=os.getcwd()
    print(current)
    # dirname = r"D:\桌面文件夹\go"
    getdir(current)
