import time
import sys
import os
import subprocess
import psutil

# Define color codes
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def type_writer(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

arch_logo = f"""{CYAN}{BOLD}
                /\\
               /  \\    {RESET}I use {BOLD}Arch Linux{RESET}{CYAN}
              /\\   \\
             /      \\
            /   ,,   \\   {RESET}- btw
           /   |  |  -\\
          /_-''    ''-_\\
{RESET}"""

os.system('clear' if os.name == 'posix' else 'cls')

def get_system_info():
    kernel = subprocess.check_output("uname -r", shell=True).decode().strip()
    cpu = subprocess.check_output("lscpu | grep 'Model name' | sed 's/Model name:/CPU:/'", shell=True).decode().strip()
    mem = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
    gpu = subprocess.check_output("lspci | grep VGA | sed 's/.*: //' | head -n 1", shell=True).decode().strip()
    
    packages = subprocess.check_output("pacman -Q | wc -l", shell=True).decode().strip()
    
    return kernel, cpu, mem, gpu, packages

kernel, cpu, mem, gpu, packages = get_system_info()

type_writer(f"{GREEN}user@arch{RESET}:{BLUE}~{RESET}$ neofetch", delay=0.05)
time.sleep(0.5)

print(arch_logo)
type_writer(f"{BOLD}OS:{RESET} Arch Linux x86_64")
type_writer(f"{BOLD}Kernel:{RESET} {kernel}")
type_writer(f"{BOLD}CPU:{RESET} {cpu}")
type_writer(f"{BOLD}Memory:{RESET} {mem:.2f} GB RAM")
type_writer(f"{BOLD}GPU:{RESET} {gpu}")
type_writer(f"{BOLD}Packages:{RESET} {packages} (pacman)")
print()

type_writer(f"{BOLD}{CYAN}Yes, I use Arch btw.{RESET}", delay=0.07)
