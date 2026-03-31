all_ips = []
total_lines = 0
total_ips = 0
total_success = 0
total_failures = 0
count = {}
success_events = []
fail_events = []
success_words = ["200", "201", "202", "204", "SUCCESS", "SUCCESSFUL", "OK", "ONLINE", "AUTHORIZED", "AUTHENTICATED", "GRANTED", "ALLOWED", "CONNECTED", "ESTABLISHED", "COMPLETED", "FINISHED", "FOUND", "FETCHED", "ALIVE", "UP", "STABLE", "VALID", "VERIFIED"]           
fail_words = ["400", "401", "403", "404", "405", "408", "429", "500", "502", "503", "504", "FAILURE", "FAILED", "FAIL", "ERROR", "ERR", "EXCEPTION", "DENIED", "REJECTED", "REFUSED", "CRITICAL", "FATAL", "EMERGENCY", "WARNING", "WARN", "TIMEOUT", "EXPIRED", "WAIT", "INVALID", "CORRUPTED", "BAD", "BREACH", "ATTACK", "INTRUSION", "EXPLOIT", "UNKNOWN", "UNDENIED", "NULL", "DISCONNECTED", "DOWN", "OFFLINE"]       

mainfile = "[$] No File Scanned."
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[35m"
RESET = "\033[0m" 
ascii1 = PURPLE + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣾⣼⢀⣆⣀⠀⡆⢀⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣠⣶⣽⣸⣯⣼⣽⣿⣼⣿⣧⣿⣷⢾⣷⣤⡎⠀⢠⠂⠀⠀⠀
⠀⠀⠀⡀⢤⣜⢯⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡳⢮⡵⢓⡔⡀⡀⠀
⠀⠀⢢⡸⣫⣿⣿⡿⢋⣵⠟⠋⢁⣀⣀⡀⠉⠛⢿⣿⣿⣿⣿⣿⣷⣿⣵⢣⠃
⠀⢈⣮⣟⣿⢻⡏⠀⣼⡏⠀⣰⡟⠋⠉⠛⢷⣄⠀⢻⡾⡻⣿⣿⣿⣽⣗⡯⠋
⠈⣾⣿⠫⠄⢸⡇⠀⢻⣧⠀⠘⠟⢛⣷⠀⠈⣿⠀⢈⣿⠎⠈⣿⢿⣷⣿⠶⠂
⠟⡹⢇⢳⢆⠈⢿⣆⠀⠙⠿⠶⠶⠿⠋⢀⣼⡟⠀⡼⠋⢀⣼⣿⢷⢥⡟⠀⠀
⠀⣕⣭⣚⠬⣑⣂⠽⠿⣶⣤⣤⣤⣤⣶⠟⢋⢤⣊⣀⣴⣿⠛⡻⡜⡼⠀⠀⠀
⠀⠀⣍⣩⣖⠄⡘⠋⠿⢲⠶⢷⡿⡴⡶⡴⢶⣟⢿⢪⢳⠓⠁⠐⡱⠃⠀⠀⠀
⠀⠀⠁⠈⠑⠮⡓⠬⣁⠀⠁⠀⡁⠏⠿⠘⠘⠺⡎⠁⡹⠔⠁⠔⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠂⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                     _                         
  / /  _    _      / _ \__ _ _  _  _ _     
 / /  / _ \ / _` |/ /_)/ _` | '__/ __|/ _ \ '__|
/ /__| (_) | (_| / _/ (_| | |  \ \  __/ |   
\____/\___/ \__, \/    \__,_|_|  |___/\___|_|   
            |___/                v1.1               
      Watch your logs, see the unseen.
"""
nim = YELLOW + r"""Enter Operation:
1 - Start
2 - Help
3 - About Project
4 - History
5 - Exit
"""
def main_menu():
    print(ascii1)
    print(nim)
def variant1():
    global mainfile, all_ips, total_lines, total_ips, total_success, total_failures, count, success_events, fail_events
    total_lines = 0
    total_ips = 0
    total_success = 0
    total_failures = 0
    count.clear()
    success_events.clear()
    fail_events.clear()
    all_ips.clear()

    mainfile = input("[+] Enter File's name:")
    with open(mainfile, "r", errors="ignore") as file:
        for line in file:
            total_lines += 1
            has_success = False
            has_fail = False

            for word in line.split():
                word = word.upper()

                if word.count(".") == 3:
                    parts = word.split(".")
                    if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
                        all_ips.append(word)
                        count[word] = count.get(word, 0) + 1
                        total_ips += 1
                if word in success_words:
                    has_success = True
                if word in fail_words:
                    has_fail = True
            if has_success:
                total_success += 1
                success_events.append(line.strip())

            if has_fail:
                total_failures += 1
                fail_events.append(line.strip())
    unique_ips = len(set(all_ips))

    print(CYAN + "=" * 39)
    print(CYAN + "          [*] Main Statistics")
    print(CYAN + "=" * 39)
    print(" ")
    print(YELLOW + "[*] Total Lines Processed:", total_lines)
    print(YELLOW + "[*] Total IP Adresses:", total_ips)
    print(YELLOW + "[*] Total Unique IP Adresses:", unique_ips)
    print(YELLOW + "Success Requests:", total_success)
    print(YELLOW + "Failed Requests:", total_failures)
    print(YELLOW + "[*] All IP Adresses:", all_ips)
    print(YELLOW + "[*] All Unique IP Adresses:", set(all_ips))
    print(" ")

    print(CYAN + "=" * 44)
    print(CYAN + "           [!] Security Anomalies")
    print(CYAN + "=" * 44)
    print(" ")

    for events in success_events:
        print(GREEN + "[!] Success Event:", events)

    for event in fail_events:
        print(RED + "[!] Failed Event:", event)

    print("")
    print(CYAN + "=" * 44)
    print(CYAN + "           [*] Top Traffic Sources")
    print(CYAN + "=" * 44)
    print("")

    for i, g in count.items():
        print(YELLOW + i, "-", g, "Events.")
def variant2():
    print(YELLOW + "Hello, here you can find documentation about all functions:")
    print(GREEN + "First, to use function 1, and start analysis of Target's file, enter 1 in the main menu.")
    print(CYAN + "Second, to use function 3, and see information about project, enter 3 in the main menu.")
    print(RED + "And finally, to use function 4, and see your lookup's history, enter 4 in the main menu.")
def variant3():
    print(CYAN + "=" * 40)
    print(CYAN + "                 [!] Main Info:")
    print(CYAN + "=" * 40)
    print("")
    print(GREEN + "{!} Project Name: LogParser v1.1")
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
    print(RED + "Real time extraction of suspicious IP Adresses and critical failure codes from raw data streams.")
    print("")
    print("")
    print(GREEN + "Copyright (c) 2026 | All Rights Reserved.")
    print(YELLOW + "[ Watch Your logs, see the unseen. ]")
def variant4():
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
            n = int(input(">_ "))
            if n == 1:
                variant1()
            if n == 2:
                variant2()
            if n == 3:
                variant3()
            if n == 4:
                variant4()
            if n == 5:
                exit()
        except ValueError:
            print(RED + "[!] Please, write down a function.")
    except KeyboardInterrupt:
        break

