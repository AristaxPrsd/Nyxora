all_ips = []
mainfile = "[$] No File Scanned."
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[35m"
RESET = "\033[0m" 
ascii1 = RED + r"""
 
 ███▄    █▓██   ██▓▒██   ██▒ ▒█████   ██▀███   ▄▄▄      
 ██ ▀█   █ ▒██  ██▒▒▒ █ █ ▒░▒██▒  ██▒▓██ ▒ ██▒▒████▄    
▓██  ▀█ ██▒ ▒██ ██░░░  █   ░▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  
▓██▒  ▐▌██▒ ░ ▐██▓░ ░ █ █ ▒ ▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ 
▒██░   ▓██░ ░ ██▒▓░▒██▒ ▒██▒░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒
░ ▒░   ▒ ▒   ██▒▒▒ ▒▒ ░ ░▓ ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
░ ░░   ░ ▒░▓██ ░▒░ ░░   ░▒ ░  ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░
   ░   ░ ░ ▒ ▒ ░░   ░    ░  ░ ░ ░ ▒    ░░   ░   ░   ▒   
         ░ ░ ░      ░    ░      ░ ░     ░           ░  ░
           ░ ░                                          
                              v1.3               
         Watch your logs, see the unseen.
"""
nim = RED + r"""                Enter Operation:
          
          [1] Start        [2] About Project
          [3] History      [4] Exit
"""
def main_menu():
    print(ascii1)
    print(nim)
def variant1():
    global all_ips, mainfile
    all_ips.clear()

    mainfile = input("[+] Enter File's name: ")
    ip_request_count = {}
    bruteforce_ips = []
    dos_ips = []
    try:
        with open(mainfile, "r", errors="ignore") as file:
            total_lines = 0
            total_ips = 0
            total_success = 0
            total_failures = 0
            success_words = ["200", "201", "202", "204", "301", "302", "SUCCESS", "SUCCESSFUL", "OK", "ONLINE", "AUTHORIZED", "AUTHENTICATED", "GRANTED", "ALLOWED", "CONNECTED", "ESTABLISHED", "COMPLETED", "FINISHED", "FOUND", "FETCHED", "ALIVE", "UP", "STABLE", "VALID", "VERIFIED"]    
            fail_words = ["400", "401", "403", "404", "405", "408", "429", "500", "502", "503", "504", "FAILURE", "FAILED", "FAIL", "ERROR", "ERR", "EXCEPTION", "DENIED", "REJECTED", "REFUSED", "CRITICAL", "FATAL", "EMERGENCY", "WARNING", "WARN", "TIMEOUT", "EXPIRED", "WAIT", "INVALID", "CORRUPTED", "BAD", "BREACH", "ATTACK", "INTRUSION", "EXPLOIT", "UNKNOWN", "UNDENIED", "NULL", "DISCONNECTED", "DOWN", "OFFLINE"]       
            count = {}
            success_events = []
            fail_events = []
            ip_fails = {}
            time_map = {}
            ip_rps = {}
            currentttt = "[?] Unknown"
            for liness in file:
                total_lines += 1
                lines = liness.split()
                has_success = False
                has_fail = False
                currentip_line = "[?] Unknown"
                for words in lines:
                    word = words.upper()
                    cleanword = words.strip("[](),. ")
                    if cleanword.count(":") == 2 and len(cleanword) >= 8:
                        tseq = cleanword.split(":")
                        if all(t.isdigit() for t in tseq[:3]):
                            currentttt = cleanword[:8]
                    if word.count(".") == 3:
                        parts = word.split(".")
                        if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
                            currentip_line = word
                            all_ips.append(word)
                            total_ips += 1
                            if word not in count:
                                count[word] = 1
                            else:
                                count[word] += 1
                    if word in success_words:
                        has_success = True
                    elif word in fail_words:
                        has_fail = True
                if has_success:
                    total_success += 1
                    success_events.append(liness.strip())
                elif has_fail:
                    total_failures += 1
                    fail_events.append(liness.strip())
                    if word.count(".") == 3:
                        partss = word.split(".")
                        if len(partss) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in partss):
                            ip_fails[word] = ip_fails.get(word, 0) + 1
                if currentttt != "[?] Unknown":
                    time_map[currentttt] = time_map.get(currentttt, 0) + 1
                    if word.count(".") == 3:
                        secur_ippkey = (currentttt, word)
                        ip_rps[secur_ippkey] = ip_rps.get(secur_ippkey, 0) + 1
            unique_ips = len(set(all_ips))
            if total_lines > 0:
                success_rate = (total_success / total_lines) * 100
                failure_rate = (total_failures / total_lines) * 100
            print(PURPLE + "=" * 39)
            print(RESET + "          [*] Main Statistics")
            print(PURPLE + "=" * 39)
            print(" ")
            print(YELLOW + "[*] Total Lines Processed:", str(total_lines))
            print(YELLOW + "[&] Total IP Adresses:", total_ips)
            print(YELLOW + "[*] Total Unique IP Adresses:", str(unique_ips))
            print(YELLOW + "[+] Success Requests:", str(total_success))
            print(YELLOW + "[-] Failed Requests:", str(total_failures))
            print(YELLOW + f"[+] Success Rate: {success_rate:.2f}%")
            print(YELLOW + f"[-] Failure Rate: {failure_rate:.2f}%")
            print(YELLOW + "[#] All IP Adresses:", str(all_ips))
            print(YELLOW + "[#] All Unique IP Adresses:", set(all_ips))
            print(" ")
            print(RED + "=" * 44)
            print(RED + "[!] Security Report")
            print(RED + "=" * 44)
            threats = False
            is_ddos = False
            ishighh_veloc = False
            for ip, gsd_count in ip_fails.items():
                if gsd_count > 5:
                    print(RED + f"[!] ALERT: Bruteforce Attack from {ip} ({gsd_count} fails)")
                    threats = True
            for ts, rps in time_map.items():
                if rps > 30:
                    ishighh_veloc = True
            for (ts, ip), rps_val in ip_rps.items():
                if rps_val > 15:
                    ishighh_veloc = True
            for ip, yrs_count in count.items():
                if yrs_count > 50:
                    print(RED + f"[!] ALERT: DoS Attack from {ip} ({yrs_count} requests)")
                    threats = True
            if ishighh_veloc:
                is_ddos = True
                threats = True
            if is_ddos:
                print(RED + "[!] ALERT: DDoS Attack Detected")
                print(YELLOW + f"[*] Magnitude: {total_lines} total requests")
                print(YELLOW + f"[*] Botnet Size: {len(set(all_ips))} unique source IPs")
                print("")
            if not threats:
                print(GREEN + "[+] System is clean. No anomalies Detected")
                print("")
            print(CYAN + "=" * 44)
            print(RESET + "           [!] Security Anomalies")
            print(CYAN + "=" * 44)
            print(" ")
            for events in success_events[:20]:
                print(GREEN + "[!] Success Event:", events)
            for event in fail_events[:20]:
                    print(RED + "[!] Failed Event:", event)
            its = 10
            print("")
            print(CYAN + "=" * 44)
            print(RESET + "           [*] Top Traffic Sources")
            print(CYAN + "=" * 44)
            print("")
            ranking = []
            for ip, dsn in count.items():
                ranking.append([dsn, ip])
            ranking.sort(reverse=True)
            for tyr in ranking[:10]:
                print(YELLOW + f"{tyr[1]} - {tyr[0]} Events.")
    except FileNotFoundError:
    print(CYAN + "=" * 40)
    print("")
    asciii2 = GREEN + r"""
    ⠀⠀⠀⠀⡀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠉⣹⠋⠉⢉⡟⢩⢋⠋⣽⡻⠭⢽⢉⠯⠭⠭⠭⢽⡍⢹⡍⠙⣯⠉⠉⠉⠉⠉⣿⢫⠉⠉⠉⢉⡟⠉⢿⢹⠉⢉⣉⢿⡝⡉⢩⢿⣻⢍⠉⠉⠩⢹⣟⡏⠉⠹⡉⢻⡍⡇
⠀⢸⢠⢹⠀⠀⢸⠁⣼⠀⣼⡝⠀⠀⢸⠘⠀⠀⠀⠀⠈⢿⠀⡟⡄⠹⣣⠀⠀⠐⠀⢸⡘⡄⣤⠀⡼⠁⠀⢺⡘⠉⠀⠀⠀⠫⣪⣌⡌⢳⡻⣦⠀⠀⢃⡽⡼⡀⠀⢣⢸⠸⡇
⠀⢸⡸⢸⠀⠀⣿⠀⣇⢠⡿⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠘⢇⠸⠘⡀⠻⣇⠀⠀⠄⠀⡇⢣⢛⠀⡇⠀⠀⣸⠇⠀⠀⠀⠀⠀⠘⠄⢻⡀⠻⣻⣧⠀⠀⠃⢧⡇⠀⢸⢸⡇⡇
⠀⢸⡇⢸⣠⠀⣿⢠⣿⡾⠁⠀⢀⡀⠤⢇⣀⣐⣀⠀⠤⢀⠈⠢⡡⡈⢦⡙⣷⡀⠀⠀⢿⠈⢻⣡⠁⠀⢀⠏⠀⠀⠀⢀⠀⠄⣀⣐⣀⣙⠢⡌⣻⣷⡀⢹⢸⡅⠀⢸⠸⡇⡇
⠀⢸⡇⢸⣟⠀⢿⢸⡿⠀⣀⣶⣷⣾⡿⠿⣿⣿⣿⣿⣿⣶⣬⡀⠐⠰⣄⠙⠪⣻⣦⡀⠘⣧⠀⠙⠄⠀⠀⠀⠀⠀⣨⣴⣾⣿⠿⣿⣿⣿⣿⣿⣶⣯⣿⣼⢼⡇⠀⢸⡇⡇⡇
⠀⢸⢧⠀⣿⡅⢸⣼⡷⣾⣿⡟⠋⣿⠓⢲⣿⣿⣿⡟⠙⣿⠛⢯⡳⡀⠈⠓⠄⡈⠚⠿⣧⣌⢧⠀⠀⠀⠀⠀⣠⣺⠟⢫⡿⠓⢺⣿⣿⣿⠏⠙⣏⠛⣿⣿⣾⡇⢀⡿⢠⠀⡇
⠀⢸⢸⠀⢹⣷⡀⢿⡁⠀⠻⣇⠀⣇⠀⠘⣿⣿⡿⠁⠐⣉⡀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠳⠄⠀⠀⠀⠀⠋⠀⠘⡇⠀⠸⣿⣿⠟⠀⢈⣉⢠⡿⠁⣼⠁⣼⠃⣼⠀⡇
⠀⢸⠸⣀⠈⣯⢳⡘⣇⠀⠀⠈⡂⣜⣆⡀⠀⠀⢀⣀⡴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣆⣀⠀⠀⠀⣀⣜⠕⡊⠀⣸⠇⣼⡟⢠⠏⠀⡇
⠀⢸⠀⡟⠀⢸⡆⢹⡜⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⣾⡏⡇⡎⡇⠀⡇
⠀⢸⠀⢃⡆⠀⢿⡄⠑⢽⣄⠀⠀⠀⢀⠂⠠⢁⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠄⡐⢀⠂⠀⠀⣠⣮⡟⢹⣯⣸⣱⠁⠀⡇
⠀⠈⠉⠉⠋⠉⠉⠋⠉⠉⠉⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠋⡟⠉⠉⡿⠋⠋⠋⠉⠉⠁     
    """
    print(asciii2)
    print(GREEN + "{!} Project Name: Nyxora v1.3")
    print(GREEN + "{!} Developer: Aristax")
    print(GREEN + "{!} Environment: Unix Based Shell // Vim Engine")
    print(GREEN + "{!} This terminal utility is engineered for advanced network forensics and automated log auditing.It is designed to identify security breaches, detect unauthorised access attempts.Have a great time using it.")
    print("")
    print(YELLOW + "=" * 40)
    print(YELLOW + "             [%] Key Features")
    print(YELLOW + "=" * 40)
    print("")
    print(RED + "{!} To ensure zero digital footprint, this tool operates exclusively in RAM. All session data, i
        print(RED + "[$] Please write down a files name.")
def variant2():
    print(CYAN + "=" * 40)
    print(CYAN + "                 [!] Main Info:")
    print(CYAN + "=" * 40)
    print("")
    asciii2 = GREEN + r"""
    ⠀⠀⠀⠀⡀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠉⣹⠋⠉⢉⡟⢩⢋⠋⣽⡻⠭⢽⢉⠯⠭⠭⠭⢽⡍⢹⡍⠙⣯⠉⠉⠉⠉⠉⣿⢫⠉⠉⠉⢉⡟⠉⢿⢹⠉⢉⣉⢿⡝⡉⢩⢿⣻⢍⠉⠉⠩⢹⣟⡏⠉⠹⡉⢻⡍⡇
⠀⢸⢠⢹⠀⠀⢸⠁⣼⠀⣼⡝⠀⠀⢸⠘⠀⠀⠀⠀⠈⢿⠀⡟⡄⠹⣣⠀⠀⠐⠀⢸⡘⡄⣤⠀⡼⠁⠀⢺⡘⠉⠀⠀⠀⠫⣪⣌⡌⢳⡻⣦⠀⠀⢃⡽⡼⡀⠀⢣⢸⠸⡇
⠀⢸⡸⢸⠀⠀⣿⠀⣇⢠⡿⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠘⢇⠸⠘⡀⠻⣇⠀⠀⠄⠀⡇⢣⢛⠀⡇⠀⠀⣸⠇⠀⠀⠀⠀⠀⠘⠄⢻⡀⠻⣻⣧⠀⠀⠃⢧⡇⠀⢸⢸⡇⡇
⠀⢸⡇⢸⣠⠀⣿⢠⣿⡾⠁⠀⢀⡀⠤⢇⣀⣐⣀⠀⠤⢀⠈⠢⡡⡈⢦⡙⣷⡀⠀⠀⢿⠈⢻⣡⠁⠀⢀⠏⠀⠀⠀⢀⠀⠄⣀⣐⣀⣙⠢⡌⣻⣷⡀⢹⢸⡅⠀⢸⠸⡇⡇
⠀⢸⡇⢸⣟⠀⢿⢸⡿⠀⣀⣶⣷⣾⡿⠿⣿⣿⣿⣿⣿⣶⣬⡀⠐⠰⣄⠙⠪⣻⣦⡀⠘⣧⠀⠙⠄⠀⠀⠀⠀⠀⣨⣴⣾⣿⠿⣿⣿⣿⣿⣿⣶⣯⣿⣼⢼⡇⠀⢸⡇⡇⡇
⠀⢸⢧⠀⣿⡅⢸⣼⡷⣾⣿⡟⠋⣿⠓⢲⣿⣿⣿⡟⠙⣿⠛⢯⡳⡀⠈⠓⠄⡈⠚⠿⣧⣌⢧⠀⠀⠀⠀⠀⣠⣺⠟⢫⡿⠓⢺⣿⣿⣿⠏⠙⣏⠛⣿⣿⣾⡇⢀⡿⢠⠀⡇
⠀⢸⢸⠀⢹⣷⡀⢿⡁⠀⠻⣇⠀⣇⠀⠘⣿⣿⡿⠁⠐⣉⡀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠳⠄⠀⠀⠀⠀⠋⠀⠘⡇⠀⠸⣿⣿⠟⠀⢈⣉⢠⡿⠁⣼⠁⣼⠃⣼⠀⡇
⠀⢸⠸⣀⠈⣯⢳⡘⣇⠀⠀⠈⡂⣜⣆⡀⠀⠀⢀⣀⡴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣆⣀⠀⠀⠀⣀⣜⠕⡊⠀⣸⠇⣼⡟⢠⠏⠀⡇
⠀⢸⠀⡟⠀⢸⡆⢹⡜⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⣾⡏⡇⡎⡇⠀⡇
⠀⢸⠀⢃⡆⠀⢿⡄⠑⢽⣄⠀⠀⠀⢀⠂⠠⢁⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠄⡐⢀⠂⠀⠀⣠⣮⡟⢹⣯⣸⣱⠁⠀⡇
⠀⠈⠉⠉⠋⠉⠉⠋⠉⠉⠉⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠋⡟⠉⠉⡿⠋⠋⠋⠉⠉⠁     
    """
    print(asciii2)
    print(GREEN + "{!} Project Name: Nyxora v1.3")
    print(GREEN + "{!} Developer: Aristax")
    print(GREEN + "{!} Environment: Unix Based Shell // Vim Engine")
    print(GREEN + "{!} This terminal utility is engineered for advanced network forensics and automated log auditing.It is designed to identify security breaches, detect unauthorised access attempts.Have a great time using it.")
    print("")
    print(YELLOW + "=" * 40)
    print(YELLOW + "             [%] Key Features")
    print(YELLOW + "=" * 40)
    print("")
    print(RED + "{!} To ensure zero digital footprint, this tool operates exclusively in RAM. All session data, including history and searches queries, are automatically wiped upon termination.")
    print(RED + "{!} Advanced sorting algorithms optimized for identifying specific threat signatures.")
    print(RED + "{!] Real time extraction of suspicious IP Adresses and critical failure codes from raw data streams.")
    print(RED + "{!} Automatic Attacks( Bruteforce, DoS, DDoS ) Detection.")

    print("")
    print("")
    print(GREEN + "Copyright (c) 2026 | All Rights Reserved.")
    print(YELLOW + "[ Watch Your logs, see the unseen. ]")
def variant3():
    global all_ips, mainfile
    random_id = id(all_ips) % 10000
    print(CYAN + "=" * 40)
    print(CYAN + "           [&] Session Logs")
    print(CYAN + "=" * 40)
    print("")
    print(GREEN + "{$} Target:", mainfile)
    print(GREEN + "{$} IP Adresses:", set(all_ips))
    print(GREEN + "{$} Session ID:", random_id)
    print(RED + "{!} WARNING: These Session Logs will be deleted once you'll leave.")
while True:
    try:
        main_menu()
        try:
            no = int(input(">_ "))
            if no == 1:
                variant1()
            if no == 2:
                variant2()
            if no == 3:
                variant3()
            if no == 4:
                exit()
        except ValueError:
            print("[!] Please Enter a Function")
    except KeyboardInterrupt:
        break

