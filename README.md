# Building Full CRUD RESTful APIs with Flask - Lab
**Completed Sept 15, 2026**

## Overview

This project is a **Full CRUD API** built with Flask that manages a list of events. The API allows users to:

- Create new events using `POST`
- Update existing events using `PATCH`
- Delete events using `DELETE`

It simulates database-like behavior with in-memory Python class objects and responds to all client requests with properly formatted JSON and appropriate status codes.

## Setup Instructions

```bash
git clone <repo-url>
cd course-8-module-5-flask-full-crud-api-lab
pipenv install
pipenv shell
```

Or with pip:

```bash
pip install flask
```

Start the server:

```bash
python app.py
```

Run the automated tests:

```bash
pytest
```

---

## API Documentation

### `POST /events`
Creates a new event.

**Request body:**
```json
{ "title": "Hackathon" }
```

**Response** — `201 Created`
```json
{ "id": 3, "title": "Hackathon" }
```

**Response** — `400 Bad Request` (missing title)
```json
{ "error": "Title is required" }
```

---

### `PATCH /events/<id>`
Updates the title of an existing event.

**Request body:**
```json
{ "title": "Hackathon 2025" }
```

**Response** — `200 OK`
```json
{ "id": 1, "title": "Hackathon 2025" }
```

**Response** — `404 Not Found` (event doesn't exist)
```json
{ "error": "Event not found" }
```

---

### `DELETE /events/<id>`
Deletes an existing event.

**Response** — `204 No Content` (empty body)

**Response** — `404 Not Found` (event doesn't exist)
```json
{ "error": "Event not found" }
```

---

## Best Practices Followed

- Uses RESTful nouns in routes (e.g., `/events`)
- Validates incoming JSON and handles missing keys gracefully
- Uses a shared `find_event()` helper to avoid repeated lookup logic
- Returns correct status codes: `201`, `200`, `204`, `400`, `404`
- Includes inline comments explaining logic

---

## Summary

This project handles incoming JSON with Flask, implements full CRUD behavior across three routes, simulates persistent resource changes in memory, and passes all automated tests and manual verification. The natural next step is swapping the in-memory list for a persistent database.