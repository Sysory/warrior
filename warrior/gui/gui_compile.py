import subprocess

def main():
    cmd_str = "pyuic6 /home/sysory/Documents/warrior/gui/RHBZ.ui \
    -o /home/sysory/Documents/warrior/RHBZ_design.py"
    subprocess.run(cmd_str, shell=True)
    
if __name__ == "__main__":
    main()