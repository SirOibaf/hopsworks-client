# JobLogDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | **String** |  |  [optional]
**path** | **String** |  |  [optional]
**type** | [**TypeEnum**](#TypeEnum) |  |  [optional]
**retriable** | [**RetriableEnum**](#RetriableEnum) |  |  [optional]

<a name="TypeEnum"></a>
## Enum: TypeEnum
Name | Value
---- | -----
OUT | &quot;OUT&quot;
ERR | &quot;ERR&quot;

<a name="RetriableEnum"></a>
## Enum: RetriableEnum
Name | Value
---- | -----
RETRIEABLE_OUT | &quot;RETRIEABLE_OUT&quot;
RETRIABLE_ERR | &quot;RETRIABLE_ERR&quot;
