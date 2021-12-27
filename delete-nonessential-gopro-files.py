import os
#r=''
def of(r):
    for p,ds,fs in os.walk(r):
        for f in fs:
            if f.endswith(['.gpr', '.lrv', '.thm']):#tuple(['.gpr', '.lrv', '.thm']) ?
                os.remove(os.path.normpath(p+'\\'+f))
