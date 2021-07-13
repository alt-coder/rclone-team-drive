import re
from pathlib import Path
home = str(Path.home())
location = home+"/.config/rclone/rclone.conf"
rconf = open(location,'r+')
st = str(rconf.read())
clientse = re.findall(r'client_secret.*?\n', st,re.I)
clid=re.findall(r'client_id.*?\n', st,re.I)
token=re.findall('''token.*?\n''', st,re.I)
if (len(clid)==0 or len(token)==0 or len(clientse)==0):
    print(" ")
    rconf.truncate(0)
    rconf.close()
    raise Exception("Credential had not been read properly\n Please run 'rclone config' again and setup at least one team drive'")
TEAMDRIVEINFO='''
 Paste the team drive information from the rlone
'''

if TEAMDRIVEINFO[-1] != '"' :
    TEAMDRIVEINFO=TEAMDRIVEINFO+'"'
# rconf.write("abcd")
s= str(TEAMDRIVEINFO)
mat1 = r'\/\s.*\n'
mat2 = r'".+?"'
names = re.findall(mat1,s,re.I)
ids = re.findall(mat2,s,re.I)
meta = '''type = drive
'''+clid[0]+clientse[0]+"scope = drive\n"+token[0]
meta2 = "root_folder_id = \n"
if len(ids)==0:
    print("Please paste the team drive information above ,from rclone shell")
else:
    rconf.truncate(0)
    rconf.close()
    with open(location,'r+') as rconf:
        for name,id in zip(names,ids):
            name = name.replace("/ ",'')
            name=name.replace("\n",'')
            name =re.sub(r'[^a-zA-Z0-9]', '', name)
            id = id.replace('"','')
            n = "[{}]\n".format(name)
            d = "team_drive = {}\n".format(id)
            meta2 = "root_folder_id = \n"
            # print(n+meta+d+meta2)
            # print(d)
            # i=i+1
            wr=n+meta+d+meta2+"\n"
            print(wr)
            n = rconf.write(wr)


rconf.close()