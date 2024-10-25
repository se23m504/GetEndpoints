# GetEndpoints

This REST API and responsive web application manage WebRTC endpoint streams. It is designed for a Unity app running on the HoloLens, where typing and changing settings can be slow and frustrating. Instead of hardcoding endpoints and having to redeploy the app whenever changes are needed, this setup provides a single source of truth (SSOT). You can easily update the endpoints whenever you want, making it simple to manage without hassle.

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
