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
import io.swagger.client.model.ProjectTeamPK;
import io.swagger.client.model.Users;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import org.threeten.bp.OffsetDateTime;

/**
 * ProjectTeam
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class ProjectTeam {

  @SerializedName("project")
  private Project project = null;

  @SerializedName("user")
  private Users user = null;

  @SerializedName("projectTeamPK")
  private ProjectTeamPK projectTeamPK = null;

  @SerializedName("teamRole")
  private String teamRole = null;

  @SerializedName("timestamp")
  private OffsetDateTime timestamp = null;
  public ProjectTeam project(Project project) {
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
  public ProjectTeam user(Users user) {
    this.user = user;
    return this;
  }

  

  /**
  * Get user
  * @return user
  **/
  @Schema(description = "")
  public Users getUser() {
    return user;
  }
  public void setUser(Users user) {
    this.user = user;
  }
  public ProjectTeam projectTeamPK(ProjectTeamPK projectTeamPK) {
    this.projectTeamPK = projectTeamPK;
    return this;
  }

  

  /**
  * Get projectTeamPK
  * @return projectTeamPK
  **/
  @Schema(description = "")
  public ProjectTeamPK getProjectTeamPK() {
    return projectTeamPK;
  }
  public void setProjectTeamPK(ProjectTeamPK projectTeamPK) {
    this.projectTeamPK = projectTeamPK;
  }
  public ProjectTeam teamRole(String teamRole) {
    this.teamRole = teamRole;
    return this;
  }

  

  /**
  * Get teamRole
  * @return teamRole
  **/
  @Schema(description = "")
  public String getTeamRole() {
    return teamRole;
  }
  public void setTeamRole(String teamRole) {
    this.teamRole = teamRole;
  }
  public ProjectTeam timestamp(OffsetDateTime timestamp) {
    this.timestamp = timestamp;
    return this;
  }

  

  /**
  * Get timestamp
  * @return timestamp
  **/
  @Schema(required = true, description = "")
  public OffsetDateTime getTimestamp() {
    return timestamp;
  }
  public void setTimestamp(OffsetDateTime timestamp) {
    this.timestamp = timestamp;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProjectTeam projectTeam = (ProjectTeam) o;
    return Objects.equals(this.project, projectTeam.project) &&
        Objects.equals(this.user, projectTeam.user) &&
        Objects.equals(this.projectTeamPK, projectTeam.projectTeamPK) &&
        Objects.equals(this.teamRole, projectTeam.teamRole) &&
        Objects.equals(this.timestamp, projectTeam.timestamp);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(project, user, projectTeamPK, teamRole, timestamp);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectTeam {\n");
    
    sb.append("    project: ").append(toIndentedString(project)).append("\n");
    sb.append("    user: ").append(toIndentedString(user)).append("\n");
    sb.append("    projectTeamPK: ").append(toIndentedString(projectTeamPK)).append("\n");
    sb.append("    teamRole: ").append(toIndentedString(teamRole)).append("\n");
    sb.append("    timestamp: ").append(toIndentedString(timestamp)).append("\n");
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