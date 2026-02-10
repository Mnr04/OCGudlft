# Güdlft - Competition Booking System (POC)

This project is developed in Python using the Flask framework. It is a platform allowing club secretaries to register their athletes for regional competitions.

The project focuses on code quality, testing coverage, and performance, in accordance with the specifications.

## Prerequisites

Before you begin, ensure you have installed:
* **Python 3.x**
* **pip**
* **virtualenv**

## Installation

Follow the steps below to set up the development environment locally.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Mnr04/OCGudlft.git
    cd OCGudlft
    ```

2.  **Create and activate the virtual environment:**
    * *On macOS/Linux:*
        ```bash
        python3 -m venv env
        source env/bin/activate
        ```
    * *On Windows:*
        ```bash
        python -m venv env
        env\Scripts\activate
        ```

3.  **Install dependencies:**
    Install the required libraries (Flask, Pytest, Locust, Coverage, etc.):
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

The project uses JSON files (`clubs.json` and `competitions.json`) as a temporary database.

1.  **Set the Flask environment variable:**
    * *Mac/Linux:* `export FLASK_APP=server.py`
    * *Windows:* `set FLASK_APP=server.py`

2.  **Start the server:**
    ```bash
    flask run
    ```
    Or alternatively:
    ```bash
    python -m flask run
    ```

3.  **Access the application:**
    Open your browser at the following address: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Main Features:
* **Login:** Use a club email found in `clubs.json` (ex : `john@simplylift.co`).
* **Dashboard:** Accessible via `/dashboard` to view club rankings (public access).
* **Booking:** Allows booking places (max 12 per competition).

---

## 🧪 Testing and Code Quality

The project follows a strict testing architecture to ensure stability and performance.

### 1. Running Unit and Integration Tests
We use **Pytest** to run all tests (unit and integration).

```bash
python -m pytest
```

### 2. Coverage
Checking Code Coverage, the goal is to maintain code coverage above 60%.
```bash
coverage run -m pytest
coverage report
```

### 3. Performance Tests (Locust)
Performance is tested with Locust to simulate user load (response time < 5s and updates < 2s)

1. Start Locust
```bash
locust -f tests/performance_tests/locustfile.py
```

2. Open the Locust interface in your browser: http://localhost:8089.

3. Start the test with the desired parameters.
