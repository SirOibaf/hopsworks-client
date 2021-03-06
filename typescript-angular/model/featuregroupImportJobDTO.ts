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

export interface FeaturegroupImportJobDTO { 
    type?: FeaturegroupImportJobDTO.TypeEnum;
    storageConnector?: string;
    path?: string;
    featuregroup?: string;
    primaryKey?: Array<string>;
    description?: string;
    featurestore?: string;
    featuregroupVersion?: number;
    jobs?: string;
    descriptiveStatistics?: boolean;
    featureCorrelation?: boolean;
    featureHistograms?: boolean;
    clusterAnalysis?: boolean;
    statsColumn?: Array<string>;
    numBins?: number;
    corrMethod?: string;
    numClusters?: number;
    partitionBy?: Array<string>;
    dataFormat?: string;
    online?: boolean;
    onlineTypes?: { [key: string]: string; };
    offline?: boolean;
    amCores?: number;
    amMemory?: number;
    executorCores?: number;
    executorMemory?: number;
    maxExecutors?: number;
}
export namespace FeaturegroupImportJobDTO {
    export type TypeEnum = 'S3' | 'REDSHIFT';
    export const TypeEnum = {
        S3: 'S3' as TypeEnum,
        REDSHIFT: 'REDSHIFT' as TypeEnum
    };
}