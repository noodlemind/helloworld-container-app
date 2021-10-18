#Hello World App
A Simple HelloWorld Application using Python that is containerized for sample/learning purposes of Docker, Kubernetes

## Steps to Use the Project for Learning Docker / Containerization
1. Download / Clone the Code into your Machine using the following command.
   
    ``` git clone https://github.com/noodlemind/helloworld-container-app.git```

2. Execute the Docker Build Command to Build and Tag the Image
    
    ```docker build -t my-registry/hello-world-app:1.0 . ```
   > Please note you are executing the command in the root folder of the project. If you are not inside the project,
   > use the ```cd helloworld-container-app``` command to navigate into the project.
   
3. *(Optional)* If you want to rename the Image, please use the following Syntax to rename the tag.

    ```docker tag my-registry/hello-world-app:1.0 new-registry/new-repository-image-name:version ```

4. Once the Image has been built, please push it to the desired registry.

    ```docker push my-registry/hello-world-app:1.0```
    > Please make sure you are logged in to docker using the command ```docker login``` before trying the push.