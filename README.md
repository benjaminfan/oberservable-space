# Observable Space

## Assumptions
1. All fields in the schema are required for both agents and customers
1. Creation and Updates to each collection can only be made one at a time
1. Data is served in memory
1. `_id` is always unique and immutable  

## Steps to Run
###### Windows users: recommended running with cygwin or MinGW for `make`.   Alternatively you can ship this on k8s with `minikube` 
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
You can also run the app locally but requires additional steps
1. (Optional) Create a `virtualenv` or `venv` 
   ```bash
    py -3 -m venv venv
    ```
1. Install required modules with `pip install requirements.txt`
2. Run the app with ngnix and gunicorn `gunicorn --chdir service app:app -w 2 --threads 2 -b 0.0.0.0:8003`

## Endpoints
- `/api/agents`
    - GET - Return List of all Agents
    - POST - Add New Agent
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
    - GET - Retrieve all Agent Details by agent’s INT ID
    - PUT - Update Any/All Fields by Agent’s INT ID
      - Example Body 
      ```json
      {
        "_id": 989,
        "address": "Updated Address",
      }
- `/api/agent/{id}/customers`
  - GET - List all customers associated with a given Agent's INT ID
- `/api/customers`
  - GET - Return all customer data from our system.
  - POST - Add New Customer
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
    - GET- Retrieve all Customer Details by customer's INT ID
    - PUT - Provide ability to Update Customer Information
       - Example Body 
      ```json
      {
        "_id": 8463,
        "isActive": false,
      }
    - DELETE - Delete Existing Customer

   
## Future Improvements
1. Finish mongoDB middleware
1. Tests with schema
1. Pipeline