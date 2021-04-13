

# Git
git is a free and open sourced version control system that allows users to handle updates and changes to source code during software development. While it is primarily designed to work with programming files, it can also work with any type of text file.    




## Setting up git

### Downloading Git
On linux, depending on the distribution and package manager   
ubuntu: ```sudo apt install Git```  
redhat / centos: ```sudo yum install Git```  

### Creating a new Repository 

move to the directory that you want to create
Initilise git using:    
```git init```  

### Add a file to the repo
This is so that git recognises changes and saves the new repo
```touch readme.txt```  
we can chech the new files that git recognises using 
```git status```  

### Adding to the staging branch
This adds all new files to the repo index (.git)
```git add . ```     

### Commiting a file to the local repository
```git commit "message"``     
This commits the files to the local version of the remote repository
If you just had a local repository this would be the last step

### Creating a new remote repository  
```git remote add origin <url>```    
This adds a new repository on the url
The origin is an alias for the url, so instead of calling
your remote repo an long url, you just call it "origin" (like a domain name)

```git remote```        
shows the remote repository that the local repo is linked to

### Uploading work to the remote repository
```git push origin master```  
This pushes the changes in the local remote to the remote repository
on the master branch

#### Additional Infomation 
To see what your origin is: 
```git remote -v```

You can also save your repositories location so you only have to type ```git push```: 
```git --no-pager branch -vv```
If the response has a ```*``` before it, it has been saved as the main repository. 


## Connecting to existing repositories


### Downloading the repository
Go to the directory that you want the repo in
```git clone <remote repo url>```
 
### Adding to the staging branch
```git add . ```       
This adds all new files to the repo index

### Commiting a file to the local repository
```git commit "message"``     
  This commits the files to the local version of the remote repository
  If you just had a local repository this would be the last step

### Pushing files to the remote repository
```git push origin master```  
This pushes files to the origin repo on the master branch

### Pulling new files from the remote repo
```git fetch origin```       
remember that you can just use the url as well

```Git status```   
shows the status of the git repo

## Git branches
git branches are multiple versions of the same projectuseful when you want to make changes to a project that you are unsure about, or when multiple people are working on a project.

### creating a branch
```git branch <branch name>``` (don't name the branch master)

### moving to a branch
```git checkout <branch name>```
 
### merging a branch
move to the branch you want to be merged into another
```git merge <branch>```
    This can result in conflicts, so rungit add <filename>
    to add the edited files to the master repo




## Fork a repository 
A fork is basically a clone of a project repository that is completely independent from its original remote / local repository and future commits are pushed to the new repository other than the old one.

Forking a repository is usually done via the github UI, due to the fact that from git’s perspective, a fork is just another clone of the repository that is now uploaded into a different location ( something other than origin) which is tracked by githubs databases 

Making a fork 
```git clone https://github.com/YOUR-USERNAME/Spoon-Knife```