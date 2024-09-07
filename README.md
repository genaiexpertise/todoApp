ToDo App
***
This is a full-stack ToDo application with a FastAPI backend and a Next.js frontend. The application allows users to create, update, delete, and filter their to-do tasks.


### Table of Contents
- Project Structure
- Features
- Prerequisites
- Installation
- Running the Application
- API Endpoints
- Frontend Usage
- Technologies Used

### Project Structure

```
root/
│
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI application entry point
│   │   ├── models.py          # Database models
│   │   ├── routes.py          # API routes
│   │   └── ...
│   ├── Dockerfile             # Dockerfile for backend
│   ├── requirements.txt       # Python dependencies
│   └── ...
│
├── frontend/
│   ├── components/
│   │   ├── todo-list.js       # ToDoList component
│   │   ├── todo.js            # ToDo component
│   │   └── ...
│   ├── pages/
│   │   ├── index.js           # Main page
│   │   └── ...
│   ├── styles/
│   ├── next.config.js         # Next.js configuration
│   ├── package.json           # npm dependencies
│   └── ...
│
└── README.md                  # Project documentation
```


### Features
- FastAPI Backend: A RESTful API that handles CRUD operations for to-do items.
- Next.js Frontend: A responsive and dynamic user interface for interacting with the to-do list.
- Debounced Input: Reduces the number of API calls while editing tasks.
- Filtering: View all, active, or completed tasks.
- Persistent Storage: Store tasks in a backend database.

### Prerequisites
Before you begin, ensure you have the following installed on your system:

- Python 3.8+ (for the backend)
- Node.js 14+ (for the frontend)
- Docker (optional, for containerization)

### Installation

#### Backend (FastAPI)
- Navigate to the backend directory:
```
cd backend

```

- Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

```

- Install the required Python packages:

```
pip install -r requirements.txt

```

#### Frontend (Next.js)
- Navigate to the frontend directory:
```
cd frontend

```

- Install the required npm packages:
```
npm install

```

### Running the Application

#### Backend
To start the FastAPI server, run the following command in the backend directory:
```
uvicorn app.main:app --reload

```
he backend API will be available at http://localhost:8000.

#### Frontend
To start the Next.js development server, run the following command in the frontend directory:

```
npm run dev

```

The frontend will be available at http://localhost:3000.


### API Endpoints
- GET /todos: Retrieve all todos.
- POST /todos/: Create a new todo.
- PUT /todos/{id}: Update an existing todo by id.
- DELETE /todos/{id}: Delete a todo by id.

### Example Request:
```
curl -X POST "http://localhost:8000/todos/" -H "Content-Type: application/json" -d '{"name": "Sample Task", "completed": false}'


```


### Frontend Usage

- Create a Task: Type your task in the input field and press Enter.

- Update a Task: Edit the task name directly in the list; changes are debounced to reduce API calls.

- Complete a Task: Check the box next to a task to mark it as completed.

- Delete a Task: Click the delete button to remove a task from the list.

- Filter Tasks: Use the filter buttons to view all, active, or completed tasks.

### Technologies Used
- Backend: FastAPI, Python, Uvicorn
- Frontend: Next.js, React, CSS Modules
- Database: Postgres 
- Deployment: Docker (optional)