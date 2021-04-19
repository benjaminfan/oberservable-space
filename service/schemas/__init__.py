from schema import Schema, And, Use, Optional

conf_schema = Schema({
    'version': And(Use(int)),
    'info': {
        'conf_one': And(Use(float)),
        'conf_two': And(Use(str)),
        'conf_three': And(Use(bool)),
        Optional('optional_conf'): And(Use(str))
    }
})
agent_schema = Schema({
        "_id": And(Use(int), lambda n: 0 <= n),
        "name": And(str, len),
        "address": And(str, len),
        "city": And(str, len),
        "state": And(str, len),
        "zipCode": And(Use(int)),
        "tier": And(Use(int), lambda n: 1 <= n <= 10),
        "phone": {
            "primary": And(str, len),
            "mobile": And(str, len),
        }
    })

customer_schema = Schema({
        "_id": And(Use(int), lambda n: 0 <= n),
        "agent_id": And(Use(int), lambda n: 0 <= n),
        "guid": And(str, len),
        "isActive": And(Use(bool)),
        "balance": And(str, len),
        "age": And(Use(int), lambda n: 0 <= n <= 120),
        "eyeColor": And(str, len),
        "name": {
            "first": And(str, len),
            "last": And(str, len),
        },
        "company": And(str, len),
        "email": And(str, len),
        "phone": And(str, len),
        "address": And(str, len),
        "registered": And(str, len),
        "latitude": And(Use(float)),
        "longitude": And(Use(float)),
        Optional("tags"): And(Use(list)),
    })




