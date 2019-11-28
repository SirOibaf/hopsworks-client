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

export interface ProjectServicePK { 
    projectId: number;
    service: ProjectServicePK.ServiceEnum;
}
export namespace ProjectServicePK {
    export type ServiceEnum = 'KAFKA' | 'HISTORY' | 'DELA' | 'JUPYTER' | 'JOBS' | 'HIVE' | 'SERVING' | 'RSTUDIO' | 'AIRFLOW' | 'PYTHON' | 'FEATURESTORE';
    export const ServiceEnum = {
        KAFKA: 'KAFKA' as ServiceEnum,
        HISTORY: 'HISTORY' as ServiceEnum,
        DELA: 'DELA' as ServiceEnum,
        JUPYTER: 'JUPYTER' as ServiceEnum,
        JOBS: 'JOBS' as ServiceEnum,
        HIVE: 'HIVE' as ServiceEnum,
        SERVING: 'SERVING' as ServiceEnum,
        RSTUDIO: 'RSTUDIO' as ServiceEnum,
        AIRFLOW: 'AIRFLOW' as ServiceEnum,
        PYTHON: 'PYTHON' as ServiceEnum,
        FEATURESTORE: 'FEATURESTORE' as ServiceEnum
    };
}