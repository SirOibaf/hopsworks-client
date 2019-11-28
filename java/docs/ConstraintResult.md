# ConstraintResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check** | **String** |  |  [optional]
**checkLevel** | [**CheckLevelEnum**](#CheckLevelEnum) |  |  [optional]
**checkStatus** | [**CheckStatusEnum**](#CheckStatusEnum) |  |  [optional]
**constraint** | **String** |  |  [optional]
**constraintStatus** | [**ConstraintStatusEnum**](#ConstraintStatusEnum) |  |  [optional]
**constraintMessage** | **String** |  |  [optional]

<a name="CheckLevelEnum"></a>
## Enum: CheckLevelEnum
Name | Value
---- | -----
WARNING | &quot;Warning&quot;
ERROR | &quot;Error&quot;

<a name="CheckStatusEnum"></a>
## Enum: CheckStatusEnum
Name | Value
---- | -----
WARNING | &quot;Warning&quot;
ERROR | &quot;Error&quot;

<a name="ConstraintStatusEnum"></a>
## Enum: ConstraintStatusEnum
Name | Value
---- | -----
SUCCESS | &quot;Success&quot;
WARNING | &quot;Warning&quot;
FAILURE | &quot;Failure&quot;
EMPTY | &quot;Empty&quot;
