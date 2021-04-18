import json
import pandas as pd


class Agents:
    REQUIRED_FIELDS = ('_id')
    OPTIONAL_FIELDS = ('name', 'address', 'state', 'zipcode', 'tier', 'phone')

    def __init__(self, filepath='./data/agents.json'):
        reset_list(filepath)

    def load_data(self, string: filepath) -> pd.DataFrame:
        with open(filepath) as f:
            data = json.load(f)
            df = pd.DataFrame([agents], index=['_id'])

    def __repr__(self):
        return "{} {} {} {} {}".format(self.first_name, self.last_name, self.birth_date, self.sex, self.address)

    def create_(self, agent):
