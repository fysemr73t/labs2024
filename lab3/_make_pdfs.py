from os.path import basename,splitext,join
import subprocess
import glob
import hashlib

def md5word(word):
    hasher = hashlib.md5()
    hasher.update(word.encode('utf-8'))
    return hasher.hexdigest()

if __name__=="__main__":
    for fn in glob.glob("infiles/*.pdf"):
        codeword = splitext(basename(fn))[0]
        md5w     = md5word(codeword)

        cmd = ['pdftk',fn,
               'output',join('labfiles',md5w+'.pdf'),
               'user_pw',codeword]
        print(f"{codeword} -> {md5w}")
        subprocess.call(cmd)
