import json
import os
from schema import SchemaError
from schemas import agent_schema, customer_schema


class MockCRUD:
    agents = {}
    customers = {}

    def __init__(self, agents_filepath='data/agents.json', customers_filepath='data/customers.json'):
        def load_from_file(rel_path: 'string'):
            script_dir = os.path.dirname(__file__)
            with open(os.path.join(script_dir, rel_path)) as f:
                data = json.load(f)
                return data

        self.agents = self.index_by_key(load_from_file(agents_filepath))
        self.customers = self.index_by_key(load_from_file(customers_filepath))

    def __repr__(self):
        return {'agents': self.agents, 'customers': self.customers}

    @staticmethod
    def index_by_key(collection, key='_id') -> dict:
        return {doc[key] : doc for doc in collection}

    @staticmethod
    def upsert(collection, data, schema, new_insert=True):
        try:
            schema.validate(data)
            if bool(data['_id'] in collection) is new_insert:
                raise AttributeError()
            collection[data['_id']] = data
        except SchemaError as e:
            raise AttributeError("{}".format(e))
        except AttributeError:
            if new_insert: raise AttributeError(f'Cannot create duplicate id {data.get("_id")}.')
            raise AttributeError(f'Id  {data.get("_id")} has not been created.')

    @staticmethod
    def update_user(_id, new_data, collection) -> dict:
        if _id not in collection:
            raise AttributeError(f'Id {_id} must be created first.')
        if new_data.pop('_id') != _id:
            raise AttributeError(f'Update id {_id} mismatch')
        return collection.get(_id) | new_data

    def add_agent(self, agent_data):
        self.upsert(self.agents, agent_data, agent_schema)

    def update_agent(self, _id, agent_data):
        updated_agent = self.update_user(_id, agent_data, self.agents)
        self.upsert(self.agents, updated_agent, agent_schema, new_insert=False)

    def update_customer(self, _id, customer_data):
        updated_customer = self.update_user(_id, customer_data, self.customers)
        self.upsert(self.customers, updated_customer, customer_schema, new_insert=False)

    def get_customers_per_agent(self, agent_id: int) -> list:
        customers_indexed_by_agent = {}
        # if this gets expensive, we can store in a cache and use compression/filter
        for cust in self.customers.values():
            customers_indexed_by_agent.setdefault(cust['agent_id'], []).append(cust)
        return customers_indexed_by_agent[agent_id]


