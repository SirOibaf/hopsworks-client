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
import io.swagger.client.model.CommandDTO;
import io.swagger.client.model.EnvironmentDTO;
import io.swagger.client.model.EnvironmentYmlDTO;
import io.swagger.client.model.LibraryDTO;
import io.swagger.client.model.LibrarySearchDTO;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PythonApi
 */
@Ignore
public class PythonApiTest {

    private final PythonApi api = new PythonApi();

    /**
     * Delete commands for this environment
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteTest() throws ApiException {
        String version = null;
        Integer projectId = null;
        api.delete(version, projectId);

        // TODO: test validations
    }
    /**
     * Delete commands for this library
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void delete1Test() throws ApiException {
        String library = null;
        String version = null;
        Integer projectId = null;
        api.delete1(library, version, projectId);

        // TODO: test validations
    }
    /**
     * Remove the python environment with the specified version for this project
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void delete2Test() throws ApiException {
        String version = null;
        Integer projectId = null;
        EnvironmentDTO response = api.delete2(version, projectId);

        // TODO: test validations
    }
    /**
     * Get commands for this environment
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getTest() throws ApiException {
        String version = null;
        Integer projectId = null;
        Integer offset = null;
        Integer limit = null;
        String sortBy = null;
        List<String> filterBy = null;
        api.get(version, projectId, offset, limit, sortBy, filterBy);

        // TODO: test validations
    }
    /**
     * Get all commands for this library
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void get1Test() throws ApiException {
        String library = null;
        String version = null;
        Integer projectId = null;
        Integer offset = null;
        Integer limit = null;
        String sortBy = null;
        List<String> filterBy = null;
        CommandDTO response = api.get1(library, version, projectId, offset, limit, sortBy, filterBy);

        // TODO: test validations
    }
    /**
     * Get the python libraries installed in this environment
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void get2Test() throws ApiException {
        String version = null;
        Integer projectId = null;
        Integer offset = null;
        Integer limit = null;
        String sortBy = null;
        List<String> filterBy = null;
        List<String> expand = null;
        LibraryDTO response = api.get2(version, projectId, offset, limit, sortBy, filterBy, expand);

        // TODO: test validations
    }
    /**
     * Get the python environment for specific python version
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void get3Test() throws ApiException {
        String version = null;
        Integer projectId = null;
        List<String> expand = null;
        EnvironmentDTO response = api.get3(version, projectId, expand);

        // TODO: test validations
    }
    /**
     * Get all python environments for this project
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getAllTest() throws ApiException {
        Integer projectId = null;
        List<String> expand = null;
        EnvironmentDTO response = api.getAll(projectId, expand);

        // TODO: test validations
    }
    /**
     * Get commands by id
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getByNameTest() throws ApiException {
        Integer commandId = null;
        String version = null;
        Integer projectId = null;
        CommandDTO response = api.getByName(commandId, version, projectId);

        // TODO: test validations
    }
    /**
     * Get command by id
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getByName1Test() throws ApiException {
        String library = null;
        Integer commandId = null;
        String version = null;
        Integer projectId = null;
        CommandDTO response = api.getByName1(library, commandId, version, projectId);

        // TODO: test validations
    }
    /**
     * Get the a python library installed in this environment
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getByName2Test() throws ApiException {
        String library = null;
        String version = null;
        Integer projectId = null;
        List<String> expand = null;
        LibraryDTO response = api.getByName2(library, version, projectId, expand);

        // TODO: test validations
    }
    /**
     * Install a python library in the environment
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void installTest() throws ApiException {
        String library = null;
        String version2 = null;
        Integer projectId = null;
        String packageManager = null;
        String version = null;
        String channel = null;
        String machine = null;
        api.install(library, version2, projectId, packageManager, version, channel, machine);

        // TODO: test validations
    }
    /**
     * Create an environment from version or export an environment as yaml file
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void postTest() throws ApiException {
        String version = null;
        Integer projectId = null;
        String action = null;
        EnvironmentDTO response = api.post(version, projectId, action);

        // TODO: test validations
    }
    /**
     * Create an environment from yaml file
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void postYmlTest() throws ApiException {
        Integer projectId = null;
        EnvironmentYmlDTO body = null;
        EnvironmentDTO response = api.postYml(projectId, body);

        // TODO: test validations
    }
    /**
     * Search for libraries using conda or pip package managers
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void searchTest() throws ApiException {
        String search = null;
        String version = null;
        Integer projectId = null;
        String query = null;
        String channel = null;
        LibrarySearchDTO response = api.search(search, version, projectId, query, channel);

        // TODO: test validations
    }
    /**
     * Uninstall a python library from the environment
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void uninstallTest() throws ApiException {
        String library = null;
        String version = null;
        Integer projectId = null;
        api.uninstall(library, version, projectId);

        // TODO: test validations
    }
    /**
     * Update commands for this library
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateTest() throws ApiException {
        String library = null;
        String version = null;
        Integer projectId = null;
        api.update(library, version, projectId);

        // TODO: test validations
    }
}