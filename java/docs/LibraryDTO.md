# LibraryDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **String** |  |  [optional]
**items** | [**List&lt;LibraryDTO&gt;**](LibraryDTO.md) |  |  [optional]
**count** | **Long** |  |  [optional]
**channel** | **String** |  |  [optional]
**packageManager** | [**PackageManagerEnum**](#PackageManagerEnum) |  |  [optional]
**machine** | [**MachineEnum**](#MachineEnum) |  |  [optional]
**library** | **String** |  |  [optional]
**version** | **String** |  |  [optional]
**status** | [**StatusEnum**](#StatusEnum) |  |  [optional]
**preinstalled** | **String** |  |  [optional]
**commands** | [**CommandDTO**](CommandDTO.md) |  |  [optional]

<a name="PackageManagerEnum"></a>
## Enum: PackageManagerEnum
Name | Value
---- | -----
CONDA | &quot;CONDA&quot;
PIP | &quot;PIP&quot;

<a name="MachineEnum"></a>
## Enum: MachineEnum
Name | Value
---- | -----
ALL | &quot;ALL&quot;
CPU | &quot;CPU&quot;
GPU | &quot;GPU&quot;

<a name="StatusEnum"></a>
## Enum: StatusEnum
Name | Value
---- | -----
NEW | &quot;NEW&quot;
SUCCESS | &quot;SUCCESS&quot;
ONGOING | &quot;ONGOING&quot;
FAILED | &quot;FAILED&quot;
