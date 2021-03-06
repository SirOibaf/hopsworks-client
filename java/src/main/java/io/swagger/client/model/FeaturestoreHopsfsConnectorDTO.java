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
import io.swagger.client.model.FeaturestoreStorageConnectorDTO;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * FeaturestoreHopsfsConnectorDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class FeaturestoreHopsfsConnectorDTO extends FeaturestoreStorageConnectorDTO {

  @SerializedName("hopsfsPath")
  private String hopsfsPath = null;

  @SerializedName("datasetName")
  private String datasetName = null;
  public FeaturestoreHopsfsConnectorDTO hopsfsPath(String hopsfsPath) {
    this.hopsfsPath = hopsfsPath;
    return this;
  }

  

  /**
  * Get hopsfsPath
  * @return hopsfsPath
  **/
  @Schema(description = "")
  public String getHopsfsPath() {
    return hopsfsPath;
  }
  public void setHopsfsPath(String hopsfsPath) {
    this.hopsfsPath = hopsfsPath;
  }
  public FeaturestoreHopsfsConnectorDTO datasetName(String datasetName) {
    this.datasetName = datasetName;
    return this;
  }

  

  /**
  * Get datasetName
  * @return datasetName
  **/
  @Schema(description = "")
  public String getDatasetName() {
    return datasetName;
  }
  public void setDatasetName(String datasetName) {
    this.datasetName = datasetName;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FeaturestoreHopsfsConnectorDTO featurestoreHopsfsConnectorDTO = (FeaturestoreHopsfsConnectorDTO) o;
    return Objects.equals(this.hopsfsPath, featurestoreHopsfsConnectorDTO.hopsfsPath) &&
        Objects.equals(this.datasetName, featurestoreHopsfsConnectorDTO.datasetName) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(hopsfsPath, datasetName, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FeaturestoreHopsfsConnectorDTO {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    hopsfsPath: ").append(toIndentedString(hopsfsPath)).append("\n");
    sb.append("    datasetName: ").append(toIndentedString(datasetName)).append("\n");
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
