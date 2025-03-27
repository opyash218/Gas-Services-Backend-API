## 🚀 Features
- **User Management**: Users can register and submit requests using their customer ID.
- **Request Tracking**: Users can track their submitted requests.
- **Admin Panel**: Admins can view all users, update request statuses, and add new entries.
- **Django REST Framework (DRF)**: APIs for interacting with the backend.

---

## 📌 Installation

### Prerequisites
Ensure you have Python installed (preferably 3.8+).

### Steps

1️⃣ Clone the repository:
   ```sh
   git clone https://github.com/opyash218/Gas-Services-Backend-API.git
   cd your-repo
2️⃣ Create and activate a virtual environment:

sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3️⃣ Install dependencies:

sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Run migrations:

sh
Copy
Edit
python manage.py migrate
5️⃣ Create a superuser for the admin panel:

sh
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set up the superuser credentials.

6️⃣ Start the server:

sh
Copy
Edit
python manage.py runserver
7️⃣ Access the Admin Panel: Open http://127.0.0.1:8000/admin/ in your browser and log in using the superuser credentials.

📡 API Endpoints
🔹 User Endpoints
Register User → POST /register/

Get User Info → GET /user-info/<customer_id>/

Submit Request → POST /submit/

Track Request → GET /track/<request_id>/

List All Requests → GET /list/

🔐 Admin Panel Features
View all users: Admins can see a list of all registered users.

Update request status: Admins can update the status of user requests.

Add new users and requests: Admins can manually add new users and their requests.

Full user and request management: Create, update, and delete entries directly through the panel.

🛠️ Usage
Use Postman or any API testing tool to interact with the endpoints.

Log in to the Django Admin panel at http://127.0.0.1:8000/admin/ to manage users and requests.
