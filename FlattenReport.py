

output = []

with open(r"D:\Temp\ReconcileOpt\BaselineReportMTXQty.txt", 'r') as f1:

    cursite = ""
    curqtytype = ""

    for line in f1.readlines():
        if "Item Total" in line:
            #itemNumber site Item Total <QTY Type String> 0

            wordsArr = line.split(" ")

            qtyStart = 0;

            if "ALL SITES" in line:
                site = "ALL SITES"
                qtyStart = 5
            else:
                site = wordsArr[1]
                qtyStart = 4

            qtytype = " ".join(wordsArr[qtyStart:len(wordsArr) - 1])

            if cursite != site:
                cursite = site

            if curqtytype != qtytype:
                curqtytype = qtytype;



        elif "Size " in line:
            sku = line[:-1]
            output.append( "{0} {1} {2}".format(cursite, curqtytype, sku))
            continue;


with open(r"D:\Temp\ReconcileOpt\baselinereportflattened.txt", 'a+') as f2:
    for line in output:
        f2.write("{0}\n".format(line))