def FindDiffs(file1, file2):
    file1List = []
    file2List = []

    pageheader = "Matrix Reconcile Item Quantities Report Page"

    with open(file1, 'r') as f1:
        for line in f1.readlines():
            if pageheader not in line:
                file1List.append(line)

    with open(file2, 'r') as f2:
        for line in f2.readlines():
            if pageheader not in line:
                if line not in file1List:
                    print "In F2 not F1: " + line
                else:
                    file1List.remove(line)

    for line in file1List:
        print "In F1 not F2 " + line

f1 = r"D:\Temp\ReconcileOpt\BaselineReportMTXQty.txt"
f2 = r"D:\Temp\ReconcileOpt\v14mtxqty.txt"
FindDiffs(f1, f2)