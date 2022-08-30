# django-graphql
GraphQL training project based on the Python Django framework for backend and Vue 2 for frontend

### Prerequirements
Installed and running **Docker** desktop application or devtool

### Setup
1. Create a new file with the name of ".env" in the project's main folder.
2. Copy-paste the following content into the file, each key-value pair should be in a new line:  
   ENVIRONMENT=dev  
   DBNAME=postgres  
   DBUSER=postgres  
   DBPASSWORD=postgres  
   DBHOST=db  
   DBPORT=5432  
   BACKEND_HOST=http://localhost  
   BACKEND_PORT=8000  
   FRONTEND_HOST=http://localhost  
   FRONTEND_PORT=8080  
   ACCESS_TOKEN=testtoken  
   DJANGO_SECRET=secretkey  
3. Run the following command in the project's main folder: **docker compose up**

After the steps above, the next time you only need to run the **docker compose up** command to start the project.

### Project setup:
- The **database** server is running on the default **http://localhost:5432** port, so please don't run any other PostgreSQL database simultaneously with this one.  
- The **backend** server is running on the **http://localhost:8000/** port. The backend does not have any html pointed on this url, so you'll see only an error page if you open it. However the **GraphiQL Playground** is accessible on the **http://localhost:8000/graphql** url, you can use it to test your requests.
- The **frontend** server is running on the **http://localhost:8080/** port. If you open it in your browser you should see the project's frontend, a simple SPA.

### Development process
You are free to modify anything and everything on the project, but first please create a branch for yourself based on the project's **main** branch.

In the project's **frontend** folder resides the SPA source code. You can work on the code like in any regular Vue 2 project, and the changes should be automatically reflected on the development server running on **http://localhost:8080/**.

Please be aware that currently the backend server only allows incoming requests from the **http://localhost:8080/** port.

To access the backend admin site you will need to create a superuser. To create one, please do the following:
1. Open a bash inside the running backend container with the following command: **docker exec -it django-graphql-backend-1 bash**
2. In the container bash run the following command: **python manage.py createsuperuser**
3. Create the superuser by givin the requested data for it.
4. You can now login with the new user on **http://localhost:8000/admin/**.