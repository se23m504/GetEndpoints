# GetEndpoints

GetEndpoints is a REST API and responsive web application that makes managing WebRTC endpoint streams easier. It is designed for Unity applications running on the HoloLens, where typing long URLs (endpoints) and changing settings can be slow and frustrating.

Instead of hardcoding endpoints and needing to redeploy the app every time you want to make a change, GetEndpoints acts as your single source of truth (SSOT). This allows you to update and manage your endpoints in real-time, keeping your application up to date.

## Features

- **Automatic service discovery**: Registers as an `_http._tcp.` service using Zeroconf, making it easily discoverable on the network.
- **Lightweight REST API**: Minimal yet robust API for managing WebRTC endpoints.
- **Responsive and bloat-free**: Built with vanilla JS and HTML for fast, adaptable performance on any device.
- **SQLite database**: Uses SQLite by default, easily extendable to other databases by adjusting the endpoint. 

## Prerequisites

- `python >= 3.11`
- `python-venv`

## Usage

1. Create your `src/.env` file according to your requirements. You can copy `src/.env.dev` as a reference.

2. Run the application:

   ```bash
   bash run.sh
   ```

   or, if you are on Windows

   ```ps
   .\start.bat
   ```

### Endpoints

- `GET /api/endpoints`: Get the list of all WebRTC endpoints.
- `POST /api/endpoints`: Add a new endpoint.
- `GET /api/endpoints/{id}`: Get a specific endpoint by ID.
- `PUT /api/endpoints/{id}`: Update an existing endpoint.
- `DELETE /api/endpoints/{id}`: Delete an endpoint.

Note that by default, the API initializes with predefined endpoints unless `DEFAULT_ENDPOINTS=false` is set in the `.env` file. The default endpoints are:

- `/api/endpoints/1: {"url": "http://$API_HOST:8100/mystream/"}`
- `/api/endpoints/2: {"url": "http://$API_HOST:8200/mystream/"}`

### cURL examples

```
curl http://$API_HOST:5000/api/endpoints
curl http://$API_HOST:5000/api/endpoints/1
curl -X PUT http://$API_HOST:5000/api/endpoints/1 -H "Content-Type: application/json" -d '{"url": "http://$API_HOST:8500/mystream/"}'
```

### Invoke-WebRequest examples

```
Invoke-WebRequest -Uri http://$API_HOST:5000/api/endpoints
Invoke-WebRequest -Uri http://$API_HOST:5000/api/endpoints/1
Invoke-WebRequest -Uri http://$API_HOST:5000/api/endpoints/1 -Method PUT -Headers @{"Content-Type"="application/json"} -Body '{"url": "http://$API_HOST:8500/mystream/"}'
```
