# Observable Space

## Assumptions
1. All fields in the schema are required for both agents and customers
1. Creation and Updates to each collection can only be made one at a time
1. Data is served in memory
1. `_id` is always unique and immutable  

## Steps to Run

1. Install Docker
1. ```bash
   make build
   ```
1. ```bash
   make run
   ```
1. Service should be running on `http://localhost:8003`
1. Use your favorite api tool (`postman`, `curl`, `wget`)
    ```bash
    curl http://localhost:8003/api/agent/101/
    ```

## Endpoints
- `/api/agents`
    - GET
    - POST
      - Example Body 
      ```json
      {
        "_id": 989,
        "address": "Fake Address",
        "city": "Denver",
        "name": "John Doe",
        "phone": {
            "mobile": "206-555-3211",
            "primary": "206-221-2345"
        },
        "state": "CO",
        "tier": 2,
        "zipCode": "12938"
      }
- `/api/agent/{id}`
    - GET
    - PUT
      - Example Body 
      ```json
      {
        "_id": 989,
        "address": "Updated Address",
      }
- `/api/agent/{id}/customers`
  - GET - a list of customers that the agent is responsible for
- `/api/customers`
  - GET - All the customers information
  - POST 
        - Example Body 
      ```json
      {
        "_id": 84613,
        "agent_id": 321,
        "guid": "1ef5fafc-4499-41fd-be0b-48d289052e43",
        "isActive": true,
        "balance": "$2,280.48",
        "age": 45,
        "eyeColor": "blue",
        "name": {
            "first": "Dina",
            "last": "Moreno"
        },
        "company": "QUONK",
        "email": "dina.moreno@quonk.biz",
        "phone": "+1 (828) 478-3414",
        "address": "378 Pershing Loop, Yardville, Virgin Islands, 6929",
        "registered": "Friday, August 5, 2016 10:58 AM",
        "latitude": "57.893847",
        "longitude": "33.137927",
        "tags": [
            "ut",
            "aliqua",
            "excepteur",
            "occaecat",
            "irure"
        ]
      }
- `/api/customer/{id}`
    - GET
    - PUT
       - Example Body 
      ```json
      {
        "_id": 8463,
        "isActive": true,
      }
    - DELETE

   
## Future Improvements
1. Finish mongoDB middleware