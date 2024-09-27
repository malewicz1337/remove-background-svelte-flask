# Remove Background Svetle + Flask App

## Overview

This project provides a web application for removing backgrounds from images using RemBG. The application is structured into two main components: a Flask-based backend and a Svelte + TypeScript frontend.

## Features

- Background removal using the RemBG tool.
- User-friendly web interface for uploading and processing images.

## Installation and Setup

### Backend

1. Clone the repository.
2. Navigate to the `backend` directory.
3. Install required dependencies: `pip install -r requirements.txt`.
4. Start the Flask app: `python app.py`.
5. The backend service will be available at `http://localhost:5100`.

### Frontend

1. Navigate to the `frontend` directory.
2. Install dependencies using `npm install`.
3. Start the frontend application with `npm run dev`.
4. Access the web interface at the provided local URL.

## Docker Compose Installation and Setup

Using Docker Compose, you can easily set up and run the entire application in Docker containers. This ensures a consistent and isolated environment regardless of the host system.

### Steps to Run

1. **Clone the Repository**:

```bash
git clone https://github.com/malewicz1337/remove-background-svelte-flask.git
```

2. Navigate to the Project Directory:

```bash
cd remove-background-svelte-flask

```

3. Build and Run with Docker Compose:

```bash
docker-compose up --build
```

## License

This project is open source and available under the [MIT License](LICENSE).
