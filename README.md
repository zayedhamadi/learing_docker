# learing_docker
 # 🚀 Project Setup and Execution

 ## <h3 align="left"> 🌐 Clone the repository:</h3>
git clone git@github.com:zayedhamadi/learing_docker.git
cd learing_docker
 ## <h3 align="left"> 🌐 Build the Docker image:
</h3>
docker build -t my_simple_app .

 ## <h3 align="left"> 🌐 Run the container:

docker run -d --name my_simple_app -p 8080:8080 my_simple_app
📌 The application is now accessible at: http://localhost:8080 🎉
