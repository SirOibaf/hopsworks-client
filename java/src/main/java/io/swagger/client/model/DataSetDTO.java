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
import io.swagger.client.model.UserCardDTO;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * DataSetDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class DataSetDTO {

  @SerializedName("inodeId")
  private Long inodeId = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("description")
  private String description = null;

  @SerializedName("isPublic")
  private Boolean isPublic = null;

  @SerializedName("searchable")
  private Boolean searchable = null;

  @SerializedName("generateReadme")
  private Boolean generateReadme = null;
  /**
   * Gets or Sets permissions
   */
  @JsonAdapter(PermissionsEnum.Adapter.class)
  public enum PermissionsEnum {
    GROUP_WRITABLE_SB("GROUP_WRITABLE_SB"),
    GROUP_WRITABLE("GROUP_WRITABLE"),
    OWNER_ONLY("OWNER_ONLY");

    private String value;

    PermissionsEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static PermissionsEnum fromValue(String text) {
      for (PermissionsEnum b : PermissionsEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<PermissionsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PermissionsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PermissionsEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return PermissionsEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("permissions")
  private PermissionsEnum permissions = null;

  @SerializedName("template")
  private Integer template = null;

  @SerializedName("projectId")
  private Integer projectId = null;

  @SerializedName("projectIds")
  private List<Integer> projectIds = null;

  @SerializedName("projectName")
  private String projectName = null;

  @SerializedName("templateName")
  private String templateName = null;

  @SerializedName("projectTeam")
  private List<UserCardDTO> projectTeam = null;

  @SerializedName("sharedWith")
  private List<String> sharedWith = null;
  /**
   * Gets or Sets type
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    DATASET("DATASET"),
    HIVEDB("HIVEDB"),
    FEATURESTORE("FEATURESTORE");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static TypeEnum fromValue(String text) {
      for (TypeEnum b : TypeEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return TypeEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("type")
  private TypeEnum type = null;

  @SerializedName("members")
  private List<UserCardDTO> members = null;
  public DataSetDTO inodeId(Long inodeId) {
    this.inodeId = inodeId;
    return this;
  }

  

  /**
  * Get inodeId
  * @return inodeId
  **/
  @Schema(description = "")
  public Long getInodeId() {
    return inodeId;
  }
  public void setInodeId(Long inodeId) {
    this.inodeId = inodeId;
  }
  public DataSetDTO name(String name) {
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
  public DataSetDTO description(String description) {
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
  public DataSetDTO isPublic(Boolean isPublic) {
    this.isPublic = isPublic;
    return this;
  }

  

  /**
  * Get isPublic
  * @return isPublic
  **/
  @Schema(description = "")
  public Boolean isIsPublic() {
    return isPublic;
  }
  public void setIsPublic(Boolean isPublic) {
    this.isPublic = isPublic;
  }
  public DataSetDTO searchable(Boolean searchable) {
    this.searchable = searchable;
    return this;
  }

  

  /**
  * Get searchable
  * @return searchable
  **/
  @Schema(description = "")
  public Boolean isSearchable() {
    return searchable;
  }
  public void setSearchable(Boolean searchable) {
    this.searchable = searchable;
  }
  public DataSetDTO generateReadme(Boolean generateReadme) {
    this.generateReadme = generateReadme;
    return this;
  }

  

  /**
  * Get generateReadme
  * @return generateReadme
  **/
  @Schema(description = "")
  public Boolean isGenerateReadme() {
    return generateReadme;
  }
  public void setGenerateReadme(Boolean generateReadme) {
    this.generateReadme = generateReadme;
  }
  public DataSetDTO permissions(PermissionsEnum permissions) {
    this.permissions = permissions;
    return this;
  }

  

  /**
  * Get permissions
  * @return permissions
  **/
  @Schema(description = "")
  public PermissionsEnum getPermissions() {
    return permissions;
  }
  public void setPermissions(PermissionsEnum permissions) {
    this.permissions = permissions;
  }
  public DataSetDTO template(Integer template) {
    this.template = template;
    return this;
  }

  

  /**
  * Get template
  * @return template
  **/
  @Schema(description = "")
  public Integer getTemplate() {
    return template;
  }
  public void setTemplate(Integer template) {
    this.template = template;
  }
  public DataSetDTO projectId(Integer projectId) {
    this.projectId = projectId;
    return this;
  }

  

  /**
  * Get projectId
  * @return projectId
  **/
  @Schema(description = "")
  public Integer getProjectId() {
    return projectId;
  }
  public void setProjectId(Integer projectId) {
    this.projectId = projectId;
  }
  public DataSetDTO projectIds(List<Integer> projectIds) {
    this.projectIds = projectIds;
    return this;
  }

  public DataSetDTO addProjectIdsItem(Integer projectIdsItem) {
    if (this.projectIds == null) {
      this.projectIds = new ArrayList<Integer>();
    }
    this.projectIds.add(projectIdsItem);
    return this;
  }

  /**
  * Get projectIds
  * @return projectIds
  **/
  @Schema(description = "")
  public List<Integer> getProjectIds() {
    return projectIds;
  }
  public void setProjectIds(List<Integer> projectIds) {
    this.projectIds = projectIds;
  }
  public DataSetDTO projectName(String projectName) {
    this.projectName = projectName;
    return this;
  }

  

  /**
  * Get projectName
  * @return projectName
  **/
  @Schema(description = "")
  public String getProjectName() {
    return projectName;
  }
  public void setProjectName(String projectName) {
    this.projectName = projectName;
  }
  public DataSetDTO templateName(String templateName) {
    this.templateName = templateName;
    return this;
  }

  

  /**
  * Get templateName
  * @return templateName
  **/
  @Schema(description = "")
  public String getTemplateName() {
    return templateName;
  }
  public void setTemplateName(String templateName) {
    this.templateName = templateName;
  }
  public DataSetDTO projectTeam(List<UserCardDTO> projectTeam) {
    this.projectTeam = projectTeam;
    return this;
  }

  public DataSetDTO addProjectTeamItem(UserCardDTO projectTeamItem) {
    if (this.projectTeam == null) {
      this.projectTeam = new ArrayList<UserCardDTO>();
    }
    this.projectTeam.add(projectTeamItem);
    return this;
  }

  /**
  * Get projectTeam
  * @return projectTeam
  **/
  @Schema(description = "")
  public List<UserCardDTO> getProjectTeam() {
    return projectTeam;
  }
  public void setProjectTeam(List<UserCardDTO> projectTeam) {
    this.projectTeam = projectTeam;
  }
  public DataSetDTO sharedWith(List<String> sharedWith) {
    this.sharedWith = sharedWith;
    return this;
  }

  public DataSetDTO addSharedWithItem(String sharedWithItem) {
    if (this.sharedWith == null) {
      this.sharedWith = new ArrayList<String>();
    }
    this.sharedWith.add(sharedWithItem);
    return this;
  }

  /**
  * Get sharedWith
  * @return sharedWith
  **/
  @Schema(description = "")
  public List<String> getSharedWith() {
    return sharedWith;
  }
  public void setSharedWith(List<String> sharedWith) {
    this.sharedWith = sharedWith;
  }
  public DataSetDTO type(TypeEnum type) {
    this.type = type;
    return this;
  }

  

  /**
  * Get type
  * @return type
  **/
  @Schema(description = "")
  public TypeEnum getType() {
    return type;
  }
  public void setType(TypeEnum type) {
    this.type = type;
  }
  public DataSetDTO members(List<UserCardDTO> members) {
    this.members = members;
    return this;
  }

  public DataSetDTO addMembersItem(UserCardDTO membersItem) {
    if (this.members == null) {
      this.members = new ArrayList<UserCardDTO>();
    }
    this.members.add(membersItem);
    return this;
  }

  /**
  * Get members
  * @return members
  **/
  @Schema(description = "")
  public List<UserCardDTO> getMembers() {
    return members;
  }
  public void setMembers(List<UserCardDTO> members) {
    this.members = members;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DataSetDTO dataSetDTO = (DataSetDTO) o;
    return Objects.equals(this.inodeId, dataSetDTO.inodeId) &&
        Objects.equals(this.name, dataSetDTO.name) &&
        Objects.equals(this.description, dataSetDTO.description) &&
        Objects.equals(this.isPublic, dataSetDTO.isPublic) &&
        Objects.equals(this.searchable, dataSetDTO.searchable) &&
        Objects.equals(this.generateReadme, dataSetDTO.generateReadme) &&
        Objects.equals(this.permissions, dataSetDTO.permissions) &&
        Objects.equals(this.template, dataSetDTO.template) &&
        Objects.equals(this.projectId, dataSetDTO.projectId) &&
        Objects.equals(this.projectIds, dataSetDTO.projectIds) &&
        Objects.equals(this.projectName, dataSetDTO.projectName) &&
        Objects.equals(this.templateName, dataSetDTO.templateName) &&
        Objects.equals(this.projectTeam, dataSetDTO.projectTeam) &&
        Objects.equals(this.sharedWith, dataSetDTO.sharedWith) &&
        Objects.equals(this.type, dataSetDTO.type) &&
        Objects.equals(this.members, dataSetDTO.members);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(inodeId, name, description, isPublic, searchable, generateReadme, permissions, template, projectId, projectIds, projectName, templateName, projectTeam, sharedWith, type, members);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DataSetDTO {\n");
    
    sb.append("    inodeId: ").append(toIndentedString(inodeId)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    isPublic: ").append(toIndentedString(isPublic)).append("\n");
    sb.append("    searchable: ").append(toIndentedString(searchable)).append("\n");
    sb.append("    generateReadme: ").append(toIndentedString(generateReadme)).append("\n");
    sb.append("    permissions: ").append(toIndentedString(permissions)).append("\n");
    sb.append("    template: ").append(toIndentedString(template)).append("\n");
    sb.append("    projectId: ").append(toIndentedString(projectId)).append("\n");
    sb.append("    projectIds: ").append(toIndentedString(projectIds)).append("\n");
    sb.append("    projectName: ").append(toIndentedString(projectName)).append("\n");
    sb.append("    templateName: ").append(toIndentedString(templateName)).append("\n");
    sb.append("    projectTeam: ").append(toIndentedString(projectTeam)).append("\n");
    sb.append("    sharedWith: ").append(toIndentedString(sharedWith)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    members: ").append(toIndentedString(members)).append("\n");
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