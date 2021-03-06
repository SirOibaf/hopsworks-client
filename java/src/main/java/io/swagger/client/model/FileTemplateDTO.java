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
 * FileTemplateDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class FileTemplateDTO {

  @SerializedName("inodePath")
  private String inodePath = null;

  @SerializedName("templateId")
  private Integer templateId = null;
  public FileTemplateDTO inodePath(String inodePath) {
    this.inodePath = inodePath;
    return this;
  }

  

  /**
  * Get inodePath
  * @return inodePath
  **/
  @Schema(description = "")
  public String getInodePath() {
    return inodePath;
  }
  public void setInodePath(String inodePath) {
    this.inodePath = inodePath;
  }
  public FileTemplateDTO templateId(Integer templateId) {
    this.templateId = templateId;
    return this;
  }

  

  /**
  * Get templateId
  * @return templateId
  **/
  @Schema(description = "")
  public Integer getTemplateId() {
    return templateId;
  }
  public void setTemplateId(Integer templateId) {
    this.templateId = templateId;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FileTemplateDTO fileTemplateDTO = (FileTemplateDTO) o;
    return Objects.equals(this.inodePath, fileTemplateDTO.inodePath) &&
        Objects.equals(this.templateId, fileTemplateDTO.templateId);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(inodePath, templateId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FileTemplateDTO {\n");
    
    sb.append("    inodePath: ").append(toIndentedString(inodePath)).append("\n");
    sb.append("    templateId: ").append(toIndentedString(templateId)).append("\n");
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
