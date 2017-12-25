import os

def solve():
    pre_cls_num=6
    cls_num=7
    #
    with open(os.path.join("class-aware","new_train_ohem.prototxt"),"w") as nf:
        with open(os.path.join("class-aware","train_ohem.prototxt"),"r") as f:
            lines=f.readlines()
            for line in lines:
                if line.strip().find("param_str: \"'num_classes':")>-1:
                    curline=line.replace(str(pre_cls_num),str(cls_num))
                    nf.write(curline)
                elif line.strip().find("wuyonglin_numoutput_forty-nine")>-1:
                    curline = line.replace(str(pre_cls_num*49), str(cls_num*49))
                    nf.write(curline)
                elif line.strip().find("wuyonglin_numoutput one hundred and ninety-six")>-1:
                    curline = line.replace(str(pre_cls_num*49*4), str(cls_num*49*4))
                    nf.write(curline)
                elif line.strip().find("wuyonglin_output_dim_cls_num")>-1:
                    curline = line.replace(str(pre_cls_num), str(cls_num))
                    nf.write(curline)
                elif line.strip().find("wuyonglin_output_dim cls_num mul four")>-1:
                    curline = line.replace(str(pre_cls_num*4), str(cls_num*4))
                    nf.write(curline)
                else:
                    nf.write(line)

    #
    with open(os.path.join("class-aware","new_test.prototxt"),"w") as nf:
        with open(os.path.join("class-aware","test.prototxt"),"r") as f:
            lines=f.readlines()
            for line in lines:
                if line.strip().find("wuyonglin_numoutput_forty-nine")>-1:
                    curline = line.replace(str(pre_cls_num * 49), str(cls_num * 49))
                    nf.write(curline)
                elif line.strip().find("wuyonglin_numoutput one hundred and ninety-six")>-1:
                    curline = line.replace(str(pre_cls_num*49*4), str(cls_num*49*4))
                    nf.write(curline)
                elif line.strip().find("wuyonglin_output_dim_cls_num")>-1:
                    curline = line.replace(str(pre_cls_num), str(cls_num))
                    nf.write(curline)
                elif line.strip().find("wuyonglin_output_dim cls_num mul four")>-1:
                    curline = line.replace(str(pre_cls_num*4), str(cls_num*4))
                    nf.write(curline)
                else:
                    nf.write(line)

    #
    with open("new_train_agnostic.prototxt","w") as nf:
        with open("train_agnostic.prototxt","r") as f:
            lines=f.readlines()
            for line in lines:
                if line.strip().find("wuyonglin_cls_num")>-1:
                    curline=line.replace(str(pre_cls_num),str(cls_num))
                    nf.write(curline)
                elif line.strip().find("wuyonglin_numoutput_forty-nine")>-1:
                    curline = line.replace(str(pre_cls_num*49), str(cls_num*49))
                    nf.write(curline)
                else:
                    nf.write(line)

    #
    with open("new_train_agnostic_ohem.prototxt","w") as nf:
        with open("train_agnostic_ohem.prototxt","r") as f:
            lines=f.readlines()
            for line in lines:
                if line.strip().find("wuyonglin_cls_num")>-1:
                    curline=line.replace(str(pre_cls_num),str(cls_num))
                    nf.write(curline)
                elif line.strip().find("wuyonglin_numoutput_forty-nine")>-1:
                    curline = line.replace(str(pre_cls_num*49), str(cls_num*49))
                    nf.write(curline)
                else:
                    nf.write(line)

    #
    with open("new_test_agnostic.prototxt","w") as nf:
        with open("test_agnostic.prototxt","r") as f:
            lines=f.readlines()
            for line in lines:
                if line.strip().find("wuyonglin_cls_num")>-1:
                    curline=line.replace(str(pre_cls_num),str(cls_num))
                    nf.write(curline)
                elif line.strip().find("wuyonglin_numoutput_forty-nine")>-1:
                    curline = line.replace(str(pre_cls_num*49), str(cls_num*49))
                    nf.write(curline)
                else:
                    nf.write(line)
    print("ok")

if __name__ == '__main__':
    solve()