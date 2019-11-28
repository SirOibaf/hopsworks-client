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
import io.swagger.client.model.ApiKeyDTO;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ApiKeyResourceApi
 */
@Ignore
public class ApiKeyResourceApiTest {

    private final ApiKeyResourceApi api = new ApiKeyResourceApi();

    /**
     * Check api key session.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void checkSessionTest() throws ApiException {
        api.checkSession();

        // TODO: test validations
    }
    /**
     * Create an api key.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createTest() throws ApiException {
        String name = null;
        List<String> scope = null;
        ApiKeyDTO response = api.create(name, scope);

        // TODO: test validations
    }
    /**
     * Delete all api keys.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteAllTest() throws ApiException {
        api.deleteAll();

        // TODO: test validations
    }
    /**
     * Delete api key by name.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteByNameTest() throws ApiException {
        String name = null;
        api.deleteByName(name);

        // TODO: test validations
    }
    /**
     * Get all api keys.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void get4Test() throws ApiException {
        Integer offset = null;
        Integer limit = null;
        String sortBy = null;
        List<String> filterBy = null;
        ApiKeyDTO response = api.get4(offset, limit, sortBy, filterBy);

        // TODO: test validations
    }
    /**
     * Find api key by name.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getByKeyTest() throws ApiException {
        String key = null;
        ApiKeyDTO response = api.getByKey(key);

        // TODO: test validations
    }
    /**
     * Find api key by name.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getByName3Test() throws ApiException {
        String name = null;
        ApiKeyDTO response = api.getByName3(name);

        // TODO: test validations
    }
    /**
     * Get all api keys scopes.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getScopesTest() throws ApiException {
        api.getScopes();

        // TODO: test validations
    }
    /**
     * Update an api key.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void update1Test() throws ApiException {
        String name = null;
        String action = null;
        List<String> scope = null;
        ApiKeyDTO response = api.update1(name, action, scope);

        // TODO: test validations
    }
}