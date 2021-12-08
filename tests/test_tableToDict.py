import pytest
from migrate.munge.tableToDict import convertTableToDict
from migrate.munge.tableToDict import findTableInText

inputTable1='''|Property       | Description|
| ---           | --- |
|bucket_name   | The name of the bucket. |
|key            | The key within the bucket. |
|content_length | Size of the body in bytes. | 
|content_type   | A standard MIME type describing the format of the object data. |
|object_acl    | An array of AWS Grants detailing permission grants on the bucket object.  |
'''

# outputDict1 = [{'property': 'bucket_name', 'description': 'The name of the bucket.'},{'property': 'key', 'description': 'The key within the bucket.'},
# {'property': 'content_length', 'description': 'The key within the bucket.'},
# {'property': 'content_type', 'description': 'Size of the body in bytes.'},
# {'property': 'object_acl', 'description': 'A standard MIME type describing the format of the object data.'}
# ]
outputDict1 = ([{'property': 'bucket_name', 'description': 'The name of the bucket.'}, {'property': 'key', 'description': 'The key within the bucket.'}, {'property': 'content_length', 'description': 'Size of the body in bytes.'}, {'property': 'content_type', 'description': 'A standard MIME type describing the format of the object data.'}, {'property': 'object_acl', 'description': 'An array of AWS Grants detailing permission grants on the bucket object.'}], '')

def test_convertTableToDict1():
  assert convertTableToDict(inputTable1) == outputDict1, ''

inputTable2='''|Property       | Description|
| ---           | --- |
|bucket_name   | The name of the bucket. |
|key            | The key within the bucket. 
|content_length | Size of the body in bytes. |
|content_type   | A standard MIME type describing the format of the object data. |
|object_acl    | An array of AWS Grants detailing permission grants on the bucket object.  |
'''

def test_convertTableToDict2():
  assert convertTableToDict(inputTable2) == ('', 'Bad table: ' + inputTable2)


inputTable3='''|Property       | Description|
| ---           | --- |
|bucket_name   | The name of the bucket. |
|key            | The key within the bucket. | Word | 
|content_length | Size of the body in bytes. |
|content_type   | A standard MIME type describing the format of the object data. |
|object_acl    | An array of AWS Grants detailing permission grants on the bucket object.  |
'''

def test_convertTableToDict3():
  assert convertTableToDict(inputTable3) == ('', 'Bad table: ' + inputTable3)

inputTable4='''|Property       | Description | Field |
| ---           | --- | --- |
|bucket_name   | The name of the bucket. |
|key            | The key within the bucket. |
|content_length | Size of the body in bytes. |
|content_type   | A standard MIME type describing the format of the object data. |
|object_acl    | An array of AWS Grants detailing permission grants on the bucket object.  |
'''


def test_convertTableToDict4():
  assert convertTableToDict(inputTable4) == ('', 'Bad table: ' + inputTable4)






inputTable5 = '''|Property                                    | Description                                       |   Field           |
| ----------------------------               | ---------------------------------                 |   ---             |
| route_table_ids                          | The route table IDs                               | `route_table_id`  |
| vpc_ids                                   | The VPC IDs                                       | `vpc_id`          |
| entries                                    | Provides access to the raw results of the query, which can be treated as an array of hashes. | Not Applicable | '''

outputDict5 =([{'property': 'route_table_ids', 'description': 'The route table IDs', 'field': '`route_table_id`'}, {'property': 'vpc_ids', 'description': 'The VPC IDs', 'field': '`vpc_id`'}, {'property': 'entries', 'description': 'Provides access to the raw results of the query, which can be treated as an array of hashes.', 'field': 'Not Applicable'}], '')

def test_convertTableToDict5():
  assert convertTableToDict(inputTable5) == outputDict5

inputTable6 = '''|Property                                    | Description                                       |   Field           |
| ----------------------------               | ---------------------------------                 |   ---             |
| route_table_ids                          | The route table IDs                               |
| vpc_ids                                   | The VPC IDs                                       | `vpc_id`          |
| entries                                    | Provides access to the raw results of the query, which can be treated as an array of hashes. | Not Applicable | '''

outputDict6 = ('', 'Bad table: |Property                                    | Description                                       |   Field           |\n| ----------------------------               | ---------------------------------                 |   ---             |\n| route_table_ids                          | The route table IDs                               |\n| vpc_ids                                   | The VPC IDs                                       | `vpc_id`          |\n| entries                                    | Provides access to the raw results of the query, which can be treated as an array of hashes. | Not Applicable | ')

def test_convertTableToDict6():
  assert convertTableToDict(inputTable6) == ('', 'Bad table: ' + inputTable6)

inputTable7 = '''

|Property                                    | Description                                       |   Field           |
| ----------------------------               | ---------------------------------                 |   ---             |
| route_table_ids                          | The route table IDs                               | `vpc_id`          |

Some words here. Ignore this.

'''

def test_findTableInText1():
  assert findTableInText(inputTable7) == ({'end': 356, 'start': 2})

inputTable8 = '''

|Property                                    | Description                                       |   Field           |
| ----------------------------               | ---------------------------------                 |   ---             |
| route_table_ids                          | The route table IDs                               | `vpc_id`          |

Some words here. Ignore this. Let's add a pipe for fun. |

'''

def test_findTableInText12():
  assert findTableInText(inputTable8) == ({'end': 356, 'start': 2})

inputTable9='''| Property             | Description                                                                    | Field              |
| :------------------: | :----------------------------------------------------------------------------: | :----------------- |
| carrier_gateway_ids  | The ID of the carrier gateway.                                                 | carrier_gateway_id |
| vpc_ids              | The ID of the VPC (Virtual Private Cloud) associated with the carrier gateway. | vpc_id             |
| states               | The state of the carrier gateway.                                              | state              |
| owner_ids            | The Amazon Web Services account ID of the owner of the carrier gateway.        | owner_id           |
'''


outputDict9 =([
  {'property': 'carrier_gateway_ids', 'description': 'The ID of the carrier gateway.', 'field': '`carrier_gateway_id`'},
  {'property': 'vpc_ids', 'description': 'The ID of the VPC (Virtual Private Cloud) associated with the carrier gateway.', 'field': '`vpc_id`'},
  {'property': 'states', 'description': 'The state of the carrier gateway.', 'field': '`state`'},
  {'property': 'owner_ids', 'description': 'The Amazon Web Services account ID of the owner of the carrier gateway.', 'field': '`owner_id`'}
  ], '')

def test_convertTableToDict9():
  assert convertTableToDict(inputTable9) == outputDict9

inputTable10 = '''| Name              | Description                                                                                                                                                         | Example                                |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| resource          | Azure resource type that the targeted resource belongs to.                                                                                                          | `users`                                |
| id                | Globally unique ID of the targeted resource.                                                                                                                        | `jdoe@contoso.com`                     |
| select            | The list of query parameters defining which attributes that the resource will expose. If not provided then the predefined attributes will be returned from the API. | `['givenName', 'surname', 'department']` |
| api_version       | API version of the GRAPH API to use when interrogating the resource. If not set then the predefined stable version will be used.                                    | `v1.0`, `beta`                         |
'''

outputDict10 = ([
    {'property': 'resource', 'description': 'Azure resource type that the targeted resource belongs to.', 'example': '`users`'},
    {'property': 'id', 'description': 'Globally unique ID of the targeted resource.', 'example': '`jdoe@contoso.com`'},
    {'property': 'select', 'description': 'The list of query parameters defining which attributes that the resource will expose. If not provided then the predefined attributes will be returned from the API.', 'example': "`['givenName', 'surname', 'department']`"},
    {'property': 'api_version', 'description': 'API version of the GRAPH API to use when interrogating the resource. If not set then the predefined stable version will be used.', 'example': '`v1.0`, `beta`'}
], '')

def test_convertTableToDict10():
    outputDict = convertTableToDict(inputTable10)
    print(outputDict)
    assert outputDict == outputDict10
