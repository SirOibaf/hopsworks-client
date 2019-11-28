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
import io.swagger.client.model.LibraryDTO;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * LibraryDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class LibraryDTO {

  @SerializedName("href")
  private String href = null;

  @SerializedName("items")
  private List<LibraryDTO> items = null;

  @SerializedName("count")
  private Long count = null;

  @SerializedName("channel")
  private String channel = null;
  /**
   * Gets or Sets packageManager
   */
  @JsonAdapter(PackageManagerEnum.Adapter.class)
  public enum PackageManagerEnum {
    CONDA("CONDA"),
    PIP("PIP");

    private String value;

    PackageManagerEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static PackageManagerEnum fromValue(String text) {
      for (PackageManagerEnum b : PackageManagerEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<PackageManagerEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PackageManagerEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PackageManagerEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return PackageManagerEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("packageManager")
  private PackageManagerEnum packageManager = null;
  /**
   * Gets or Sets machine
   */
  @JsonAdapter(MachineEnum.Adapter.class)
  public enum MachineEnum {
    ALL("ALL"),
    CPU("CPU"),
    GPU("GPU");

    private String value;

    MachineEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static MachineEnum fromValue(String text) {
      for (MachineEnum b : MachineEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<MachineEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final MachineEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public MachineEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return MachineEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("machine")
  private MachineEnum machine = null;

  @SerializedName("library")
  private String library = null;

  @SerializedName("version")
  private String version = null;
  /**
   * Gets or Sets status
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    NEW("NEW"),
    SUCCESS("SUCCESS"),
    ONGOING("ONGOING"),
    FAILED("FAILED");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static StatusEnum fromValue(String text) {
      for (StatusEnum b : StatusEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return StatusEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("status")
  private StatusEnum status = null;

  @SerializedName("preinstalled")
  private String preinstalled = null;

  @SerializedName("commands")
  private CommandDTO commands = null;
  public LibraryDTO href(String href) {
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
  public LibraryDTO items(List<LibraryDTO> items) {
    this.items = items;
    return this;
  }

  public LibraryDTO addItemsItem(LibraryDTO itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<LibraryDTO>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
  * Get items
  * @return items
  **/
  @Schema(description = "")
  public List<LibraryDTO> getItems() {
    return items;
  }
  public void setItems(List<LibraryDTO> items) {
    this.items = items;
  }
  public LibraryDTO count(Long count) {
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
  public LibraryDTO channel(String channel) {
    this.channel = channel;
    return this;
  }

  

  /**
  * Get channel
  * @return channel
  **/
  @Schema(description = "")
  public String getChannel() {
    return channel;
  }
  public void setChannel(String channel) {
    this.channel = channel;
  }
  public LibraryDTO packageManager(PackageManagerEnum packageManager) {
    this.packageManager = packageManager;
    return this;
  }

  

  /**
  * Get packageManager
  * @return packageManager
  **/
  @Schema(description = "")
  public PackageManagerEnum getPackageManager() {
    return packageManager;
  }
  public void setPackageManager(PackageManagerEnum packageManager) {
    this.packageManager = packageManager;
  }
  public LibraryDTO machine(MachineEnum machine) {
    this.machine = machine;
    return this;
  }

  

  /**
  * Get machine
  * @return machine
  **/
  @Schema(description = "")
  public MachineEnum getMachine() {
    return machine;
  }
  public void setMachine(MachineEnum machine) {
    this.machine = machine;
  }
  public LibraryDTO library(String library) {
    this.library = library;
    return this;
  }

  

  /**
  * Get library
  * @return library
  **/
  @Schema(description = "")
  public String getLibrary() {
    return library;
  }
  public void setLibrary(String library) {
    this.library = library;
  }
  public LibraryDTO version(String version) {
    this.version = version;
    return this;
  }

  

  /**
  * Get version
  * @return version
  **/
  @Schema(description = "")
  public String getVersion() {
    return version;
  }
  public void setVersion(String version) {
    this.version = version;
  }
  public LibraryDTO status(StatusEnum status) {
    this.status = status;
    return this;
  }

  

  /**
  * Get status
  * @return status
  **/
  @Schema(description = "")
  public StatusEnum getStatus() {
    return status;
  }
  public void setStatus(StatusEnum status) {
    this.status = status;
  }
  public LibraryDTO preinstalled(String preinstalled) {
    this.preinstalled = preinstalled;
    return this;
  }

  

  /**
  * Get preinstalled
  * @return preinstalled
  **/
  @Schema(description = "")
  public String getPreinstalled() {
    return preinstalled;
  }
  public void setPreinstalled(String preinstalled) {
    this.preinstalled = preinstalled;
  }
  public LibraryDTO commands(CommandDTO commands) {
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
    LibraryDTO libraryDTO = (LibraryDTO) o;
    return Objects.equals(this.href, libraryDTO.href) &&
        Objects.equals(this.items, libraryDTO.items) &&
        Objects.equals(this.count, libraryDTO.count) &&
        Objects.equals(this.channel, libraryDTO.channel) &&
        Objects.equals(this.packageManager, libraryDTO.packageManager) &&
        Objects.equals(this.machine, libraryDTO.machine) &&
        Objects.equals(this.library, libraryDTO.library) &&
        Objects.equals(this.version, libraryDTO.version) &&
        Objects.equals(this.status, libraryDTO.status) &&
        Objects.equals(this.preinstalled, libraryDTO.preinstalled) &&
        Objects.equals(this.commands, libraryDTO.commands);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(href, items, count, channel, packageManager, machine, library, version, status, preinstalled, commands);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LibraryDTO {\n");
    
    sb.append("    href: ").append(toIndentedString(href)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    channel: ").append(toIndentedString(channel)).append("\n");
    sb.append("    packageManager: ").append(toIndentedString(packageManager)).append("\n");
    sb.append("    machine: ").append(toIndentedString(machine)).append("\n");
    sb.append("    library: ").append(toIndentedString(library)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    preinstalled: ").append(toIndentedString(preinstalled)).append("\n");
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
