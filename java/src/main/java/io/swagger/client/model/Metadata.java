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
import io.swagger.client.model.MetadataPK;
import io.swagger.client.model.RawData;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * Metadata
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class Metadata {

  @SerializedName("metadataPK")
  private MetadataPK metadataPK = null;

  @SerializedName("data")
  private String data = null;

  @SerializedName("rawData")
  private RawData rawData = null;

  @SerializedName("id")
  private Integer id = null;
  public Metadata metadataPK(MetadataPK metadataPK) {
    this.metadataPK = metadataPK;
    return this;
  }

  

  /**
  * Get metadataPK
  * @return metadataPK
  **/
  @Schema(description = "")
  public MetadataPK getMetadataPK() {
    return metadataPK;
  }
  public void setMetadataPK(MetadataPK metadataPK) {
    this.metadataPK = metadataPK;
  }
  public Metadata data(String data) {
    this.data = data;
    return this;
  }

  

  /**
  * Get data
  * @return data
  **/
  @Schema(required = true, description = "")
  public String getData() {
    return data;
  }
  public void setData(String data) {
    this.data = data;
  }
  public Metadata rawData(RawData rawData) {
    this.rawData = rawData;
    return this;
  }

  

  /**
  * Get rawData
  * @return rawData
  **/
  @Schema(description = "")
  public RawData getRawData() {
    return rawData;
  }
  public void setRawData(RawData rawData) {
    this.rawData = rawData;
  }
  public Metadata id(Integer id) {
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
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Metadata metadata = (Metadata) o;
    return Objects.equals(this.metadataPK, metadata.metadataPK) &&
        Objects.equals(this.data, metadata.data) &&
        Objects.equals(this.rawData, metadata.rawData) &&
        Objects.equals(this.id, metadata.id);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(metadataPK, data, rawData, id);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Metadata {\n");
    
    sb.append("    metadataPK: ").append(toIndentedString(metadataPK)).append("\n");
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
    sb.append("    rawData: ").append(toIndentedString(rawData)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
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