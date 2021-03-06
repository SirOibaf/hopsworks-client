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
 * EnvironmentYmlDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class EnvironmentYmlDTO {

  @SerializedName("allYmlPath")
  private String allYmlPath = null;

  @SerializedName("cpuYmlPath")
  private String cpuYmlPath = null;

  @SerializedName("gpuYmlPath")
  private String gpuYmlPath = null;

  @SerializedName("installJupyter")
  private Boolean installJupyter = null;
  public EnvironmentYmlDTO allYmlPath(String allYmlPath) {
    this.allYmlPath = allYmlPath;
    return this;
  }

  

  /**
  * Path to a yml with libraries to be installed on all machine types.
  * @return allYmlPath
  **/
  @Schema(description = "Path to a yml with libraries to be installed on all machine types.")
  public String getAllYmlPath() {
    return allYmlPath;
  }
  public void setAllYmlPath(String allYmlPath) {
    this.allYmlPath = allYmlPath;
  }
  public EnvironmentYmlDTO cpuYmlPath(String cpuYmlPath) {
    this.cpuYmlPath = cpuYmlPath;
    return this;
  }

  

  /**
  * Path to a yml with libraries to be installed on CPU machines.
  * @return cpuYmlPath
  **/
  @Schema(description = "Path to a yml with libraries to be installed on CPU machines.")
  public String getCpuYmlPath() {
    return cpuYmlPath;
  }
  public void setCpuYmlPath(String cpuYmlPath) {
    this.cpuYmlPath = cpuYmlPath;
  }
  public EnvironmentYmlDTO gpuYmlPath(String gpuYmlPath) {
    this.gpuYmlPath = gpuYmlPath;
    return this;
  }

  

  /**
  * Path to a yml with libraries to be installed on GPU machines.
  * @return gpuYmlPath
  **/
  @Schema(description = "Path to a yml with libraries to be installed on GPU machines.")
  public String getGpuYmlPath() {
    return gpuYmlPath;
  }
  public void setGpuYmlPath(String gpuYmlPath) {
    this.gpuYmlPath = gpuYmlPath;
  }
  public EnvironmentYmlDTO installJupyter(Boolean installJupyter) {
    this.installJupyter = installJupyter;
    return this;
  }

  

  /**
  * Install Jupyter in the environment.
  * @return installJupyter
  **/
  @Schema(description = "Install Jupyter in the environment.")
  public Boolean isInstallJupyter() {
    return installJupyter;
  }
  public void setInstallJupyter(Boolean installJupyter) {
    this.installJupyter = installJupyter;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EnvironmentYmlDTO environmentYmlDTO = (EnvironmentYmlDTO) o;
    return Objects.equals(this.allYmlPath, environmentYmlDTO.allYmlPath) &&
        Objects.equals(this.cpuYmlPath, environmentYmlDTO.cpuYmlPath) &&
        Objects.equals(this.gpuYmlPath, environmentYmlDTO.gpuYmlPath) &&
        Objects.equals(this.installJupyter, environmentYmlDTO.installJupyter);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(allYmlPath, cpuYmlPath, gpuYmlPath, installJupyter);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EnvironmentYmlDTO {\n");
    
    sb.append("    allYmlPath: ").append(toIndentedString(allYmlPath)).append("\n");
    sb.append("    cpuYmlPath: ").append(toIndentedString(cpuYmlPath)).append("\n");
    sb.append("    gpuYmlPath: ").append(toIndentedString(gpuYmlPath)).append("\n");
    sb.append("    installJupyter: ").append(toIndentedString(installJupyter)).append("\n");
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
