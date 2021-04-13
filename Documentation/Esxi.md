# Setting up an Esxi Install
Esxi is a type one bare metal hypervisor used by vmware to run virtual machines and is specifically used by vmware as a way to run its virtual machines. 

## Rufus 
Rufus is a windows program that allows users to create bootable usb drives for installing operating systems such as linux or windows, or in this case, our Esxi Installation. 


1. Download Rufus 
2. Download or create a ESXi image - as of writing the latest version of ESXi is 6.7, however downloads for erlier verions up to 5.5 can be used 
3. Connect the USB drive to the computer, while it does not have to be formatted at this stage, i find that it helps if it is. 

## Using Rufus 
Rufus is a windows program that allows users to create bootable usb drives for installing operating systems such as linux or windows, or in this case, our Esxi Installation. 


**Device Properties**
Device: ```USB drive name```
Boot Selection: ```VMware isntallation ISO Image```
Partition Scheme: ```MBR``` 
>**Note:** MBR (Master Boot Record) and GPT (GUID Partition Table) are two different ways of partitioning data on a storage drive. 
Target system: ```BIOS or UEFI```

**Format Options** 
Volume Lable: ```(Usually autofilled)```

