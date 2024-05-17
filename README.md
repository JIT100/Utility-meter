# README 

## Django Meter Management Application 
This project is a Django-based web application designed to manage meters and their associated data. The application allows users to create meter instances and add data associated with each meter. The list view of meters displays all meters, and clicking on a single meter opens its detail view in JSON format, showing all associated meter data. 

This version uses the Generic Docker Platform 

#### Features

- Create and manage meter instances.
- Add and manage data for each meter instance.
- View a list of all meters.
- Retrieve detailed information about each meter, including its associated data.
- Timezone is set to UTC for ease of understanding.

#### Prerequisites

- Docker
- Docker compose

### Getting Started

These instructions will help you set up and run the application on your local machine for development and testing purposes.


### Clone the Repository

```bash
git clone https://github.com/JIT100/Utility-meter.git
```
### Running the Application

###### *Assuming you have installed docker-compose (https://docs.docker.com/compose/)*
* Take The Pull from the Github, Then create a file named ```.env``` in the project directory where ```manage.py``` file is located.

* Give **SECRET_KEY** ( You can generate one secret key & assign it to this variable ) in ```.env``` file & put ```.env``` in ```.gitignore``` file.

- ##### **Building the Docker Containers**
    To build the Docker containers for the application, run:
    * ``` docker-compose --build ```

- ##### **Run the Docker Container**
    After You have successfully build The docker image, start the server using:
    * ``` docker-compose up ```


This will start the application, and it will be accessible at http://localhost:8000.


### Usage
##### Accessing the Admin Interface
You can access the Django admin interface at http://localhost:8000/admin/ using the credentials ```admin (username) / 1234 (password)```.

##### Viewing Meters
Visit http://localhost:8000/meters/ to view a list of all meters. Clicking on a Meter item will display its details in JSON format ( Django Rest Browsable API view Json format).

##### API Endpoints

- **List of Meters**
    - URL: /meters/
    - Method: GET
    - Response: List of all meters in a HTML template

- **Meter Details**
    - URL: /meters/\<int:pk\>/
    - Method: GET
    - Response: Detailed information about a specific meter, including associated meter data sorted by time in Json format

- **Create Meter**
    - URL: /meters/create/
    - Method: POST
    - Request Body: JSON object with meter details
    - Response: Created meter instance

- **Create Meter Data**
    - URL: /meter-data/create/
    - Method: POST
    - Request Body: JSON object with meter data details
    - Response: Created meter data instance

#### Common Issues

- **Network Issues**: Ensure the correct ports are exposed and not blocked by firewalls
- **Database Errors**: Ensure the database is properly set up and migrations have been run.

#### Logs
To view the logs of the running containers, use: ```docker-compose logs```

### Project Components

##### Dockerfile
The ```Dockerfile``` is used to create a Docker image for the Django application. It includes steps to install dependencies, copy project files, and set up the entry point for the application.

##### docker-compose.yml
The ```docker-compose.yml``` file defines the services for the project. It includes the web service for the Django application and can be extended to include other services like a database if needed but for this project we chose to use Django's inbuilt Database which is SQLite .

##### entrypoint\.sh
The ```entrypoint.sh``` script initializes the application by running database migrations, collecting static files, running the Initial Seed Data script to predefined some data in the DB and starting the Django development server.

##### Seed Data
The ```seed_data.py``` script initializes the database with some predefined data for testing purposes. It sets up an admin user, meters, and meter data.

##### Views and URLs

The Django application includes various views for managing meters and their data. These views include:
- **MeterListView**: Displays a list of all meters in HTML format. We can click on each item in the list.
- **MeterCreateView**: Allows the creation of new meter instances using Django Rest Browsable API format.
- **MeterDataCreateView**: Allows the creation of new meter data instances associated with a Meter instance , using Django Rest Browsable API format. 
- **MeterDetailsView**: Displays detailed information about a specific meter Django Rest Browsable API Json format .





### Purpose

- The goal of this API is to manage meter instances and the associated meter data. It allows users to create, retrieve, and list meters and their respective data, providing a way to track various metrics such as temperature, size, radiation, and speed. The API is designed to be simple and easy to use, suitable for applications that need to monitor and display meter readings.
