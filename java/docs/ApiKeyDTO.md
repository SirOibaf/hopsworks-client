# ApiKeyDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **String** |  |  [optional]
**items** | [**List&lt;ApiKeyDTO&gt;**](ApiKeyDTO.md) |  |  [optional]
**count** | **Long** |  |  [optional]
**key** | **String** |  |  [optional]
**name** | **String** |  |  [optional]
**prefix** | **String** |  |  [optional]
**created** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional]
**modified** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional]
**scope** | [**List&lt;ScopeEnum&gt;**](#List&lt;ScopeEnum&gt;) |  |  [optional]

<a name="List<ScopeEnum>"></a>
## Enum: List&lt;ScopeEnum&gt;
Name | Value
---- | -----
JOB | &quot;JOB&quot;
DATASET_VIEW | &quot;DATASET_VIEW&quot;
DATASET_CREATE | &quot;DATASET_CREATE&quot;
DATASET_DELETE | &quot;DATASET_DELETE&quot;
INFERENCE | &quot;INFERENCE&quot;
FEATURESTORE | &quot;FEATURESTORE&quot;
PROJECT | &quot;PROJECT&quot;
