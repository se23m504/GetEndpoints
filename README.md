# GetEndpoints

GetEndpoints is a REST API and responsive web application that makes managing WebRTC endpoint streams easier. It is designed for Unity applications running on the HoloLens, where typing long URLs (endpoints) and changing settings can be slow and frustrating.

Instead of hardcoding endpoints and needing to redeploy the app every time you want to make a change, GetEndpoints acts as your single source of truth (SSOT). This allows you to update and manage your endpoints in real-time, keeping your application up to date.

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
- `GET /api/endpoints/{id}`: Get a specific endpoint by ID.
- `PUT /api/endpoints/{id}`: Update an existing endpoint.

### cURL examples

```
curl http://windows.local:5000/api/endpoints
curl http://windows.local:5000/api/endpoints/1
curl -X PUT http://windows.local:5000/api/endpoints/1 -H "Content-Type: application/json" -d '{"url": "http://windows.local:8500/mystream/"}'
```

### Invoke-WebRequest examples

```
Invoke-WebRequest -Uri http://windows.local:5000/api/endpoints
Invoke-WebRequest -Uri http://windows.local:5000/api/endpoints/1
Invoke-WebRequest -Uri http://windows.local:5000/api/endpoints/1 -Method PUT -Headers @{"Content-Type"="application/json"} -Body '{"url": "http://windows.local:8500/mystream/"}'
```

## API host

By default, this API expects `windows.local` to be an existing DNS record on your DNS server (which could also be defined in your hosts file). If you don't want to use `windows.local`, update the `API_HOST` in your `.env` file.
