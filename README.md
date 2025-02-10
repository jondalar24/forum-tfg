#  Forum-TFG: AI-Enhanced Academic Forum







## 📌 About the Project

Forum-TFG is an AI-enhanced academic discussion forum designed for students and teachers. This project started as a fork of fenya123/forum123, but has been significantly modified to integrate AI capabilities, enhance user interaction, and improve system architecture.

The forum allows:

* Students to post questions and discuss topics.

* Teachers to answer and validate responses.

* AI assistance to guide students using Hugging Face Transformers and IBM Watsonx.

* Role-based access control (students & teachers).

### 🚀 Features

* ✅ Flask-based Web Application for handling user authentication, topics, and posts.
* ✅ PostgreSQL Database for efficient storage and management of discussions.
* ✅ AI Integration using Hugging Face Sentence Transformers & IBM WatsonxLLM.
* ✅ RESTful API for managing users, topics, and AI-assisted queries.
* ✅ Dockerized Environment for easy deployment and development.
* ✅ Tailwind CSS for a modern and responsive UI.
* ✅ User roles (Student & Teacher) with role-based access.

### 🛠️ System Requirements

* Python 3.10
* PostgreSQL (Dockerized instance recommended)
* Docker & Docker Compose
* Node.js & npm (for Tailwind CSS)
* Flask, SQLAlchemy, Alembic (for backend management)

### ⚙️ Installation & Setup

- 1️⃣ Clone the Repository

$ git clone https://github.com/jondalar24/forum-tfg.git
$ cd forum-tfg

- 2️⃣ Set Up a Virtual Environment

$ python3.10 -m venv .venv/forum-tfg
$ source .venv/forum-tfg/bin/activate

- 3️⃣ Install Dependencies

$ pip install -r requirements.txt -r requirements-dev.txt
$ npm install

- 4️⃣ Database Setup

$ docker-compose -f envs/dev/docker-compose.yml up --detach
$ alembic upgrade head  # Apply latest migrations

- 5️⃣ Run the Application

$ flask run

The server will be available at http://127.0.0.1:5000

### 🧑‍💻 API Endpoints

| Método  | Endpoint            | Descripción                           |
|---------|---------------------|---------------------------------------|
| `GET`   | `/api/topics`       | Obtiene todos los temas del foro.    |
| `POST`  | `/api/topics`       | Crea un nuevo tema.                  |
| `GET`   | `/api/topics/{id}`  | Obtiene un tema por su ID.           |
| `PUT`   | `/api/topics/{id}`  | Actualiza un tema existente.         |
| `DELETE`| `/api/topics/{id}`  | Elimina un tema.                     |
| `GET`   | `/api/posts`        | Obtiene todas las publicaciones.     |
| `POST`  | `/api/posts`        | Crea una nueva publicación.          |
| `GET`   | `/api/posts/{id}`   | Obtiene una publicación por ID.      |
| `DELETE`| `/api/posts/{id}`   | Elimina una publicación.             |
| `POST`  | `/api/ia/ask`       | Envia una pregunta a la IA y obtiene respuesta. |


### 🛠 Running Tests

To run unit tests:
```bash
$ pytest --cov=src
```
To check code quality:
```bash
$ flake8
$ pylint src
$ mypy src
```

### 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

### 🙌 Credits & Acknowledgements

Based on the original forum123 by fenya123

AI functionality integrated using Hugging Face and IBM Watsonx

UI enhancements using Tailwind CSS

### 🏗️ How to Contribute

Feel free to fork the repository and submit pull requests! If you find any issues, please open an issue.


