# Homework 2 -- CS-4300
## How to Run HW2 Movie Theater Project
### Step 1: Clone the repository
```bash
git clone https://github.com/Lumbag0/cs4300
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv .venv
```

### Step 3: Activate Virtual Environment
```bash
source .venv/bin/activate
```

### Step 4: Change into homework 2 directory
```bash
cd cs4300/homework2
```

### Step 5: Install Dependencies
```bash
pip3 install -r ../requirements.txt
```

### Step 6: Create a Super User
```bash
python3 movie_theater_booking/manage.py createsuperuser
```
- Follow the prompts to create your admin user

### Step 7: Start the server
```bash
python3 movie_theater_booking/manage.py runserver
```
- By default it will run on port 8000

### Step 8: Navigate to admin panel
- On the website, navigate to `http://localhost/admin` and enter your user credentials
- Within the admin panel you can create and manage users, seats, and movies which will dynamically appear on the application. 

## AI Usage Disclosure
- Per the course requirements, the following is times I used AI during this project

| Platform | Reason                                 |
| -------- | -------------------------------------- |
| Claude   | Format for test cases                  |
| Claude   | Help fixing a bug regarding seats      |
| Claude   | How to make rows based on lettering    |
| Claude   | Misc. HTML + CSS formatting questions  |
| Claude   | How to create a navbar using CSS + HTML|
