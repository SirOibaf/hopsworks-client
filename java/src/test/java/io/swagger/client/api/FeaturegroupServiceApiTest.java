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

import io.swagger.client.ApiException;
import io.swagger.client.model.FeaturegroupDTO;
import io.swagger.client.model.FeaturegroupPreview;
import io.swagger.client.model.RowValueQueryResult;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for FeaturegroupServiceApi
 */
@Ignore
public class FeaturegroupServiceApiTest {

    private final FeaturegroupServiceApi api = new FeaturegroupServiceApi();

    /**
     * Create feature group in a featurestore
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createFeaturegroupTest() throws ApiException {
        Integer featurestoreId = null;
        Integer projectId = null;
        FeaturegroupDTO body = null;
        FeaturegroupDTO response = api.createFeaturegroup(featurestoreId, projectId, body);

        // TODO: test validations
    }
    /**
     * Delete specific featuregroup from a specific featurestore
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteFeatureGroupFromFeatureStoreTest() throws ApiException {
        Integer featuregroupId = null;
        Integer featurestoreId = null;
        Integer projectId = null;
        FeaturegroupDTO response = api.deleteFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId);

        // TODO: test validations
    }
    /**
     * Delete featuregroup contents
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteFeaturegroupContentsTest() throws ApiException {
        Integer featuregroupId = null;
        Integer featurestoreId = null;
        Integer projectId = null;
        FeaturegroupDTO response = api.deleteFeaturegroupContents(featuregroupId, featurestoreId, projectId);

        // TODO: test validations
    }
    /**
     * Get specific featuregroup from a specific featurestore
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getFeatureGroupFromFeatureStoreTest() throws ApiException {
        Integer featuregroupId = null;
        Integer featurestoreId = null;
        Integer projectId = null;
        FeaturegroupDTO response = api.getFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId);

        // TODO: test validations
    }
    /**
     * Preview feature data of a featuregroup
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getFeatureGroupPreviewTest() throws ApiException {
        Integer featuregroupId = null;
        Integer featurestoreId = null;
        Integer projectId = null;
        List<FeaturegroupPreview> response = api.getFeatureGroupPreview(featuregroupId, featurestoreId, projectId);

        // TODO: test validations
    }
    /**
     * Get the SQL schema of a featuregroup
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getFeatureGroupSchemaTest() throws ApiException {
        Integer featuregroupId = null;
        Integer featurestoreId = null;
        Integer projectId = null;
        RowValueQueryResult response = api.getFeatureGroupSchema(featuregroupId, featurestoreId, projectId);

        // TODO: test validations
    }
    /**
     * Get the list of feature groups for a featurestore
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getFeaturegroupsForFeaturestoreTest() throws ApiException {
        Integer featurestoreId = null;
        Integer projectId = null;
        List<FeaturegroupDTO> response = api.getFeaturegroupsForFeaturestore(featurestoreId, projectId);

        // TODO: test validations
    }
    /**
     * Synchornize Hive Table with the feature store
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void syncWithFeaturestoreTest() throws ApiException {
        Integer featurestoreId = null;
        Integer projectId = null;
        FeaturegroupDTO body = null;
        FeaturegroupDTO response = api.syncWithFeaturestore(featurestoreId, projectId, body);

        // TODO: test validations
    }
    /**
     * Update featuregroup contents
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateFeaturegroupTest() throws ApiException {
        Integer featuregroupId = null;
        Integer featurestoreId = null;
        Integer projectId = null;
        FeaturegroupDTO body = null;
        Boolean updateMetadata = null;
        Boolean updateStats = null;
        Boolean enableOnline = null;
        Boolean disableOnline = null;
        Boolean updateStatsSettings = null;
        FeaturegroupDTO response = api.updateFeaturegroup(featuregroupId, featurestoreId, projectId, body, updateMetadata, updateStats, enableOnline, disableOnline, updateStatsSettings);

        // TODO: test validations
    }
}