from inspec.munge.dictToDefinition import convertDictToDef


dict1 = [{'property': 'bucket_name', 'description': 'The name of the bucket.'},
  {'property': 'key', 'description': 'The key within the bucket.'},
  {'property': 'content_length', 'description': 'Size of the body in bytes.'},
  ]

def1 = '''
`bucket_name`
: The name of the bucket.

`key`
: The key within the bucket.

`content_length`
: Size of the body in bytes.

'''

def testConvertDictToDef1():
  assert convertDictToDef(dict1) == def1

dict2 = [{'property': 'route_table_ids', 'description': 'The route table IDs', 'field': '`route_table_id`'},
  {'property': 'vpc_ids', 'description': 'The VPC IDs', 'field': '`vpc_id`'},
  {'property': 'entries', 'description': 'Provides access to the raw results of the query, which can be treated as an array of hashes.', 'field': 'Not Applicable'}
  ]

def2 ='''
`route_table_ids`
: The route table IDs.

: **Field**: `route_table_id`

`vpc_ids`
: The VPC IDs.

: **Field**: `vpc_id`

`entries`
: Provides access to the raw results of the query, which can be treated as an array of hashes.

: **Field**: Not Applicable

'''

def testConvertDictToDef2():
  assert convertDictToDef(dict2) == def2