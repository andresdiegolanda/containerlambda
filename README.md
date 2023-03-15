# containerlambda

This project contains the files for creating a container lambda that runs a python script 

These are the commands for buiding the image and running it in local:

>docker build -t pythonlambdacontainer .

>docker run -p 9000:8080 pythonlambdacontainer

>curl --request POST   --url http://localhost:9000/2015-03-31/functions/function/invocations   --header 'Content-Type: application/json'   --data '{"Input": 4}'

The example was taken from : https://towardsdatascience.com/building-aws-lambda-container-images-5c4a9a15e8a2

For using the container in a Lambda, it has to be deployed to an ECR registry:

>aws ecr get-login-password --region eu-west-1

>aws ecr --region eu-west-1 | docker login -u AWS -p <token> 974396178048.dkr.ecr.eu-west-1.amazonaws.com/repo0
  
>docker images
  
>docker tag pythonlambdacontainer 974396178048.dkr.ecr.eu-west-1.amazonaws.com/repo0
  
>docker push 974396178048.dkr.ecr.eu-west-1.amazonaws.com/repo0

The example was taken from https://www.freecodecamp.org/news/build-and-push-docker-images-to-aws-ecr/
