# Enabling the Hardware Watchdog on Raspberry Pi 4/5

Often RaspberryPis are left running unattended. The Pi could run out of memory and freeze especially
if you have swap disabled when running the SD card in read-only mode.  
Luckily RaspberryPis have a built-in hardware watchdog.
This wathcdog will reboot the Pi if /dev/watchdog is left open but nothing is
inserted in a while (usually 15 seconds). The watchdog daemon ran by systemd is the easiest
way of poking the watchdog but it can also be done by your own script.  

Optionally you can define a heartbeat file which must be updated regularly. I have used this in a 
Python program that once froze because the Pi ran out of memory. This didn't stop the watchdog
daemon so no reboot occured. The Python program was modified to update a file (/tmp/heartbeat)
with the current unix timestamp every 30 seconds and the watchdog daemon was set to look at the file.
Now if the Python program ever becomes unresponsive the watchdog daemon will reboot the Pi after some time.  
Remember that if you make the daemon look at a heartbeat file and then stop the program writing to the file
the system will reboot unless you also stop the watchdog daemon.

## 1. Enable the Watchdog Kernel Module

Edit `/boot/firmware/config.txt` and add:
```ini
dtparam=watchdog=on
```
Reboot to apply changes:
```sh
sudo reboot
```

## 2. Install Watchdog Utilities

```sh
sudo apt update
sudo apt install watchdog
```

## 3. Configure the Watchdog Service

Edit `/etc/watchdog.conf` and ensure these lines are present:
```ini
watchdog-device = /dev/watchdog  
watchdog-timout = 15  # 15 seconds is the maximum for RaspberryPi

# max-load-1 = 24  
# file = /var/run/watchdog-heartbeat
# change = 60
```
- `max-load-1`: Average load for 1 minute span (optional).  

- `file`: Path to the heartbeat file to monitor (optional).
- `change`: Time in seconds before the file must be updated.

## 4. Enable and Start the Watchdog Service

```sh
sudo systemctl enable watchdog
sudo systemctl start watchdog
```

## 5. (Optional) Heartbeat File Script

If using a heartbeat file, create a script to update it regularly:
```sh
while true; do
    touch /var/run/watchdog-heartbeat
    sleep 30
done
```
Run this script as a background service or cron job.

---

**References:**
- [man watchdog.conf](https://manpages.debian.org/testing/watchdog/watchdog.conf.5.en.html)