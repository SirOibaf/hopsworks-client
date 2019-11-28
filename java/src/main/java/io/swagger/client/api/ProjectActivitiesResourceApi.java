/*
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

package io.swagger.client.api;

import io.swagger.client.ApiCallback;
import io.swagger.client.ApiClient;
import io.swagger.client.ApiException;
import io.swagger.client.ApiResponse;
import io.swagger.client.Configuration;
import io.swagger.client.Pair;
import io.swagger.client.ProgressRequestBody;
import io.swagger.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import io.swagger.client.model.ActivitiesDTO;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProjectActivitiesResourceApi {
    private ApiClient apiClient;

    public ProjectActivitiesResourceApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProjectActivitiesResourceApi(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return apiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /**
     * Build call for findAllById
     * @param activityId  (required)
     * @param projectId  (required)
     * @param expand ex. expand&#x3D;creator (optional)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call findAllByIdCall(Integer activityId, Integer projectId, List<String> expand, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = null;
        
        // create path and map variables
        String localVarPath = "/project/{projectId}/activities/{activityId}"
            .replaceAll("\\{" + "activityId" + "\\}", apiClient.escapeString(activityId.toString()))
            .replaceAll("\\{" + "projectId" + "\\}", apiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        if (expand != null)
        localVarCollectionQueryParams.addAll(apiClient.parameterToPairs("multi", "expand", expand));

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] {  };
        return apiClient.buildCall(localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call findAllByIdValidateBeforeCall(Integer activityId, Integer projectId, List<String> expand, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'activityId' is set
        if (activityId == null) {
            throw new ApiException("Missing the required parameter 'activityId' when calling findAllById(Async)");
        }
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling findAllById(Async)");
        }
        
        com.squareup.okhttp.Call call = findAllByIdCall(activityId, projectId, expand, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * Finds an activity in project.
     * 
     * @param activityId  (required)
     * @param projectId  (required)
     * @param expand ex. expand&#x3D;creator (optional)
     * @return ActivitiesDTO
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ActivitiesDTO findAllById(Integer activityId, Integer projectId, List<String> expand) throws ApiException {
        ApiResponse<ActivitiesDTO> resp = findAllByIdWithHttpInfo(activityId, projectId, expand);
        return resp.getData();
    }

    /**
     * Finds an activity in project.
     * 
     * @param activityId  (required)
     * @param projectId  (required)
     * @param expand ex. expand&#x3D;creator (optional)
     * @return ApiResponse&lt;ActivitiesDTO&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<ActivitiesDTO> findAllByIdWithHttpInfo(Integer activityId, Integer projectId, List<String> expand) throws ApiException {
        com.squareup.okhttp.Call call = findAllByIdValidateBeforeCall(activityId, projectId, expand, null, null);
        Type localVarReturnType = new TypeToken<ActivitiesDTO>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     * Finds an activity in project. (asynchronously)
     * 
     * @param activityId  (required)
     * @param projectId  (required)
     * @param expand ex. expand&#x3D;creator (optional)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call findAllByIdAsync(Integer activityId, Integer projectId, List<String> expand, final ApiCallback<ActivitiesDTO> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = findAllByIdValidateBeforeCall(activityId, projectId, expand, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<ActivitiesDTO>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
    /**
     * Build call for findAllByProject
     * @param projectId  (required)
     * @param offset  (optional)
     * @param limit  (optional)
     * @param sortBy ex. sort_by&#x3D;ID:asc,date_created:desc (optional)
     * @param filterBy ex. filter_by&#x3D;flag:dataset (optional)
     * @param expand ex. expand&#x3D;creator (optional)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call findAllByProjectCall(Integer projectId, Integer offset, Integer limit, String sortBy, List<String> filterBy, List<String> expand, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = null;
        
        // create path and map variables
        String localVarPath = "/project/{projectId}/activities"
            .replaceAll("\\{" + "projectId" + "\\}", apiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        if (offset != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("offset", offset));
        if (limit != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("limit", limit));
        if (sortBy != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("sort_by", sortBy));
        if (filterBy != null)
        localVarCollectionQueryParams.addAll(apiClient.parameterToPairs("multi", "filter_by", filterBy));
        if (expand != null)
        localVarCollectionQueryParams.addAll(apiClient.parameterToPairs("multi", "expand", expand));

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] {  };
        return apiClient.buildCall(localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call findAllByProjectValidateBeforeCall(Integer projectId, Integer offset, Integer limit, String sortBy, List<String> filterBy, List<String> expand, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling findAllByProject(Async)");
        }
        
        com.squareup.okhttp.Call call = findAllByProjectCall(projectId, offset, limit, sortBy, filterBy, expand, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * Finds activities in project.
     * 
     * @param projectId  (required)
     * @param offset  (optional)
     * @param limit  (optional)
     * @param sortBy ex. sort_by&#x3D;ID:asc,date_created:desc (optional)
     * @param filterBy ex. filter_by&#x3D;flag:dataset (optional)
     * @param expand ex. expand&#x3D;creator (optional)
     * @return ActivitiesDTO
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ActivitiesDTO findAllByProject(Integer projectId, Integer offset, Integer limit, String sortBy, List<String> filterBy, List<String> expand) throws ApiException {
        ApiResponse<ActivitiesDTO> resp = findAllByProjectWithHttpInfo(projectId, offset, limit, sortBy, filterBy, expand);
        return resp.getData();
    }

    /**
     * Finds activities in project.
     * 
     * @param projectId  (required)
     * @param offset  (optional)
     * @param limit  (optional)
     * @param sortBy ex. sort_by&#x3D;ID:asc,date_created:desc (optional)
     * @param filterBy ex. filter_by&#x3D;flag:dataset (optional)
     * @param expand ex. expand&#x3D;creator (optional)
     * @return ApiResponse&lt;ActivitiesDTO&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<ActivitiesDTO> findAllByProjectWithHttpInfo(Integer projectId, Integer offset, Integer limit, String sortBy, List<String> filterBy, List<String> expand) throws ApiException {
        com.squareup.okhttp.Call call = findAllByProjectValidateBeforeCall(projectId, offset, limit, sortBy, filterBy, expand, null, null);
        Type localVarReturnType = new TypeToken<ActivitiesDTO>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     * Finds activities in project. (asynchronously)
     * 
     * @param projectId  (required)
     * @param offset  (optional)
     * @param limit  (optional)
     * @param sortBy ex. sort_by&#x3D;ID:asc,date_created:desc (optional)
     * @param filterBy ex. filter_by&#x3D;flag:dataset (optional)
     * @param expand ex. expand&#x3D;creator (optional)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call findAllByProjectAsync(Integer projectId, Integer offset, Integer limit, String sortBy, List<String> filterBy, List<String> expand, final ApiCallback<ActivitiesDTO> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = findAllByProjectValidateBeforeCall(projectId, offset, limit, sortBy, filterBy, expand, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<ActivitiesDTO>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
}
