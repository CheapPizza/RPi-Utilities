# Automount external drive
This fstab entry allows you to automatically mount an external device and doesn't require it to be connected on boot.


```
PARTUUID=YOUR_PARTUUID  /mnt/drive        exfat   defaults,noatime,rw,nofail,x-systemd.automount,x-systemd.idle-timeout=30s  0  0
```
Check PARTUUID and filesystem type with  
```
sudo blkid
```
Don't include the "" quotes in the PARTUUID  

Arguments:  
PARTUUID=YOUR_PARTUUID -> Partition UUID  
/mnt/drive -> mount point, change to an existing directory  
exfat -> filesystem type on disk, change accordingly  
defaults -> only needs to be included if line would otherwise be empty  
noatime -> no access time logging for slight performance boost  
rw -> read/write access  
nofail -> allow boot without mounting (in case drive is not connected when powering on)  
x-systemd.automount  -> automatically mount drive when attached  
x-systemd.idle-timeout=30s  -> unmount after idling for 30s (will stop a HDD from spinning unnecessarily)  
0 -> don't include in backup  
0 -> don't check on boot with fsck  

## Note about OverlayFS
If you are using OverlayFS to make your SD card read only you may fail to boot even with the nofail argument.  
To stop OverlayFS from touching your external drive add :recurse=0 to /boot/firmware/cmdline.txt like so:  
```
overlayroot=tmpfs:recurse=0
```
The raspi-config utility adds overlayroot=tmpfs to cmdline.txt when enabling OverlayFS but doens't include the recurse=0 option (it apparently used to not recurse by default but now does).  
When exiting raspi-config after enabling OverlayFS choose not to restart, then edit cmdline.txt and reboot.  
Note that changing /boot/firmware/cmdline.txt will stop raspi-config from disabling OverlayFS without warning.  
Presumably this happens because the line now contains :recurse=0 and it is specifically looking for overlayroot=tmpfs.  
Remove :recurse=0 from cmdline.txt and then use raspi-config to disable OverlayFS.  
After rebooting OverlayFS should be disabled.  
If your /boot/firmware/ is already mounted as read-only you need to remount it as read/write to make changes to cmdline.txt:  
```
sudo mount -o remount,rw /boot/firmware
```
