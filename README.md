# containerlambda

This project contains the files for creating a container lambda that runs a python script 

These are the commands for buiding the image and running it in local:

`docker build -t pythonlambdacontainer .
`docker run -p 9000:8080 pythonlambdacontainer
`curl --request POST   --url http://localhost:9000/2015-03-31/functions/function/invocations   --header 'Content-Type: application/json'   --data '{"Input": 4}'

The example was taken from : https://towardsdatascience.com/building-aws-lambda-container-images-5c4a9a15e8a2
