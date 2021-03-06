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

export interface FeaturestoreDTO { 
    featurestoreId?: number;
    featurestoreName?: string;
    created?: Date;
    hdfsStorePath?: string;
    projectName?: string;
    projectId?: number;
    featurestoreDescription?: string;
    inodeId?: number;
    onlineFeaturestoreType?: string;
    onlineFeaturestoreName?: string;
    onlineFeaturestoreSize?: number;
    offlineFeaturestoreType?: string;
    offlineFeaturestoreName?: string;
    hiveEndpoint?: string;
    mysqlServerEndpoint?: string;
    onlineEnabled?: boolean;
}