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
 */import { QuotasDTO } from './quotasDTO';


export interface ProjectAdminInfoDTO { 
    projectName?: string;
    projectOwner?: string;
    archived?: boolean;
    paymentType?: ProjectAdminInfoDTO.PaymentTypeEnum;
    lastQuotaUpdate?: Date;
    projectQuotas?: QuotasDTO;
}
export namespace ProjectAdminInfoDTO {
    export type PaymentTypeEnum = 'PREPAID' | 'NOLIMIT';
    export const PaymentTypeEnum = {
        PREPAID: 'PREPAID' as PaymentTypeEnum,
        NOLIMIT: 'NOLIMIT' as PaymentTypeEnum
    };
}