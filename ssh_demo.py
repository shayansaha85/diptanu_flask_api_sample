import paramiko

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect(hostname="192.168.1.10", port=22, username="root", password="shayan")
output = conn.exec_command("whoami")

print(output)