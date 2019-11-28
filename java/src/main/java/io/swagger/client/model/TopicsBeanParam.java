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
import io.swagger.client.model.TopicsFilterBy;
import io.swagger.client.model.TopicsSortBy;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * TopicsBeanParam
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class TopicsBeanParam {

  @SerializedName("sortBy")
  private String sortBy = null;

  @SerializedName("sortBySet")
  private List<TopicsSortBy> sortBySet = null;

  @SerializedName("filter")
  private List<TopicsFilterBy> filter = null;
  public TopicsBeanParam sortBy(String sortBy) {
    this.sortBy = sortBy;
    return this;
  }

  

  /**
  * Get sortBy
  * @return sortBy
  **/
  @Schema(description = "")
  public String getSortBy() {
    return sortBy;
  }
  public void setSortBy(String sortBy) {
    this.sortBy = sortBy;
  }
  public TopicsBeanParam sortBySet(List<TopicsSortBy> sortBySet) {
    this.sortBySet = sortBySet;
    return this;
  }

  public TopicsBeanParam addSortBySetItem(TopicsSortBy sortBySetItem) {
    if (this.sortBySet == null) {
      this.sortBySet = new ArrayList<TopicsSortBy>();
    }
    this.sortBySet.add(sortBySetItem);
    return this;
  }

  /**
  * Get sortBySet
  * @return sortBySet
  **/
  @Schema(description = "")
  public List<TopicsSortBy> getSortBySet() {
    return sortBySet;
  }
  public void setSortBySet(List<TopicsSortBy> sortBySet) {
    this.sortBySet = sortBySet;
  }
  public TopicsBeanParam filter(List<TopicsFilterBy> filter) {
    this.filter = filter;
    return this;
  }

  public TopicsBeanParam addFilterItem(TopicsFilterBy filterItem) {
    if (this.filter == null) {
      this.filter = new ArrayList<TopicsFilterBy>();
    }
    this.filter.add(filterItem);
    return this;
  }

  /**
  * Get filter
  * @return filter
  **/
  @Schema(description = "")
  public List<TopicsFilterBy> getFilter() {
    return filter;
  }
  public void setFilter(List<TopicsFilterBy> filter) {
    this.filter = filter;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TopicsBeanParam topicsBeanParam = (TopicsBeanParam) o;
    return Objects.equals(this.sortBy, topicsBeanParam.sortBy) &&
        Objects.equals(this.sortBySet, topicsBeanParam.sortBySet) &&
        Objects.equals(this.filter, topicsBeanParam.filter);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(sortBy, sortBySet, filter);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TopicsBeanParam {\n");
    
    sb.append("    sortBy: ").append(toIndentedString(sortBy)).append("\n");
    sb.append("    sortBySet: ").append(toIndentedString(sortBySet)).append("\n");
    sb.append("    filter: ").append(toIndentedString(filter)).append("\n");
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
