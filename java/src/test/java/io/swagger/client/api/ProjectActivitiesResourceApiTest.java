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
import io.swagger.client.model.ActivitiesDTO;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ProjectActivitiesResourceApi
 */
@Ignore
public class ProjectActivitiesResourceApiTest {

    private final ProjectActivitiesResourceApi api = new ProjectActivitiesResourceApi();

    /**
     * Finds an activity in project.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void findAllByIdTest() throws ApiException {
        Integer activityId = null;
        Integer projectId = null;
        List<String> expand = null;
        ActivitiesDTO response = api.findAllById(activityId, projectId, expand);

        // TODO: test validations
    }
    /**
     * Finds activities in project.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void findAllByProjectTest() throws ApiException {
        Integer projectId = null;
        Integer offset = null;
        Integer limit = null;
        String sortBy = null;
        List<String> filterBy = null;
        List<String> expand = null;
        ActivitiesDTO response = api.findAllByProject(projectId, offset, limit, sortBy, filterBy, expand);

        // TODO: test validations
    }
}
