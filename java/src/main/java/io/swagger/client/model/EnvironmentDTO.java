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
import io.swagger.client.model.CommandDTO;
import io.swagger.client.model.EnvironmentDTO;
import io.swagger.client.model.LibraryDTO;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * EnvironmentDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class EnvironmentDTO {

  @SerializedName("href")
  private String href = null;

  @SerializedName("items")
  private List<EnvironmentDTO> items = null;

  @SerializedName("count")
  private Long count = null;

  @SerializedName("pythonVersion")
  private String pythonVersion = null;

  @SerializedName("condaChannel")
  private String condaChannel = null;

  @SerializedName("libraries")
  private LibraryDTO libraries = null;

  @SerializedName("commands")
  private CommandDTO commands = null;
  public EnvironmentDTO href(String href) {
    this.href = href;
    return this;
  }

  

  /**
  * Get href
  * @return href
  **/
  @Schema(description = "")
  public String getHref() {
    return href;
  }
  public void setHref(String href) {
    this.href = href;
  }
  public EnvironmentDTO items(List<EnvironmentDTO> items) {
    this.items = items;
    return this;
  }

  public EnvironmentDTO addItemsItem(EnvironmentDTO itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<EnvironmentDTO>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
  * Get items
  * @return items
  **/
  @Schema(description = "")
  public List<EnvironmentDTO> getItems() {
    return items;
  }
  public void setItems(List<EnvironmentDTO> items) {
    this.items = items;
  }
  public EnvironmentDTO count(Long count) {
    this.count = count;
    return this;
  }

  

  /**
  * Get count
  * @return count
  **/
  @Schema(description = "")
  public Long getCount() {
    return count;
  }
  public void setCount(Long count) {
    this.count = count;
  }
  public EnvironmentDTO pythonVersion(String pythonVersion) {
    this.pythonVersion = pythonVersion;
    return this;
  }

  

  /**
  * Get pythonVersion
  * @return pythonVersion
  **/
  @Schema(description = "")
  public String getPythonVersion() {
    return pythonVersion;
  }
  public void setPythonVersion(String pythonVersion) {
    this.pythonVersion = pythonVersion;
  }
  public EnvironmentDTO condaChannel(String condaChannel) {
    this.condaChannel = condaChannel;
    return this;
  }

  

  /**
  * Get condaChannel
  * @return condaChannel
  **/
  @Schema(description = "")
  public String getCondaChannel() {
    return condaChannel;
  }
  public void setCondaChannel(String condaChannel) {
    this.condaChannel = condaChannel;
  }
  public EnvironmentDTO libraries(LibraryDTO libraries) {
    this.libraries = libraries;
    return this;
  }

  

  /**
  * Get libraries
  * @return libraries
  **/
  @Schema(description = "")
  public LibraryDTO getLibraries() {
    return libraries;
  }
  public void setLibraries(LibraryDTO libraries) {
    this.libraries = libraries;
  }
  public EnvironmentDTO commands(CommandDTO commands) {
    this.commands = commands;
    return this;
  }

  

  /**
  * Get commands
  * @return commands
  **/
  @Schema(description = "")
  public CommandDTO getCommands() {
    return commands;
  }
  public void setCommands(CommandDTO commands) {
    this.commands = commands;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EnvironmentDTO environmentDTO = (EnvironmentDTO) o;
    return Objects.equals(this.href, environmentDTO.href) &&
        Objects.equals(this.items, environmentDTO.items) &&
        Objects.equals(this.count, environmentDTO.count) &&
        Objects.equals(this.pythonVersion, environmentDTO.pythonVersion) &&
        Objects.equals(this.condaChannel, environmentDTO.condaChannel) &&
        Objects.equals(this.libraries, environmentDTO.libraries) &&
        Objects.equals(this.commands, environmentDTO.commands);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(href, items, count, pythonVersion, condaChannel, libraries, commands);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EnvironmentDTO {\n");
    
    sb.append("    href: ").append(toIndentedString(href)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    pythonVersion: ").append(toIndentedString(pythonVersion)).append("\n");
    sb.append("    condaChannel: ").append(toIndentedString(condaChannel)).append("\n");
    sb.append("    libraries: ").append(toIndentedString(libraries)).append("\n");
    sb.append("    commands: ").append(toIndentedString(commands)).append("\n");
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