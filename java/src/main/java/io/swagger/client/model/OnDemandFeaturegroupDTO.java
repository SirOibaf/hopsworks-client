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

package io.swagger.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.client.model.ClusterAnalysisDTO;
import io.swagger.client.model.DescriptiveStatsDTO;
import io.swagger.client.model.FeatureCorrelationMatrixDTO;
import io.swagger.client.model.FeatureDTO;
import io.swagger.client.model.FeatureDistributionsDTO;
import io.swagger.client.model.FeaturegroupDTO;
import io.swagger.client.model.FeaturestoreJobDTO;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.List;
import org.threeten.bp.OffsetDateTime;

/**
 * OnDemandFeaturegroupDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class OnDemandFeaturegroupDTO extends FeaturegroupDTO {

  @SerializedName("jdbcConnectorId")
  private Integer jdbcConnectorId = null;

  @SerializedName("jdbcConnectorName")
  private String jdbcConnectorName = null;

  @SerializedName("query")
  private String query = null;
  public OnDemandFeaturegroupDTO jdbcConnectorId(Integer jdbcConnectorId) {
    this.jdbcConnectorId = jdbcConnectorId;
    return this;
  }

  

  /**
  * Get jdbcConnectorId
  * @return jdbcConnectorId
  **/
  @Schema(description = "")
  public Integer getJdbcConnectorId() {
    return jdbcConnectorId;
  }
  public void setJdbcConnectorId(Integer jdbcConnectorId) {
    this.jdbcConnectorId = jdbcConnectorId;
  }
  public OnDemandFeaturegroupDTO jdbcConnectorName(String jdbcConnectorName) {
    this.jdbcConnectorName = jdbcConnectorName;
    return this;
  }

  

  /**
  * Get jdbcConnectorName
  * @return jdbcConnectorName
  **/
  @Schema(description = "")
  public String getJdbcConnectorName() {
    return jdbcConnectorName;
  }
  public void setJdbcConnectorName(String jdbcConnectorName) {
    this.jdbcConnectorName = jdbcConnectorName;
  }
  public OnDemandFeaturegroupDTO query(String query) {
    this.query = query;
    return this;
  }

  

  /**
  * Get query
  * @return query
  **/
  @Schema(description = "")
  public String getQuery() {
    return query;
  }
  public void setQuery(String query) {
    this.query = query;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OnDemandFeaturegroupDTO onDemandFeaturegroupDTO = (OnDemandFeaturegroupDTO) o;
    return Objects.equals(this.jdbcConnectorId, onDemandFeaturegroupDTO.jdbcConnectorId) &&
        Objects.equals(this.jdbcConnectorName, onDemandFeaturegroupDTO.jdbcConnectorName) &&
        Objects.equals(this.query, onDemandFeaturegroupDTO.query) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(jdbcConnectorId, jdbcConnectorName, query, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OnDemandFeaturegroupDTO {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    jdbcConnectorId: ").append(toIndentedString(jdbcConnectorId)).append("\n");
    sb.append("    jdbcConnectorName: ").append(toIndentedString(jdbcConnectorName)).append("\n");
    sb.append("    query: ").append(toIndentedString(query)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
