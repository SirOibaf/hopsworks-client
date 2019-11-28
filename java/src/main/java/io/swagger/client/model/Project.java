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
import io.swagger.client.model.Activity;
import io.swagger.client.model.CondaCommands;
import io.swagger.client.model.Dataset;
import io.swagger.client.model.Inode;
import io.swagger.client.model.JupyterProject;
import io.swagger.client.model.JupyterSettings;
import io.swagger.client.model.ProjectServices;
import io.swagger.client.model.ProjectTeam;
import io.swagger.client.model.PythonDep;
import io.swagger.client.model.Serving;
import io.swagger.client.model.TensorBoard;
import io.swagger.client.model.Users;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.threeten.bp.OffsetDateTime;

/**
 * Project
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class Project {

  @SerializedName("conda")
  private Boolean conda = null;

  @SerializedName("archived")
  private Boolean archived = null;

  @SerializedName("logs")
  private Boolean logs = null;

  @SerializedName("condaEnv")
  private Boolean condaEnv = null;

  @SerializedName("projectTeamCollection")
  private List<ProjectTeam> projectTeamCollection = null;

  @SerializedName("activityCollection")
  private List<Activity> activityCollection = null;

  @SerializedName("projectServicesCollection")
  private List<ProjectServices> projectServicesCollection = null;

  @SerializedName("datasetCollection")
  private List<Dataset> datasetCollection = null;

  @SerializedName("condaCommandsCollection")
  private List<CondaCommands> condaCommandsCollection = null;

  @SerializedName("jupyterSettingsCollection")
  private List<JupyterSettings> jupyterSettingsCollection = null;

  @SerializedName("servingCollection")
  private List<Serving> servingCollection = null;

  @SerializedName("tensorBoardCollection")
  private List<TensorBoard> tensorBoardCollection = null;

  @SerializedName("id")
  private Integer id = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("owner")
  private Users owner = null;

  @SerializedName("created")
  private OffsetDateTime created = null;

  @SerializedName("retentionPeriod")
  private OffsetDateTime retentionPeriod = null;

  @SerializedName("deleted")
  private Boolean deleted = null;
  /**
   * Gets or Sets paymentType
   */
  @JsonAdapter(PaymentTypeEnum.Adapter.class)
  public enum PaymentTypeEnum {
    PREPAID("PREPAID"),
    NOLIMIT("NOLIMIT");

    private String value;

    PaymentTypeEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static PaymentTypeEnum fromValue(String text) {
      for (PaymentTypeEnum b : PaymentTypeEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<PaymentTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PaymentTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PaymentTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return PaymentTypeEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("paymentType")
  private PaymentTypeEnum paymentType = null;

  @SerializedName("pythonVersion")
  private String pythonVersion = null;

  @SerializedName("description")
  private String description = null;

  @SerializedName("kafkaMaxNumTopics")
  private Integer kafkaMaxNumTopics = null;

  @SerializedName("lastQuotaUpdate")
  private OffsetDateTime lastQuotaUpdate = null;

  @SerializedName("inode")
  private Inode inode = null;

  @SerializedName("pythonDepCollection")
  private List<PythonDep> pythonDepCollection = null;

  @SerializedName("jupyterProjectCollection")
  private List<JupyterProject> jupyterProjectCollection = null;

  @SerializedName("paymentTypeString")
  private String paymentTypeString = null;
  public Project conda(Boolean conda) {
    this.conda = conda;
    return this;
  }

  

  /**
  * Get conda
  * @return conda
  **/
  @Schema(description = "")
  public Boolean isConda() {
    return conda;
  }
  public void setConda(Boolean conda) {
    this.conda = conda;
  }
  public Project archived(Boolean archived) {
    this.archived = archived;
    return this;
  }

  

  /**
  * Get archived
  * @return archived
  **/
  @Schema(description = "")
  public Boolean isArchived() {
    return archived;
  }
  public void setArchived(Boolean archived) {
    this.archived = archived;
  }
  public Project logs(Boolean logs) {
    this.logs = logs;
    return this;
  }

  

  /**
  * Get logs
  * @return logs
  **/
  @Schema(description = "")
  public Boolean isLogs() {
    return logs;
  }
  public void setLogs(Boolean logs) {
    this.logs = logs;
  }
  public Project condaEnv(Boolean condaEnv) {
    this.condaEnv = condaEnv;
    return this;
  }

  

  /**
  * Get condaEnv
  * @return condaEnv
  **/
  @Schema(description = "")
  public Boolean isCondaEnv() {
    return condaEnv;
  }
  public void setCondaEnv(Boolean condaEnv) {
    this.condaEnv = condaEnv;
  }
  public Project projectTeamCollection(List<ProjectTeam> projectTeamCollection) {
    this.projectTeamCollection = projectTeamCollection;
    return this;
  }

  public Project addProjectTeamCollectionItem(ProjectTeam projectTeamCollectionItem) {
    if (this.projectTeamCollection == null) {
      this.projectTeamCollection = new ArrayList<ProjectTeam>();
    }
    this.projectTeamCollection.add(projectTeamCollectionItem);
    return this;
  }

  /**
  * Get projectTeamCollection
  * @return projectTeamCollection
  **/
  @Schema(description = "")
  public List<ProjectTeam> getProjectTeamCollection() {
    return projectTeamCollection;
  }
  public void setProjectTeamCollection(List<ProjectTeam> projectTeamCollection) {
    this.projectTeamCollection = projectTeamCollection;
  }
  public Project activityCollection(List<Activity> activityCollection) {
    this.activityCollection = activityCollection;
    return this;
  }

  public Project addActivityCollectionItem(Activity activityCollectionItem) {
    if (this.activityCollection == null) {
      this.activityCollection = new ArrayList<Activity>();
    }
    this.activityCollection.add(activityCollectionItem);
    return this;
  }

  /**
  * Get activityCollection
  * @return activityCollection
  **/
  @Schema(description = "")
  public List<Activity> getActivityCollection() {
    return activityCollection;
  }
  public void setActivityCollection(List<Activity> activityCollection) {
    this.activityCollection = activityCollection;
  }
  public Project projectServicesCollection(List<ProjectServices> projectServicesCollection) {
    this.projectServicesCollection = projectServicesCollection;
    return this;
  }

  public Project addProjectServicesCollectionItem(ProjectServices projectServicesCollectionItem) {
    if (this.projectServicesCollection == null) {
      this.projectServicesCollection = new ArrayList<ProjectServices>();
    }
    this.projectServicesCollection.add(projectServicesCollectionItem);
    return this;
  }

  /**
  * Get projectServicesCollection
  * @return projectServicesCollection
  **/
  @Schema(description = "")
  public List<ProjectServices> getProjectServicesCollection() {
    return projectServicesCollection;
  }
  public void setProjectServicesCollection(List<ProjectServices> projectServicesCollection) {
    this.projectServicesCollection = projectServicesCollection;
  }
  public Project datasetCollection(List<Dataset> datasetCollection) {
    this.datasetCollection = datasetCollection;
    return this;
  }

  public Project addDatasetCollectionItem(Dataset datasetCollectionItem) {
    if (this.datasetCollection == null) {
      this.datasetCollection = new ArrayList<Dataset>();
    }
    this.datasetCollection.add(datasetCollectionItem);
    return this;
  }

  /**
  * Get datasetCollection
  * @return datasetCollection
  **/
  @Schema(description = "")
  public List<Dataset> getDatasetCollection() {
    return datasetCollection;
  }
  public void setDatasetCollection(List<Dataset> datasetCollection) {
    this.datasetCollection = datasetCollection;
  }
  public Project condaCommandsCollection(List<CondaCommands> condaCommandsCollection) {
    this.condaCommandsCollection = condaCommandsCollection;
    return this;
  }

  public Project addCondaCommandsCollectionItem(CondaCommands condaCommandsCollectionItem) {
    if (this.condaCommandsCollection == null) {
      this.condaCommandsCollection = new ArrayList<CondaCommands>();
    }
    this.condaCommandsCollection.add(condaCommandsCollectionItem);
    return this;
  }

  /**
  * Get condaCommandsCollection
  * @return condaCommandsCollection
  **/
  @Schema(description = "")
  public List<CondaCommands> getCondaCommandsCollection() {
    return condaCommandsCollection;
  }
  public void setCondaCommandsCollection(List<CondaCommands> condaCommandsCollection) {
    this.condaCommandsCollection = condaCommandsCollection;
  }
  public Project jupyterSettingsCollection(List<JupyterSettings> jupyterSettingsCollection) {
    this.jupyterSettingsCollection = jupyterSettingsCollection;
    return this;
  }

  public Project addJupyterSettingsCollectionItem(JupyterSettings jupyterSettingsCollectionItem) {
    if (this.jupyterSettingsCollection == null) {
      this.jupyterSettingsCollection = new ArrayList<JupyterSettings>();
    }
    this.jupyterSettingsCollection.add(jupyterSettingsCollectionItem);
    return this;
  }

  /**
  * Get jupyterSettingsCollection
  * @return jupyterSettingsCollection
  **/
  @Schema(description = "")
  public List<JupyterSettings> getJupyterSettingsCollection() {
    return jupyterSettingsCollection;
  }
  public void setJupyterSettingsCollection(List<JupyterSettings> jupyterSettingsCollection) {
    this.jupyterSettingsCollection = jupyterSettingsCollection;
  }
  public Project servingCollection(List<Serving> servingCollection) {
    this.servingCollection = servingCollection;
    return this;
  }

  public Project addServingCollectionItem(Serving servingCollectionItem) {
    if (this.servingCollection == null) {
      this.servingCollection = new ArrayList<Serving>();
    }
    this.servingCollection.add(servingCollectionItem);
    return this;
  }

  /**
  * Get servingCollection
  * @return servingCollection
  **/
  @Schema(description = "")
  public List<Serving> getServingCollection() {
    return servingCollection;
  }
  public void setServingCollection(List<Serving> servingCollection) {
    this.servingCollection = servingCollection;
  }
  public Project tensorBoardCollection(List<TensorBoard> tensorBoardCollection) {
    this.tensorBoardCollection = tensorBoardCollection;
    return this;
  }

  public Project addTensorBoardCollectionItem(TensorBoard tensorBoardCollectionItem) {
    if (this.tensorBoardCollection == null) {
      this.tensorBoardCollection = new ArrayList<TensorBoard>();
    }
    this.tensorBoardCollection.add(tensorBoardCollectionItem);
    return this;
  }

  /**
  * Get tensorBoardCollection
  * @return tensorBoardCollection
  **/
  @Schema(description = "")
  public List<TensorBoard> getTensorBoardCollection() {
    return tensorBoardCollection;
  }
  public void setTensorBoardCollection(List<TensorBoard> tensorBoardCollection) {
    this.tensorBoardCollection = tensorBoardCollection;
  }
  public Project id(Integer id) {
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
  public Project name(String name) {
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
  public Project owner(Users owner) {
    this.owner = owner;
    return this;
  }

  

  /**
  * Get owner
  * @return owner
  **/
  @Schema(description = "")
  public Users getOwner() {
    return owner;
  }
  public void setOwner(Users owner) {
    this.owner = owner;
  }
  public Project created(OffsetDateTime created) {
    this.created = created;
    return this;
  }

  

  /**
  * Get created
  * @return created
  **/
  @Schema(required = true, description = "")
  public OffsetDateTime getCreated() {
    return created;
  }
  public void setCreated(OffsetDateTime created) {
    this.created = created;
  }
  public Project retentionPeriod(OffsetDateTime retentionPeriod) {
    this.retentionPeriod = retentionPeriod;
    return this;
  }

  

  /**
  * Get retentionPeriod
  * @return retentionPeriod
  **/
  @Schema(description = "")
  public OffsetDateTime getRetentionPeriod() {
    return retentionPeriod;
  }
  public void setRetentionPeriod(OffsetDateTime retentionPeriod) {
    this.retentionPeriod = retentionPeriod;
  }
  public Project deleted(Boolean deleted) {
    this.deleted = deleted;
    return this;
  }

  

  /**
  * Get deleted
  * @return deleted
  **/
  @Schema(description = "")
  public Boolean isDeleted() {
    return deleted;
  }
  public void setDeleted(Boolean deleted) {
    this.deleted = deleted;
  }
  public Project paymentType(PaymentTypeEnum paymentType) {
    this.paymentType = paymentType;
    return this;
  }

  

  /**
  * Get paymentType
  * @return paymentType
  **/
  @Schema(required = true, description = "")
  public PaymentTypeEnum getPaymentType() {
    return paymentType;
  }
  public void setPaymentType(PaymentTypeEnum paymentType) {
    this.paymentType = paymentType;
  }
  public Project pythonVersion(String pythonVersion) {
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
  public Project description(String description) {
    this.description = description;
    return this;
  }

  

  /**
  * Get description
  * @return description
  **/
  @Schema(description = "")
  public String getDescription() {
    return description;
  }
  public void setDescription(String description) {
    this.description = description;
  }
  public Project kafkaMaxNumTopics(Integer kafkaMaxNumTopics) {
    this.kafkaMaxNumTopics = kafkaMaxNumTopics;
    return this;
  }

  

  /**
  * Get kafkaMaxNumTopics
  * @return kafkaMaxNumTopics
  **/
  @Schema(required = true, description = "")
  public Integer getKafkaMaxNumTopics() {
    return kafkaMaxNumTopics;
  }
  public void setKafkaMaxNumTopics(Integer kafkaMaxNumTopics) {
    this.kafkaMaxNumTopics = kafkaMaxNumTopics;
  }
  public Project lastQuotaUpdate(OffsetDateTime lastQuotaUpdate) {
    this.lastQuotaUpdate = lastQuotaUpdate;
    return this;
  }

  

  /**
  * Get lastQuotaUpdate
  * @return lastQuotaUpdate
  **/
  @Schema(required = true, description = "")
  public OffsetDateTime getLastQuotaUpdate() {
    return lastQuotaUpdate;
  }
  public void setLastQuotaUpdate(OffsetDateTime lastQuotaUpdate) {
    this.lastQuotaUpdate = lastQuotaUpdate;
  }
  public Project inode(Inode inode) {
    this.inode = inode;
    return this;
  }

  

  /**
  * Get inode
  * @return inode
  **/
  @Schema(description = "")
  public Inode getInode() {
    return inode;
  }
  public void setInode(Inode inode) {
    this.inode = inode;
  }
  public Project pythonDepCollection(List<PythonDep> pythonDepCollection) {
    this.pythonDepCollection = pythonDepCollection;
    return this;
  }

  public Project addPythonDepCollectionItem(PythonDep pythonDepCollectionItem) {
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
  public Project jupyterProjectCollection(List<JupyterProject> jupyterProjectCollection) {
    this.jupyterProjectCollection = jupyterProjectCollection;
    return this;
  }

  public Project addJupyterProjectCollectionItem(JupyterProject jupyterProjectCollectionItem) {
    if (this.jupyterProjectCollection == null) {
      this.jupyterProjectCollection = new ArrayList<JupyterProject>();
    }
    this.jupyterProjectCollection.add(jupyterProjectCollectionItem);
    return this;
  }

  /**
  * Get jupyterProjectCollection
  * @return jupyterProjectCollection
  **/
  @Schema(description = "")
  public List<JupyterProject> getJupyterProjectCollection() {
    return jupyterProjectCollection;
  }
  public void setJupyterProjectCollection(List<JupyterProject> jupyterProjectCollection) {
    this.jupyterProjectCollection = jupyterProjectCollection;
  }
  public Project paymentTypeString(String paymentTypeString) {
    this.paymentTypeString = paymentTypeString;
    return this;
  }

  

  /**
  * Get paymentTypeString
  * @return paymentTypeString
  **/
  @Schema(description = "")
  public String getPaymentTypeString() {
    return paymentTypeString;
  }
  public void setPaymentTypeString(String paymentTypeString) {
    this.paymentTypeString = paymentTypeString;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Project project = (Project) o;
    return Objects.equals(this.conda, project.conda) &&
        Objects.equals(this.archived, project.archived) &&
        Objects.equals(this.logs, project.logs) &&
        Objects.equals(this.condaEnv, project.condaEnv) &&
        Objects.equals(this.projectTeamCollection, project.projectTeamCollection) &&
        Objects.equals(this.activityCollection, project.activityCollection) &&
        Objects.equals(this.projectServicesCollection, project.projectServicesCollection) &&
        Objects.equals(this.datasetCollection, project.datasetCollection) &&
        Objects.equals(this.condaCommandsCollection, project.condaCommandsCollection) &&
        Objects.equals(this.jupyterSettingsCollection, project.jupyterSettingsCollection) &&
        Objects.equals(this.servingCollection, project.servingCollection) &&
        Objects.equals(this.tensorBoardCollection, project.tensorBoardCollection) &&
        Objects.equals(this.id, project.id) &&
        Objects.equals(this.name, project.name) &&
        Objects.equals(this.owner, project.owner) &&
        Objects.equals(this.created, project.created) &&
        Objects.equals(this.retentionPeriod, project.retentionPeriod) &&
        Objects.equals(this.deleted, project.deleted) &&
        Objects.equals(this.paymentType, project.paymentType) &&
        Objects.equals(this.pythonVersion, project.pythonVersion) &&
        Objects.equals(this.description, project.description) &&
        Objects.equals(this.kafkaMaxNumTopics, project.kafkaMaxNumTopics) &&
        Objects.equals(this.lastQuotaUpdate, project.lastQuotaUpdate) &&
        Objects.equals(this.inode, project.inode) &&
        Objects.equals(this.pythonDepCollection, project.pythonDepCollection) &&
        Objects.equals(this.jupyterProjectCollection, project.jupyterProjectCollection) &&
        Objects.equals(this.paymentTypeString, project.paymentTypeString);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(conda, archived, logs, condaEnv, projectTeamCollection, activityCollection, projectServicesCollection, datasetCollection, condaCommandsCollection, jupyterSettingsCollection, servingCollection, tensorBoardCollection, id, name, owner, created, retentionPeriod, deleted, paymentType, pythonVersion, description, kafkaMaxNumTopics, lastQuotaUpdate, inode, pythonDepCollection, jupyterProjectCollection, paymentTypeString);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Project {\n");
    
    sb.append("    conda: ").append(toIndentedString(conda)).append("\n");
    sb.append("    archived: ").append(toIndentedString(archived)).append("\n");
    sb.append("    logs: ").append(toIndentedString(logs)).append("\n");
    sb.append("    condaEnv: ").append(toIndentedString(condaEnv)).append("\n");
    sb.append("    projectTeamCollection: ").append(toIndentedString(projectTeamCollection)).append("\n");
    sb.append("    activityCollection: ").append(toIndentedString(activityCollection)).append("\n");
    sb.append("    projectServicesCollection: ").append(toIndentedString(projectServicesCollection)).append("\n");
    sb.append("    datasetCollection: ").append(toIndentedString(datasetCollection)).append("\n");
    sb.append("    condaCommandsCollection: ").append(toIndentedString(condaCommandsCollection)).append("\n");
    sb.append("    jupyterSettingsCollection: ").append(toIndentedString(jupyterSettingsCollection)).append("\n");
    sb.append("    servingCollection: ").append(toIndentedString(servingCollection)).append("\n");
    sb.append("    tensorBoardCollection: ").append(toIndentedString(tensorBoardCollection)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    owner: ").append(toIndentedString(owner)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    retentionPeriod: ").append(toIndentedString(retentionPeriod)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    paymentType: ").append(toIndentedString(paymentType)).append("\n");
    sb.append("    pythonVersion: ").append(toIndentedString(pythonVersion)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    kafkaMaxNumTopics: ").append(toIndentedString(kafkaMaxNumTopics)).append("\n");
    sb.append("    lastQuotaUpdate: ").append(toIndentedString(lastQuotaUpdate)).append("\n");
    sb.append("    inode: ").append(toIndentedString(inode)).append("\n");
    sb.append("    pythonDepCollection: ").append(toIndentedString(pythonDepCollection)).append("\n");
    sb.append("    jupyterProjectCollection: ").append(toIndentedString(jupyterProjectCollection)).append("\n");
    sb.append("    paymentTypeString: ").append(toIndentedString(paymentTypeString)).append("\n");
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