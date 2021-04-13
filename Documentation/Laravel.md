# Setup 
The requires programs are required to run a homestead environment 


# Vagrant 
Vagrant allows for virtualization of linux systems within a computer, allowing for projects to work within their own containerized environment (basically it means that you know what dependencies are installed onto a system) 

### Installing a Virtulisation Software 
To use vagrant, a pre-esixting virtulisation software needs to be installed. In our case, we can use virtualbox a common virtulisation software.

```
sudo apt-get install virtualbox
```

## Installation 
Download the vagrant packages from the [vagrant website](https://www.vagrantup.com/downloads.html) and move the files to your preffered directory location (if you dont know where this, a good starting location is /opt)

Add vagrant to the PATH using ```Export PATH=$PATH:/opt/vagrant```

> **Note** You can commonly run across issues if vagrant is not updated, if this happens, simply download thje latest version of vagrant and unzip the file in the same location as the old version of vagrant (```/opt/vagrant```). You can check the version of vagrant using ```vagrant version```

### What is PATH?
PATH allows vagrant to be run from various projects, without having to find / import the executibles into the project first. Programs that are stored in the path directories (like ```/usr/bin```) can be accessed anywhere. 

This means that you can use the “vagrant” cmd anywhere on your linux system. 
> To add the program permanently (on ubuntu), add the path to ```/etc/environment``` by modifying the file, adding ```:/opt/vagrant``` to the end of file (inside the quotation marks).

Its directories seperated by a ```:``` 

## Alternate Installation 
If the download or your package manager doesnt work, you can also use ```wget``` to install the latest version:  
```
wget https://releases.hashicorp.com/vagrant/2.2.7/vagrant_2.2.7_x86_64.deb
```
then run:   
```
sudo apt install ./vagrant_2.2.7_x86_64.deb
```

### Setting up a Vagrant VM 
One of the great things about vagrant is the ability to pull pre-existing, user generated repos of common operating systems to virtulise, these are known as vagrant boxes

In the project file use:
```
vagrant init hasicorp/prescise64
//or for a more updated ubuntu build, use 
vagrant init ubuntu/xenial64
```
This generates a .vagrant file in the project that contains the infomation used to set up the vm in the future - similar to a .git file

#### Boot up and Connection 
To boot up the VM, use ```vagrant up```
To connect to the VM, use ```vagrant ssh```

You are now using a bash shell script in another virtual computer

Default vagrant boxes are usually set up with a vagrant and the root account by default. You can access the root account using ```- su``` but you will first need to set a password usign ```sudo passwd root```. 

If the current VM does not have the most up to date software, we can use ```do-release-upgrade``` to update the version of the vagrent box to the latest version released.

Another issue is that in some boxes, software that is normally on linux systems can be 'stuck' at version 1.0, below is a list of commands to update the software: 

* pip (python packages): ```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```



One of the cool things about vagrant VM's is that any file that is stored in the same project directory that that .vagrant file is in, is accessable within the VM under the ```/vagrant``` directory.  

 > **Common Vagrant Commands**  
    ```destroy```:        stops and deletes all traces of the vagrant machine  
    ```status ```:        outputs status Vagrant environment  
    ```halt   ```:        stops the vagrant machine  
    ```help   ```:        shows the help for a subcommand  
    ```init   ```:        initializes a new Vagrant environment by creating a Vagrantfile  
    ```reload ```:        restarts vagrant machine, loads new Vagrantfile configuration  
    ```resume ```:        resume a suspended vagrant machine  
    ```ssh    ```:        connects to machine via SSH  
    ```up     ```:        starts and provisions the vagrant environment  



#### Outside Connections 
Vagrant will not normally allow outside connections to the VM withoug going through proper channles (ssh / http access). This can be an issue if you want to use the VM to act as a LAMP stack or a database host.

This can be changed in the Vagrantfile, located in the directory you set up the vagrant VM in 
```
#config.vm.network "private_network", ip: "192.168.33.10" 
to 
config.vm.network "private_network", ip: "192.168.33.10" 
```
However even though we can now ping the vm, we still can access it via mysql, this is due to the firewall not allowing us through 

Port forwarding vagrant to allow communication with own computer / database 

#### Issues i've run into 
> VM hangs on ```ssh auth method``` on bootup  
This is due to the vm failing to port forward its ssh port (2222), while vagrant usually automatically port forwards the ssh port, this can sometimes fail. To solve this issue, we need to add the port forwarding manually into the Vagrantfile.
```ruby
  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080
    config.vm.network "forwarded_port", guest: 22, host: 2222, host_ip: "127.0.0.1", id: 'ssh'

```

# Homestead 
When installing homestead, install into /home directory as a precaution. 
```git clone https://github.com/laravel/homestead.git ~/Homestead```

Once the homestead directory is cloned, run ```bash init.sh``` to create a ```homestead.yaml``` repository. 

```yaml
---
ip: "192.168.10.10"
memory: 2048
cpus: 2
provider: virtualbox

authorize: ~/.ssh/id_rsa.pub ## RSA public key

keys:
    - ~/.ssh/id_rsa ## Private key file - very precious, keep secure

folders:
    - map: ~/Documents/Programming/Projects/PHP/Laravel-Boilerplate/ # map the computers folder to -
      to: /vagrant/Laravel-Boilerplate/ # the folder inside the VM

sites:
    - map: boilerplate.test # URL want to access from computer browser
      to:  /vagrant/Laravel-Boilerplate/public # what folder the user wants to access when they use the URL 

databases:
    - homestead

features:
    - mariadb: false
    - ohmyzsh: false
    - webdriver: false

# ports:
#     - send: 50000
#       to: 5000
#     - send: 7777
#       to: 777
#       protocol: udp

```
## Settings RSA Keys 
RSA keys are the primary way in which computers encypt and decypt infomation. 2 Asymmestric keys are used; a ```public``` key and a ```private``` key. The public key is the one handed out to sites, with the private key being used to prove that you have the correct permissions 

> Essentially, if a directory was a chest or somethign; the public key is a lock, with the private key being the actual key. A user needs to prove they have permiessions by unlocking the lock to get access to the chest.

To find your ssh keys, run:
```
file ~/.ssh/id_rsa.pub 
```
 
private key: ```file ~/.ssh/id_rsa```

Generating an ssh key: 
```ssh-keygen -t rsa -C "you@homestead"```

## Setting Hosts 
To access a website via its adress, we normally have to go through a DNS server, for local hosts, we can use a program called mDNS that provides the services for small networks that dont have a dedicated name server (DNS). This is done automatically on linux systems, so we dont have to worry about it.

Our hosts file is located at ```/etc/hosts```
Example host file: 
```yaml
127.0.0.1       localhost
127.0.1.1       george-Aspire-VN7-592G # computer name
127.0.0.1       boilerplate
127.0.0.1       dissertation

## added hosts
192.168.10.10   boilerplate.test  #example vagrant vm connection

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

```


## Composer 
Installing composer:    
```shell
sudo apt-get install composer 
```

## Laravel 
Once composer is installed, we can install laravel using the package manager:   
```shell
composer global require laravel/installer
```
## Creating the first project 
We can boot up a boiler template with laravel using the following command:  
```laravel new <name>```

This pastes code into the folder that does the following:  
- databases
- views (MVC)
- storage 
- testing
- configuration 

## Application structure 
```shell
/app
/bootstrap
/config
/database
/public
/resources
/routes
/storage
/tests
/vendor
   .env
   .env.example
   .gitattributes
   .gitignore
   artisan
   phpunit.xml
   readme.md
   server.php
```

**app** 
Application folder and contains the entire source code of the project. When a user first enters a website, this hadles scripts and exceptions.

**Bootstrap**
This include all the scripts that app needs to set up the site. It is not twitters 'bootstrap' which is a frontend add on.

**Database**
This directory incudes variosu paarameters for datbase functionality.

**Public**
THis is the root folder of the application, it functions in the same manner as a basic application, as the root. This contains the `index.php` initilisation script.

**Resources**
This contains the filres that enhance the web application. Images, css and other assets are stored here. 

**Storage** 
This contains the files neccesarry for site logging.

**Tests**
Unit tests are stored in this directory.

**Vendor**
Laravel is built ontop of composer depedancies (packages). This file containts all of these dependacies. if you've ever used node, its like the npm file.


## Laravel Confiuration 
### Environment Configuration 
the laravel environent can be confugired using the `.env` file, which contains the necessary variables such a urls, database connections and ports for your application. This limits the need to 





















### Migrating 
Migrating allows laravel to make modifications to the database.
```
php artisan migrate
```
Initially this will run the three files located in `database/migrations`. When run again, php migrations will run any migrations that havent already be run.






## blade template 
```html
<!doctype html>
<html land="en">
<head>
   <meta charset="UTF-8">
   <meta 
      name="viewport"
      content="width=device-width, user-scalable=no, initial-scale=1.0, maximun-scale=1.0, minimum-scale=1.0" 
   >
   <meta
      http-equiv="X-UA-Compatible"
      content="ie-edge"
   >
   <title>Document</title>

</head>
<body>
   <h1>Heading</h1>
<body>
</html>
```



