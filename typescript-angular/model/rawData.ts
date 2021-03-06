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
 */import { Field } from './field';
import { Metadata } from './metadata';
import { RawDataPK } from './rawDataPK';
import { TupleToFile } from './tupleToFile';


export interface RawData { 
    rawdataPK?: RawDataPK;
    tupleToFile?: TupleToFile;
    metadata?: Array<Metadata>;
    field?: Field;
    id?: number;
}