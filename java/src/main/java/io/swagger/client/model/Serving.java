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
import io.swagger.client.model.Project;
import io.swagger.client.model.ProjectTopics;
import io.swagger.client.model.Users;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import org.threeten.bp.OffsetDateTime;

/**
 * Serving
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class Serving {

  @SerializedName("id")
  private Integer id = null;

  @SerializedName("created")
  private OffsetDateTime created = null;

  @SerializedName("creator")
  private Users creator = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("artifactPath")
  private String artifactPath = null;

  @SerializedName("version")
  private Integer version = null;

  @SerializedName("optimized")
  private Boolean optimized = null;

  @SerializedName("instances")
  private Integer instances = null;

  @SerializedName("project")
  private Project project = null;

  @SerializedName("batchingEnabled")
  private Boolean batchingEnabled = null;

  @SerializedName("lockIP")
  private String lockIP = null;

  @SerializedName("lockTimestamp")
  private Long lockTimestamp = null;

  @SerializedName("kafkaTopic")
  private ProjectTopics kafkaTopic = null;

  @SerializedName("localPort")
  private Integer localPort = null;

  @SerializedName("localPid")
  private Integer localPid = null;

  @SerializedName("localDir")
  private String localDir = null;
  /**
   * Gets or Sets servingType
   */
  @JsonAdapter(ServingTypeEnum.Adapter.class)
  public enum ServingTypeEnum {
    TENSORFLOW("TENSORFLOW"),
    SKLEARN("SKLEARN");

    private String value;

    ServingTypeEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static ServingTypeEnum fromValue(String text) {
      for (ServingTypeEnum b : ServingTypeEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<ServingTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ServingTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ServingTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return ServingTypeEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("servingType")
  private ServingTypeEnum servingType = null;
  public Serving id(Integer id) {
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
  public Serving created(OffsetDateTime created) {
    this.created = created;
    return this;
  }

  

  /**
  * Get created
  * @return created
  **/
  @Schema(description = "")
  public OffsetDateTime getCreated() {
    return created;
  }
  public void setCreated(OffsetDateTime created) {
    this.created = created;
  }
  public Serving creator(Users creator) {
    this.creator = creator;
    return this;
  }

  

  /**
  * Get creator
  * @return creator
  **/
  @Schema(description = "")
  public Users getCreator() {
    return creator;
  }
  public void setCreator(Users creator) {
    this.creator = creator;
  }
  public Serving name(String name) {
    this.name = name;
    return this;
  }

  

  /**
  * Get name
  * @return name
  **/
  @Schema(required = true, description = "")
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public Serving artifactPath(String artifactPath) {
    this.artifactPath = artifactPath;
    return this;
  }

  

  /**
  * Get artifactPath
  * @return artifactPath
  **/
  @Schema(required = true, description = "")
  public String getArtifactPath() {
    return artifactPath;
  }
  public void setArtifactPath(String artifactPath) {
    this.artifactPath = artifactPath;
  }
  public Serving version(Integer version) {
    this.version = version;
    return this;
  }

  

  /**
  * Get version
  * @return version
  **/
  @Schema(required = true, description = "")
  public Integer getVersion() {
    return version;
  }
  public void setVersion(Integer version) {
    this.version = version;
  }
  public Serving optimized(Boolean optimized) {
    this.optimized = optimized;
    return this;
  }

  

  /**
  * Get optimized
  * @return optimized
  **/
  @Schema(required = true, description = "")
  public Boolean isOptimized() {
    return optimized;
  }
  public void setOptimized(Boolean optimized) {
    this.optimized = optimized;
  }
  public Serving instances(Integer instances) {
    this.instances = instances;
    return this;
  }

  

  /**
  * Get instances
  * @return instances
  **/
  @Schema(description = "")
  public Integer getInstances() {
    return instances;
  }
  public void setInstances(Integer instances) {
    this.instances = instances;
  }
  public Serving project(Project project) {
    this.project = project;
    return this;
  }

  

  /**
  * Get project
  * @return project
  **/
  @Schema(description = "")
  public Project getProject() {
    return project;
  }
  public void setProject(Project project) {
    this.project = project;
  }
  public Serving batchingEnabled(Boolean batchingEnabled) {
    this.batchingEnabled = batchingEnabled;
    return this;
  }

  

  /**
  * Get batchingEnabled
  * @return batchingEnabled
  **/
  @Schema(description = "")
  public Boolean isBatchingEnabled() {
    return batchingEnabled;
  }
  public void setBatchingEnabled(Boolean batchingEnabled) {
    this.batchingEnabled = batchingEnabled;
  }
  public Serving lockIP(String lockIP) {
    this.lockIP = lockIP;
    return this;
  }

  

  /**
  * Get lockIP
  * @return lockIP
  **/
  @Schema(description = "")
  public String getLockIP() {
    return lockIP;
  }
  public void setLockIP(String lockIP) {
    this.lockIP = lockIP;
  }
  public Serving lockTimestamp(Long lockTimestamp) {
    this.lockTimestamp = lockTimestamp;
    return this;
  }

  

  /**
  * Get lockTimestamp
  * @return lockTimestamp
  **/
  @Schema(description = "")
  public Long getLockTimestamp() {
    return lockTimestamp;
  }
  public void setLockTimestamp(Long lockTimestamp) {
    this.lockTimestamp = lockTimestamp;
  }
  public Serving kafkaTopic(ProjectTopics kafkaTopic) {
    this.kafkaTopic = kafkaTopic;
    return this;
  }

  

  /**
  * Get kafkaTopic
  * @return kafkaTopic
  **/
  @Schema(description = "")
  public ProjectTopics getKafkaTopic() {
    return kafkaTopic;
  }
  public void setKafkaTopic(ProjectTopics kafkaTopic) {
    this.kafkaTopic = kafkaTopic;
  }
  public Serving localPort(Integer localPort) {
    this.localPort = localPort;
    return this;
  }

  

  /**
  * Get localPort
  * @return localPort
  **/
  @Schema(description = "")
  public Integer getLocalPort() {
    return localPort;
  }
  public void setLocalPort(Integer localPort) {
    this.localPort = localPort;
  }
  public Serving localPid(Integer localPid) {
    this.localPid = localPid;
    return this;
  }

  

  /**
  * Get localPid
  * @return localPid
  **/
  @Schema(description = "")
  public Integer getLocalPid() {
    return localPid;
  }
  public void setLocalPid(Integer localPid) {
    this.localPid = localPid;
  }
  public Serving localDir(String localDir) {
    this.localDir = localDir;
    return this;
  }

  

  /**
  * Get localDir
  * @return localDir
  **/
  @Schema(description = "")
  public String getLocalDir() {
    return localDir;
  }
  public void setLocalDir(String localDir) {
    this.localDir = localDir;
  }
  public Serving servingType(ServingTypeEnum servingType) {
    this.servingType = servingType;
    return this;
  }

  

  /**
  * Get servingType
  * @return servingType
  **/
  @Schema(required = true, description = "")
  public ServingTypeEnum getServingType() {
    return servingType;
  }
  public void setServingType(ServingTypeEnum servingType) {
    this.servingType = servingType;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Serving serving = (Serving) o;
    return Objects.equals(this.id, serving.id) &&
        Objects.equals(this.created, serving.created) &&
        Objects.equals(this.creator, serving.creator) &&
        Objects.equals(this.name, serving.name) &&
        Objects.equals(this.artifactPath, serving.artifactPath) &&
        Objects.equals(this.version, serving.version) &&
        Objects.equals(this.optimized, serving.optimized) &&
        Objects.equals(this.instances, serving.instances) &&
        Objects.equals(this.project, serving.project) &&
        Objects.equals(this.batchingEnabled, serving.batchingEnabled) &&
        Objects.equals(this.lockIP, serving.lockIP) &&
        Objects.equals(this.lockTimestamp, serving.lockTimestamp) &&
        Objects.equals(this.kafkaTopic, serving.kafkaTopic) &&
        Objects.equals(this.localPort, serving.localPort) &&
        Objects.equals(this.localPid, serving.localPid) &&
        Objects.equals(this.localDir, serving.localDir) &&
        Objects.equals(this.servingType, serving.servingType);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(id, created, creator, name, artifactPath, version, optimized, instances, project, batchingEnabled, lockIP, lockTimestamp, kafkaTopic, localPort, localPid, localDir, servingType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Serving {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    creator: ").append(toIndentedString(creator)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    artifactPath: ").append(toIndentedString(artifactPath)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("    optimized: ").append(toIndentedString(optimized)).append("\n");
    sb.append("    instances: ").append(toIndentedString(instances)).append("\n");
    sb.append("    project: ").append(toIndentedString(project)).append("\n");
    sb.append("    batchingEnabled: ").append(toIndentedString(batchingEnabled)).append("\n");
    sb.append("    lockIP: ").append(toIndentedString(lockIP)).append("\n");
    sb.append("    lockTimestamp: ").append(toIndentedString(lockTimestamp)).append("\n");
    sb.append("    kafkaTopic: ").append(toIndentedString(kafkaTopic)).append("\n");
    sb.append("    localPort: ").append(toIndentedString(localPort)).append("\n");
    sb.append("    localPid: ").append(toIndentedString(localPid)).append("\n");
    sb.append("    localDir: ").append(toIndentedString(localDir)).append("\n");
    sb.append("    servingType: ").append(toIndentedString(servingType)).append("\n");
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
