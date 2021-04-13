
# Setting up vagrant 
ubuntu/trusty64 Vagrant box


# Vagrant 
Vagrant allows for virtualization of linux system within a computer, allowing for projects to work within their own containerized environment (basically it means that you know what dependencies are installed onto a system) 

## Installation 
Download the vagrant packages:   
```npm apt-get install vagrant```

Move them to the correct location + unzip files 


Extra: Add vagrant to the PATH:  
```Export PATH=$PATH:/opt/vagrant``` (in my case)

This means that you can use the “vagrant” cmd anywhere on your linux system
To add the program permanently (on ubuntu), add the path to ```/etc/environment ```

> add :/opt/vagrant to the end of path (inside the quotation marks)

## Install a virtualization software
In this case we will install the commmonly used virtualbox

```Sudo apt-get install virtualbox ```

## Setting up a vagrant vm
Make sure to make a directory and use ```cd ~/vagrantProject``` to be inside the directory you want the vagrant box to be located in.

You can pull pre existing repos of common operating systems with no dependencies installed as vagrant boxes 

```Vagrant init hashicorp/precise64```   
Or for a more updated ubuntu build, use 
```Vagrant init ubuntu/trusty64```

This will place a vagrantfile in your directory

Connect to the box using:   
```Vagrant up```  - boots up the vm (you have to be in the directory storing the vm)  
```Vagrant ssh``` - ssh’s you into the vm

The location with the Vagrantfile in is copied across to the VM
Any files stored in the directory with Vagrantfile will also appear (sync) in the VM under /vagrant

Install the software you want to use 
Run    do-release-upgrade to upgrade the version of the vagrant box (setup) that you are using
If installing pip (because pip --version == 1.0)
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py


phpMyAdmin login screen
We can also use the VM as a seperate system so we can test connections as if there were two seperate computers, this is great for testing database and server connections, as well as hosting both on seperate VM's then attempting to connect to your system using you main OS - just like a normal user would in real life. 


## Shuting Down a Vagrant Machine
To suspend a machine (save current state and stop it): 



# Initial Server Setup 
While setting up a lamp stack from a fresh install of a linux distrabution, there can be some issues - mainly to do with the security of the server.

## Connecting to the server 
When you first finish the installation of the linux operating system onme of the first things to do is actually access it from another computer that has a UI or a terminal interface - basically anything with a screen can do.

### Secure Shell (SSH)
Secure Shell can be used to access the server over port 22
```
ssh root@server_ip 
```
We want to log in as root so that we can get administrator privilages from a remote system.

## Create a new User 
While changing the system (specifically /var/www in our case) using root can be easy, one of the major issues with using root is that it has access to all of the operating system. 

We can create a new user using:
```
adduser <username>
```

We can then grant the ability for the account to use `sudo` privilages by adding the user to the `sudo group`:
```
usermod -aG sudo <username>
```
This allows the user to use the `sudo` command without having to enter in the password every time he wants to change something outside of the home directory / requires admin access.


## Setting up Firewalls
More infomation is avalible at: https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands
Ubuntu apps can use the ufw firewall (uncomplicated firewall)
The firewall acts as an interface to the computers iptables to easily set access to certian applications by name or by port number. 
For the web server, we need to make sure that `OpenSSH` is allowed by the firewall, this can also be 

To start ufw:
```
ufw enable
```

To stop ufw: 
```
ufw disable
```

You can allow access through the firewall either by stating the name of the program or the port number that it uses:
```
ufw allow OpenSSH
```
or alternitivly
```
ufw allow 22
```

To block a program or port access to the server - once again, this can be done via port numebr as well: 
```
ufw deny OpenSSH 
```

To find out the status of ufw:
```
ufw status
```



# Setting up LAMP Stack
L - linux
A - apache
M - mySQL
P - php 

>**Note:** Most of what is below can be found at: 
https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04





## 1 Setting up Apache
you can install apache on ubuntus package manager, ```apt```:  
```sudo apt-get install apache2```

### Adjusting firewall 
we should check / adjust the firewall to allow incoming traffic from other computers.
```sudo ufw app list```

with this command we should get the following results
```
Output
Available applications:
  Apache
  Apache Full
  Apache Secure
  OpenSSH

```

If we look at the ```Apache Full``` we get:
```
Output
Profile: Apache Full
Title: Web Server (HTTP,HTTPS)
Description: Apache v2 is the next generation of the omnipresent Apache web
server.

Ports:
  80,443/tcp
```

we can allowin incoming http and https using 
```sudo ufw allow in "Apache Full"```

### Accessing the server through a browser 
On a browser we can access our apache server using:
```http://your_server_ip```

>**Note:** if your accessing the server on the same computer you set the server up on, you can access it by going to:
```http://localhost:80``` with the ```80``` standing for the port number we set up earlier.

### Starting / Stopping the server 
On debian / ubuntu applications we can use: 
```
## Start command ##
systemctl start apache2.service
## Stop command ##
systemctl stop apache2.service
## Restart command ##
systemctl restart apache2.service
```
On Centos/RHEL : 
```
## Start command ##
systemctl start httpd.service
## Stop command ##
systemctl stop httpd.service
## Restart command ##
systemctl restart httpd.service
```





## 2 Installing MySQL 
We can install MySQL using:  
```sudo apt-get install mysql-server```

we can set up security for the system by running:
```sudo mysql_secure_installation``` 
THis asks if you want to secure a password, y for yes or press any other key for no 

The script the asks you to set up a root account - this is the admin account for the mysql database 

**MySQL is now installed**

We can run MySQL using:  
```sudo mysql```

You can run MySQL commands, or exit using:
```exit```






## 3 Installing PHP / mySQL
PHP allows us to display dynamic content with data from a database such as MySQL 

We can install php using - with some pacakges that help us use MySQL:  
```
sudo apt install php libapache2-mod-php php-mysql
```

In most cases we will need to modify the type of file that the apache system looks for. Currently if a user requests a directory from the server, apache will first look for ```index.html```. We can modify this so that it prefers PHP files over others so that it looks for ```index.php```

We can use the text editor nano: 
```sudo nano /etc/apache2/mods-enabled/dir.conf```

We need to turn 
```
<IfModule mod_dir.c>
    DirectoryIndex index.html index.cgi index.pl index.php index.xhtml index.htm
</IfModule>
``` 
Into 
```
<IfModule mod_dir.c>
    DirectoryIndex index.php index.html index.cgi index.pl index.xhtml index.htm
</IfModule>
```
we can then restart apache by using:  
```sudo systemctl restart apache2```

we can also check on the state of apache by using: 
```sudo systemctl status apache2```

Apache should now be serving your domain name. You can test this by navigating to http://your_domain, where you should see something like this:


### Basic SQL commands 
Entering mySQL via a terminal: `mysql -u root -p`
This will propmt you with a password, if entering with root 

Showing all Databases: `show databases;` 
Access Database: mysql -u 
Showing all tables 


##### Databases 
Show all databases:  
`show databases;`

Create new database:  
`create database [database];`  

Select database:   
`use [database];`

Determine what database is in use:   
`select database();`

##### Tables
Show all tables:   
`show tables;`

Show table structure:   
`describe [table];`

List all indexes on a table:  
`show index from [table];`

Create new table with columns: 
`CREATE TABLE [table] ([column] VARCHAR(120), [another-column] DATETIME);`

Adding a column:   
`ALTER TABLE [table] ADD COLUMN [column] VARCHAR(120);`

Adding a column with an unique, auto-incrementing ID:   
`ALTER TABLE [table] ADD COLUMN [column] int NOT NULL AUTO_INCREMENT PRIMARY KEY;`

Inserting a record:   
`INSERT INTO [table] ([column], [column]) VALUES ('[value]', '[value]');`

MySQL function for datetime input:   
`NOW()`

Selecting records:   
`SELECT * FROM [table];`

Explain records:   
`EXPLAIN SELECT * FROM [table];`

Selecting parts of records:   
`SELECT [column], [another-column] FROM [table];`

Counting records: 
`SELECT COUNT([column]) FROM [table];`







## 4 Setting up Virtual Hosts (Not Manditory)
When using apache, you can set up different *virtual* hosts to save different states of configuration.
This is great if you want to set up multiple sites on a single computer / IP address 

On ubuntu 18.04, apache has one set up by default to serve documents from the ```/var/www/html``` directory. 

While this works well for a single site, it can become unweildy if multiple sites need to be hosted. We can create a directory structure starting within ```/var/www``` for a domain. 

>**Note:** While most domains now serve ```www.``` protocol, in the past it was common to have sites with ```ftp``` or other domains so that a single url could be used for multiple purporses.  

Creating the directory for the domian: 
```sudo mkdir /var/www/your_domain```

We can assign ownership to the user (instead of root) by using:  
```sudo chown -R $USER:$USER /var/www/your_domain```

If the permissions have changed, we can use:  
```sudo chmod -R 755 /var/www/your_domain```

Next, create a sample index page:  
```nano /var/www/your_domain/index.html```

And paste: 
```html
<html>
    <head>
        <title>Index 2</title>
    </head>
    <body>
        <h1>This is a second site running on the same IP</h1>
    </body>
</html>
```

In order for apache to serve the correct files, we need to create a virtual host file with the correct dirrectives.  Instead of modifying the default configuration file located at ```/etc/apache2/sites-available/000-default.conf``` directly, let’s make a new one at ```/etc/apache2/sites-available/boilerplate.conf```:    

```sudo nano /etc/apache2/sites-available/boilerplate.conf```

For each site use the following template:
`/etc/apache2/sites-avalible/boilerplate.conf`
```conf
<VirtualHost *:80>
    # Admin email, Server Name (domain name) and any aliases
    ServerAdmin admin@boilerplate.com
    ServerName boilerplate.com
    ServerAlias www.boilerplate.com

    # Index file and Document Root (where the public files are located)
    DocumentRoot /var/www/boilerplate/routes/index.html

    # Custom log file locations
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

We also need to make changes to the httpd.conf file
`/etc/apache2/sites-enabled/httpd.conf`
```conf
<VirtualHost *:80>
    # This first-listed virtual host is also the default for *:80
    ServerName boilerplate.localhost.com
    ServerAlias boilerplate.com 
    DocumentRoot "/var/www/boilerplate"
</VirtualHost>

<VirtualHost *:80>
    ServerName dissertation.localhost.com
    DocumentRoot "/var/www/dissertation"
</VirtualHost>

```


Save and close the file when you are finished.

Let’s enable the file with the a2ensite tool (apache 2 enable site):   
```sudo a2ensite dissertation.conf``` 
#
Disable the default site defined in 000-default.conf:
```sudo a2dissite 000-default.conf```

>**Note:** 000-default.conf is the "welcome to apache" default site

Next, let’s test for configuration errors:
```sudo apache2ctl configtest```

You should see the following output:
```
Output
Syntax OK
```
If not, configtest should usually report back on whats wrong with the file setup.

Restart Apache to implement your changes:  
```sudo systemctl restart apache2```

#### Setting Hosts 
Even though we have out apache sites set up, if they dont have domain names (for example are located on localhost / 127.0.0.1 ) we can modify the hosts file to add the urls to our local IP address. 



you can now go to ```http://dissertation.localhost/``` instead of ```http://localhost/``` due to your new fancy domian



### Problems I Have Run Into 

**Default vhost file**  

From: ```https://support.rackspace.com/how-to/set-up-apache-virtual-hosts-on-the-ubuntu-operating-system/``` 
 
Although you changed the default virtual host, you did leave it in place.

If someone enters the IP address of the cloud server, they are served the contents of that default vhosts file (if you did not set up a separate vhost for the IP address).

Why are they served from that vhost file?

>Apache searches the enabled vhost files in alphabetical order and if it can’t find one for the requested IP address or domain name, it serves the first one (alphabetically).

If you had disabled or deleted the default vhost file, then the contents of domain1.com would be displayed (being before domain2.com alphabetically).

This is something to consider when planning your websites. Do you want a particular domain to be the default? Do you want the IP address to have completely different content?

>**Note:** 
Creating virtual host configurations on your Apache server does not magically cause DNS entries to be created for those host names. You must have the names in DNS, resolving to your IP address, or nobody else will be able to see your web site. You can put entries in your hosts file for local testing, but that will work only from the machine with those hosts entries.

 - each conf is a different server 
 - if you want to have multiple domians on one server, just have them in the same file

### Removing Apache 
You can remove apache by using:  
```sudo apt-get remove apache2```

### Site not found
This is usally because while the configuration file is avalible, it is not enabled - you can enable a site by using ```sudo a2ensite <exampelsite.conf>```. After this you can run ```systemctl reload apache``` to restart the server.


## 5 Testing PHP Processing on the Web Server

In order to test that your system is configured properly for PHP, create a very basic PHP script called info.php. In order for Apache to find this file and serve it correctly, it must be saved to your web root directory.

Create the file at the web root you created in the previous step by running:  
```sudo nano /var/www/your_domain/info.php```

This will open a blank file. Add the following text, which is valid PHP code, inside the file:  
info.php
```php
<?php
phpinfo();
?>
```
When you are finished, save and close the file.

Now you can test whether your web server is able to correctly display content generated by this PHP script. To try this out, visit this page in your web browser. You’ll need your server’s public IP address again.

The address you will want to visit is:

```http://your_domain/info.php```


The page provides basic details about the server from the perspective of php - you can remove this file (for security reasons) using:  
```sudo rm /var/www/your_domain/info.php```


## 6 (Optional) Creating a symlink from your files to the actual location 
Our files for the web server are hosted under ```/var/www```, while this is a good place for the computer to store files, for us it can make it difficult to create an deploy data if we want to keep a normal directory strucutre ```home/Documents/Programming ```. 

This is where simulated links / soft links, come in:

### Creating a symlink 
The syntax for a symlink is 
Files:  
```ln -s {source-filename} {symbolic-filename}```
Directories:  
```ln -s {source-dir-name} {symbolic-dir-name}```

We can verify our links by using:   
```ln -l {source-filename} {symbolic-filename}```

So for our web server, we can use:   
```ls -s /var/www/ /home/user/Documents/Programming/```

In my case, we can see that the ```dissertation``` project links to ```/var/www/dissertation```:
```
1 george george     22 May 29 12:08  dissertation -> /var/www/dissertation/
```


## 7 phpMyAdmin 
### Installation 
phpMyAdmin can be used to setup and look at your databases without neeeding to use the mySQL command line.

To install phpMyAdmin, we can use ubuntus ```apt``` package manager:  
```sudo apt install phpmyadmin php-mbstring php-gettext```

>**Note:** **Warning**: When the prompt appears, ```apache2``` is highlighted, but **not** selected. If you do not hit SPACE to select Apache, the installer will not move the necessary files during installation. Hit ```SPACE```, ```TAB```, and then ```ENTER``` to select Apache.

After this we need to enable the ```mbstring``` addon:  
```sudo phpenmod mbstring```

Then we can restart apache to see if it works:  
```sudo systemctl restart apache2```

### Configuring Password Access 

Installing PHP onto a server account will automatically create a database *user* called ```phpmyadmin``` which peforms underlying processes in the program. 

Using this account can cause security risks so instead we can log in as ```root```. 

In Ubuntu systems running MySQL 5.7 (and later versions), the root MySQL user is set to authenticate using the auth_socket plugin by default rather than with a password. This allows for some greater security and usability in many cases, but it can also complicate things when you need to allow an external program — like phpMyAdmin — to access the user.

In order to log in to phpMyAdmin as your root MySQL user, you will need to switch its authentication method from auth_socket to mysql_native_password if you haven’t already done so. To do this, open up the MySQL prompt from your terminal:  

```
sudo mysql
```

Next, check which authentication method each of your MySQL user accounts use with the following command:
```
mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;
```


To configure the root account to authenticate with a password, run the following ```ALTER USER``` command. Be sure to change ```password``` to a strong password of your choosing:  

```
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'; 
```

Then we can run ```FLUSH PRIVILEGES``` which tells the server to reload the grant tables.

we can check that this works by looking at the ```mysql.user``` table using:   
```
mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;
```
If the root account now has the ```mysql_native_password``` as its plugin, the change worked and you can now log in as root with the chosen password


### Problems I Have Run Into 

When trying to access phpmyadmin, the following error comes up:  
Errors have been detected on the server. 

```
Warning in ./libraries/plugin_interface.lib.php#551
count(): Parameter must be an array or an object that implements Countable

Backtrace

./libraries/display_import.lib.php#371: PMA_pluginGetOptions(
string 'Import',
array,
)
./libraries/display_import.lib.php#456: PMA_getHtmlForImportOptionsFormat(array)
./libraries/display_import.lib.php#691: PMA_getHtmlForImport(
string '5ef4add4e9d69',
string 'database',
string 'hovercraft',
string '',
integer 2097152,
array,
NULL,
NULL,
string '',
)
./db_import.php#43: PMA_getImportDisplay(
string 'database',
string 'hovercraft',
string '',
integer 2097152,
)
```

This is due to the version of phpmyadmin being outdated on ubuntus apt-get / centos yum repositories - you end up installing a depreciated (outdated) version. 


#### Upgrading phpmyadmin to the latest version 
```
 1997  cd Documents/Programming/Projects/PHP
 1998  ls
 1999  code PHP_Diss/
 2000  clea
 2001  clear
 2002  ls
 2003  top
 2004  clear
 2005  cd
 2006  sudo zip -r ~/Documents/phpmyadmin.zip P/dissertation$ ls
 2007  sudo zip -r ~/Documents/phpmyadmin.zip /usr/share/phpmyadmin
 2008  ls
 2009  cd Documents/
 2010  ls
 2011  cd /usr/share/
 2012  ls
 2013  clear
 2014  ls
 2015  rm -rf phpmyadmin
 2016  clear
 2017  ls
 2018  sudo rm -rf phpmyadmin
 2019  ls
 2020  cd
 2021  clear
 2022  ls Downloads/
 2023  sudo unzip ~/Downloads/phpMyAdmin-5.0.2-all-languages.zip /usr/share/phpmyadmin
 2024  sudo mkdir /usr/share/phpmyadmin
 2025  sudo unzip ~/Downloads/phpMyAdmin-5.0.2-all-languages.zip /usr/share/phpmyadmin
 2026  cd /usr/share
 2027  ls
 2028  ls phpmyadmin/
 2029  ls
 2030  ls phpmyadmin/
 2031  sudo unzip ~/Downloads/phpMyAdmin-5.0.2-all-languages.zip -d usr/share/phpmyadmin
 2032  sudo unzip ~/Downloads/phpMyAdmin-5.0.2-all-languages.zip -d /usr/share/phpmyadmin
 2033  ls phpmyadmin/
 2034  cd phpmyadmin/
 2035  ls
 2036  clear
 2037  ls
 2038  sudo mv phpMyAdmin-5.0.2-all-languages/ /usr/share
 2039  ls
 2040  cd ..
 2041  ls
 2042  sudo rm -rf phpmyadmin
 2043  ls
 2044  sudo mv phpMyAdmin-5.0.2-all-languages/ phpmyadmin
 2045  ls
 2046  ls phpmyadmin/
 2047  cd 
 2048  sudo systemctl restart apache2
 2049  history

```














## General Tips
Checking that apache is running: `service apache2 status`  
Checking that mySQL is running: `service mysql status`  
Checking the active sites on apache: `cd /etc/apache2/sites-enabled`    
quit vim / less: `SHIFT + :` + `q`   
Accessing mysql via a terminal: `mysql -u root -p`












# XAMPP
XAMPP is the linux version of WAMP - Windows, Apache, MySQL, PHP.

>**Note:** Most of what is below can be found at: https://www.apachefriends.org/faq_linux.html

## Installing XAMPP 
You can download the installer at : https://www.apachefriends.org/index.html

Once downloaded, we can change the permissions of the installer (so it has permission to execute on our linux system):
```chmod 755 xampp-linux-*-installer.run```
Run the installer using:
```sudo ./xampp-linux-*-installer.run```

This will run a installation wizard with a graphical component.

## Starting XAMPP 
We can start XAMPP by using: 
```sudo /opt/lampp start```

You can also launch a graphical interface by using:
```
cd /opt/lampp

sudo ./manager-linux.run (or manager-linux-x64.run)
```

We can stop XAMPP using:  
```sudo /opt/lampp/lampp stop```







# AWS (Amazon Web Services)

Note: Most of the infomation for this came from: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.html#prepare-lamp-server

You can use a EC2 (Elastic Container 2) virtual machine, hosted on AWS to host a LAMP server, allowing your server to already be set up with an IP and port configurations. (overall it just makes some of the steps easier)

We can start by launching a EC2 virtual machine with a AMI (Amazon Machine Image). This can be picked from a variety of linux distrubutions or windows servers. 

>**Note:** For a basic LAMP stack instace, you can follow through with the default settings that amazon used when generating a EC2 instance.

For Step 6 of the generation - configuring security groups, you can set up the base ports for a LAMP stack as such: 
```
Type          Protocol    Port Range  Source Description
SSH             TCP          22          0.0.0.0/0
HTTP            TCP          80          0.0.0.0/0
HTTP            TCP          80          ::/0
MYSQL/Aurora    TCP         3306        0.0.0.0/0
```

### Creating a Key pair 
This step will create (or re-use) a public-private key pair.
You should download the `.pem` file, this contains the private part of the key to the server (think of it like the key to a lock)

If your using a linux system, you will need to change the permissions of the private key. This can be done using: 
```chmod 400 key-pair.pem```


Generate the instance 

## Connecting to the AWS instance 
The main way that you can connect to your instace is via a remote SSH link.   

Linux: 
```ssh -i /path/my-key-pair.pem my-instance-user-name@my-instance-public-dns-name```

For example:
```
ssh -i LAMPStack.pem ec2-user@ec2-18-132-39-13.eu-west-2.compute.amazonaws.com
```

>**Note:** when logging into the instance, the username is usually defaulted to `ec2-user`. Its recommended to log in as this user rather than root.

IF working correctly, your terminal should now be linked, showing files and data from the aws system rather than your own computer. 


## Preparing the LAMP Server 
First, to ensure that all of the software packages are up to date, we can run the package update manager using:  
`sudo yum update -y`

## Installing Require Content 
We can now install the required packages for a LAMP server.
```
sudo yum install httpd -y
sudo yum install php
sudo yum install mysql
```
This will install apache,php,mysql to the instance.


## Setting up the Stack

### Setting up apache
Run apache using: 
`sudo service httpd start`  

Set file presmissions using: 
`sudo usermod -a -G apache ec2-user` 

This will create a new user group called `apache` and add `ec2-user` into it.  

Restart your connection by exiting using `exit` 

We can see that we are in the apache group by using `groups`  

Change the ownership of `/var/www` (the websites location) to the apache group.
```sudo chown -R ec2-user:apache /var/www```

We can add group read/write permission to `/var/www` using:
```sudo chmod 2775 /var/www```

Then: 
`find /var/www -type d -exec sudo chmod 2775 {} \;`

We can add group read/write permission recursivly to existing `/var/www` files using: 
`find /var/www -type f -exec sudo chmod 0664 {} \;`

The above code allows the ec2-user and any future members of the `apache` group to read, write, edit and delete files in the apache document root.

We can test the above code by adding a new page and seeing if it appears on our server: 
`echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php`

The above code will add the phpinfo.php page to our site root, for example: 
`http://my.public.dns.amazonaws.com/phpinfo.php` 

In my case this was: 
http://ec2-18-132-39-13.eu-west-2.compute.amazonaws.com/phpinfo.php 


### Setting up mysql 
Start mysql using:   
`sudo service mysqld start`

If the service does not exist (meaning mysql is proberbly not installed) we can install mysql using:  
`sudo yum install mysql mysql-server`

We can secure the installation by running:   
`sudo mysql_secure_installation`

- Set a password (you can also leave it blank)
- choose whether to allow remote access (if unsure, say no)
- remove the anonymose users
- remove the test database 
- reload the privilege table and save changes 


### Installing phpMyAdmin
If using an aws-linux instance, phpMyAdmin does not come on the package manager, we can install it manually though.

Install the required dependancies:   
`sudo yum install php72-mbstring.x86_64 -y`

Restart apache:   
`sudo service httpd restart`

Navigate to the apache document root:   
`cd /var/www/html`  

We can select a phpMyAdmin source and download it into the current directory using:
`sudo wget https://www.phpmyadmin.net/downloads/phpMyAdmin-latest-all-languages.tar.gz`   

Extract the pakage using: 
`tar -xvzf phpMyAdmin-latest-all-languages.tar.gz`   

We now have the phpmyadmin directory in the html folder, abeilt with a complex name, we can change this using: 
`sudo mv phpMyAdmin-5.0.2-all-languages phpmyadmin`  

We should now have a directory called `phpmyadmin`

If not already, start mysqld using: 
`sudo service mysqld start`

You should be able to go to http://my.public.dns.amazonaws.com/phpmyadmin and access the database 






## Issues ive run into 
### PHP version not correct 
Amazon will usually install php version 5 isntead of 7, this can be fixed by running the below commands in sequence: 
```
sudo service httpd stop
sudo yum remove php*
sudo yum remove httpd*
sudo yum clean all
sudo yum upgrade -y
sudo yum install php73
```
Installing php73 will also install httpd with the correct version
(remember to start httpd (apache) again)

### mysqqi extension is missing when going to /phpmyadmin
First restart apache to check that all the scritps installed are running:   
`sudo /etc/init.d/httpd restart`  

Otherwise this is due to the package `php73-mysqlnd` missing, you can install it for php7 using:   
`sudo yum install php73-mysqlnd`  


