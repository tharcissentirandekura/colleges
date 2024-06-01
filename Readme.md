# College Scholarships API

The College Scholarships API is a Django-based RESTful API that provides endpoints for managing college scholarships on a website.

- For students, search schools based on your preferences: majors, name of collage, location

## Installation

1. Clone the repository:

    ```bash
    gh repo clone tharcissentirandekura/colleges
    ```

2. Change into the project directory:

    ```bash
    cd colleges
    ```

3. Create a virtual environment and activate it:

    ```bash
    python3 -m venv env
    source /bin/activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up the database:
    ```bash
    python manage.py makemigrations
    ```

    ```bash
    python manage.py migrate
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

The following endpoints are available in the College Scholarships API:

### Scholarships

- `GET /colleges/`: Retrieve a list of all scholarships.
- `POST /colleges/`: Create a new scholarship.
- `GET /colleges/{id}/`: Retrieve details of a specific scholarship.
- `PUT /colleges/{id}/`: Update details of a specific scholarship.
- `DELETE /colleges/{id}/`: Delete a specific scholarship.

### Users

- `POST /api/users/`: Create a new user.
- `GET /api/users/{id}/`: Retrieve details of a specific user.
- `PUT /api/users/{id}/`: Update details of a specific user.
- `DELETE /api/users/{id}/`: Delete a specific user.

### Authentication

- `POST /api/token/`: Obtain an access token by providing valid credentials.
- `POST /api/token/refresh/`: Refresh an access token.

## Authentication and Permissions

The College Scholarships API uses token-based authentication. To access protected endpoints, clients must include an `Authorization` header with a valid token.

Certain endpoints may have additional permissions requirements, such as requiring the user to be an admin or the owner of the resource.

## Error Handling

The API follows standard HTTP status codes for indicating success or failure. In case of an error, additional information may be provided in the response body.

## Examples

### Create a Scholarship

Request:

