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
 *//* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent }                           from '@angular/common/http';
import { CustomHttpUrlEncodingCodec }                        from '../encoder';

import { Observable }                                        from 'rxjs/Observable';

import { ActivitiesDTO } from '../model/activitiesDTO';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class UserActivitiesResourceService {

    protected basePath = '///hopsworks-api/api';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {
        if (basePath) {
            this.basePath = basePath;
        }
        if (configuration) {
            this.configuration = configuration;
            this.basePath = basePath || configuration.basePath || this.basePath;
        }
    }

    /**
     * @param consumes string[] mime-types
     * @return true: consumes contains 'multipart/form-data', false: otherwise
     */
    private canConsumeForm(consumes: string[]): boolean {
        const form = 'multipart/form-data';
        for (const consume of consumes) {
            if (form === consume) {
                return true;
            }
        }
        return false;
    }


    /**
     * Finds an activity for a user by id.
     * 
     * @param activityId 
     * @param expand ex. expand&#x3D;creator
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public findAllById1(activityId: number, expand?: Array<string>, observe?: 'body', reportProgress?: boolean): Observable<ActivitiesDTO>;
    public findAllById1(activityId: number, expand?: Array<string>, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<ActivitiesDTO>>;
    public findAllById1(activityId: number, expand?: Array<string>, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<ActivitiesDTO>>;
    public findAllById1(activityId: number, expand?: Array<string>, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (activityId === null || activityId === undefined) {
            throw new Error('Required parameter activityId was null or undefined when calling findAllById1.');
        }


        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (expand) {
            expand.forEach((element) => {
                queryParameters = queryParameters.append('expand', <any>element);
            })
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.get<ActivitiesDTO>(`${this.basePath}/users/activities/${encodeURIComponent(String(activityId))}`,
            {
                params: queryParameters,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Finds all activities for a user.
     * 
     * @param offset 
     * @param limit 
     * @param sortBy ex. sort_by&#x3D;ID:asc,date_created:desc
     * @param filterBy ex. filter_by&#x3D;flag:dataset
     * @param expand ex. expand&#x3D;creator
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public findAllByUser1(offset?: number, limit?: number, sortBy?: string, filterBy?: Array<string>, expand?: Array<string>, observe?: 'body', reportProgress?: boolean): Observable<ActivitiesDTO>;
    public findAllByUser1(offset?: number, limit?: number, sortBy?: string, filterBy?: Array<string>, expand?: Array<string>, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<ActivitiesDTO>>;
    public findAllByUser1(offset?: number, limit?: number, sortBy?: string, filterBy?: Array<string>, expand?: Array<string>, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<ActivitiesDTO>>;
    public findAllByUser1(offset?: number, limit?: number, sortBy?: string, filterBy?: Array<string>, expand?: Array<string>, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {






        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (offset !== undefined && offset !== null) {
            queryParameters = queryParameters.set('offset', <any>offset);
        }
        if (limit !== undefined && limit !== null) {
            queryParameters = queryParameters.set('limit', <any>limit);
        }
        if (sortBy !== undefined && sortBy !== null) {
            queryParameters = queryParameters.set('sort_by', <any>sortBy);
        }
        if (filterBy) {
            filterBy.forEach((element) => {
                queryParameters = queryParameters.append('filter_by', <any>element);
            })
        }
        if (expand) {
            expand.forEach((element) => {
                queryParameters = queryParameters.append('expand', <any>element);
            })
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.get<ActivitiesDTO>(`${this.basePath}/users/activities`,
            {
                params: queryParameters,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}