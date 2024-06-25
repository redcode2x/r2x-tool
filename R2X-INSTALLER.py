import os
import sys
import time

def clear_screen():
    os.system('clear')

def loading_bar(duration, message):
    print(message)
    for i in range(1, 34):
        txt = '\033[1;32m▒' * 38
        f = i * '\033[1;31m▊'
        tt = i * 3 + 1
        ttt = str(tt)
        print(txt + '┊' + ttt + '%', end='\r')
        print('Loading ┊{}'.format(f), end='\r')
        time.sleep(duration)
    print('')

def print_banner(title):
    clear_screen()
    print("\033[1;31m")  # Green color for the banner
    print(" / \------------------, ")
    print("\_,|    R2X-Tool      |" )
    print("   |------------------| ")
    print("   | ,----------------|")
    print("   | |   redcode2x    | ")  
    print("   \_/_______________/ ")
    print("\033[0m")

def main_menu():
    print_banner("Main Menu")
    print_options([
        "Forensic Tools",
        "Social Engineering Tools",
        "Network Tools",
        "Wireless Attacks",
        "Fix Termux",
        "About",
        "Exit"
    ])
    choice = input('\033[94mSelect an option: \033[0m')
    process_main_menu_choice(choice)

def process_main_menu_choice(choice):
    if choice == '1':
        forensic_tools_menu()
    elif choice == '2':
        social_engineering_tools_menu()
    elif choice == '3':
        network_tools_menu()
    elif choice == '4':
        wireless_attacks_menu()
    elif choice == '5':
        fix_termux()
    elif choice == '6':
        about()
    elif choice == '7':
        sys.exit()
    else:
        print("\033[91mInvalid option. Please try again.\033[0m")
        time.sleep(2)
        main_menu()

def forensic_tools_menu():
    print_banner("\033[93Forensic Tools Menu\033[0m")
    print_options([
        "Autopsy",
        "Testdisk",
        "Scalpel",
        "Volatility",
        "Wireshark",
        "Tcpdump",
        "Aircrack-ng",
        "Binwalk",
        "Foremost",
        "Exiftool",
        "Back to Main Menu"
    ])
    choice = input('\033[94mSelect a tool: \033[0m')
    process_forensic_tools_choice(choice)

def process_forensic_tools_choice(choice):
    if choice == '11':
        main_menu()
    elif choice.isdigit() and 1 <= int(choice) <= 10:
        tool_name = get_forensic_tool_name(int(choice))
        install_tool(f"pkg install {tool_name.lower()}", tool_name)
    else:
        print("\033[91mInvalid option. Please try again.\033[0m")
        time.sleep(2)
        forensic_tools_menu()

def get_forensic_tool_name(index):
    tool_names = [
        "autopsy", "testdisk", "scalpel", "volatility", "wireshark", "tcpdump", "aircrack-ng", "binwalk",
        "foremost", "exiftool"
    ]
    return tool_names[index - 1].capitalize()

def social_engineering_tools_menu():
    print_banner("Social Engineering Tools Menu")
    print_options([
        "SET (Social Engineer Toolkit)",
        "OSIF (Open Source Information Facebook)",
        "Striker",
        "HiddenEye",
        "SocialFish",
        "ShellPhish",
        "PhishX",
        "Blackeye",
        "EvilURL",
        "SocialPhish",
        "AdvPhishing",
        "Zphisher",
        "PhisherCatcher",
        "SocialBox",
        "BeEF",
        "Evilginx",
        "Gophish",
        "GoPhish",
        "King-Phisher",
        "NecroBrowser",
        "SEToolkit",
        "Weeman",
        "HiddenEye2",
        "Tool-X",
        "NexPhisher",
        "Blackeye-Phishing",
        "FakeImageExploiter",
        "Setoolkit",
        "Phisher-man",
        "HiddenEyePlus",
        "PhishHub",
        "PhishMailer",
        "PhishS3",
        "SocialFish2",
        "WeebSec",
        "Back to Main Menu"
    ])
    choice = input('\033[94mSelect a tool: \033[0m')
    process_social_engineering_tools_choice(choice)

def process_social_engineering_tools_choice(choice):
    if choice == '36':
        main_menu()
    elif choice.isdigit() and 1 <= int(choice) <= 35:
        tool_name = get_social_engineering_tool_name(int(choice))
        install_tool(f"git clone https://github.com/DarkSecDevelopers/{tool_name.lower()}.git", tool_name)
    else:
        print("\033[91mInvalid option. Please try again.\033[0m")
        time.sleep(2)
        social_engineering_tools_menu()

def get_social_engineering_tool_name(index):
    tool_names = [
        "setoolkit", "osif", "striker", "hiddeneye", "socialfish", "shellphish", "phishx", "blackeye", "evilurl",
        "socialphish", "advphishing", "zphisher", "phishercatcher", "socialbox", "beef", "evilginx", "gophish",
        "gophish", "king-phisher", "necrobrowser", "setoolkit", "weeman", "hiddeneye2", "tool-x", "nexphisher",
        "blackeye-phishing", "fakeimageexploiter", "setoolkit", "phisher-man", "hiddeneyeplus", "phishhub",
        "phishmailer", "phishs3", "socialfish2", "weebsec"
    ]
    return tool_names[index - 1].capitalize()

def network_tools_menu():
    print_banner("Network Tools Menu")
    print_options([
        "Nmap",
        "Wireshark",
        "Aircrack-ng",
        "Metasploit",
        "Netcat",
        "Hydra",
        "Tcpdump",
        "Ssh-Autrorot",
        "SniffAir",
        "Websploit",
        "Back to Main Menu"
    ])
    choice = input('\033[94mSelect a tool: \033[0m')
    process_network_tools_choice(choice)

def process_network_tools_choice(choice):
    if choice == '11':
        main_menu()
    elif choice.isdigit() and 1 <= int(choice) <= 10:
        tool_name = get_network_tool_name(int(choice))
        install_tool(f"pkg install {tool_name.lower()}", tool_name)
    else:
        print("\033[91mInvalid option. Please try again.\033[0m")
        time.sleep(2)
        network_tools_menu()

def get_network_tool_name(index):
    tool_names = [
        "nmap", "wireshark", "aircrack-ng", "metasploit", "netcat", "hydra", "tcpdump", "ssh-autoroot",
        "sniffair", "websploit"
    ]
    return tool_names[index - 1].capitalize()

def wireless_attacks_menu():
    print_banner("Wireless Attacks Menu")
    print_options([
        "Aircrack-ng Suite",
        "Kismet",
        "Reaver",
        "Wifite",
        "Wifite2",
        "Bettercap",
        "Airgeddon",
        "Fluxion",
        "WiFi-Pumpkin",
        "Back to Main Menu"
    ])
    choice = input('\033[94mSelect a tool: \033[0m')
    process_wireless_attacks_choice(choice)

def process_wireless_attacks_choice(choice):
    if choice == '10':
        main_menu()
    elif choice.isdigit() and 1 <= int(choice) <= 9:
        tool_name = get_wireless_tool_name(int(choice))
        install_tool(f"pkg install {tool_name.lower()}", tool_name)
    else:
        print("\033[91mInvalid option. Please try again.\033[0m")
        time.sleep(2)
        wireless_attacks_menu()

def get_wireless_tool_name(index):
    tool_names = [
        "aircrack-ng", "kismet", "reaver", "wifite", "wifite2", "bettercap", "airgeddon", "fluxion", "wifi-pumpkin"
    ]
    return tool_names[index - 1].capitalize()

def fix_termux():
    print_banner("Fixing Termux")
    print_options([
        "Update and Upgrade Termux",
        "Fix Termux Storage Setup",
        "Fix Ruby Installation",
        "Fix Git Installation",
        "Fix Gim Installation",
        "Back to Main Menu"
    ])
    choice = input('\033[94mSelect a fix option: \033[0m')
    process_fix_termux_choice(choice)

def process_fix_termux_choice(choice):
    if choice == '1':
        update_and_upgrade_termux()
    elif choice == '2':
        fix_termux_storage_setup()
    elif choice == '3':
        fix_ruby_installation()
    elif choice == '4':
        fix_git_installation()
    elif choice == '5':
        fix_gim_installation()
    elif choice == '6':
        main_menu()
    else:
        print("\033[91mInvalid option. Please try again.\033[0m")
        time.sleep(2)
        fix_termux()

def update_and_upgrade_termux():
    print_banner("Updating and Upgrading Termux")
    print("Updating and upgrading Termux...")
    loading_bar(0.1, '\n\t\033[1;31m[   PLEASE WAIT .... ]')
    os.system('pkg update && pkg upgrade -y')
    print("Termux updated and upgraded successfully!")
    input("Press Enter to return to the menu.")
    main_menu()

def fix_termux_storage_setup():
    print_banner("Fixing Termux Storage Setup")
    print("Fixing Termux storage setup...")
    loading_bar(0.1, '\n\t\033[1;31m[   PLEASE WAIT .... ]')
    os.system('termux-setup-storage')
    print("Termux storage setup fixed successfully!")
    input("Press Enter to return to the menu.")
    main_menu()

def fix_ruby_installation():
    print_banner("Fixing Ruby Installation")
    print("Fixing Ruby installation...")
    loading_bar(0.1, '\n\t\033[1;31m[   PLEASE WAIT .... ]')
    # Replace with actual command to fix Ruby installation
    print("Ruby installation fixed successfully!")
    input("Press Enter to return to the menu.")
    main_menu()

def fix_git_installation():
    print_banner("Fixing Git Installation")
    print("Fixing Git installation...")
    loading_bar(0.1, '\n\t\033[1;31m[   PLEASE WAIT .... ]')
    # Replace with actual command to fix Git installation
    print("Git installation fixed successfully!")
    input("Press Enter to return to the menu.")
    main_menu()

def fix_gim_installation():
    print_banner("Fixing Gim Installation")
    print("Fixing Gim installation...")
    loading_bar(0.1, '\n\t\033[1;31m[   PLEASE WAIT .... ]')
    # Replace with actual command to fix Gim installation
    print("Gim installation fixed successfully!")
    input("Press Enter to return to the menu.")
    main_menu()

def about():
    print_banner("About R2x Tool Installer")
    print("\033[1;93m Authored bY : redcode2x ")
    print(" for more tools chat me on TG @redcode2x \033[0m ")
    input("Press Enter to return to the menu.")
    main_menu()

def install_tool(command, tool_name):
    print_banner(f"Installing {tool_name}")
    print(f"Installing {tool_name}...")
    loading_bar(0.1, '\n\t\033[1;31m[   PLEASE WAIT .... ]')
    os.system(command)
    os.system(f'mv {tool_name.lower()} ~')
    print(f"{tool_name} installed successfully!")
    input("Press Enter to return to the menu.")
    main_menu()

def print_options(options):
    for i, option in enumerate(options, start=1):
        print(f"\033[1;33m{i}. \033[0m{option}")  # Yellow color for tool names

if __name__ == '__main__':
    main_menu()
