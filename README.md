# Shop Registration System

## Project Overview
The Shop Registration System is a Django web application that allows users to register shops with details such as name, latitude, and longitude. It provides an API for users to register and search for shops based on their geographical location.

## Technologies Used
- **Django**: Backend framework
- **Django Rest Framework**: API framework
- **SQLite**: Default database
- **HTML/CSS/JavaScript**: Frontend technologies
- **Git**: Version control

## Installation Guide
1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/myshop_project.git
   cd myshop_project
   
2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

6. **Migrate the Database**
   ```bash
   python manage.py migrate

8. **Run the Development Server**
   ```bash
   python manage.py runserver

## API Endpoints
**Register Shop:** 
```bash
POST /api/shops/
 
Search Shops:
 GET /api/shops/?lat=LATITUDE&lng=LONGITUDE

     
## THANKS
   


