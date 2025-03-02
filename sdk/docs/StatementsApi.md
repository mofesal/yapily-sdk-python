# yapily.StatementsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statement_file_using_get**](StatementsApi.md#get_statement_file_using_get) | **GET** /accounts/{accountId}/statements/{statementId}/file | Get account statement file
[**get_statement_using_get**](StatementsApi.md#get_statement_using_get) | **GET** /accounts/{accountId}/statements/{statementId} | Get account statement
[**get_statements_using_get**](StatementsApi.md#get_statements_using_get) | **GET** /accounts/{accountId}/statements | Get account statements


# **get_statement_file_using_get**
> str get_statement_file_using_get(consent, account_id, statement_id)

Get account statement file

### Example
```python
from __future__ import print_function
import time
import yapily
from yapily.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: tokenAuth
configuration = yapily.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = yapily.StatementsApi(yapily.ApiClient(configuration))
consent = 'consent_example' # str | Consent Token
account_id = 'account_id_example' # str | accountId
statement_id = 'statement_id_example' # str | statementId

try:
    # Get account statement file
    api_response = api_instance.get_statement_file_using_get(consent, account_id, statement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->get_statement_file_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **account_id** | **str**| accountId | 
 **statement_id** | **str**| statementId | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement_using_get**
> ApiResponseOfAccountStatement get_statement_using_get(consent, account_id, statement_id)

Get account statement

### Example
```python
from __future__ import print_function
import time
import yapily
from yapily.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: tokenAuth
configuration = yapily.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = yapily.StatementsApi(yapily.ApiClient(configuration))
consent = 'consent_example' # str | Consent Token
account_id = 'account_id_example' # str | accountId
statement_id = 'statement_id_example' # str | statementId

try:
    # Get account statement
    api_response = api_instance.get_statement_using_get(consent, account_id, statement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->get_statement_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **account_id** | **str**| accountId | 
 **statement_id** | **str**| statementId | 

### Return type

[**ApiResponseOfAccountStatement**](ApiResponseOfAccountStatement.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statements_using_get**
> ApiListResponseOfAccountStatement get_statements_using_get(consent, account_id, _from=_from, before=before, limit=limit, sort=sort, offset=offset)

Get account statements

### Example
```python
from __future__ import print_function
import time
import yapily
from yapily.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: tokenAuth
configuration = yapily.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = yapily.StatementsApi(yapily.ApiClient(configuration))
consent = 'consent_example' # str | Consent Token
account_id = 'account_id_example' # str | accountId
_from = '_from_example' # str | from (optional)
before = 'before_example' # str | before (optional)
limit = 56 # int | limit (optional)
sort = 'sort_example' # str | sort (optional)
offset = 56 # int | offset (optional)

try:
    # Get account statements
    api_response = api_instance.get_statements_using_get(consent, account_id, _from=_from, before=before, limit=limit, sort=sort, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->get_statements_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | 
 **account_id** | **str**| accountId | 
 **_from** | **str**| from | [optional] 
 **before** | **str**| before | [optional] 
 **limit** | **int**| limit | [optional] 
 **sort** | **str**| sort | [optional] 
 **offset** | **int**| offset | [optional] 

### Return type

[**ApiListResponseOfAccountStatement**](ApiListResponseOfAccountStatement.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

