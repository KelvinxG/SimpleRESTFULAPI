##Overview
This project is a demonstration of a RESTful API built using Django and Restframework. The API provides functionalities for performing CRUD operations and includes additional features related to Email management. The project showcases the usage of multiple databases and incorporates user authentication for enhanced security.

##Features
* RESTful API: The project implements a RESTful API design to ensure a standardized and intuitive way of interacting with the application.
* CRUD Operations: Users can perform Create, Read, Update, and Delete operations on various resources through the API endpoints.
* Email Management: The API includes additional functionalities related to Email handling, such as sending emails, retrieving email data, and managing email settings.
* Multiple Databases: The project utilizes multiple databases to efficiently manage and store different types of data.
* User Authentication: To enhance security and restrict access to certain features, the API incorporates user authentication, ensuring that only authorized users can perform certain actions.

# Project Documentation

## Setup and Installation

### 1. Clone the Repository

To get started, first, you need to clone the project repository to your local machine. Open a terminal or command prompt and execute the following command:

```bash
git clone <repository_url>
```

Replace `<repository_url>` with the URL of the project repository.

### 2. Set up a Virtual Python Environment

Setting up a virtual environment is a recommended practice to isolate the project's dependencies from your system-wide Python installation. Navigate to the project directory and create a virtual environment by running the following commands:

```bash
cd <project_directory>
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

On macOS and Linux:

```bash
source venv/bin/activate
```

### 4. Install Project Requirements

Now that the virtual environment is activated, you can install the project's required dependencies. In the root of the project directory, run the following command:

```bash
pip install -r requirements.txt
```

### 5. Navigate to the Project Directory

Change the current working directory to the `myapp` folder:

```bash
cd myapp
```

## Running the Project

### 1. Migrate the Database

Before running the project, you need to apply the database migrations to set up the initial database schema. Run the following command:

```bash
python manage.py migrate
```

### 2. Start the Development Server

Now you're all set to start the Django development server and run the project locally. Use the following command:

```bash
python manage.py runserver
```

The development server will start, and you should see an output similar to:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### 3. Access the Application

Open your web browser and navigate to `http://127.0.0.1:8000/` to access the project. If everything is set up correctly, you should see your Django application running.

## Additional Notes

- If you want to work on the project in the future, make sure to activate the virtual environment again before running the development server. You can do this using the activation command mentioned in Step 3 of the Setup and Installation section.
- For security purposes, avoid committing your virtual environment (`venv`) and `__pycache__` folders to version control. Add them to your `.gitignore` file.
- If you encounter any issues or have any questions, feel free to refer to the project documentation or reach out to the project maintainers for support.

That's it! You now have the project set up, the virtual environment running, and the Django development server up and running. Happy coding!