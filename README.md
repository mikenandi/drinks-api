# Drinks API

The Drinks API is a RESTful API project that allows you to perform CRUD (Create, Read, Update, Delete) operations on
drinks. It serves as a learning resource for building APIs using Django Rest Framework, specifically focusing on
managing a collection of drinks.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your/repository.git
   ```

2. Navigate to the project directory:
   ```
   cd drinks-api
   ```

3. Create a virtual environment:
   ```
   python -m venv env
   ```

4. Activate the virtual environment:
    - On macOS and Linux:
      ```
      source env/bin/activate
      ```
    - On Windows:
      ```
      .\env\Scripts\activate
      ```

5. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Run database migrations:
   ```
   python manage.py migrate
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

The Drinks API project provides the following endpoints:

- `/drinks/`: Endpoint for retrieving a list of drinks or creating a new drink.
- `/drinks/<int:pk>/`: Endpoint for retrieving, updating, or deleting a specific drink by its ID.

You can use tools like cURL, Postman, or web browsers to interact with these endpoints. Ensure that the development
server is running (`python manage.py runserver`) before making API requests.

## API Documentation

For detailed documentation on the API endpoints and their usage, please refer to the [API Documentation](docs/api.md)
file. The documentation provides information about the request/response format, available endpoints, and examples of API
usage specifically related to managing drinks.

## Contributing

Contributions to the Drinks API project are highly appreciated. If you have any suggestions, improvements, or bug fixes,
please submit a pull request. Follow the project's coding conventions and include appropriate tests.

## License

The Drinks API project is licensed under the [MIT License](LICENSE). Feel free to modify and use it as a learning
resource or as a starting point for your own projects.

## Acknowledgements

This project was created based on the learnings and examples from the Django Rest Framework documentation and various
online tutorials. Special thanks to the Django and Django Rest Framework communities for their valuable contributions to
the open-source community.

If you have any questions or need further assistance, please don't hesitate to contact me. Enjoy working with the Drinks
API and happy coding!