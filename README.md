# Decodelabs_internship_repo
# DecodeLabs Backend: REST API Fundamentals

## Overview
This project is a high-performance, stateless web server built with **Python** and **FastAPI**. It serves as a foundational backend communication layer designed to handle REST API requests and serve structured JSON data to frontend client applications. 

## Key Features
* **Stateless Architecture:** Adheres to REST principles by treating every HTTP request as fully self-contained with no server-side session memory.
* **Core Routing:** Implements standard HTTP verbs (`GET` for safe data retrieval and `POST` for state-changing resource creation) on the `/users` endpoint.
* **Automatic Data Validation:** Utilizes Pydantic models to ensure strict contract enforcement on incoming JSON payloads.
* **Interactive Documentation:** Features out-of-the-box Swagger UI (`/docs`) for visual endpoint testing and API exploration.

*Built as part of the DecodeLabs Industrial Training.
