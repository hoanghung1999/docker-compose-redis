import  redis
from datetime import datetime
def writeStatus(status):
    f = open("statuslogin.txt", "a")
    time=datetime.now();
    f.write("userlogin" + " " + str(status)+"  time:"+str(time)+"\n");
    f.close()
redis_connect=redis.StrictRedis(host='redis', port=6379,db=0);
friststatus=redis_connect.get("userlogin");
writeStatus(friststatus);
print("userlogin" + " " + str(friststatus));
while True:
    try:
        result=redis_connect.get("userlogin");
        if(friststatus!=result):
            print("userlogin"+" "+str(result));
            writeStatus(result)
            friststatus=result
    except :
        redis_connect.close();


