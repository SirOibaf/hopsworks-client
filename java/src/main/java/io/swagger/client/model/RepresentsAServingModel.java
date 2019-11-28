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
import io.swagger.client.model.TopicDTO;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import org.threeten.bp.OffsetDateTime;

/**
 * RepresentsAServingModel
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class RepresentsAServingModel {

  @SerializedName("id")
  private Integer id = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("artifactPath")
  private String artifactPath = null;

  @SerializedName("modelVersion")
  private Integer modelVersion = null;

  @SerializedName("availableInstances")
  private Integer availableInstances = null;

  @SerializedName("requestedInstances")
  private Integer requestedInstances = null;

  @SerializedName("nodePort")
  private Integer nodePort = null;

  @SerializedName("created")
  private OffsetDateTime created = null;

  @SerializedName("batchingEnabled")
  private Boolean batchingEnabled = null;
  /**
   * Type of serving, sklearn or tfserving
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

  @SerializedName("creator")
  private String creator = null;
  /**
   * Status of the Serving entry
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    RUNNING("RUNNING"),
    STOPPED("STOPPED"),
    STARTING("STARTING"),
    UPDATING("UPDATING"),
    STOPPING("STOPPING"),
    TRANSFORMING("TRANSFORMING");

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

  @SerializedName("kafkaTopicDTO")
  private TopicDTO kafkaTopicDTO = null;
  public RepresentsAServingModel id(Integer id) {
    this.id = id;
    return this;
  }

  

  /**
  * ID of the Serving entry
  * @return id
  **/
  @Schema(description = "ID of the Serving entry")
  public Integer getId() {
    return id;
  }
  public void setId(Integer id) {
    this.id = id;
  }
  public RepresentsAServingModel name(String name) {
    this.name = name;
    return this;
  }

  

  /**
  * Name of the serving
  * @return name
  **/
  @Schema(description = "Name of the serving")
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public RepresentsAServingModel artifactPath(String artifactPath) {
    this.artifactPath = artifactPath;
    return this;
  }

  

  /**
  * HOPSFS directory path containing the model (tf) or python script (sklearn)
  * @return artifactPath
  **/
  @Schema(description = "HOPSFS directory path containing the model (tf) or python script (sklearn)")
  public String getArtifactPath() {
    return artifactPath;
  }
  public void setArtifactPath(String artifactPath) {
    this.artifactPath = artifactPath;
  }
  public RepresentsAServingModel modelVersion(Integer modelVersion) {
    this.modelVersion = modelVersion;
    return this;
  }

  

  /**
  * Version of the serving
  * @return modelVersion
  **/
  @Schema(description = "Version of the serving")
  public Integer getModelVersion() {
    return modelVersion;
  }
  public void setModelVersion(Integer modelVersion) {
    this.modelVersion = modelVersion;
  }
  /**
  * Number of Serving instances available for serving
  * @return availableInstances
  **/
  @Schema(description = "Number of Serving instances available for serving")
  public Integer getAvailableInstances() {
    return availableInstances;
  }
  public RepresentsAServingModel requestedInstances(Integer requestedInstances) {
    this.requestedInstances = requestedInstances;
    return this;
  }

  

  /**
  * Number of Serving instances to use for serving
  * @return requestedInstances
  **/
  @Schema(description = "Number of Serving instances to use for serving")
  public Integer getRequestedInstances() {
    return requestedInstances;
  }
  public void setRequestedInstances(Integer requestedInstances) {
    this.requestedInstances = requestedInstances;
  }
  /**
  * Port on which the Serving instance(s) are listening
  * @return nodePort
  **/
  @Schema(description = "Port on which the Serving instance(s) are listening")
  public Integer getNodePort() {
    return nodePort;
  }
  /**
  * Date on which the Serving entry was created
  * @return created
  **/
  @Schema(description = "Date on which the Serving entry was created")
  public OffsetDateTime getCreated() {
    return created;
  }
  public RepresentsAServingModel batchingEnabled(Boolean batchingEnabled) {
    this.batchingEnabled = batchingEnabled;
    return this;
  }

  

  /**
  * Is request batching enabled
  * @return batchingEnabled
  **/
  @Schema(description = "Is request batching enabled")
  public Boolean isBatchingEnabled() {
    return batchingEnabled;
  }
  public void setBatchingEnabled(Boolean batchingEnabled) {
    this.batchingEnabled = batchingEnabled;
  }
  public RepresentsAServingModel servingType(ServingTypeEnum servingType) {
    this.servingType = servingType;
    return this;
  }

  

  /**
  * Type of serving, sklearn or tfserving
  * @return servingType
  **/
  @Schema(description = "Type of serving, sklearn or tfserving")
  public ServingTypeEnum getServingType() {
    return servingType;
  }
  public void setServingType(ServingTypeEnum servingType) {
    this.servingType = servingType;
  }
  /**
  * User whom created the Serving entry
  * @return creator
  **/
  @Schema(description = "User whom created the Serving entry")
  public String getCreator() {
    return creator;
  }
  /**
  * Status of the Serving entry
  * @return status
  **/
  @Schema(description = "Status of the Serving entry")
  public StatusEnum getStatus() {
    return status;
  }
  public RepresentsAServingModel kafkaTopicDTO(TopicDTO kafkaTopicDTO) {
    this.kafkaTopicDTO = kafkaTopicDTO;
    return this;
  }

  

  /**
  * Get kafkaTopicDTO
  * @return kafkaTopicDTO
  **/
  @Schema(description = "")
  public TopicDTO getKafkaTopicDTO() {
    return kafkaTopicDTO;
  }
  public void setKafkaTopicDTO(TopicDTO kafkaTopicDTO) {
    this.kafkaTopicDTO = kafkaTopicDTO;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RepresentsAServingModel representsAServingModel = (RepresentsAServingModel) o;
    return Objects.equals(this.id, representsAServingModel.id) &&
        Objects.equals(this.name, representsAServingModel.name) &&
        Objects.equals(this.artifactPath, representsAServingModel.artifactPath) &&
        Objects.equals(this.modelVersion, representsAServingModel.modelVersion) &&
        Objects.equals(this.availableInstances, representsAServingModel.availableInstances) &&
        Objects.equals(this.requestedInstances, representsAServingModel.requestedInstances) &&
        Objects.equals(this.nodePort, representsAServingModel.nodePort) &&
        Objects.equals(this.created, representsAServingModel.created) &&
        Objects.equals(this.batchingEnabled, representsAServingModel.batchingEnabled) &&
        Objects.equals(this.servingType, representsAServingModel.servingType) &&
        Objects.equals(this.creator, representsAServingModel.creator) &&
        Objects.equals(this.status, representsAServingModel.status) &&
        Objects.equals(this.kafkaTopicDTO, representsAServingModel.kafkaTopicDTO);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(id, name, artifactPath, modelVersion, availableInstances, requestedInstances, nodePort, created, batchingEnabled, servingType, creator, status, kafkaTopicDTO);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RepresentsAServingModel {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    artifactPath: ").append(toIndentedString(artifactPath)).append("\n");
    sb.append("    modelVersion: ").append(toIndentedString(modelVersion)).append("\n");
    sb.append("    availableInstances: ").append(toIndentedString(availableInstances)).append("\n");
    sb.append("    requestedInstances: ").append(toIndentedString(requestedInstances)).append("\n");
    sb.append("    nodePort: ").append(toIndentedString(nodePort)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    batchingEnabled: ").append(toIndentedString(batchingEnabled)).append("\n");
    sb.append("    servingType: ").append(toIndentedString(servingType)).append("\n");
    sb.append("    creator: ").append(toIndentedString(creator)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    kafkaTopicDTO: ").append(toIndentedString(kafkaTopicDTO)).append("\n");
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
