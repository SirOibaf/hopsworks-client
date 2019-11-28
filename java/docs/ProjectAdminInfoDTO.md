# ProjectAdminInfoDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projectName** | **String** |  |  [optional]
**projectOwner** | **String** |  |  [optional]
**archived** | **Boolean** |  |  [optional]
**paymentType** | [**PaymentTypeEnum**](#PaymentTypeEnum) |  |  [optional]
**lastQuotaUpdate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional]
**projectQuotas** | [**QuotasDTO**](QuotasDTO.md) |  |  [optional]

<a name="PaymentTypeEnum"></a>
## Enum: PaymentTypeEnum
Name | Value
---- | -----
PREPAID | &quot;PREPAID&quot;
NOLIMIT | &quot;NOLIMIT&quot;
