from inp import inp

inp = inp[:-1].replace("; ",";").replace("q[","").replace("]","").replace("(","").replace(")","")

inp = inp.split(";")

res = []
for i in inp:
    i = [i[:2],i[2:]]
    if " " in i[1]:
        i[1] = i[1].split(" ")
        i = [i[0],i[1][0],i[1][1]]
    if i[1] == "":
        i = [i[0],i[2]]
    if "," in i[1]:
        i[1] = i[1].split(",")
    if type(i[1]) == list:
        i = [i[0],i[1][0],i[1][1]]
    if i[1] == "":
        i = [i[0],i[2]]
    res.append(i)

resstr = ""

for cmd in res:
    if len(cmd) == 2:
        resstr = resstr + f"qc_qiskit.{cmd[0]}({cmd[1]})\n"
    elif len(cmd) == 3:
        resstr = resstr + f"qc_qiskit.{cmd[0]}({cmd[1]},{cmd[2]})\n"
    else:
        print(cmd,"<-----")
        raise Exception
    
with open("converted.txt","w") as converted:
    converted.write(resstr)