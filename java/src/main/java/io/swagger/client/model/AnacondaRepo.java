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
import io.swagger.client.model.PythonDep;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * AnacondaRepo
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class AnacondaRepo {

  @SerializedName("id")
  private Integer id = null;

  @SerializedName("url")
  private String url = null;

  @SerializedName("pythonDepCollection")
  private List<PythonDep> pythonDepCollection = null;
  public AnacondaRepo id(Integer id) {
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
  public AnacondaRepo url(String url) {
    this.url = url;
    return this;
  }

  

  /**
  * Get url
  * @return url
  **/
  @Schema(required = true, description = "")
  public String getUrl() {
    return url;
  }
  public void setUrl(String url) {
    this.url = url;
  }
  public AnacondaRepo pythonDepCollection(List<PythonDep> pythonDepCollection) {
    this.pythonDepCollection = pythonDepCollection;
    return this;
  }

  public AnacondaRepo addPythonDepCollectionItem(PythonDep pythonDepCollectionItem) {
    if (this.pythonDepCollection == null) {
      this.pythonDepCollection = new ArrayList<PythonDep>();
    }
    this.pythonDepCollection.add(pythonDepCollectionItem);
    return this;
  }

  /**
  * Get pythonDepCollection
  * @return pythonDepCollection
  **/
  @Schema(description = "")
  public List<PythonDep> getPythonDepCollection() {
    return pythonDepCollection;
  }
  public void setPythonDepCollection(List<PythonDep> pythonDepCollection) {
    this.pythonDepCollection = pythonDepCollection;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AnacondaRepo anacondaRepo = (AnacondaRepo) o;
    return Objects.equals(this.id, anacondaRepo.id) &&
        Objects.equals(this.url, anacondaRepo.url) &&
        Objects.equals(this.pythonDepCollection, anacondaRepo.pythonDepCollection);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(id, url, pythonDepCollection);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AnacondaRepo {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
    sb.append("    pythonDepCollection: ").append(toIndentedString(pythonDepCollection)).append("\n");
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
