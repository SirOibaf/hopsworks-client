/**
 * Hopsworks api
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.1.0-SNAPSHOT
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

export interface QuotasDTO { 
    hdfsUsageInBytes?: number;
    hdfsQuotaInBytes?: number;
    hdfsNsCount?: number;
    hdfsNsQuota?: number;
    hiveHdfsUsageInBytes?: number;
    hiveHdfsQuotaInBytes?: number;
    hiveHdfsNsCount?: number;
    hiveHdfsNsQuota?: number;
    featurestoreHdfsUsageInBytes?: number;
    featurestoreHdfsQuotaInBytes?: number;
    featurestoreHdfsNsCount?: number;
    featurestoreHdfsNsQuota?: number;
    yarnQuotaInSecs?: number;
    yarnUsedQuotaInSecs?: number;
    kafkaMaxNumTopics?: number;
}