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
 */import { LocalResourceDTO } from './localResourceDTO';
import { YarnJobConfiguration } from './yarnJobConfiguration';


export interface SparkJobConfiguration extends YarnJobConfiguration { 
    appPath?: string;
    mainClass?: string;
    args?: string;
    properties?: string;
    experimentType?: SparkJobConfiguration.ExperimentTypeEnum;
    distributionStrategy?: SparkJobConfiguration.DistributionStrategyEnum;
    executorInstances?: number;
    executorCores?: number;
    executorMemory?: number;
    executorGpus?: number;
    numPs?: number;
    dynamicAllocationEnabled?: boolean;
    dynamicAllocationMinExecutors?: number;
    dynamicAllocationMaxExecutors?: number;
    dynamicAllocationInitialExecutors?: number;
    blacklistingEnabled?: boolean;
    pyFiles?: string;
    files?: string;
    jars?: string;
    archives?: string;
}
export namespace SparkJobConfiguration {
    export type ExperimentTypeEnum = 'EXPERIMENT' | 'PARALLEL_EXPERIMENTS' | 'DISTRIBUTED_TRAINING';
    export const ExperimentTypeEnum = {
        EXPERIMENT: 'EXPERIMENT' as ExperimentTypeEnum,
        PARALLELEXPERIMENTS: 'PARALLEL_EXPERIMENTS' as ExperimentTypeEnum,
        DISTRIBUTEDTRAINING: 'DISTRIBUTED_TRAINING' as ExperimentTypeEnum
    };
    export type DistributionStrategyEnum = 'MIRRORED' | 'PARAMETER_SERVER' | 'COLLECTIVE_ALL_REDUCE';
    export const DistributionStrategyEnum = {
        MIRRORED: 'MIRRORED' as DistributionStrategyEnum,
        PARAMETERSERVER: 'PARAMETER_SERVER' as DistributionStrategyEnum,
        COLLECTIVEALLREDUCE: 'COLLECTIVE_ALL_REDUCE' as DistributionStrategyEnum
    };
}