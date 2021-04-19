# Observable Space

## Assumptions
1. All fields in the schema are required for both agents and customers
1. Creation and Updates to each collection can only be made one at a time
1. Data is served in memory

## Steps to Run

1. Install Dockear
1. ```bash
   make build
   ```
1. ```bash
   make run
   ```
1. Service should be running on `http://localhost:8003`
1. Use your desired api tool (`postman`, `curl`, `wget`)
    ```bash
    curl http://localhost:8003/api/agent/101/
    ```

## Endpoints
- `/api/agents`
    - GET
    - POST 
- `/api/agent/{id}`
    - GET
    - PUT
- `/api/agent/{id}/customers`
  - GET
- `/api/customers`
  - GET
  - POST 
- `/api/customer/{id}`
    - GET
    - PUT
    - DELETE

   
## Future Improvements
1. Finish mongoDB middleware