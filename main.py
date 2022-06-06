# Credit to useragents

# Github: https://github.com/useragents/Proxyless-Spotify-Follow-Bot

from colorama import Back, Fore, Style
from follow_bot import spotify
import threading, os, time

banner = (f"""
$$$$$$$\  $$\        $$$$$$\ $$\     $$\ $$\       $$$$$$\  $$$$$$\ $$$$$$$$\ 
$$  __$$\ $$ |      $$  __$$\\$$\   $$  |$$ |      \_$$  _|$$  __$$\\__$$  __|
$$ |  $$ |$$ |      $$ /  $$ |\$$\ $$  / $$ |        $$ |  $$ /  \__|  $$ |   
$$$$$$$  |$$ |      $$$$$$$$ | \$$$$  /  $$ |        $$ |  \$$$$$$\    $$ |   
$$  ____/ $$ |      $$  __$$ |  \$$  /   $$ |        $$ |   \____$$\   $$ |   
$$ |      $$ |      $$ |  $$ |   $$ |    $$ |        $$ |  $$\   $$ |  $$ |   
$$ |      $$$$$$$$\ $$ |  $$ |   $$ |    $$$$$$$$\ $$$$$$\ \$$$$$$  |  $$ |   
\__|      \________|\__|  \__|   \__|    \________|\______| \______/   \__|   
                                                                                                                                                            
                                                                              
$$$$$$$$\  $$$$$$\  $$\       $$\       $$$$$$\  $$\      $$\                 
$$  _____|$$  __$$\ $$ |      $$ |     $$  __$$\ $$ | $\  $$ |                
$$ |      $$ /  $$ |$$ |      $$ |     $$ /  $$ |$$ |$$$\ $$ |                
$$$$$\    $$ |  $$ |$$ |      $$ |     $$ |  $$ |$$ $$ $$\$$ |                
$$  __|   $$ |  $$ |$$ |      $$ |     $$ |  $$ |$$$$  _$$$$ |                
$$ |      $$ |  $$ |$$ |      $$ |     $$ |  $$ |$$$  / \$$$ |                
$$ |       $$$$$$  |$$$$$$$$\ $$$$$$$$\ $$$$$$  |$$  /   \$$ |                
\__|       \______/ \________|\________|\______/ \__/     \__|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
""")
os.system('cls' if os.name == 'nt' else 'clear')

lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0
print(Fore.LIGHTRED_EX + banner)
print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}~{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} Spotify Playlist ID ex (5rKVRN1nBDhlw1m1q23d49):{Fore.RESET}")
spotify_profile = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}~{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} Threads (default = 100) : {Fore.RESET}")
threads = int(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))

def load_proxies():
    if not os.path.exists("proxies.txt"):
        print("\nFile proxies.txt not found")
        time.sleep(10)
        os._exit(0)
    with open("proxies.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print("\nNo proxies loaded in proxies.txt")
            time.sleep(10)
            os._exit(0)

print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}~{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} [1] Proxies File (default = proxies.txt)   [2] Auto Proxies Scrap{Fore.RESET}")
option = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
if option == 1:
    load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        safe_print(Fore.LIGHTGREEN_EX + "Followed {}".format(counter))
    else:
        safe_print(f"{Fore.LIGHTRED_EX}Error {error}")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter:
            proxy_counter = 0
