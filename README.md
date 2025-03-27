# Gas Services Backend API

This is the backend API for the Gas Services project, built using **Django** and **Django REST Framework**. It provides endpoints for user registration, request submission, tracking, and retrieving user information.

## 🚀 Features

- **User Management**: Users can register and submit requests using their customer ID.
- **Request Tracking**: Users can track their submitted requests.
- **Admin Panel**: Admins can view all users, update request statuses, and add new entries.
- **Django REST Framework (DRF)**: APIs for interacting with the backend.


---

## 📌 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/opyash218/Gas-Services-Backend-API.git
cd gas-services-backend
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```

Now, the backend is running at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** 🎉

###6️⃣  set up the superuser credentials.

sh
Copy
Edit
python manage.py createsuperuser

###7️⃣ Access the Admin Panel: Open http://127.0.0.1:8000/admin/ in your browser and log in using the superuser credentials.

Already user or privious user Details otherwise use above cmt to create new Superuser that also fine.
username:-yash
pass:Rane12yash 


---

## 📡 API Endpoints

### 🔹 User Registration

**POST** `/gas_services/register/`

```json
{
   "username": "prathik",
    "password": "securepassword123",
    "email": "p@gmail.com",
    "first_name": "prathik",
    "last_name": "bhosale"
}
```
Response:

``` json

{
    "message": "User registered successfully",
    "user_id": 11
}

```

### 🔹 Retrieve User Information (No Login Required)

**GET** `/gas_services/user-info/{customer_id}/`

```json
Response:

{
  "id": 11,
    "first_name": "prathik",
    "last_name": "bhosale",
    "email": "p@gmail.com"
}
```


### 🔹 Submit a Service Request

**POST**  /`gas_services/submit/`

```json
{
    "customer_id": 11,
    "service_type": "installation ",
    "description": "Need a new gas connection to pratik"
     "attachment": null       #png and jpg
}
```

Response

```json

{
    "message": "Service request submitted successfully",
    "request_id": 9
}

```

### 🔹 Track a Service Request

**GET** /gas_services/track/{request_id}/`

```env
{
"customer": "prathik",
    "service_type": "installation ",
    "description": "Need a new gas connection tp pratik",
    "status": "resolved",
    "submitted_at": "2025-03-27 07:35:20",
    "resolved_at": "2025-03-27 07:35:53",
    "attachment": null
}

```

### 🔹 List All Requests

**GET** `gas_services/list/`

```env
{
    "requests": [
        {
            "id": 1,
            "customer": "testuser",
            "status": "pending"
        },
        {
            "id": 2,
            "customer": "admin",
            "status": "resolved"
        },
        {
            "id": 3,
            "customer": "yash",
            "status": "pending"
        }
        }
```

---

## 🛠️ Tech Stack

- **Python** (Django, Django REST Framework)
- **SQLite / PostgreSQL** (Database)
- **Postman** (For API Testing)

---



##🔐 Admin Panel Features
View all users: Admins can see a list of all registered users.

Update request status: Admins can update the status of user requests.

Add new users and requests: Admins can manually add new users and their requests.

Full user and request management: Create, update, and delete entries directly through the panel.

##🛠️ Usage
Use Postman or any API testing tool to interact with the endpoints.

Log in to the Django Admin panel at http://127.0.0.1:8000/admin/ to manage users and requests.




## 📞 Contact

For questions, contact: **yashsatyajit38@gmail.com**

