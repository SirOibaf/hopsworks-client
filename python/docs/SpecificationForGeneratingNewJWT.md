# SpecificationForGeneratingNewJWT

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Subject to be encoded in JWT | 
**audiences** | **list[str]** | Appropriate audience for the JWT | 
**key_name** | **str** | Name of the signing key | 
**expires_at** | **datetime** | Expiration date of the token | [optional] 
**nbf** | **datetime** | Not-valid-before date | [optional] 
**renewable** | **bool** | Flag to indicate if the token is auto-renewable | 
**exp_leeway** | **int** | Number of seconds after the expiration the token is still valid | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

