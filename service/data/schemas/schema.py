import pandas as pd
from io import StringIO
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, CanConvertValidation, MatchesPatternValidation, InRangeValidation, InListValidation

agentSchema = Schema([
    Column('_id', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('address', [InRangeValidation(0, 120)]),
    Column('state', [InListValidation(['Male', 'Female', 'Other'])]),
    Column('zipCode', [MatchesPatternValidation(r'\d{4}[A-Z]{4}')]),
    Column('tier', [InRangeValidation(0, 5)]),
    Column('phone', [MatchesPatternValidation(r'\d{4}[A-Z]{4}')]),
])

agentSchema = Schema([
    Column('_id', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('agent_id', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('guid', [InRangeValidation(0, 120)]),
    Column('isActive', [InListValidation(['Male', 'Female', 'Other'])]),
    Column('zipCode', [MatchesPatternValidation(r'\d{4}[A-Z]{4}')]),
    Column('tier', [MatchesPatternValidation(r'\d{4}[A-Z]{4}')]),
    Column('phone', [MatchesPatternValidation(r'\d{4}[A-Z]{4}')]),
])

test_data = pd.read_csv(StringIO('''Given Name,Family Name,Age,Sex,Customer ID
Gerald ,Hampton,82,Male,2582GABK
Yuuwa,Miyake,270,male,7951WVLW
Edyta,Majewska ,50,Female,775ANSID
'''))

errors = agentSchema.validate(test_data)

for error in errors:
    print(error)