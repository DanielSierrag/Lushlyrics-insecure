## Lushlyrics-insecure

This project is a fork of [https://github.com/mohammedwed/Lushlyrics-insecure](https://github.com/mohammedwed/Lushlyrics-insecure).

## Explanation

This fork extends the original project by adding authentication features, including:

- **User login:** Secure authentication for users.
- **Email verification:** Users must verify their email address before accessing certain features.
- **Two-factor authentication (2FA):** An additional layer of security requiring a second verification step during login.

## Setup

To run this project, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/Lushlyrics-insecure.git
    cd Lushlyrics-insecure
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv env
    # On Windows
    env\Scripts\activate
    # On macOS/Linux
    source env/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

6. **Access the app:**

    Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---
