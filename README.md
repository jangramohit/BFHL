# BFHL REST API – Chitkara University Qualifier

This repository contains the implementation of the required REST APIs for the Chitkara University Qualifier 2026.

---

## Tech Stack
- Python
- FastAPI
- OpenAI API
- Render (Hosting)

---

## Base URL
https://bfhl-gi4o.onrender.com

---

## API Endpoints

### GET /health
Health check endpoint.

URL:
https://bfhl-gi4o.onrender.com/health

Response:
{
  "is_success": true,
  "official_email": "mohit3878.beai23@chitkara.edu.in"
}

---

### POST /bfhl
Processes a single input key per request.

URL:
https://bfhl-gi4o.onrender.com/bfhl

Supported keys:
- fibonacci (integer)
- prime (integer array)
- lcm (integer array)
- hcf (integer array)
- AI (string question, single-word response)

Example:
{
  "fibonacci": 7
}

Response:
{
  "is_success": true,
  "official_email": "mohit3878.beai23@chitkara.edu.in",
  "data": [0,1,1,2,3,5,8]
}

---

## Testing
POST endpoint tested using Swagger UI, Postman, and curl.

Swagger URL:
https://bfhl-gi4o.onrender.com/docs

---

## GitHub Repository
https://github.com/jangramohit/BFHL

---

## Hosting Platform
Render

---

## Author
Mohit  
Chitkara University  
Email: mohit3878.beai23@chitkara.edu.in
