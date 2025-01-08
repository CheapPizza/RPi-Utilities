This fstab entry allows you to automatically mount an external device and doesn't require it to be connected on boot.


```
PARTUUID=YOUR_PARTUUID  /mnt/drive        exfat   defaults,noatime,rw,nofail,x-systemd.automount,x-systemd.idle-timeout=30s  0  0
```
Check PARTUUID and filesystem type with  
```
blkid
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
