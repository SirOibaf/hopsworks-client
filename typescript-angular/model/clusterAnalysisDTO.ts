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
 */import { ClusterDTO } from './clusterDTO';
import { DatapointDTO } from './datapointDTO';


export interface ClusterAnalysisDTO { 
    dataPoints?: Array<DatapointDTO>;
    clusters?: Array<ClusterDTO>;
    statisticType?: ClusterAnalysisDTO.StatisticTypeEnum;
}
export namespace ClusterAnalysisDTO {
    export type StatisticTypeEnum = 'DESCRIPTIVESTATISTICS' | 'CLUSTERANALYSIS' | 'FEATUREDISTRIBUTIONS' | 'FEATURECORRELATIONS';
    export const StatisticTypeEnum = {
        DESCRIPTIVESTATISTICS: 'DESCRIPTIVESTATISTICS' as StatisticTypeEnum,
        CLUSTERANALYSIS: 'CLUSTERANALYSIS' as StatisticTypeEnum,
        FEATUREDISTRIBUTIONS: 'FEATUREDISTRIBUTIONS' as StatisticTypeEnum,
        FEATURECORRELATIONS: 'FEATURECORRELATIONS' as StatisticTypeEnum
    };
}