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
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * MetadataPK
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class MetadataPK {

  @SerializedName("id")
  private Integer id = null;

  @SerializedName("fieldid")
  private Integer fieldid = null;

  @SerializedName("tupleid")
  private Integer tupleid = null;
  public MetadataPK id(Integer id) {
    this.id = id;
    return this;
  }

  

  /**
  * Get id
  * @return id
  **/
  @Schema(required = true, description = "")
  public Integer getId() {
    return id;
  }
  public void setId(Integer id) {
    this.id = id;
  }
  public MetadataPK fieldid(Integer fieldid) {
    this.fieldid = fieldid;
    return this;
  }

  

  /**
  * Get fieldid
  * @return fieldid
  **/
  @Schema(required = true, description = "")
  public Integer getFieldid() {
    return fieldid;
  }
  public void setFieldid(Integer fieldid) {
    this.fieldid = fieldid;
  }
  public MetadataPK tupleid(Integer tupleid) {
    this.tupleid = tupleid;
    return this;
  }

  

  /**
  * Get tupleid
  * @return tupleid
  **/
  @Schema(required = true, description = "")
  public Integer getTupleid() {
    return tupleid;
  }
  public void setTupleid(Integer tupleid) {
    this.tupleid = tupleid;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MetadataPK metadataPK = (MetadataPK) o;
    return Objects.equals(this.id, metadataPK.id) &&
        Objects.equals(this.fieldid, metadataPK.fieldid) &&
        Objects.equals(this.tupleid, metadataPK.tupleid);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(id, fieldid, tupleid);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MetadataPK {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    fieldid: ").append(toIndentedString(fieldid)).append("\n");
    sb.append("    tupleid: ").append(toIndentedString(tupleid)).append("\n");
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