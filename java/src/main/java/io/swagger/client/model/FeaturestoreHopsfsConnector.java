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
import io.swagger.client.model.Dataset;
import io.swagger.client.model.Featurestore;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * FeaturestoreHopsfsConnector
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class FeaturestoreHopsfsConnector {

  @SerializedName("id")
  private Integer id = null;

  @SerializedName("featurestore")
  private Featurestore featurestore = null;

  @SerializedName("hopsfsDataset")
  private Dataset hopsfsDataset = null;

  @SerializedName("description")
  private String description = null;

  @SerializedName("name")
  private String name = null;
  public FeaturestoreHopsfsConnector id(Integer id) {
    this.id = id;
    return this;
  }

  

  /**
  * Get id
  * @return id
  **/
  @Schema(description = "")
  public Integer getId() {
    return id;
  }
  public void setId(Integer id) {
    this.id = id;
  }
  public FeaturestoreHopsfsConnector featurestore(Featurestore featurestore) {
    this.featurestore = featurestore;
    return this;
  }

  

  /**
  * Get featurestore
  * @return featurestore
  **/
  @Schema(description = "")
  public Featurestore getFeaturestore() {
    return featurestore;
  }
  public void setFeaturestore(Featurestore featurestore) {
    this.featurestore = featurestore;
  }
  public FeaturestoreHopsfsConnector hopsfsDataset(Dataset hopsfsDataset) {
    this.hopsfsDataset = hopsfsDataset;
    return this;
  }

  

  /**
  * Get hopsfsDataset
  * @return hopsfsDataset
  **/
  @Schema(description = "")
  public Dataset getHopsfsDataset() {
    return hopsfsDataset;
  }
  public void setHopsfsDataset(Dataset hopsfsDataset) {
    this.hopsfsDataset = hopsfsDataset;
  }
  public FeaturestoreHopsfsConnector description(String description) {
    this.description = description;
    return this;
  }

  

  /**
  * Get description
  * @return description
  **/
  @Schema(description = "")
  public String getDescription() {
    return description;
  }
  public void setDescription(String description) {
    this.description = description;
  }
  public FeaturestoreHopsfsConnector name(String name) {
    this.name = name;
    return this;
  }

  

  /**
  * Get name
  * @return name
  **/
  @Schema(description = "")
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FeaturestoreHopsfsConnector featurestoreHopsfsConnector = (FeaturestoreHopsfsConnector) o;
    return Objects.equals(this.id, featurestoreHopsfsConnector.id) &&
        Objects.equals(this.featurestore, featurestoreHopsfsConnector.featurestore) &&
        Objects.equals(this.hopsfsDataset, featurestoreHopsfsConnector.hopsfsDataset) &&
        Objects.equals(this.description, featurestoreHopsfsConnector.description) &&
        Objects.equals(this.name, featurestoreHopsfsConnector.name);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(id, featurestore, hopsfsDataset, description, name);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FeaturestoreHopsfsConnector {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    featurestore: ").append(toIndentedString(featurestore)).append("\n");
    sb.append("    hopsfsDataset: ").append(toIndentedString(hopsfsDataset)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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
