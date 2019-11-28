# Users

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **Integer** |  |  [optional]
**username** | **String** |  | 
**password** | **String** |  | 
**email** | **String** |  |  [optional]
**fname** | **String** |  |  [optional]
**lname** | **String** |  |  [optional]
**activated** | [**OffsetDateTime**](OffsetDateTime.md) |  | 
**title** | **String** |  |  [optional]
**orcid** | **String** |  |  [optional]
**falseLogin** | **Integer** |  | 
**status** | [**StatusEnum**](#StatusEnum) |  | 
**isonline** | **Integer** |  | 
**secret** | **String** |  |  [optional]
**validationKey** | **String** |  |  [optional]
**validationKeyUpdated** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional]
**validationKeyType** | [**ValidationKeyTypeEnum**](#ValidationKeyTypeEnum) |  |  [optional]
**securityQuestion** | [**SecurityQuestionEnum**](#SecurityQuestionEnum) |  |  [optional]
**securityAnswer** | **String** |  |  [optional]
**mode** | [**ModeEnum**](#ModeEnum) |  | 
**passwordChanged** | [**OffsetDateTime**](OffsetDateTime.md) |  | 
**notes** | **String** |  |  [optional]
**mobile** | **String** |  |  [optional]
**maxNumProjects** | **Integer** |  |  [optional]
**numCreatedProjects** | **Integer** |  | 
**numActiveProjects** | **Integer** |  | 
**twoFactor** | **Boolean** |  | 
**salt** | **String** |  | 
**toursState** | **Integer** |  | 
**bbcGroupCollection** | [**List&lt;BbcGroup&gt;**](BbcGroup.md) |  |  [optional]
**address** | [**Address**](Address.md) |  |  [optional]
**organization** | [**Organization**](Organization.md) |  |  [optional]
**jupyterSettingsCollection** | [**List&lt;JupyterSettings&gt;**](JupyterSettings.md) |  |  [optional]
**tensorBoardCollection** | [**List&lt;TensorBoard&gt;**](TensorBoard.md) |  |  [optional]
**groupName** | **String** |  |  [optional]
**groupNames** | [**List&lt;BbcGroup&gt;**](BbcGroup.md) |  |  [optional]
**statusName** | **String** |  |  [optional]

<a name="StatusEnum"></a>
## Enum: StatusEnum
Name | Value
---- | -----
NEW_MOBILE_ACCOUNT | &quot;NEW_MOBILE_ACCOUNT&quot;
VERIFIED_ACCOUNT | &quot;VERIFIED_ACCOUNT&quot;
ACTIVATED_ACCOUNT | &quot;ACTIVATED_ACCOUNT&quot;
DEACTIVATED_ACCOUNT | &quot;DEACTIVATED_ACCOUNT&quot;
BLOCKED_ACCOUNT | &quot;BLOCKED_ACCOUNT&quot;
LOST_MOBILE | &quot;LOST_MOBILE&quot;
SPAM_ACCOUNT | &quot;SPAM_ACCOUNT&quot;
TEMP_PASSWORD | &quot;TEMP_PASSWORD&quot;

<a name="ValidationKeyTypeEnum"></a>
## Enum: ValidationKeyTypeEnum
Name | Value
---- | -----
EMAIL | &quot;EMAIL&quot;
PASSWORD | &quot;PASSWORD&quot;
PASSWORD_RESET | &quot;PASSWORD_RESET&quot;
QR_RESET | &quot;QR_RESET&quot;

<a name="SecurityQuestionEnum"></a>
## Enum: SecurityQuestionEnum
Name | Value
---- | -----
MAIDEN_NAME | &quot;MAIDEN_NAME&quot;
PET | &quot;PET&quot;
LOVE | &quot;LOVE&quot;
NICK_NAME | &quot;NICK_NAME&quot;
CHILDHOOD_FRIEND | &quot;CHILDHOOD_FRIEND&quot;
STREET | &quot;STREET&quot;
SIBLING_MAIDEN_NAME | &quot;SIBLING_MAIDEN_NAME&quot;
SCHOOL | &quot;SCHOOL&quot;
COUSIN_MAIDEN_NAME | &quot;COUSIN_MAIDEN_NAME&quot;
STUFFED_ANIMAL | &quot;STUFFED_ANIMAL&quot;
SIBLING_LIVE | &quot;SIBLING_LIVE&quot;
FIRST_JOB_TOWN | &quot;FIRST_JOB_TOWN&quot;

<a name="ModeEnum"></a>
## Enum: ModeEnum
Name | Value
---- | -----
M_ACCOUNT_TYPE | &quot;M_ACCOUNT_TYPE&quot;
REMOTE_ACCOUNT_TYPE | &quot;REMOTE_ACCOUNT_TYPE&quot;
