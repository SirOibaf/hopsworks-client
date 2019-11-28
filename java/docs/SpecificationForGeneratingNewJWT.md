# SpecificationForGeneratingNewJWT

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **String** | Subject to be encoded in JWT | 
**audiences** | **List&lt;String&gt;** | Appropriate audience for the JWT | 
**keyName** | **String** | Name of the signing key | 
**expiresAt** | [**OffsetDateTime**](OffsetDateTime.md) | Expiration date of the token |  [optional]
**nbf** | [**OffsetDateTime**](OffsetDateTime.md) | Not-valid-before date |  [optional]
**renewable** | **Boolean** | Flag to indicate if the token is auto-renewable | 
**expLeeway** | **Integer** | Number of seconds after the expiration the token is still valid | 
