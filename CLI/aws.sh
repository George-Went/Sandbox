## ---------------------------------
## AWS CLI General Commands 
## ---------------------------------

## Sign in to AWS console 
aws configure

# Get account infomantion 
aws sts get-caller-identity

## ---------------------------------
## S3
## ---------------------------------
# List all dirctories 
aws s3 ls

# List all items in a directory (bucket-name can be considered a directory)
aws s3 ls s3://<bucket-name>

# Copy a file to your local machine
aws s3 cp s3 s3://<s3-bucket> <local file>

## Example (copy hive install files to home directory on a linux system)
aws s3 cp s3 s3://offline-hive-install/install_files/hive_install_1.3.zip ~/

## Copy an entire [bucket/directory] to your local machine
aws s3 cp s3://<s3-bucket> ~/ --recursive 

# Create a bucket
aws s3 mb s3://<bucket-name>

# Delete a bucket 
aws s3 rb s3://<bucket-name>


## ---------------------------------
## ECR
## ---------------------------------
# Log into aws ecr
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 334064387568.dkr.ecr.eu-west-2.amazonaws.com

# list ecr registry 
aws ecr describe-registry

# list all repositories
aws ecr describe-repositories

# list all images (needs --repository-name)
aws ecr describe-images --repository-name hello-world

# Pull docker images 
docker pull 

## Push local image to ECR -------------------------------------
# 1. list images in local docker
docker image ls -a

# 2. tag (name) the image to push to ECR
# (Note: Account is the company account, not your user id)
docker tag hello-world:latest <aws_account_id>.dkr.ecr.eu-west-2.amazonaws.com/hello-world:latest

# 3. you can re-tag an image using
docker tag <image.id> <image.tag>

# 4. Push image to the ECR Repisitory
docker push <account_id>.dkr.ecr.eu-west-2.amazonaws.com/hello-world:latest

# Pull a docker image from ECR 
docker pull <aws_account_id>.dkr.ecr.eu-west-2.amazonaws.com/hello-world:latest

## Delete an Image from ECR --------------------------------------
# 1. List images in a repository 
aws ecr list-images --repository-name <repo name>

# 2. (optional) delete any unwanted tags for the image
aws ecr batch-delete-image --repository-name my-repo --image-ids imageTag=<tag1> imageTag=<tag2>

# 3. Delete a image via the image digest
aws ecr batch-delete-image --repository-name my-repo --image-ids imageDigest=sha256:4f70ef7a4d29e8c0c302b13e25962d8f7a0bd304EXAMPLE

# Note: you can get image digest using 
aws ecr describe-images --repository-name <repo-name>

# You can alost run this all at once: 
# Note that this requires 3 variables: repository name, image-tag, region 
aws ecr batch-delete-image --repository-name hello-world --image-ids imageTag=latest --region region


