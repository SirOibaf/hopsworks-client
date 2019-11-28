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
 * LocalResourceDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class LocalResourceDTO {

  @SerializedName("name")
  private String name = null;

  @SerializedName("path")
  private String path = null;

  @SerializedName("visibility")
  private String visibility = null;

  @SerializedName("type")
  private String type = null;

  @SerializedName("pattern")
  private String pattern = null;
  public LocalResourceDTO name(String name) {
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
  public LocalResourceDTO path(String path) {
    this.path = path;
    return this;
  }

  

  /**
  * Get path
  * @return path
  **/
  @Schema(description = "")
  public String getPath() {
    return path;
  }
  public void setPath(String path) {
    this.path = path;
  }
  public LocalResourceDTO visibility(String visibility) {
    this.visibility = visibility;
    return this;
  }

  

  /**
  * Get visibility
  * @return visibility
  **/
  @Schema(description = "")
  public String getVisibility() {
    return visibility;
  }
  public void setVisibility(String visibility) {
    this.visibility = visibility;
  }
  public LocalResourceDTO type(String type) {
    this.type = type;
    return this;
  }

  

  /**
  * Get type
  * @return type
  **/
  @Schema(description = "")
  public String getType() {
    return type;
  }
  public void setType(String type) {
    this.type = type;
  }
  public LocalResourceDTO pattern(String pattern) {
    this.pattern = pattern;
    return this;
  }

  

  /**
  * Get pattern
  * @return pattern
  **/
  @Schema(description = "")
  public String getPattern() {
    return pattern;
  }
  public void setPattern(String pattern) {
    this.pattern = pattern;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LocalResourceDTO localResourceDTO = (LocalResourceDTO) o;
    return Objects.equals(this.name, localResourceDTO.name) &&
        Objects.equals(this.path, localResourceDTO.path) &&
        Objects.equals(this.visibility, localResourceDTO.visibility) &&
        Objects.equals(this.type, localResourceDTO.type) &&
        Objects.equals(this.pattern, localResourceDTO.pattern);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(name, path, visibility, type, pattern);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LocalResourceDTO {\n");
    
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    path: ").append(toIndentedString(path)).append("\n");
    sb.append("    visibility: ").append(toIndentedString(visibility)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    pattern: ").append(toIndentedString(pattern)).append("\n");
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
