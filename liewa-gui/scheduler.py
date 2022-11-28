import os
import subprocess
from getpass import getpass
import re

from execute_command import execute

class Systemd:
    def __init__(self):
        self.service_name = "liewa.service"
        self.timer_name = "liewa.timer"

    def update(self):
        timer_output = execute(f"systemctl --user status {self.timer_name}").decode("utf-8")
        service_output = execute(f"systemctl --user status {self.service_name}").decode("utf-8")
        running = False
        if re.search("(?<=Active:\s)\w*", timer_output):
            running = True

        return timer_output+'\n'+service_output,running


        # password = "sudo_password"
        # proc = subprocess.Popen(['sudo', 'systemctl', 'status', self.service_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # proc.communicate(password.encode())
        # output, errors = proc.communicate()
        # print(output,errors)
    
    def create_scheduler(self):
        with open("liewa.service", "w") as f:
            f.write("""[Unit]
Description=Liewa Service
[Service]
Type=simple
ExecStart=$(which liewa)""")
        with open("liewa.timer", "w") as f:
            f.write("""[Unit]
Description=Liewa Timer
[Timer]
OnBootSec=10
OnUnitActiveSec=30
AccuracySec=1ms
[Install]
WantedBy=timers.target""")
        os.system("mkdir -p ~/.config/systemd/user/")        

        os.system(f"cp {self.service_name} ~/.config/systemd/user/")
        os.system(f"cp {self.timer_name} ~/.config/systemd/user/")

        execute(f"systemctl --user enable {self.timer_name}")
        execute(f"systemctl --user start {self.timer_name}")
        execute(f"systemctl --user status {self.timer_name}")

        os.system(f"rm {self.service_name}")
        os.system(f"rm {self.timer_name}")

    def delete_scheduler(self):
        for unit_file in [self.service_name, self.timer_name]:
            execute(f"systemctl --user stop {unit_file}")
            execute(f"systemctl --user disable {unit_file}")
            os.system(f"rm ~/.config/systemd/user/{unit_file}")

    def reload_scheduler(self):
        execute("systemctl --user daemon-reload")


class Launchd:
    def __init__(self):
        self.service_name = "liewa.service"
        self.timer_name = "liewa.timer"
        self.update()
    
    def update(self):
        pass

    def create_scheduler(self):
        pass

    def delete_scheduler(self):
        pass

    def reload_scheduler(self):
        pass


class Schtasks:
    def __init__(self):
        self.service_name = "liewa.service"
        self.timer_name = "liewa.timer"
        self.update()
    
    def update(self):
        pass

    def create_scheduler(self):
        pass

    def delete_scheduler(self):
        pass

    def reload_scheduler(self):
        pass

if __name__ == '__main__':
    scheduler = Systemd()
    # scheduler.create_scheduler()
    # scheduler.delete_scheduler()
    # scheduler.reload_schedluer()
    # scheduler.test_now()
    scheduler.update()
