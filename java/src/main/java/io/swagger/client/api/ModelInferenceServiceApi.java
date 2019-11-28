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



import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ModelInferenceServiceApi {
    private ApiClient apiClient;

    public ModelInferenceServiceApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ModelInferenceServiceApi(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return apiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /**
     * Build call for infer
     * @param modelName Name of the model to query (required)
     * @param version Version of the model to query (required)
     * @param verb Type of query (required)
     * @param projectId  (required)
     * @param body  (optional)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call inferCall(String modelName, String version, String verb, Integer projectId, String body, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = body;
        
        // create path and map variables
        String localVarPath = "/project/{projectId}/inference/models/{modelName}{version}{verb}"
            .replaceAll("\\{" + "modelName" + "\\}", apiClient.escapeString(modelName.toString()))
            .replaceAll("\\{" + "version" + "\\}", apiClient.escapeString(version.toString()))
            .replaceAll("\\{" + "verb" + "\\}", apiClient.escapeString(verb.toString()))
            .replaceAll("\\{" + "projectId" + "\\}", apiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            "application/json"
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
        return apiClient.buildCall(localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call inferValidateBeforeCall(String modelName, String version, String verb, Integer projectId, String body, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'modelName' is set
        if (modelName == null) {
            throw new ApiException("Missing the required parameter 'modelName' when calling infer(Async)");
        }
        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling infer(Async)");
        }
        // verify the required parameter 'verb' is set
        if (verb == null) {
            throw new ApiException("Missing the required parameter 'verb' when calling infer(Async)");
        }
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling infer(Async)");
        }
        
        com.squareup.okhttp.Call call = inferCall(modelName, version, verb, projectId, body, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * Make inference
     * 
     * @param modelName Name of the model to query (required)
     * @param version Version of the model to query (required)
     * @param verb Type of query (required)
     * @param projectId  (required)
     * @param body  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public void infer(String modelName, String version, String verb, Integer projectId, String body) throws ApiException {
        inferWithHttpInfo(modelName, version, verb, projectId, body);
    }

    /**
     * Make inference
     * 
     * @param modelName Name of the model to query (required)
     * @param version Version of the model to query (required)
     * @param verb Type of query (required)
     * @param projectId  (required)
     * @param body  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Void> inferWithHttpInfo(String modelName, String version, String verb, Integer projectId, String body) throws ApiException {
        com.squareup.okhttp.Call call = inferValidateBeforeCall(modelName, version, verb, projectId, body, null, null);
        return apiClient.execute(call);
    }

    /**
     * Make inference (asynchronously)
     * 
     * @param modelName Name of the model to query (required)
     * @param version Version of the model to query (required)
     * @param verb Type of query (required)
     * @param projectId  (required)
     * @param body  (optional)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call inferAsync(String modelName, String version, String verb, Integer projectId, String body, final ApiCallback<Void> callback) throws ApiException {

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

        com.squareup.okhttp.Call call = inferValidateBeforeCall(modelName, version, verb, projectId, body, progressListener, progressRequestListener);
        apiClient.executeAsync(call, callback);
        return call;
    }
}
