import pytest
from inspec.munge.tableToDict import convertTableToDict
from inspec.munge.tableToDict import findTableInText

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
  assert convertTableToDict(inputTable2) == ('', 'Error. Incorrectly formatted table: ' + inputTable2)


inputTable3='''|Property       | Description|
| ---           | --- |
|bucket_name   | The name of the bucket. |
|key            | The key within the bucket. | Word | 
|content_length | Size of the body in bytes. |
|content_type   | A standard MIME type describing the format of the object data. |
|object_acl    | An array of AWS Grants detailing permission grants on the bucket object.  |
'''

def test_convertTableToDict3():
  assert convertTableToDict(inputTable3) == ('', 'Error. Incorrectly formatted table: ' + inputTable3)

inputTable4='''|Property       | Description | Field |
| ---           | --- | --- |
|bucket_name   | The name of the bucket. |
|key            | The key within the bucket. |
|content_length | Size of the body in bytes. |
|content_type   | A standard MIME type describing the format of the object data. |
|object_acl    | An array of AWS Grants detailing permission grants on the bucket object.  |
'''


def test_convertTableToDict4():
  assert convertTableToDict(inputTable4) == ('', 'Error. Incorrectly formatted table: ' + inputTable4)






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

outputDict6 = ('', 'Error. Incorrectly formatted table: |Property                                    | Description                                       |   Field           |\n| ----------------------------               | ---------------------------------                 |   ---             |\n| route_table_ids                          | The route table IDs                               |\n| vpc_ids                                   | The VPC IDs                                       | `vpc_id`          |\n| entries                                    | Provides access to the raw results of the query, which can be treated as an array of hashes. | Not Applicable | ')

def test_convertTableToDict6():
  assert convertTableToDict(inputTable6) == ('', 'Error. Incorrectly formatted table: ' + inputTable6)

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