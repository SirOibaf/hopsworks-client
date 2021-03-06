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

import { ApiKeyDTO } from '../model/apiKeyDTO';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class ApiKeyResourceService {

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
     * Check api key session.
     * 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public checkSession(observe?: 'body', reportProgress?: boolean): Observable<any>;
    public checkSession(observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public checkSession(observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public checkSession(observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.get<any>(`${this.basePath}/users/apiKey/session`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Create an api key.
     * 
     * @param name 
     * @param scope 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public create(name?: string, scope?: Array<string>, observe?: 'body', reportProgress?: boolean): Observable<ApiKeyDTO>;
    public create(name?: string, scope?: Array<string>, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<ApiKeyDTO>>;
    public create(name?: string, scope?: Array<string>, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<ApiKeyDTO>>;
    public create(name?: string, scope?: Array<string>, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {



        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (name !== undefined && name !== null) {
            queryParameters = queryParameters.set('name', <any>name);
        }
        if (scope) {
            scope.forEach((element) => {
                queryParameters = queryParameters.append('scope', <any>element);
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

        return this.httpClient.post<ApiKeyDTO>(`${this.basePath}/users/apiKey`,
            null,
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
     * Delete all api keys.
     * 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public deleteAll(observe?: 'body', reportProgress?: boolean): Observable<any>;
    public deleteAll(observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public deleteAll(observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public deleteAll(observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.delete<any>(`${this.basePath}/users/apiKey`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Delete api key by name.
     * 
     * @param name 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public deleteByName(name: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public deleteByName(name: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public deleteByName(name: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public deleteByName(name: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (name === null || name === undefined) {
            throw new Error('Required parameter name was null or undefined when calling deleteByName.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.delete<any>(`${this.basePath}/users/apiKey/${encodeURIComponent(String(name))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Get all api keys.
     * 
     * @param offset 
     * @param limit 
     * @param sortBy ex. sort_by&#x3D;Name:asc,created:desc,modified:desc
     * @param filterBy ex. filter_by&#x3D;name:key, created:2019-01-01T00:00:00.000, created_lt:2019-01-01T00:00:00.000, created_gt:2019-01-01T00:00:00.000, modified:2019-01-01T00:00:00.000, modified_lt:2019-01-01T00:00:00.000, modified_gt:2019-01-01T00:00:00.000
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public get4(offset?: number, limit?: number, sortBy?: string, filterBy?: Array<string>, observe?: 'body', reportProgress?: boolean): Observable<ApiKeyDTO>;
    public get4(offset?: number, limit?: number, sortBy?: string, filterBy?: Array<string>, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<ApiKeyDTO>>;
    public get4(offset?: number, limit?: number, sortBy?: string, filterBy?: Array<string>, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<ApiKeyDTO>>;
    public get4(offset?: number, limit?: number, sortBy?: string, filterBy?: Array<string>, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {





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

        return this.httpClient.get<ApiKeyDTO>(`${this.basePath}/users/apiKey`,
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
     * Find api key by name.
     * 
     * @param key 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public getByKey(key?: string, observe?: 'body', reportProgress?: boolean): Observable<ApiKeyDTO>;
    public getByKey(key?: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<ApiKeyDTO>>;
    public getByKey(key?: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<ApiKeyDTO>>;
    public getByKey(key?: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {


        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (key !== undefined && key !== null) {
            queryParameters = queryParameters.set('key', <any>key);
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

        return this.httpClient.get<ApiKeyDTO>(`${this.basePath}/users/apiKey/key`,
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
     * Find api key by name.
     * 
     * @param name 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public getByName3(name: string, observe?: 'body', reportProgress?: boolean): Observable<ApiKeyDTO>;
    public getByName3(name: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<ApiKeyDTO>>;
    public getByName3(name: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<ApiKeyDTO>>;
    public getByName3(name: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (name === null || name === undefined) {
            throw new Error('Required parameter name was null or undefined when calling getByName3.');
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

        return this.httpClient.get<ApiKeyDTO>(`${this.basePath}/users/apiKey/${encodeURIComponent(String(name))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Get all api keys scopes.
     * 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public getScopes(observe?: 'body', reportProgress?: boolean): Observable<any>;
    public getScopes(observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public getScopes(observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public getScopes(observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.get<any>(`${this.basePath}/users/apiKey/scopes`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Update an api key.
     * 
     * @param name 
     * @param action 
     * @param scope 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public update1(name?: string, action?: string, scope?: Array<string>, observe?: 'body', reportProgress?: boolean): Observable<ApiKeyDTO>;
    public update1(name?: string, action?: string, scope?: Array<string>, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<ApiKeyDTO>>;
    public update1(name?: string, action?: string, scope?: Array<string>, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<ApiKeyDTO>>;
    public update1(name?: string, action?: string, scope?: Array<string>, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {




        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (name !== undefined && name !== null) {
            queryParameters = queryParameters.set('name', <any>name);
        }
        if (action !== undefined && action !== null) {
            queryParameters = queryParameters.set('action', <any>action);
        }
        if (scope) {
            scope.forEach((element) => {
                queryParameters = queryParameters.append('scope', <any>element);
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

        return this.httpClient.put<ApiKeyDTO>(`${this.basePath}/users/apiKey`,
            null,
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
