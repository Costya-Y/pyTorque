# AUTO-GENERATED: Do not edit manually. Run scripts/generate_models.py
from __future__ import annotations
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, RootModel

__all__ = []  # populated at end

SCHEMA_NAME_MAP = {
    "Quali.Colony.Abstractions.Exceptions.Error": "Error",
    "Quali.Colony.Accounts.Contracts.Users.CreateUserRequest": "CreateUserRequest",
    "Quali.Colony.Contracts.Blueprints.BlueprintCostResponse": "BlueprintCostResponse",
    "Quali.Colony.Contracts.Blueprints.BlueprintCustomIcon": "BlueprintCustomIcon",
    "Quali.Colony.Contracts.Blueprints.BlueprintGrainForList": "BlueprintGrainForList",
    "Quali.Colony.Contracts.Blueprints.BlueprintInputStyle": "BlueprintInputStyle",
    "Quali.Colony.Contracts.Blueprints.BlueprintInputType": "BlueprintInputType",
    "Quali.Colony.Contracts.Blueprints.BlueprintValidationResponse": "BlueprintValidationResponse",
    "Quali.Colony.Contracts.Blueprints.ElementSource": "ElementSource",
    "Quali.Colony.Contracts.Blueprints.EnvironmentForList": "EnvironmentForList",
    "Quali.Colony.Contracts.Blueprints.EnvironmentLabels": "EnvironmentLabels",
    "Quali.Colony.Contracts.Blueprints.EnvironmentType": "EnvironmentType",
    "Quali.Colony.Contracts.Blueprints.GrainLabel": "GrainLabel",
    "Quali.Colony.Contracts.Blueprints.GrainSourceType": "GrainSourceType",
    "Quali.Colony.Contracts.Blueprints.ResourceType": "ResourceType",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintDetails": "BlueprintDetails",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintDetailsResponse": "BlueprintDetailsResponse",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintEnvLabelResponse": "BlueprintEnvLabelResponse",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintEnvReferenceResponse": "BlueprintEnvReferenceResponse",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintInputOverride": "BlueprintInputOverride",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintInputParameterResponse": "BlueprintInputParameterResponse",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintInstructions": "BlueprintInstructions",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintLabel": "BlueprintLabel",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintLayout": "BlueprintLayout",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintOutputParameterResponse": "BlueprintOutputParameterResponse",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintPolicy": "BlueprintPolicy",
    "Quali.Colony.Contracts.BlueprintsV2.BlueprintTag": "BlueprintTag",
    "Quali.Colony.Contracts.Color": "Color",
    "Quali.Colony.Contracts.Tags.TagType": "TagType",
    "Quali.Colony.Gateway.Api.Model.Requests.AddAgentRequest": "AddAgentRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.AddCatalogRequest": "AddCatalogRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.AddGrainRequest": "AddGrainRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.AddScriptRequest": "AddScriptRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.AddScriptWithOutputsRequest": "AddScriptWithOutputsRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.AddScriptsRequest": "AddScriptsRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.AddSourceRequest": "AddSourceRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.AddTagsRequest": "AddTagsRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.CollaboratorsRequest": "CollaboratorsRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.CreateSandboxRequest": "CreateSandboxRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.EacRegisterRequest": "EacRegisterRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.EacUnRegisterRequest": "EacUnRegisterRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.GrainDriftCheckRequest": "GrainDriftCheckRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.GrainUpdateRequest": "GrainUpdateRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.ImportEnvironmentFromBlueprintRequest": "ImportEnvironmentFromBlueprintRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.ImportEnvironmentRequest": "ImportEnvironmentRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.ImportGrainHost": "ImportGrainHost",
    "Quali.Colony.Gateway.Api.Model.Requests.ImportGrainRequest": "ImportGrainRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.ImportGrainSource": "ImportGrainSource",
    "Quali.Colony.Gateway.Api.Model.Requests.ModelForLogin": "ModelForLogin",
    "Quali.Colony.Gateway.Api.Model.Requests.PlanEnvironmentRequest": "PlanEnvironmentRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.ReconcileSandboxGrainsRequest": "ReconcileSandboxGrainsRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.RestartEnvironmentGrainsRequest": "RestartEnvironmentGrainsRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.RestartGrainRequest": "RestartGrainRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.RunResourceActionRequest": "RunResourceActionRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.ScheduleEnvironmentRequest": "ScheduleEnvironmentRequest",
    "Quali.Colony.Gateway.Api.Model.Requests.UpdateEnvironmentGrainsRequestV2": "UpdateEnvironmentGrainsRequestV2",
    "Quali.Colony.Gateway.Api.Model.Responses.CollaboratorsGroupResponse": "CollaboratorsGroupResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.CollaboratorsResponse": "CollaboratorsResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.CreateEnvResponse": "CreateEnvResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.EacCandidateResponse": "EacCandidateResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.EnvCost": "EnvCost",
    "Quali.Colony.Gateway.Api.Model.Responses.EnvironmentListItemDefinitionResponse": "EnvironmentListItemDefinitionResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.EnvironmentListItemDetailsResponse": "EnvironmentListItemDetailsResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.EnvironmentListItemResponse": "EnvironmentListItemResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.EnvironmentListItemStateResponse": "EnvironmentListItemStateResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.EnvironmentResponse": "EnvironmentResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.EnvironmentsResponse": "EnvironmentsResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.ExtendEnvDurationResponse": "ExtendEnvDurationResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.ImportEnvResponse": "ImportEnvResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.ReleaseEnvResponse": "ReleaseEnvResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.RepositoryDetailsResponse": "RepositoryDetailsResponse",
    "Quali.Colony.Gateway.Api.Model.Responses.ScheduleEnvironmentResponse": "ScheduleEnvironmentResponse",
    "Quali.Colony.Gateway.Api.Space.CreateSpaceRequest": "CreateSpaceRequest",
    "Quali.Colony.Services.Audit.Contracts.AuditStorage.Responses.AuditEventActorResponse": "AuditEventActorResponse",
    "Quali.Colony.Services.Audit.Contracts.AuditStorage.Responses.PageInfoResponse": "PageInfoResponse",
    "Quali.Colony.Services.Audit.Contracts.AuditStorage.Responses.PagedAuditEventsResponse": "PagedAuditEventsResponse",
    "Quali.Colony.Services.Audit.Contracts.AuditStorage.Responses.StoredAuditEventResponse": "StoredAuditEventResponse",
    "Quali.Colony.Services.Automation.Contracts.Workflows.Requests.LaunchScheduleRequest": "LaunchScheduleRequest",
    "Quali.Colony.Services.Automation.Contracts.Workflows.Requests.LaunchWorkflowRequest": "LaunchWorkflowRequest",
    "Quali.Colony.Services.Blueprints.Contracts.Requests.CreateBlueprintRequest": "CreateBlueprintRequest",
    "Quali.Colony.Services.Blueprints.Contracts.Requests.Repository.UpdateRepositoryRequest": "UpdateRepositoryRequest",
    "Quali.Colony.Services.Blueprints.Contracts.Responses.Repository.RepositoryAgentResponse": "RepositoryAgentResponse",
    "Quali.Colony.Services.Blueprints.Contracts.Responses.Repository.RepositoryScanningStatus": "RepositoryScanningStatus",
    "Quali.Colony.Services.Blueprints.Contracts.Responses.Repository.RepositoryType": "RepositoryType",
    "Quali.Colony.Services.Common.Blueprints.V2BlueprintValidation.BlueprintValidationRequest": "BlueprintValidationRequest",
    "Quali.Colony.Services.Common.Model.Requests.Blueprint.BlueprintSourceRequest": "BlueprintSourceRequest",
    "Quali.Colony.Services.Common.Model.Requests.Blueprint.EditBlueprintDisplayNameRequest": "EditBlueprintDisplayNameRequest",
    "Quali.Colony.Services.Common.Model.Requests.Blueprint.EditBlueprintLabelsRequest": "EditBlueprintLabelsRequest",
    "Quali.Colony.Services.Common.Model.Requests.Blueprint.EditBlueprintMetadataRequest": "EditBlueprintMetadataRequest",
    "Quali.Colony.Services.Common.Model.Requests.Blueprint.UpdateBlueprintLaunchAllowedRequest": "UpdateBlueprintLaunchAllowedRequest",
    "Quali.Colony.Services.Common.Model.Requests.EnableEacRequest": "EnableEacRequest",
    "Quali.Colony.Services.Common.Model.Requests.EnvEditSaveSessionRequest": "EnvEditSaveSessionRequest",
    "Quali.Colony.Services.Common.Model.Requests.EnvEditStartSessionRequest": "EnvEditStartSessionRequest",
    "Quali.Colony.Services.Common.Model.Requests.GenerateBlueprintYamlFromAssetsRequest": "GenerateBlueprintYamlFromAssetsRequest",
    "Quali.Colony.Services.Common.Model.Requests.Labels.AddLabelRequest": "AddLabelRequest",
    "Quali.Colony.Services.Common.Model.Requests.Labels.UpdateLabelRequest": "UpdateLabelRequest",
    "Quali.Colony.Services.Common.Model.Responses.BlueprintApplicationForGetAllResponse": "BlueprintApplicationForGetAllResponse",
    "Quali.Colony.Services.Common.Model.Responses.BlueprintForGetAllResponse": "BlueprintForGetAllResponse",
    "Quali.Colony.Services.Common.Model.Responses.BlueprintInputResponse": "BlueprintInputResponse",
    "Quali.Colony.Services.Common.Model.Responses.BlueprintPolicyResponse": "BlueprintPolicyResponse",
    "Quali.Colony.Services.Common.Model.Responses.BlueprintServiceForGetAllResponse": "BlueprintServiceForGetAllResponse",
    "Quali.Colony.Services.Common.Model.Responses.BlueprintSimplifiedListItemResponse": "BlueprintSimplifiedListItemResponse",
    "Quali.Colony.Services.Common.Model.Responses.BlueprintTagResponse": "BlueprintTagResponse",
    "Quali.Colony.Services.Common.Model.Responses.CatalogForGetAllResponse": "CatalogForGetAllResponse",
    "Quali.Colony.Services.Common.Model.Responses.CloudComputeServiceResponse": "CloudComputeServiceResponse",
    "Quali.Colony.Services.Common.Model.Responses.CloudRegionResponse": "CloudRegionResponse",
    "Quali.Colony.Services.Common.Model.Responses.CloudResponse": "CloudResponse",
    "Quali.Colony.Services.Common.Model.Responses.EacResponse": "EacResponse",
    "Quali.Colony.Services.Common.Model.Responses.EnvEditListSessionsResponse": "EnvEditListSessionsResponse",
    "Quali.Colony.Services.Common.Model.Responses.EnvEditPlanCommitDiffResponse": "EnvEditPlanCommitDiffResponse",
    "Quali.Colony.Services.Common.Model.Responses.EnvEditPlanDependenciesDiffResponse": "EnvEditPlanDependenciesDiffResponse",
    "Quali.Colony.Services.Common.Model.Responses.EnvEditPlanGrainDiffResponse": "EnvEditPlanGrainDiffResponse",
    "Quali.Colony.Services.Common.Model.Responses.EnvEditPlanInputsDiffResponse": "EnvEditPlanInputsDiffResponse",
    "Quali.Colony.Services.Common.Model.Responses.EnvEditPlanResponse": "EnvEditPlanResponse",
    "Quali.Colony.Services.Common.Model.Responses.EnvEditSessionListItemResponse": "EnvEditSessionListItemResponse",
    "Quali.Colony.Services.Common.Model.Responses.IACAssetDetailResponse": "IACAssetDetailResponse",
    "Quali.Colony.Services.Common.Model.Responses.IACAssetListItemResponse": "IACAssetListItemResponse",
    "Quali.Colony.Services.Common.Model.Responses.IACAssetListMetricsResponse": "IACAssetListMetricsResponse",
    "Quali.Colony.Services.Common.Model.Responses.IACAssetListMetricsResponse+IACAssetListMetricsRepository": "IACAssetListMetricsResponse_IACAssetListMetricsRepository",
    "Quali.Colony.Services.Common.Model.Responses.IACAssetSimplifiedListItemResponse": "IACAssetSimplifiedListItemResponse",
    "Quali.Colony.Services.Common.Model.Responses.InstructionsResponse": "InstructionsResponse",
    "Quali.Colony.Services.Common.Model.Responses.Links.Hyperlink": "Hyperlink",
    "Quali.Colony.Services.Common.Model.Responses.LongTokenSafeResponse": "LongTokenSafeResponse",
    "Quali.Colony.Services.Common.Model.Responses.PagedIACAssetListItemResponse": "PagedIACAssetListItemResponse",
    "Quali.Colony.Services.Common.Model.Responses.PagedSimplifiedBlueprintListItemResponse": "PagedSimplifiedBlueprintListItemResponse",
    "Quali.Colony.Services.Common.Model.Responses.PagedSimplifiedIACAssetListItemResponse": "PagedSimplifiedIACAssetListItemResponse",
    "Quali.Colony.Services.Common.Model.Responses.PlanDiffType": "PlanDiffType",
    "Quali.Colony.Services.Common.Model.Responses.TokenResponse": "TokenResponse",
    "Quali.Colony.Services.Common.Model.Responses.UserResponse": "UserResponse",
    "Quali.Colony.Services.Common.Workflow_V2.BoundedEntityMetadata": "BoundedEntityMetadata",
    "Quali.Colony.Services.ComputeServices.Contracts.ComputeServiceDetailsResponse": "ComputeServiceDetailsResponse",
    "Quali.Colony.Services.ComputeServices.Contracts.ComputeServiceResponse": "ComputeServiceResponse",
    "Quali.Colony.Services.ComputeServices.Contracts.ComputeServiceStatus": "ComputeServiceStatus",
    "Quali.Colony.Services.ComputeServices.Contracts.InfraSettingsResponse": "InfraSettingsResponse",
    "Quali.Colony.Services.ComputeServices.Contracts.Requests.CreateComputeServiceRequest": "CreateComputeServiceRequest",
    "Quali.Colony.Services.ComputeServices.Contracts.Requests.K8sSpaceAssociationSpec": "K8sSpaceAssociationSpec",
    "Quali.Colony.Services.ComputeServices.Contracts.Requests.UpdateComputeServiceDetails": "UpdateComputeServiceDetails",
    "Quali.Colony.Services.ComputeServices.Contracts.Requests.UpdateComputeServiceRequest": "UpdateComputeServiceRequest",
    "Quali.Colony.Services.ComputeServices.Contracts.Responses.ComputeServiceUsagesResponse": "ComputeServiceUsagesResponse",
    "Quali.Colony.Services.ComputeServices.Contracts.SpaceComputeServiceResponse": "SpaceComputeServiceResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.AssetDefinitions.AssetDefinition": "AssetDefinition",
    "Quali.Colony.Services.Environments.Api.Contracts.AssetDriftResponse": "AssetDriftResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Automation.Actions.Responses.EnvironmentWorkflowResponse": "EnvironmentWorkflowResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Automation.Actions.Responses.WorkflowActionExecutionResponse": "WorkflowActionExecutionResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Automation.Actions.Responses.WorkflowExecutionStepResponse": "WorkflowExecutionStepResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Automation.Actions.Responses.WorkflowOccurrence": "WorkflowOccurrence",
    "Quali.Colony.Services.Environments.Api.Contracts.BlueprintLayoutResponse": "BlueprintLayoutResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.CollaboratorsFeedData": "CollaboratorsFeedData",
    "Quali.Colony.Services.Environments.Api.Contracts.ConnectedEnvironmentResponse": "ConnectedEnvironmentResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.ConnectionsResponse": "ConnectionsResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.DeploymentDriftResponse": "DeploymentDriftResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentAnnotationResponse": "EnvironmentAnnotationResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentDefinitionResponse": "EnvironmentDefinitionResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentDetailsResponse": "EnvironmentDetailsResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentEacDataResponse": "EnvironmentEacDataResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentEnvReferenceResponse": "EnvironmentEnvReferenceResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentErrorResponse": "EnvironmentErrorResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentExecutionResponse": "EnvironmentExecutionResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentFeedDetails": "EnvironmentFeedDetails",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentFeedResponse": "EnvironmentFeedResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentGrainActivityResponse": "EnvironmentGrainActivityResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentGrainResponse": "EnvironmentGrainResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentGrainStageDetails": "EnvironmentGrainStageDetails",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentGrainStageResponse": "EnvironmentGrainStageResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentGrainStateResponse": "EnvironmentGrainStateResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentMetadataResponse": "EnvironmentMetadataResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentNameValueResponse": "EnvironmentNameValueResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentOutputResponse": "EnvironmentOutputResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentPhase": "EnvironmentPhase",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentPhaseExternal": "EnvironmentPhaseExternal",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentReservedResourceResponse": "EnvironmentReservedResourceResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.EnvironmentStateResponse": "EnvironmentStateResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.ExecutionType": "ExecutionType",
    "Quali.Colony.Services.Environments.Api.Contracts.GrainAssetResponse": "GrainAssetResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.GrainDetailsResponse": "GrainDetailsResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.GrainDriftResponse": "GrainDriftResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.GrainInputResponse": "GrainInputResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.GrainSourceResponse": "GrainSourceResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Grains.GrainPhaseExternal": "GrainPhaseExternal",
    "Quali.Colony.Services.Environments.Api.Contracts.IEnvironmentExecutionRetentionResponse": "IEnvironmentExecutionRetentionResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Labels.AttachEnvironmentLabelsRequest": "AttachEnvironmentLabelsRequest",
    "Quali.Colony.Services.Environments.Api.Contracts.Labels.EnvironmentLabelRequest": "EnvironmentLabelRequest",
    "Quali.Colony.Services.Environments.Api.Contracts.Labels.EnvironmentLabelResponse": "EnvironmentLabelResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Labels.LabelOrigins": "LabelOrigins",
    "Quali.Colony.Services.Environments.Api.Contracts.Messages.ExtendEnvironment": "ExtendEnvironment",
    "Quali.Colony.Services.Environments.Api.Contracts.Messages.InstantiateWorkflowRequest": "InstantiateWorkflowRequest",
    "Quali.Colony.Services.Environments.Api.Contracts.ParametersDrift.ParameterDriftType": "ParameterDriftType",
    "Quali.Colony.Services.Environments.Api.Contracts.PolicyEnforcement": "PolicyEnforcement",
    "Quali.Colony.Services.Environments.Api.Contracts.Requests.EnvironmentParameterDriftResponse": "EnvironmentParameterDriftResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Requests.EnvironmentParametersExternalResponse": "EnvironmentParametersExternalResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Requests.EnvironmentPlanResultEnvironmentInfo": "EnvironmentPlanResultEnvironmentInfo",
    "Quali.Colony.Services.Environments.Api.Contracts.Requests.EnvironmentPlanResultGrainInfo": "EnvironmentPlanResultGrainInfo",
    "Quali.Colony.Services.Environments.Api.Contracts.Requests.EnvironmentPlanResultInfo": "EnvironmentPlanResultInfo",
    "Quali.Colony.Services.Environments.Api.Contracts.Requests.EvaluateConsumptionPoliciesResponse": "EvaluateConsumptionPoliciesResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Requests.GetEnvironmentPlanResultResponse": "GetEnvironmentPlanResultResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Requests.ParameterStoreItemInfoResponse": "ParameterStoreItemInfoResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Requests.PlanEnvironmentResponse": "PlanEnvironmentResponse",
    "Quali.Colony.Services.Environments.Api.Contracts.Requests.PlanStatus": "PlanStatus",
    "Quali.Colony.Services.Environments.Api.Contracts.ResourceActionData": "ResourceActionData",
    "Quali.Colony.Services.Environments.Api.Contracts.SandboxTag": "SandboxTag",
    "Quali.Colony.Services.Environments.Api.Contracts.TagScope": "TagScope",
    "Quali.Colony.Services.Environments.Api.Contracts.TimeDataResponse": "TimeDataResponse",
    "Quali.Colony.Services.Environments.Runners.Contracts.Common.Kubernetes.KubeConfigDetails": "KubeConfigDetails",
    "Quali.Colony.Services.Governance.Contracts.Responses.AccountPolicyInstances.GetAccountPolicyInstancesResponse": "GetAccountPolicyInstancesResponse",
    "Quali.Colony.Services.Governance.Contracts.Responses.AccountPolicyInstances.PolicyInstanceVariableForGetResponse": "PolicyInstanceVariableForGetResponse",
    "Quali.Colony.Services.Governance.Contracts.Responses.AccountPolicyInstances.PolicyTemplateDataForGetInstancesResponse": "PolicyTemplateDataForGetInstancesResponse",
    "Quali.Colony.Services.Governance.Contracts.Responses.OpaPolicyFileResponse": "OpaPolicyFileResponse",
    "Quali.Colony.Services.Inventory.Contracts.InventoryMetrics.Responses.GetInventoryMetricsResponse": "GetInventoryMetricsResponse",
    "Quali.Colony.Services.Inventory.Contracts.InventoryMetrics.Responses.MetricSectionResponse": "MetricSectionResponse",
    "Quali.Colony.Services.Inventory.Contracts.InventoryProviders.Responses.GetCustomResourceTypeResponse": "GetCustomResourceTypeResponse",
    "Quali.Colony.Services.Inventory.Contracts.Resources.CustomResources.Requests.AttributeDefinition": "AttributeDefinition",
    "Quali.Colony.Services.Inventory.Contracts.Resources.CustomResources.Requests.AttributeValue": "AttributeValue",
    "Quali.Colony.Services.Inventory.Contracts.Resources.CustomResources.Requests.CreateCustomResourceRequest": "CreateCustomResourceRequest",
    "Quali.Colony.Services.Inventory.Contracts.Resources.CustomResources.Requests.CreateCustomResourceTypeRequest": "CreateCustomResourceTypeRequest",
    "Quali.Colony.Services.Inventory.Contracts.Resources.CustomResources.Requests.Tag": "Tag",
    "Quali.Colony.Services.Inventory.Contracts.Resources.CustomResources.Requests.UpdateCustomResourceRequest": "UpdateCustomResourceRequest",
    "Quali.Colony.Services.Inventory.Contracts.Resources.CustomResources.Requests.UpdateCustomResourceTypeRequest": "UpdateCustomResourceTypeRequest",
    "Quali.Colony.Services.Inventory.Contracts.Resources.Requests.ToggleResourceExcludedFromReservingRequest": "ToggleResourceExcludedFromReservingRequest",
    "Quali.Colony.Services.Inventory.Contracts.Resources.Responses.GetAllResourcesResponse": "GetAllResourcesResponse",
    "Quali.Colony.Services.Inventory.Contracts.Resources.Responses.GetResourceDataResponse": "GetResourceDataResponse",
    "Quali.Colony.Services.Inventory.Contracts.Resources.Responses.GetResourceResponse": "GetResourceResponse",
    "Quali.Colony.Services.Inventory.Contracts.Resources.Responses.ResourceAttributeResponse": "ResourceAttributeResponse",
    "Quali.Colony.Services.Inventory.Contracts.Resources.Responses.ResourceTagResponse": "ResourceTagResponse",
    "Quali.Colony.Services.ParameterStore.Contracts.AddParameterRequest": "AddParameterRequest",
    "Quali.Colony.Services.ParameterStore.Contracts.ParameterStoreItemResponse": "ParameterStoreItemResponse",
    "Quali.Colony.Services.ParameterStore.Contracts.SpaceParameterStoreItemResponse": "SpaceParameterStoreItemResponse",
    "Quali.Colony.Services.ParameterStore.Contracts.UpdateParameterRequest": "UpdateParameterRequest",
    "Quali.Colony.Web.Contracts.Pagination.PagingInfoResponse": "PagingInfoResponse",
    "Quali.Colony.Web.Response.ErrorResponse": "ErrorResponse",
    "Quali.Torque.Git.RepositorySecretInfo": "RepositorySecretInfo",
}

class Error(BaseModel):
    """Error information"""
    message: Optional[str] = Field(None, description="Error message")
    name: Optional[str] = Field(None, description="Error name")
    code: Optional[str] = Field(None, description="Error code")

__all__.append("Error")

class CreateUserRequest(BaseModel):
    """Create User Request"""
    account_role: Optional[str] = Field(None, description="Built in roles: Admin or leave empty.")
    space_name: Optional[str] = None
    space_role: Optional[str] = Field(None, description="Built in roles include: Space Member, Space Developer, Space Admin or the name of the custom role.")
    email: str = ...
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = Field(None, description="Password field. To create a pending SSO user, this field should not be provided. To create a non sso user this field is mandatory.")
    timezone: Optional[str] = None

__all__.append("CreateUserRequest")

class BlueprintCostResponse(BaseModel):
    average_hourly_cost: Optional[float] = None

__all__.append("BlueprintCostResponse")

class BlueprintCustomIcon(BaseModel):
    file_name: Optional[str] = None
    file_byte_size: Optional[int] = None
    url: Optional[str] = None
    key: Optional[str] = None

__all__.append("BlueprintCustomIcon")

class BlueprintGrainForList(BaseModel):
    name: Optional[str] = None
    kind: Optional[str] = None

__all__.append("BlueprintGrainForList")

class BlueprintInputStyle(RootModel[str]):
    """Display style of blueprint input as returned by the API.

    Using RootModel[str] keeps this flexible to accept any server-provided string
    (e.g., "text", "password", etc.) without failing validation.
    """
    pass

class BlueprintInputType(RootModel[str]):
    """Type of blueprint input as returned by the API.

    Using RootModel[str] keeps this flexible to accept any server-provided string
    (e.g., "string", "number", "boolean", etc.) without failing validation.
    """
    pass

class BlueprintValidationResponse(BaseModel):
    """Blueprint validation response"""
    errors: Optional[List[Error]] = None

__all__.append("BlueprintValidationResponse")

class ElementSource(BaseModel):
    type: Optional[GrainSourceType] = Field(None, description="possible values: Artifactory, SourceControl, EnvStorage")
    resourceType: Optional[ResourceType] = Field(None, description="possible values: HelmChart, File")
    name: Optional[str] = None
    store: Optional[str] = None
    credentials: Optional[str] = None
    path: Optional[str] = None
    pathDefinition: Optional[str] = None
    branch: Optional[str] = None
    commit: Optional[str] = None
    tag: Optional[str] = None
    chartVersion: Optional[str] = None

__all__.append("ElementSource")

class EnvironmentForList(BaseModel):
    environmentName: Optional[str] = None
    spaces: Optional[List[str]] = None
    ownerEmail: Optional[str] = None

__all__.append("EnvironmentForList")

class EnvironmentLabels(BaseModel):
    onSuccess: Optional[List[GrainLabel]] = None
    onFailure: Optional[List[GrainLabel]] = None

__all__.append("EnvironmentLabels")

class EnvironmentType(BaseModel):
    """possible values: Sandbox, Production, None"""
    pass

class GrainLabel(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

__all__.append("GrainLabel")

class GrainSourceType(BaseModel):
    """possible values: Artifactory, SourceControl, EnvStorage"""
    pass

class ResourceType(BaseModel):
    """possible values: HelmChart, File"""
    pass

class BlueprintDetails(BaseModel):
    name: Optional[str] = Field(None, description="Blueprint name")
    display_name: Optional[str] = None
    repository_branch: Optional[str] = None
    commit: Optional[str] = None
    url: Optional[str] = None
    repository_url: Optional[str] = None
    repository_name: Optional[str] = None
    relative_path: Optional[str] = Field(None, description="The relative path of the blueprint inside the repository. For examples: \"blueprints\" -> if its the default blueprints folder in the repo \"myCustomFolder/myBlueprintFolder\" -> a folder in the repo that has \".blueprints\" marker file in it")
    is_editable: Optional[bool] = None
    description: Optional[str] = None
    instructions: Optional[BlueprintInstructions] = None
    layout: Optional[BlueprintLayout] = None
    spec: Optional[str] = None
    last_modified: Optional[str] = None
    modified_by: Optional[str] = None
    inputs: Optional[List[BlueprintInputParameterResponse]] = None
    outputs: Optional[List[BlueprintOutputParameterResponse]] = None
    environment_labels: Optional[List[BlueprintEnvLabelResponse]] = None
    env_references: Optional[List[BlueprintEnvReferenceResponse]] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    favorite: Optional[bool] = None
    custom_icon: Optional[BlueprintCustomIcon] = None
    labels: Optional[List[BlueprintLabel]] = None
    enabled: Optional[bool] = None
    is_approval_required: Optional[bool] = None
    cost: Optional[BlueprintCostResponse] = None
    num_of_active_environments: Optional[int] = None

__all__.append("BlueprintDetails")

class BlueprintDetailsResponse(BaseModel):
    details: Optional[BlueprintDetails] = Field(None, description="the Blueprint Details")
    tags: Optional[List[BlueprintTag]] = Field(None, description="Blueprint tags information")
    policies: Optional[BlueprintPolicy] = Field(None, description="Policies information")

__all__.append("BlueprintDetailsResponse")

class BlueprintEnvLabelResponse(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

__all__.append("BlueprintEnvLabelResponse")

class BlueprintEnvReferenceResponse(BaseModel):
    name: Optional[str] = None
    labels_selector: Optional[str] = None

__all__.append("BlueprintEnvReferenceResponse")

class BlueprintInputOverride(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

__all__.append("BlueprintInputOverride")

class BlueprintInputParameterResponse(BaseModel):
    name: Optional[str] = None
    type: Optional[BlueprintInputType] = None
    style: Optional[BlueprintInputStyle] = None
    default_value: Optional[str] = None
    has_default_value: Optional[bool] = Field(None, description="Indicates whether default value was defined in the yaml, even if it is not returned in the default_value field (e.g. when sensitive)")
    sensitive: Optional[bool] = None
    description: Optional[str] = None
    allowed_values: Optional[List[str]] = None
    parameter_name: Optional[str] = None
    pattern: Optional[str] = None
    validation_description: Optional[str] = None
    depends_on: Optional[List[str]] = None
    source_name: Optional[str] = None
    overrides: Optional[List[BlueprintInputOverride]] = None
    max_size_in_mb: Optional[float] = None
    max_files: Optional[int] = None
    allowed_formats: Optional[List[str]] = None

__all__.append("BlueprintInputParameterResponse")

class BlueprintInstructions(BaseModel):
    text: Optional[str] = None
    source: Optional[ElementSource] = None

__all__.append("BlueprintInstructions")

class BlueprintLabel(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None

__all__.append("BlueprintLabel")

class BlueprintLayout(BaseModel):
    source: Optional[ElementSource] = None
    exclude_from_layout: Optional[List[str]] = Field(None, alias="exclude-from-layout")

__all__.append("BlueprintLayout")

class BlueprintOutputParameterResponse(BaseModel):
    name: Optional[str] = None

__all__.append("BlueprintOutputParameterResponse")

class BlueprintPolicy(BaseModel):
    max_duration: Optional[str] = Field(None, description="Max duration of environment in ISO 8601 format: P{days}DT{hours}H{minutes}M{seconds}S] (for example, 'P0DT2H3M4S')")
    default_duration: Optional[str] = Field(None, description="Default duration of environment in ISO 8601 format: P{days}DT{hours}H{minutes}M{seconds}S] (for example, 'P0DT2H3M4S')")
    default_extend: Optional[str] = Field(None, description="Default Extend of environment in ISO 8601 format: P{days}DT{hours}H{minutes}M{seconds}S] (for example, 'P0DT2H3M4S')")
    max_active_environments: Optional[int] = Field(None, description="Max active environments that can be launched from the blueprint")
    always_on: Optional[bool] = Field(None, description="When True, the environment will always be on, when False, it will be ephemeral.")
    allow_scheduling: Optional[bool] = Field(None, description="When True, the environment may be scheduled.")

__all__.append("BlueprintPolicy")

class BlueprintTag(BaseModel):
    name: Optional[str] = Field(None, description="Tag name")
    default_value: Optional[str] = Field(None, description="Tag value")
    possible_values: Optional[List[str]] = Field(None, description="Tag possible values")
    description: Optional[str] = Field(None, description="the Tag's description")

__all__.append("BlueprintTag")

class Color(BaseModel):
    """possible values: FrogGreen, Grey"""
    pass

class TagType(RootModel[str]):
    """Tag type as string (system, user_defined, override, pre_defined)."""
    pass

class AddAgentRequest(BaseModel):
    name: Optional[str] = None
    service_account: Optional[str] = None

__all__.append("AddAgentRequest")

class AddCatalogRequest(BaseModel):
    """Request to add a blueprint to blueprint catalog"""
    blueprint_name: Optional[str] = Field(None, description="Blueprint name")
    repository_name: Optional[str] = Field(None, description="Blueprint's repository name")

__all__.append("AddCatalogRequest")

class AddGrainRequest(BaseModel):
    kind: Optional[str] = None
    name: Optional[str] = None
    depends_on: Optional[List[str]] = None
    inputs: Optional[Dict[str, str]] = None
    env_vars: Optional[Dict[str, str]] = None
    outputs: Optional[List[str]] = None
    agent: Optional[AddAgentRequest] = None
    source: Optional[AddSourceRequest] = None
    scripts: Optional[AddScriptsRequest] = None
    auto_approve: Optional[bool] = None
    tags: Optional[AddTagsRequest] = None

__all__.append("AddGrainRequest")

class AddScriptRequest(BaseModel):
    source: Optional[AddSourceRequest] = None
    arguments: Optional[str] = None

__all__.append("AddScriptRequest")

class AddScriptWithOutputsRequest(BaseModel):
    outputs: Optional[List[str]] = None
    source: Optional[AddSourceRequest] = None
    arguments: Optional[str] = None

__all__.append("AddScriptWithOutputsRequest")

class AddScriptsRequest(BaseModel):
    pre_tf_init: Optional[AddScriptRequest] = Field(None, alias="pre-tf-init")
    pre_tf_destroy: Optional[AddScriptRequest] = Field(None, alias="pre-tf-destroy")
    post_tf_plan: Optional[AddScriptRequest] = Field(None, alias="post-tf-plan")
    pre_open_tofu_init: Optional[AddScriptRequest] = Field(None, alias="pre-open-tofu-init")
    pre_open_tofu_destroy: Optional[AddScriptRequest] = Field(None, alias="pre-open-tofu-destroy")
    post_open_tofu_plan: Optional[AddScriptRequest] = Field(None, alias="post-open-tofu-plan")
    post_helm_install: Optional[AddScriptWithOutputsRequest] = Field(None, alias="post-helm-install")
    post_kubernetes_install: Optional[AddScriptWithOutputsRequest] = Field(None, alias="post-kubernetes-install")
    pre_aws_cdk_deploy: Optional[AddScriptRequest] = Field(None, alias="pre-aws-cdk-deploy")
    post_aws_cdk_deploy: Optional[AddScriptRequest] = Field(None, alias="post-aws-cdk-deploy")

__all__.append("AddScriptsRequest")

class AddSourceRequest(BaseModel):
    store: Optional[str] = None
    path: Optional[str] = None
    branch: Optional[str] = None
    commit: Optional[str] = None
    name: Optional[str] = None

__all__.append("AddSourceRequest")

class AddTagsRequest(BaseModel):
    auto_tag: Optional[bool] = Field(None, alias="auto-tag")
    disable_tags_for: Optional[List[str]] = Field(None, alias="disable-tags-for")

__all__.append("AddTagsRequest")

class CollaboratorsRequest(BaseModel):
    collaborators_emails: Optional[List[str]] = Field(None, description="List of emails of users that will be added to the new environment as collaborators so will have access to the environment.")
    collaborators_groups: Optional[List[str]] = Field(None, description="List of emails of users that will be added to the new environment as collaborators so will have access to the environment.")
    all_space_members: Optional[bool] = Field(None, description="Set this field to True to add all users in the space as collaborators in the new environment.")

__all__.append("CollaboratorsRequest")

class CreateSandboxRequest(BaseModel):
    """Request structure that should be passed as a json body to the 'Start new environment' API. This structure is required."""
    environment_name: Optional[str] = Field(None, description="The name for the newly created environment. Environment name can contain any character including special character and spaces.")
    blueprint_name: str = Field(..., description="The blueprint name that should be used for creating the new environment.")
    owner_email: Optional[str] = Field(None, description="The email of the user that should be set as the owner of the new environment. if omitted the current user will be used.")
    description: Optional[str] = Field(None, description="The new environment description that will be presented in the Torque UI following the launch of the environment.")
    inputs: Optional[Dict[str, str]] = Field(None, description="Dictionary of key-value string pairs that will be used as values for the blueprint inputs. In case a value is not provided the input default value will be used. If a default value is not set, a validation error will be thrown upon launch. <example> For example: { \"region\": \"eu-west-1\", \"application version\": \"1.0.8\" } </example>")
    env_references_values: Optional[Dict[str, str]] = Field(None, description="Dictionary of key-value string pairs that will be used to assign values to blueprint's environment references. In case a value is not provided for a defined environment reference, a validation error will be thrown upon launch. <example> For example: { \"rds_env\": \"A1WV5HtQ8rhG\" } </example>")
    tags: Optional[Dict[str, str]] = Field(None, description="Environment blueprint tags /// Dictionary of key-value string pairs that will be used to tag deployed resources in the environment. In case a configured tag value is not provided the tag default value will be used. Note that tags that were configured in the account and space level will be set regardless of this field. <example> For example: { \"activity_type\": \"demo\"} </example>")
    labels: Optional[List[EnvironmentLabelRequest]] = None
    collaborators: Optional[CollaboratorsRequest] = None
    automation: Optional[bool] = Field(None, description="Indicates if the environment was launched from automation using integrated pipeline tool, For example: Jenkins, GitHub Actions and GitLal CI.")
    scheduled_end_time: Optional[str] = Field(None, description="Environment scheduled end time in ISO 8601 format <example>For example, 2021-10-06T08:27:05.215Z.</example><remarks> NOTE: Environment request cannot include both \"duration\" and \"scheduled_end_time\" fields. </remarks>")
    duration: Optional[str] = Field(None, description="Environment duration time in ISO 8601 format: \"P{days}DT{hours}H{minutes}M{seconds}S]]\" <example>For example, P0DT2H3M4S.</example><remarks> NOTE: Environment request cannot include both \"duration\" and \"scheduled_end_time\" fields. </remarks>")
    source: Optional[BlueprintSourceRequest] = Field(None, description="Additional details about the blueprint repository to be used. By default, this information is taken from the repository already confiured in the space.")
    workflows: Optional[List[LaunchWorkflowRequest]] = Field(None, description="Array of workflows that will be attached and enabled on the new environment.")
    resource_handles: Optional[Dict[str, str]] = Field(None, description="A mapping from grain name to cloud resource handle name")
    workflows_v2: Optional[List[InstantiateWorkflowRequest]] = Field(None, description="Array of workflows that will be attached and enabled on the new environment (new workflows)")
    entity_metadata: Optional[BoundedEntityMetadata] = None
    instantiation_name: Optional[str] = None
    enable_termination_protection: Optional[bool] = Field(None, description="Indicates if termination protection should be enabled on the new environment.")

__all__.append("CreateSandboxRequest")

class EacRegisterRequest(BaseModel):
    repository_name: Optional[str] = None
    environment_file_name: Optional[str] = None

__all__.append("EacRegisterRequest")

class EacUnRegisterRequest(BaseModel):
    eac_url: Optional[str] = None

__all__.append("EacUnRegisterRequest")

class GrainDriftCheckRequest(BaseModel):
    force: Optional[bool] = Field(None, description="Should perform drift check even if it conflicts with current running operation")

__all__.append("GrainDriftCheckRequest")

class GrainUpdateRequest(BaseModel):
    path: Optional[str] = None
    branch: Optional[str] = None
    commit_hash: Optional[str] = None
    tag: Optional[str] = None
    inputs: Optional[Dict[str, str]] = None
    depends_on: Optional[List[str]] = None
    asset_definition: Optional[AssetDefinition] = None
    mark_changes: Optional[bool] = None

__all__.append("GrainUpdateRequest")

class ImportEnvironmentFromBlueprintRequest(BaseModel):
    """Request to import a new env using existing resources from existing blueprint"""
    source: Optional[BlueprintSourceRequest] = Field(None, description="Additional details about the blueprint repository to be used. By default, this information is taken from the repository already confiured in the space.")
    environment_name: Optional[str] = Field(None, description="Environment name")
    description: Optional[str] = Field(None, description="Environment description")
    owner_email: Optional[str] = None
    enable_termination_protection: Optional[bool] = Field(None, description="Indicates if termination protection should be enabled on the new environment.")
    visibility: Optional[str] = Field(None, description="Indicates if the sandbox is hidden or visible <remarks> - \"normal\": sandbox is visible - \"hidden\": sandbox is hidden </remarks>")
    notes: Optional[str] = None
    grains: Optional[List[ImportGrainRequest]] = None
    outputs: Optional[Dict[str, str]] = None
    inputs: Optional[Dict[str, str]] = Field(None, description="Environment blueprint inputs")
    tags: Optional[Dict[str, str]] = Field(None, description="Environment blueprint tags")
    compute_availability: Optional[int] = Field(None, description="possible values: OnDemand, Spot")

__all__.append("ImportEnvironmentFromBlueprintRequest")

class ImportEnvironmentRequest(BaseModel):
    """Request to import a new env using existing resources with auto-generated blueprint"""
    environment_name: Optional[str] = Field(None, description="Environment name")
    description: Optional[str] = Field(None, description="Environment description")
    owner_email: Optional[str] = None
    enable_termination_protection: Optional[bool] = Field(None, description="Indicates if termination protection should be enabled on the new environment.")
    visibility: Optional[str] = Field(None, description="Indicates if the sandbox is hidden or visible <remarks> - \"normal\": sandbox is visible - \"hidden\": sandbox is hidden </remarks>")
    notes: Optional[str] = None
    grains: Optional[List[ImportGrainRequest]] = None
    outputs: Optional[Dict[str, str]] = None
    inputs: Optional[Dict[str, str]] = Field(None, description="Environment blueprint inputs")
    tags: Optional[Dict[str, str]] = Field(None, description="Environment blueprint tags")
    compute_availability: Optional[int] = Field(None, description="possible values: OnDemand, Spot")

__all__.append("ImportEnvironmentRequest")

class ImportGrainHost(BaseModel):
    name: Optional[str] = None
    service_account: Optional[str] = None

__all__.append("ImportGrainHost")

class ImportGrainRequest(BaseModel):
    """Request to import a grain with existing resources"""
    kind: Optional[str] = None
    name: Optional[str] = None
    agent: Optional[ImportGrainHost] = Field(None, description="Agent name that will be used for grain execution")
    source: Optional[ImportGrainSource] = None
    environment_variables: Optional[Dict[str, str]] = None
    inputs: Optional[Dict[str, str]] = None
    outputs: Optional[List[str]] = None
    authentication: Optional[List[str]] = None

__all__.append("ImportGrainRequest")

class ImportGrainSource(BaseModel):
    store: Optional[str] = None
    path: Optional[str] = None
    branch: Optional[str] = None

__all__.append("ImportGrainSource")

class ModelForLogin(BaseModel):
    """Login request"""
    email: str = Field(..., description="User email")
    password: str = Field(..., description="User password")

__all__.append("ModelForLogin")

class PlanEnvironmentRequest(BaseModel):
    env_yaml_content: Optional[str] = Field(None, description="Environment yaml content")

__all__.append("PlanEnvironmentRequest")

class ReconcileSandboxGrainsRequest(BaseModel):
    grain_paths: Optional[List[str]] = Field(None, description="List of grain paths to update.")
    grain_ids: Optional[List[str]] = Field(None, description="List of grain ids to update.")
    force: Optional[bool] = Field(None, description="Should perform reconcile even if it conflicts with current running operation")

__all__.append("ReconcileSandboxGrainsRequest")

class RestartEnvironmentGrainsRequest(BaseModel):
    grains: Optional[List[RestartGrainRequest]] = None
    force: Optional[bool] = Field(None, description="Should restart environment even if it conflicts with current running operation")

__all__.append("RestartEnvironmentGrainsRequest")

class RestartGrainRequest(BaseModel):
    id: Optional[str] = None
    path: Optional[str] = None
    branch: Optional[str] = None
    commit: Optional[str] = None
    inputs: Optional[Dict[str, str]] = None

__all__.append("RestartGrainRequest")

class RunResourceActionRequest(BaseModel):
    force: Optional[bool] = Field(None, description="Should run resource action even if it conflicts with current running operation")

__all__.append("RunResourceActionRequest")

class ScheduleEnvironmentRequest(BaseModel):
    scheduled_launch_time: Optional[str] = Field(None, description="Environment scheduled launch time in ISO 8601 format <example>For example, 2021-10-06T08:27:05.215Z.</example><remarks> NOTE: Launch time can't be greater than scheduled end time </remarks>")
    environment_name: Optional[str] = Field(None, description="The name for the newly created environment. Environment name can contain any character including special character and spaces.")
    blueprint_name: str = Field(..., description="The blueprint name that should be used for creating the new environment.")
    owner_email: Optional[str] = Field(None, description="The email of the user that should be set as the owner of the new environment. if omitted the current user will be used.")
    description: Optional[str] = Field(None, description="The new environment description that will be presented in the Torque UI following the launch of the environment.")
    inputs: Optional[Dict[str, str]] = Field(None, description="Dictionary of key-value string pairs that will be used as values for the blueprint inputs. In case a value is not provided the input default value will be used. If a default value is not set, a validation error will be thrown upon launch. <example> For example: { \"region\": \"eu-west-1\", \"application version\": \"1.0.8\" } </example>")
    env_references_values: Optional[Dict[str, str]] = Field(None, description="Dictionary of key-value string pairs that will be used to assign values to blueprint's environment references. In case a value is not provided for a defined environment reference, a validation error will be thrown upon launch. <example> For example: { \"rds_env\": \"A1WV5HtQ8rhG\" } </example>")
    tags: Optional[Dict[str, str]] = Field(None, description="Environment blueprint tags /// Dictionary of key-value string pairs that will be used to tag deployed resources in the environment. In case a configured tag value is not provided the tag default value will be used. Note that tags that were configured in the account and space level will be set regardless of this field. <example> For example: { \"activity_type\": \"demo\"} </example>")
    labels: Optional[List[EnvironmentLabelRequest]] = None
    collaborators: Optional[CollaboratorsRequest] = None
    automation: Optional[bool] = Field(None, description="Indicates if the environment was launched from automation using integrated pipeline tool, For example: Jenkins, GitHub Actions and GitLal CI.")
    scheduled_end_time: Optional[str] = Field(None, description="Environment scheduled end time in ISO 8601 format <example>For example, 2021-10-06T08:27:05.215Z.</example><remarks> NOTE: Environment request cannot include both \"duration\" and \"scheduled_end_time\" fields. </remarks>")
    duration: Optional[str] = Field(None, description="Environment duration time in ISO 8601 format: \"P{days}DT{hours}H{minutes}M{seconds}S]]\" <example>For example, P0DT2H3M4S.</example><remarks> NOTE: Environment request cannot include both \"duration\" and \"scheduled_end_time\" fields. </remarks>")
    source: Optional[BlueprintSourceRequest] = Field(None, description="Additional details about the blueprint repository to be used. By default, this information is taken from the repository already confiured in the space.")
    workflows: Optional[List[LaunchWorkflowRequest]] = Field(None, description="Array of workflows that will be attached and enabled on the new environment.")
    resource_handles: Optional[Dict[str, str]] = Field(None, description="A mapping from grain name to cloud resource handle name")
    workflows_v2: Optional[List[InstantiateWorkflowRequest]] = Field(None, description="Array of workflows that will be attached and enabled on the new environment (new workflows)")
    entity_metadata: Optional[BoundedEntityMetadata] = None
    instantiation_name: Optional[str] = None
    enable_termination_protection: Optional[bool] = Field(None, description="Indicates if termination protection should be enabled on the new environment.")

__all__.append("ScheduleEnvironmentRequest")

class UpdateEnvironmentGrainsRequestV2(BaseModel):
    grains: Optional[List[GrainUpdateRequest]] = Field(None, description="List of grains to update.")
    grains_to_add: Optional[List[AddGrainRequest]] = Field(None, description="List of grains to add")
    grains_to_remove: Optional[List[str]] = Field(None, description="List of grains to remove")
    inputs: Optional[Dict[str, str]] = Field(None, description="Environment inputs to update")
    labels: Optional[List[EnvironmentLabelRequest]] = Field(None, description="Environment labels to add or update")
    removed_labels: Optional[List[EnvironmentLabelRequest]] = Field(None, description="Environment labels to remove")
    force: Optional[bool] = Field(None, description="Should update sandbox even if it conflicts with current running operation")
    replace_excluded_resources: Optional[bool] = Field(None, description="Should try to replace excluded reserved resources with non-excluded ones")

__all__.append("UpdateEnvironmentGrainsRequestV2")

class CollaboratorsGroupResponse(BaseModel):
    name: Optional[str] = None

__all__.append("CollaboratorsGroupResponse")

class CollaboratorsResponse(BaseModel):
    collaborators: Optional[List[UserResponse]] = None
    collaborators_groups: Optional[List[CollaboratorsGroupResponse]] = None
    all_space_members: Optional[bool] = None

__all__.append("CollaboratorsResponse")

class CreateEnvResponse(BaseModel):
    """Create environment response"""
    id: Optional[str] = Field(None, description="The id of the newly created environment")
    ticket_id: Optional[str] = None

__all__.append("CreateEnvResponse")

class EacCandidateResponse(BaseModel):
    repository_name: Optional[str] = None
    environment_file_name: Optional[str] = None
    errors: Optional[List[Error]] = None

__all__.append("EacCandidateResponse")

class EnvCost(BaseModel):
    """Environment cost information"""
    sum: Optional[float] = Field(None, description="Total cost sum")
    last_update: Optional[str] = Field(None, description="Time of the last update of environment cost")
    final: Optional[bool] = Field(None, description="Is the cost final")
    currency: Optional[str] = Field(None, description="Currency code in ISO 4217 format (3 letters like USD, EUR, GBP etc.)")
    incomplete: Optional[bool] = Field(None, description="Is the cost incomplete")

__all__.append("EnvCost")

class EnvironmentListItemDefinitionResponse(BaseModel):
    metadata: Optional[EnvironmentMetadataResponse] = None
    labels: Optional[List[EnvironmentLabelResponse]] = None

__all__.append("EnvironmentListItemDefinitionResponse")

class EnvironmentListItemDetailsResponse(BaseModel):
    definition: Optional[EnvironmentListItemDefinitionResponse] = None
    state: Optional[EnvironmentListItemStateResponse] = None
    computed_status: Optional[EnvironmentPhaseExternal] = Field(None, description="Environment Phase as presented to client")

__all__.append("EnvironmentListItemDetailsResponse")

class EnvironmentListItemResponse(BaseModel):
    id: Optional[str] = Field(None, description="Environment Id")
    owner: Optional[UserResponse] = Field(None, description="Owner details")
    initiator: Optional[UserResponse] = Field(None, description="Initiator details")
    collaborators_info: Optional[CollaboratorsResponse] = Field(None, description="Collaborators details")
    details: Optional[EnvironmentListItemDetailsResponse] = Field(None, description="Environment details")
    cost: Optional[EnvCost] = Field(None, description="Environment cost details")
    read_only: Optional[bool] = Field(None, description="Determines if user can perform actions on environment or not")
    last_used: Optional[str] = Field(None, description="Environment last used datetime")
    annotations: Optional[List[EnvironmentAnnotationResponse]] = Field(None, description="Environment annotations")
    is_workflow: Optional[bool] = None
    is_published: Optional[bool] = None
    entity_metadata: Optional[BoundedEntityMetadata] = None
    has_incoming_connections: Optional[bool] = None
    has_workflow_executions: Optional[bool] = None
    has_eac_history: Optional[bool] = None
    incoming_connections_count: Optional[int] = None
    workflows_attached_count: Optional[int] = None
    termination_protection_enabled: Optional[bool] = None
    eac: Optional[EnvironmentEacDataResponse] = None

__all__.append("EnvironmentListItemResponse")

class EnvironmentListItemStateResponse(BaseModel):
    current_state: Optional[str] = None
    execution: Optional[EnvironmentExecutionResponse] = None
    quick_links: Optional[List[EnvironmentOutputResponse]] = None
    outputs_count: Optional[int] = None
    drift: Optional[GrainDriftResponse] = None
    errors: Optional[List[EnvironmentErrorResponse]] = None

__all__.append("EnvironmentListItemStateResponse")

class EnvironmentResponse(BaseModel):
    """Environment information"""
    owner: Optional[UserResponse] = Field(None, description="Owner details")
    initiator: Optional[UserResponse] = Field(None, description="Initiator details")
    collaborators_info: Optional[CollaboratorsResponse] = Field(None, description="Collaborators details")
    is_workflow: Optional[bool] = None
    is_published: Optional[bool] = None
    details: Optional[EnvironmentDetailsResponse] = Field(None, description="Environment details")
    cost: Optional[EnvCost] = Field(None, description="Environment cost details")
    read_only: Optional[bool] = Field(None, description="Determines if user can perform actions on environment or not")
    last_used: Optional[str] = Field(None, description="Environment last used datetime")
    annotations: Optional[List[EnvironmentAnnotationResponse]] = Field(None, description="Environment annotations")
    entity_metadata: Optional[BoundedEntityMetadata] = Field(None, description="the entity metadata of which this workflow execution operates on. only if this env is workflow")
    workflow_instantiation_name: Optional[str] = None
    has_incoming_connections: Optional[bool] = None
    connections: Optional[ConnectionsResponse] = None
    incoming_connections_count: Optional[int] = None
    termination_protection_enabled: Optional[bool] = None
    reserved_resources: Optional[List[EnvironmentReservedResourceResponse]] = None
    eac: Optional[EnvironmentEacDataResponse] = None

__all__.append("EnvironmentResponse")

class EnvironmentsResponse(BaseModel):
    environment_list: Optional[List[EnvironmentListItemResponse]] = None
    paging_info: Optional[PagingInfoResponse] = None
    active_environments: Optional[int] = None
    user_environments: Optional[int] = None
    environments_with_errors: Optional[int] = None
    always_on_environments: Optional[int] = None

__all__.append("EnvironmentsResponse")

class ExtendEnvDurationResponse(BaseModel):
    ticket_id: Optional[str] = None

__all__.append("ExtendEnvDurationResponse")

class ImportEnvResponse(BaseModel):
    id: Optional[str] = Field(None, description="Environment ID")
    generated_blueprint_name: Optional[str] = None

__all__.append("ImportEnvResponse")

class ReleaseEnvResponse(BaseModel):
    """Release environment response"""
    ticket_id: Optional[str] = None
    id: Optional[str] = None

__all__.append("ReleaseEnvResponse")

class RepositoryDetailsResponse(BaseModel):
    repository_url: Optional[str] = None
    branch: Optional[str] = None
    errors: Optional[List[Error]] = None
    name: Optional[str] = None
    repository_type: Optional[RepositoryType] = None
    last_synced: Optional[str] = None
    status: Optional[RepositoryScanningStatus] = Field(None, description="possible values: NotAvailable, Connected, Syncing, SyncFailed, Disconnected")
    webhook_ids: Optional[List[str]] = None
    credentials: Optional[str] = None
    iac_assets_count: Optional[Dict[str, int]] = None
    space_name: Optional[str] = None
    agents: Optional[List[RepositoryAgentResponse]] = None
    use_all_agents: Optional[bool] = None
    eac_auto_registration: Optional[bool] = None

__all__.append("RepositoryDetailsResponse")

class ScheduleEnvironmentResponse(BaseModel):
    """Schedule environment response"""
    id: Optional[str] = Field(None, description="The id of the newly created and scheduled environment")
    ticket_id: Optional[str] = None

__all__.append("ScheduleEnvironmentResponse")

class CreateSpaceRequest(BaseModel):
    name: str = ...
    color: Optional[str] = Field(None, description="allowed values: darkGray, mediumGray, darkBlue, mediumBlue, blueGrey, darkGreen, frogGreen, pinkPurple, pinkBrown, lightGrey, pinkRed, midnightBlue")
    icon: Optional[str] = Field(None, description="allowed values: star, face, cloud, re, puzzle, uploadIcon, server, flow, pen, screen, suitcase, shovel")

__all__.append("CreateSpaceRequest")

class AuditEventActorResponse(BaseModel):
    type: Optional[str] = None
    details: Optional[Dict[str, Any]] = None

__all__.append("AuditEventActorResponse")

class PageInfoResponse(BaseModel):
    full_count: Optional[int] = None
    requested_page_size: Optional[int] = None
    requested_page: Optional[int] = None
    total_pages: Optional[int] = None

__all__.append("PageInfoResponse")

class PagedAuditEventsResponse(BaseModel):
    audit_events: Optional[List[StoredAuditEventResponse]] = None
    page_info: Optional[PageInfoResponse] = None

__all__.append("PagedAuditEventsResponse")

class StoredAuditEventResponse(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    scope: Optional[Dict[str, str]] = None
    data: Optional[Dict[str, Any]] = None
    actor: Optional[AuditEventActorResponse] = None
    timestamp: Optional[str] = None

__all__.append("StoredAuditEventResponse")

class LaunchScheduleRequest(BaseModel):
    scheduler: Optional[str] = None
    overridden: Optional[bool] = None

__all__.append("LaunchScheduleRequest")

class LaunchWorkflowRequest(BaseModel):
    name: Optional[str] = None
    schedules: Optional[List[LaunchScheduleRequest]] = None
    reminder: Optional[float] = None
    inputs_overrides: Optional[Dict[str, str]] = None

__all__.append("LaunchWorkflowRequest")

class CreateBlueprintRequest(BaseModel):
    blueprintDisplayName: Optional[str] = None
    blueprintYaml: Optional[str] = None
    isAsset: Optional[bool] = None

__all__.append("CreateBlueprintRequest")

class UpdateRepositoryRequest(BaseModel):
    credential_name: Optional[str] = None
    agents: Optional[List[str]] = None
    use_all_agents: Optional[bool] = None
    eac_auto_registration: Optional[bool] = None

__all__.append("UpdateRepositoryRequest")

class RepositoryAgentResponse(BaseModel):
    name: Optional[str] = None
    status: Optional[ComputeServiceStatus] = Field(None, description="possible values: Tentative, Active, Error")

__all__.append("RepositoryAgentResponse")

class RepositoryScanningStatus(BaseModel):
    """possible values: NotAvailable, Connected, Syncing, SyncFailed, Disconnected"""
    pass

class RepositoryType(BaseModel):
    pass

class BlueprintValidationRequest(BaseModel):
    blueprint_name: Optional[str] = Field(None, description="Blueprint name")
    blueprint_raw_64: Optional[str] = Field(None, description="Blueprint file content in a base64 encoding")

__all__.append("BlueprintValidationRequest")

class BlueprintSourceRequest(BaseModel):
    """Additional details about the blueprint repository to be used. By default, this information is taken from the repository already confiured in the space."""
    blueprint_name: Optional[str] = Field(None, description="Sandbox blueprint name")
    repository_name: Optional[str] = Field(None, description="The name of the repository to be used. This repository should be on-boarded to the space prior to launching the environment. In case you want to launch a \"Stored in Torque\" Blueprint, you should set this field to \"qtorque\"")
    blueprint_folder: Optional[str] = None
    branch: Optional[str] = Field(None, description="Use this field to provide a branch from which the blueprint yaml will be launched")
    commit: Optional[str] = Field(None, description="Use this field to provide a specific commit id from which the blueprint yaml will be launched")

__all__.append("BlueprintSourceRequest")

class EditBlueprintDisplayNameRequest(BaseModel):
    blueprint_name: Optional[str] = Field(None, description="Blueprint name")
    repository_name: Optional[str] = Field(None, description="repository name associated with the blueprint")
    display_name: Optional[str] = None

__all__.append("EditBlueprintDisplayNameRequest")

class EditBlueprintLabelsRequest(BaseModel):
    """Request to edit a blueprint's labels"""
    blueprint_name: Optional[str] = Field(None, description="Blueprint name")
    repository_name: Optional[str] = Field(None, description="repository name associated with the blueprint")
    labels: Optional[List[str]] = Field(None, description="names of the labels we want to have associated with this blueprint")

__all__.append("EditBlueprintLabelsRequest")

class EditBlueprintMetadataRequest(BaseModel):
    """Request to edit a blueprint's metadata"""
    blueprint_name: Optional[str] = Field(None, description="Blueprint name")
    repository_name: Optional[str] = Field(None, description="repository name associated with the blueprint")
    color: Optional[str] = Field(None, description="Blueprint color name corresponding to UI mapping")
    icon: Optional[str] = Field(None, description="Blueprint icon name corresponding to UI mapping")
    labels: Optional[List[str]] = Field(None, description="names of the labels we want to have associated with this blueprint")

__all__.append("EditBlueprintMetadataRequest")

class UpdateBlueprintLaunchAllowedRequest(BaseModel):
    blueprint_name: Optional[str] = Field(None, description="Blueprint name")
    space_name: Optional[str] = Field(None, description="Space name")
    repository_name: Optional[str] = Field(None, description="repository name associated with the blueprint")
    launch_allowed: Optional[bool] = None

__all__.append("UpdateBlueprintLaunchAllowedRequest")

class EnableEacRequest(BaseModel):
    eac_path: Optional[str] = None
    enable: Optional[bool] = None

__all__.append("EnableEacRequest")

class EnvEditSaveSessionRequest(BaseModel):
    content: Optional[str] = None

__all__.append("EnvEditSaveSessionRequest")

class EnvEditStartSessionRequest(BaseModel):
    environment_id: Optional[str] = None

__all__.append("EnvEditStartSessionRequest")

class GenerateBlueprintYamlFromAssetsRequest(BaseModel):
    iac_asset_names: Optional[List[str]] = None

__all__.append("GenerateBlueprintYamlFromAssetsRequest")

class AddLabelRequest(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = Field(None, description="allowed values: darkGray, frogGreen, pink, orange, blueGray, blue, bordeaux")
    quick_filter: Optional[bool] = None

__all__.append("AddLabelRequest")

class UpdateLabelRequest(BaseModel):
    original_name: Optional[str] = None
    name: Optional[str] = None
    color: Optional[str] = Field(None, description="allowed values: darkGray, frogGreen, pink, orange, blueGray, blue, bordeaux")
    quick_filter: Optional[bool] = None

__all__.append("UpdateLabelRequest")

class BlueprintApplicationForGetAllResponse(BaseModel):
    """Blueprint application information"""
    name: Optional[str] = Field(None, description="Application name")
    version: Optional[str] = Field(None, description="Application version")
    icon_url: Optional[str] = Field(None, description="URL of the application icon")

__all__.append("BlueprintApplicationForGetAllResponse")

class BlueprintForGetAllResponse(BaseModel):
    """Blueprint information"""
    enabled: Optional[bool] = Field(None, description="Indicates if the blueprint is published or not")
    launch_allowed: Optional[bool] = Field(None, description="Indicates if the blueprint launch is allowed or not")
    is_approval_required: Optional[bool] = Field(None, description="Indicates if the blueprint is published or not")
    services: Optional[List[BlueprintServiceForGetAllResponse]] = None
    environment_type: Optional[EnvironmentType] = Field(None, description="Blueprint environment type ('sandbox' or 'production')")
    blueprint_name: Optional[str] = Field(None, description="Blueprint name")
    name: Optional[str] = Field(None, description="Blueprint name")
    display_name: Optional[str] = Field(None, description="Blueprint name")
    relative_path: Optional[str] = Field(None, description="The relative path of the blueprint inside the repository. For examples: \"blueprints\" -> if its the default blueprints folder in the repo \"myCustomFolder/myBlueprintFolder\" -> a folder in the repo that has \".blueprints\" marker file in it")
    repository_name: Optional[str] = Field(None, description="Blueprint's repository name")
    repository_branch: Optional[str] = Field(None, description="Blueprint's repository branch")
    commit: Optional[str] = Field(None, description="Blueprint's repository branch")
    last_synced: Optional[str] = Field(None, description="Blueprint's repository branch")
    repository_url: Optional[str] = Field(None, description="Blueprint's repository url")
    is_editable: Optional[bool] = Field(None, description="Is the blueprint editable")
    description: Optional[str] = Field(None, description="Blueprint description")
    spec_version: Optional[str] = Field(None, description="Blueprint spec version")
    url: Optional[str] = Field(None, description="URL to blueprint yaml file in source repository")
    inputs: Optional[List[BlueprintInputResponse]] = None
    last_modified: Optional[str] = Field(None, description="Last modification date and time of the blueprint")
    modified_by: Optional[str] = Field(None, description="Name of the last user who modified the blueprint")
    grains: Optional[List[BlueprintGrainForList]] = None
    environment: Optional[EnvironmentForList] = None
    applications: Optional[List[BlueprintApplicationForGetAllResponse]] = None
    clouds: Optional[List[CloudResponse]] = None
    is_sample: Optional[bool] = Field(None, description="Indicates if the blueprint is a sample blueprint")
    artifacts: Optional[Dict[str, str]] = Field(None, description="Artifact files of the blueprint applications <remarks>Maps application name to its relative artifacts path in the space</remarks>")
    errors: Optional[List[Error]] = None
    tags: Optional[List[BlueprintTagResponse]] = None
    policies: Optional[BlueprintPolicyResponse] = Field(None, description="Blueprint policy response")
    cost: Optional[BlueprintCostResponse] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    favorite: Optional[bool] = None
    custom_icon: Optional[BlueprintCustomIcon] = None
    labels: Optional[List[BlueprintLabel]] = None
    num_of_active_environments: Optional[int] = None
    asset_library: Optional[bool] = None
    sub_type: Optional[str] = None
    scope: Optional[str] = None
    iac_asset: Optional[bool] = None
    iac_asset_type: Optional[str] = None
    links: Optional[List[Hyperlink]] = None

__all__.append("BlueprintForGetAllResponse")

class BlueprintInputResponse(BaseModel):
    """Blueprint input information"""
    name: Optional[str] = Field(None, description="Input name")
    default_value: Optional[str] = Field(None, description="When the sandbox is created, Torque automatically populates the input with this value. <remarks> User can choose to edit the value or leave it as-is </remarks>")
    display_style: Optional[str] = Field(None, description="Indicates how to display the input value in UI <remarks> - To display the input value in plain text in the UI, do not assign a value.<br /> - To hide the input value behind bullets, enter the value \"masked\". </remarks>")
    description: Optional[str] = Field(None, description="Input description")
    optional: Optional[bool] = Field(None, description="Indicates if the input is optional or not <remarks> - When optional is set to true, the user can leave the parameter empty.<br /> - When optional is set to false, empty value(s) will result in validation error(s). </remarks>")
    possible_values: Optional[List[str]] = Field(None, description="Possible values for the input <remarks> - Possible_values are optional - The default value is one of the possible values - Possible values must be unique </remarks>")

__all__.append("BlueprintInputResponse")

class BlueprintPolicyResponse(BaseModel):
    """Blueprint policy response"""
    max_duration: Optional[str] = Field(None, description="Max duration of environment in ISO 8601 format: P{days}DT{hours}H{minutes}M{seconds}S] (for example, 'P0DT2H3M4S')")
    default_duration: Optional[str] = Field(None, description="Default duration of environment in ISO 8601 format: P{days}DT{hours}H{minutes}M{seconds}S] (for example, 'P0DT2H3M4S')")
    default_extend: Optional[str] = Field(None, description="Default Extend of environment in ISO 8601 format: P{days}DT{hours}H{minutes}M{seconds}S] (for example, 'P0DT2H3M4S')")
    max_active_environments: Optional[int] = Field(None, description="Max active environments that can be launched from the blueprint")
    always_on: Optional[bool] = Field(None, description="When True, the environment will always be on, when False, it will be ephemeral.")
    allow_scheduling: Optional[bool] = Field(None, description="When True, the environment may be scheduled.")

__all__.append("BlueprintPolicyResponse")

class BlueprintServiceForGetAllResponse(BaseModel):
    """Blueprint service information"""
    name: Optional[str] = Field(None, description="Service name <remarks>A service folder and YAML with this name should reside in the \"/services\" folder in the blueprint YAML’s repository</remarks>")
    type: Optional[str] = Field(None, description="Service type (e.g. \"Terraform\")")

__all__.append("BlueprintServiceForGetAllResponse")

class BlueprintSimplifiedListItemResponse(BaseModel):
    name: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    repository: Optional[str] = None
    icon: Optional[str] = None
    custom_icon: Optional[BlueprintCustomIcon] = None
    in_designer_library: Optional[bool] = None

__all__.append("BlueprintSimplifiedListItemResponse")

class BlueprintTagResponse(BaseModel):
    name: Optional[str] = None
    default_value: Optional[str] = None
    possible_values: Optional[List[str]] = None
    description: Optional[str] = None

__all__.append("BlueprintTagResponse")

class CatalogForGetAllResponse(BaseModel):
    """Published blueprint information

<remarks>

Published blueprint is a blueprint that is available in blueprint catalog

</remarks>"""
    launch_allowed: Optional[bool] = Field(None, description="Blueprint launch allowed")
    blueprint_name: Optional[str] = Field(None, description="Blueprint name")
    name: Optional[str] = Field(None, description="Blueprint name")
    display_name: Optional[str] = Field(None, description="Blueprint name")
    relative_path: Optional[str] = Field(None, description="The relative path of the blueprint inside the repository. For examples: \"blueprints\" -> if its the default blueprints folder in the repo \"myCustomFolder/myBlueprintFolder\" -> a folder in the repo that has \".blueprints\" marker file in it")
    repository_name: Optional[str] = Field(None, description="Blueprint's repository name")
    repository_branch: Optional[str] = Field(None, description="Blueprint's repository branch")
    commit: Optional[str] = Field(None, description="Blueprint's repository branch")
    last_synced: Optional[str] = Field(None, description="Blueprint's repository branch")
    repository_url: Optional[str] = Field(None, description="Blueprint's repository url")
    is_editable: Optional[bool] = Field(None, description="Is the blueprint editable")
    description: Optional[str] = Field(None, description="Blueprint description")
    spec_version: Optional[str] = Field(None, description="Blueprint spec version")
    url: Optional[str] = Field(None, description="URL to blueprint yaml file in source repository")
    inputs: Optional[List[BlueprintInputResponse]] = None
    last_modified: Optional[str] = Field(None, description="Last modification date and time of the blueprint")
    modified_by: Optional[str] = Field(None, description="Name of the last user who modified the blueprint")
    grains: Optional[List[BlueprintGrainForList]] = None
    environment: Optional[EnvironmentForList] = None
    applications: Optional[List[BlueprintApplicationForGetAllResponse]] = None
    clouds: Optional[List[CloudResponse]] = None
    is_sample: Optional[bool] = Field(None, description="Indicates if the blueprint is a sample blueprint")
    artifacts: Optional[Dict[str, str]] = Field(None, description="Artifact files of the blueprint applications <remarks>Maps application name to its relative artifacts path in the space</remarks>")
    errors: Optional[List[Error]] = None
    tags: Optional[List[BlueprintTagResponse]] = None
    policies: Optional[BlueprintPolicyResponse] = Field(None, description="Blueprint policy response")
    cost: Optional[BlueprintCostResponse] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    favorite: Optional[bool] = None
    custom_icon: Optional[BlueprintCustomIcon] = None
    labels: Optional[List[BlueprintLabel]] = None
    num_of_active_environments: Optional[int] = None
    asset_library: Optional[bool] = None
    sub_type: Optional[str] = None
    scope: Optional[str] = None
    iac_asset: Optional[bool] = None
    iac_asset_type: Optional[str] = None
    links: Optional[List[Hyperlink]] = None

__all__.append("CatalogForGetAllResponse")

class CloudComputeServiceResponse(BaseModel):
    """Cloud compute service information"""
    name: Optional[str] = Field(None, description="Cloud compute service name")
    type: Optional[str] = Field(None, description="Cloud compute service type (EC2, Azure virtual machine, AKS, EKS, etc.)")
    created_date: Optional[str] = Field(None, description="Cloud compute service creation date and time")
    created_by: Optional[str] = Field(None, description="User name of the cloud compute service owner")
    user_defined: Optional[bool] = Field(None, description="Indicates if the cloud compute service created automatically or defined by the user<br /><example>EC2 and Azure VM are not user defined while K8s, EKS and AKS are user-defined.</example>")

__all__.append("CloudComputeServiceResponse")

class CloudRegionResponse(BaseModel):
    """Cloud region information"""
    id: Optional[str] = Field(None, description="Cloud region ID")
    name: Optional[str] = Field(None, description="Cloud region name")

__all__.append("CloudRegionResponse")

class CloudResponse(BaseModel):
    """Cloud account or Kubernetes compute service information"""
    provider: Optional[str] = Field(None, description="Cloud provider name")
    cloud_account_name: Optional[str] = Field(None, description="Cloud account name")
    compute_service: Optional[CloudComputeServiceResponse] = Field(None, description="Cloud compute service information")
    region: Optional[CloudRegionResponse] = Field(None, description="Cloud region information")

__all__.append("CloudResponse")

class EacResponse(BaseModel):
    url: Optional[str] = None
    environment_name: Optional[str] = None
    environment_id: Optional[str] = None
    owner_email: Optional[str] = None
    blueprint_name: Optional[str] = None
    inputs: Optional[Dict[str, str]] = None
    status: Optional[str] = None
    file_applied: Optional[bool] = None
    registered: Optional[bool] = None
    deleted_from_repository: Optional[bool] = None
    errors: Optional[List[Error]] = Field(None, description="Errors as result of applying the environment file")
    validation_errors: Optional[List[Error]] = Field(None, description="Errors validating the environment file")
    enabled: Optional[bool] = None

__all__.append("EacResponse")

class EnvEditListSessionsResponse(BaseModel):
    sessions: Optional[List[EnvEditSessionListItemResponse]] = None

__all__.append("EnvEditListSessionsResponse")

class EnvEditPlanCommitDiffResponse(BaseModel):
    diff_type: Optional[PlanDiffType] = Field(None, description="possible values: Unchanged, Added, Deleted, Updated")
    value: Optional[str] = None
    old_value: Optional[str] = None

__all__.append("EnvEditPlanCommitDiffResponse")

class EnvEditPlanDependenciesDiffResponse(BaseModel):
    diff_type: Optional[PlanDiffType] = Field(None, description="possible values: Unchanged, Added, Deleted, Updated")
    value: Optional[str] = None

__all__.append("EnvEditPlanDependenciesDiffResponse")

class EnvEditPlanGrainDiffResponse(BaseModel):
    kind: Optional[str] = None
    name: Optional[str] = None
    diff_type: Optional[PlanDiffType] = Field(None, description="possible values: Unchanged, Added, Deleted, Updated")
    inputs: Optional[List[EnvEditPlanInputsDiffResponse]] = None
    dependencies: Optional[List[EnvEditPlanDependenciesDiffResponse]] = None
    commit: Optional[EnvEditPlanCommitDiffResponse] = None

__all__.append("EnvEditPlanGrainDiffResponse")

class EnvEditPlanInputsDiffResponse(BaseModel):
    diff_type: Optional[PlanDiffType] = Field(None, description="possible values: Unchanged, Added, Deleted, Updated")
    name: Optional[str] = None
    value: Optional[str] = None
    old_value: Optional[str] = None

__all__.append("EnvEditPlanInputsDiffResponse")

class EnvEditPlanResponse(BaseModel):
    grains: Optional[List[EnvEditPlanGrainDiffResponse]] = None
    inputs: Optional[List[EnvEditPlanInputsDiffResponse]] = None

__all__.append("EnvEditPlanResponse")

class EnvEditSessionListItemResponse(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    environment_id: Optional[str] = None

__all__.append("EnvEditSessionListItemResponse")

class IACAssetDetailResponse(BaseModel):
    commit: Optional[str] = None
    last_sync: Optional[str] = None
    modified_by: Optional[str] = None
    name: Optional[str] = None
    iac_resource_type: Optional[str] = None
    path: Optional[str] = None
    repository_type: Optional[str] = None
    repository: Optional[str] = None
    repository_url: Optional[str] = None
    branch: Optional[str] = None
    icon: Optional[str] = None
    custom_icon: Optional[BlueprintCustomIcon] = None
    labels: Optional[List[BlueprintLabel]] = None
    in_catalog: Optional[bool] = None
    in_designer_library: Optional[bool] = None
    average_hourly_cost: Optional[float] = None
    link: Optional[str] = None
    in_error: Optional[bool] = None
    blueprint_count: Optional[int] = None
    workflow_count: Optional[int] = None
    environment_count: Optional[int] = None
    total_usage_count: Optional[int] = None

__all__.append("IACAssetDetailResponse")

class IACAssetListItemResponse(BaseModel):
    name: Optional[str] = None
    iac_resource_type: Optional[str] = None
    path: Optional[str] = None
    repository_type: Optional[str] = None
    repository: Optional[str] = None
    repository_url: Optional[str] = None
    branch: Optional[str] = None
    icon: Optional[str] = None
    custom_icon: Optional[BlueprintCustomIcon] = None
    labels: Optional[List[BlueprintLabel]] = None
    in_catalog: Optional[bool] = None
    in_designer_library: Optional[bool] = None
    average_hourly_cost: Optional[float] = None
    link: Optional[str] = None
    in_error: Optional[bool] = None
    blueprint_count: Optional[int] = None
    workflow_count: Optional[int] = None
    environment_count: Optional[int] = None
    total_usage_count: Optional[int] = None

__all__.append("IACAssetListItemResponse")

class IACAssetListMetricsResponse(BaseModel):
    iac_asset_type_and_count: Optional[Dict[str, int]] = None
    repositories: Optional[List[IACAssetListMetricsResponse_IACAssetListMetricsRepository]] = None
    invalid_count: Optional[int] = None
    total_count: Optional[int] = None

__all__.append("IACAssetListMetricsResponse")

class IACAssetListMetricsResponse_IACAssetListMetricsRepository(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    connected: Optional[bool] = None

__all__.append("IACAssetListMetricsResponse_IACAssetListMetricsRepository")

class IACAssetSimplifiedListItemResponse(BaseModel):
    name: Optional[str] = None
    iac_resource_type: Optional[str] = None
    display_name: Optional[str] = None
    path: Optional[str] = None
    repository: Optional[str] = None
    icon: Optional[str] = None
    custom_icon: Optional[BlueprintCustomIcon] = None
    in_designer_library: Optional[bool] = None

__all__.append("IACAssetSimplifiedListItemResponse")

class InstructionsResponse(BaseModel):
    text: Optional[str] = None
    url: Optional[str] = None

__all__.append("InstructionsResponse")

class Hyperlink(BaseModel):
    """Links to API"""
    rel: Optional[str] = Field(None, description="Link relation type that describes how the current context (source) is related to the target resource")
    href: Optional[str] = Field(None, description="URI link to the API")
    method: Optional[str] = Field(None, description="HTTP method (GET, POST, PUT, etc.)")

__all__.append("Hyperlink")

class LongTokenSafeResponse(BaseModel):
    id: Optional[str] = None
    user: Optional[str] = None
    title: Optional[str] = None
    created_at: Optional[str] = None

__all__.append("LongTokenSafeResponse")

class PagedIACAssetListItemResponse(BaseModel):
    iac_assets: Optional[List[IACAssetListItemResponse]] = None
    paging_info: Optional[PagingInfoResponse] = None

__all__.append("PagedIACAssetListItemResponse")

class PagedSimplifiedBlueprintListItemResponse(BaseModel):
    blueprints: Optional[List[BlueprintSimplifiedListItemResponse]] = None
    paging_info: Optional[PagingInfoResponse] = None

__all__.append("PagedSimplifiedBlueprintListItemResponse")

class PagedSimplifiedIACAssetListItemResponse(BaseModel):
    iac_assets: Optional[List[IACAssetSimplifiedListItemResponse]] = None
    paging_info: Optional[PagingInfoResponse] = None

__all__.append("PagedSimplifiedIACAssetListItemResponse")

class PlanDiffType(BaseModel):
    """possible values: Unchanged, Added, Deleted, Updated"""
    pass

class TokenResponse(BaseModel):
    """Describes the authentication server response if the request for an access token is valid

<remarks>

 Contains access token and some additional properties about the authorization

</remarks>"""
    access_token: Optional[str] = Field(None, description="Access token string as issued by the authorization server")
    refresh_token: Optional[str] = Field(None, description="Refresh token to be used to extend existing session")
    token_type: Optional[str] = Field(None, description="Token type, typically just the string \"bearer\"")
    expires_in: Optional[int] = Field(None, description="Access token validity period")

__all__.append("TokenResponse")

class UserResponse(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    timezone: Optional[str] = None
    email: Optional[str] = None
    join_date: Optional[str] = None
    display_first_name: Optional[str] = None
    display_last_name: Optional[str] = None

__all__.append("UserResponse")

class BoundedEntityMetadata(BaseModel):
    type: str = ...

__all__.append("BoundedEntityMetadata")

class ComputeServiceDetailsResponse(BaseModel):
    service_type: Optional[str] = None
    type: Optional[str] = None

__all__.append("ComputeServiceDetailsResponse")

class ComputeServiceResponse(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quali_owned: Optional[bool] = None
    is_sample: Optional[bool] = None
    type: Optional[str] = None
    create_date: Optional[str] = None
    create_user: Optional[str] = None
    status: Optional[ComputeServiceStatus] = Field(None, description="possible values: Tentative, Active, Error")
    spaces: Optional[List[str]] = None
    errors: Optional[List[Error]] = None
    additional_details: Optional[ComputeServiceDetailsResponse] = None
    last_keep_alive: Optional[str] = None

__all__.append("ComputeServiceResponse")

class ComputeServiceStatus(BaseModel):
    """possible values: Tentative, Active, Error"""
    pass

class InfraSettingsResponse(BaseModel):
    service_type: Optional[str] = None

__all__.append("InfraSettingsResponse")

class CreateComputeServiceRequest(BaseModel):
    service_type: str = ...
    service_name: str = ...
    quali_owned: Optional[bool] = None
    is_sample: Optional[bool] = None

__all__.append("CreateComputeServiceRequest")

class K8sSpaceAssociationSpec(BaseModel):
    type: Optional[str] = None
    default_namespace: Optional[str] = None
    default_service_account: Optional[str] = None

__all__.append("K8sSpaceAssociationSpec")

class UpdateComputeServiceDetails(BaseModel):
    type: str = ...

__all__.append("UpdateComputeServiceDetails")

class UpdateComputeServiceRequest(BaseModel):
    service_name: str = ...
    description: Optional[str] = None
    details: Optional[UpdateComputeServiceDetails] = None

__all__.append("UpdateComputeServiceRequest")

class ComputeServiceUsagesResponse(BaseModel):
    agent_name: Optional[str] = None
    active_environments_count: Optional[int] = None
    spaces: Optional[List[str]] = None
    repositories: Optional[List[str]] = None

__all__.append("ComputeServiceUsagesResponse")

class SpaceComputeServiceResponse(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    create_date: Optional[str] = None
    create_user: Optional[str] = None
    status: Optional[ComputeServiceStatus] = Field(None, description="possible values: Tentative, Active, Error")
    spec: Optional[InfraSettingsResponse] = None
    errors: Optional[List[Error]] = None
    last_keep_alive: Optional[str] = None
    additional_details: Optional[ComputeServiceDetailsResponse] = None
    quali_owned: Optional[bool] = None

__all__.append("SpaceComputeServiceResponse")

class AssetDefinition(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    dependsOn: Optional[List[str]] = None
    inputs: Optional[Dict[str, Any]] = None
    environmentVariables: Optional[Dict[str, Any]] = None
    outputs: Optional[Dict[str, Any]] = None
    credentials: Optional[List[str]] = None
    repositorySource: Optional[ElementSource] = None
    repositorySources: Optional[List[ElementSource]] = None
    workspaceDirectories: Optional[List[ElementSource]] = None
    environmentLabels: Optional[EnvironmentLabels] = None
    computeService: Optional[str] = Field(None, description="Compute service id")
    executionHost: Optional[str] = None
    cloudAccountName: Optional[str] = None
    scriptsNames: Optional[List[str]] = None
    kubeConfigDetails: Optional[KubeConfigDetails] = Field(None, description="Kube config for grains that require custom permissions to kubernetes cluster")
    policiesEnforcements: Optional[List[PolicyEnforcement]] = None

__all__.append("AssetDefinition")

class AssetDriftResponse(BaseModel):
    detected: Optional[bool] = None
    dismissed: Optional[bool] = None
    deployed_commit_sha: Optional[str] = None
    latest_commit_sha: Optional[str] = None

__all__.append("AssetDriftResponse")

class EnvironmentWorkflowResponse(BaseModel):
    next_occurrence: Optional[str] = None
    name: Optional[str] = None
    display_name: Optional[str] = None
    occurrences: Optional[List[WorkflowOccurrence]] = None

__all__.append("EnvironmentWorkflowResponse")

class WorkflowActionExecutionResponse(BaseModel):
    status: Optional[str] = None
    log: Optional[str] = None
    start: Optional[str] = None
    duration: Optional[str] = None
    grain_path: Optional[str] = None
    resource_identifier: Optional[str] = None
    action_id: Optional[str] = None
    error_response: Optional[ErrorResponse] = None

__all__.append("WorkflowActionExecutionResponse")

class WorkflowExecutionStepResponse(BaseModel):
    name: Optional[str] = None
    state: Optional[str] = None
    status: Optional[str] = None
    executed: Optional[bool] = None
    actions: Optional[List[WorkflowActionExecutionResponse]] = None

__all__.append("WorkflowExecutionStepResponse")

class WorkflowOccurrence(BaseModel):
    state: Optional[str] = None
    status: Optional[str] = None
    create_date: Optional[str] = None
    end_date: Optional[str] = None
    actions: Optional[List[WorkflowActionExecutionResponse]] = None
    steps: Optional[List[WorkflowExecutionStepResponse]] = None
    is_manual: Optional[bool] = None
    is_delayed: Optional[bool] = None
    reason: Optional[str] = None

__all__.append("WorkflowOccurrence")

class BlueprintLayoutResponse(BaseModel):
    store: Optional[str] = None
    path: Optional[str] = None
    exclude_from_layout: Optional[List[str]] = None
    errors: Optional[List[Error]] = None

__all__.append("BlueprintLayoutResponse")

class CollaboratorsFeedData(BaseModel):
    all_space_members: Optional[bool] = None
    collaborators_emails: Optional[List[str]] = None
    collaborators_groups: Optional[List[str]] = None

__all__.append("CollaboratorsFeedData")

class ConnectedEnvironmentResponse(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    space_name: Optional[str] = None
    execution_type: Optional[ExecutionType] = Field(None, description="possible values: GitOpsEnvironment, ManagedEnvironment, Workflow")
    read_only: Optional[bool] = None
    eac_path: Optional[str] = None
    status: Optional[str] = None
    outputs: Optional[List[EnvironmentOutputResponse]] = None

__all__.append("ConnectedEnvironmentResponse")

class ConnectionsResponse(BaseModel):
    outgoing_connections: Optional[List[ConnectedEnvironmentResponse]] = None
    outgoing_connections_count: Optional[int] = None
    incoming_connections: Optional[List[ConnectedEnvironmentResponse]] = None
    incoming_connections_count: Optional[int] = None

__all__.append("ConnectionsResponse")

class DeploymentDriftResponse(BaseModel):
    detected: Optional[bool] = None

__all__.append("DeploymentDriftResponse")

class EnvironmentAnnotationResponse(BaseModel):
    """Annotation Response that return to the UI.

Result of combining the info from:

Quali.Colony.Services.Environments.Domain.Annotations.EnvironmentAnnotation.cs

+

Quali.Colony.Services.Environments.Domain.Annotations.EnvironmentAnnotationDefinition.cs"""
    key: Optional[str] = None
    value: Optional[str] = None
    color: Optional[Color] = Field(None, description="possible values: FrogGreen, Grey")
    filterable: Optional[bool] = None
    last_updated: Optional[str] = None

__all__.append("EnvironmentAnnotationResponse")

class EnvironmentDefinitionResponse(BaseModel):
    metadata: Optional[EnvironmentMetadataResponse] = None
    inputs: Optional[List[EnvironmentNameValueResponse]] = None
    env_references: Optional[List[EnvironmentEnvReferenceResponse]] = None
    instructions: Optional[InstructionsResponse] = None
    layout: Optional[BlueprintLayoutResponse] = None
    tags: Optional[List[SandboxTag]] = None
    labels: Optional[List[EnvironmentLabelResponse]] = None

__all__.append("EnvironmentDefinitionResponse")

class EnvironmentDetailsResponse(BaseModel):
    state: Optional[EnvironmentStateResponse] = None
    id: Optional[str] = None
    definition: Optional[EnvironmentDefinitionResponse] = None
    computed_status: Optional[EnvironmentPhaseExternal] = Field(None, description="Environment Phase as presented to client")
    estimated_launch_duration_in_seconds: Optional[int] = None

__all__.append("EnvironmentDetailsResponse")

class EnvironmentEacDataResponse(BaseModel):
    url: Optional[str] = None
    status: Optional[str] = None
    eac_synced: Optional[bool] = None
    registered: Optional[bool] = None
    enabled: Optional[bool] = None
    errors: Optional[List[Error]] = None
    validation_errors: Optional[List[Error]] = None
    inputs: Optional[Dict[str, str]] = None

__all__.append("EnvironmentEacDataResponse")

class EnvironmentEnvReferenceResponse(BaseModel):
    reference_name: Optional[str] = None
    reference_value: Optional[str] = None
    reference_display_value: Optional[str] = None

__all__.append("EnvironmentEnvReferenceResponse")

class EnvironmentErrorResponse(BaseModel):
    message: Optional[str] = None

__all__.append("EnvironmentErrorResponse")

class EnvironmentExecutionResponse(BaseModel):
    retention: Optional[IEnvironmentExecutionRetentionResponse] = None
    start_time: Optional[str] = None
    scheduled_launch_time: Optional[str] = None
    scheduled_end_time: Optional[str] = None
    end_time: Optional[str] = None

__all__.append("EnvironmentExecutionResponse")

class EnvironmentFeedDetails(BaseModel):
    type: Optional[str] = None

__all__.append("EnvironmentFeedDetails")

class EnvironmentFeedResponse(BaseModel):
    space_name: Optional[str] = None
    sandbox_id: Optional[str] = Field(None, description="Obsolete")
    environment_id: Optional[str] = None
    sandbox_name: Optional[str] = Field(None, description="Obsolete")
    environment_name: Optional[str] = None
    start_time: Optional[str] = None
    owner_name: Optional[str] = None
    actor: Optional[str] = None
    feed_type: Optional[str] = None
    grain_path: Optional[str] = None
    duration: Optional[str] = None
    is_drift_detected: Optional[bool] = None
    collaborators: Optional[CollaboratorsFeedData] = None
    workflow_name: Optional[str] = None
    resource_action: Optional[ResourceActionData] = None
    request_name: Optional[str] = None
    details: Optional[EnvironmentFeedDetails] = None

__all__.append("EnvironmentFeedResponse")

class EnvironmentGrainActivityResponse(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    log: Optional[str] = None
    execution: Optional[TimeDataResponse] = None
    errors: Optional[List[EnvironmentErrorResponse]] = None

__all__.append("EnvironmentGrainActivityResponse")

class EnvironmentGrainResponse(BaseModel):
    state: Optional[EnvironmentGrainStateResponse] = None
    asset: Optional[GrainAssetResponse] = None
    id: Optional[str] = None
    name: Optional[str] = None
    path: Optional[str] = None
    kind: Optional[str] = None
    imported: Optional[bool] = None
    execution_host: Optional[str] = None
    details: Optional[GrainDetailsResponse] = None
    sources: Optional[List[GrainSourceResponse]] = Field(None, description="Grain sources, some grains have one source and some have a few (like shell or K8S)")
    workspace_directories: Optional[List[GrainSourceResponse]] = None
    depends_on: Optional[List[str]] = None
    inputs: Optional[List[GrainInputResponse]] = None

__all__.append("EnvironmentGrainResponse")

class EnvironmentGrainStageDetails(BaseModel):
    Type: str = ...

__all__.append("EnvironmentGrainStageDetails")

class EnvironmentGrainStageResponse(BaseModel):
    id: Optional[str] = None
    runner_id: Optional[str] = None
    name: Optional[str] = None
    execution: Optional[TimeDataResponse] = None
    activities: Optional[List[EnvironmentGrainActivityResponse]] = None
    errors: Optional[List[EnvironmentErrorResponse]] = None
    details: Optional[EnvironmentGrainStageDetails] = None

__all__.append("EnvironmentGrainStageResponse")

class EnvironmentGrainStateResponse(BaseModel):
    storage_name: Optional[str] = None
    stages: Optional[List[EnvironmentGrainStageResponse]] = None
    current_state: Optional[GrainPhaseExternal] = Field(None, description="possible values: Deployed, DeployFailed, Deploying, Importing, Releasing, Terminating, Terminated, Updating, Pending, WaitingApproval")
    drift: Optional[GrainDriftResponse] = None

__all__.append("EnvironmentGrainStateResponse")

class EnvironmentMetadataResponse(BaseModel):
    name: Optional[str] = None
    space_name: Optional[str] = None
    automation: Optional[bool] = None
    eac_url: Optional[str] = None
    blueprint: Optional[str] = None
    blueprint_name: Optional[str] = None
    blueprint_display_name: Optional[str] = None
    blueprint_inputs: Optional[List[BlueprintInputParameterResponse]] = None
    blueprint_commit: Optional[str] = None
    repository_name: Optional[str] = None
    blueprint_branch: Optional[str] = None
    blueprint_folder: Optional[str] = None
    inline_blueprint: Optional[bool] = Field(None, description="Indicates that the environment definition was changed, diverged from the original blueprint, and the new version is saved 'inline', in the environment.")

__all__.append("EnvironmentMetadataResponse")

class EnvironmentNameValueResponse(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

__all__.append("EnvironmentNameValueResponse")

class EnvironmentOutputResponse(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None
    kind: Optional[str] = None
    quick: Optional[bool] = None
    pattern: Optional[str] = None

__all__.append("EnvironmentOutputResponse")

class EnvironmentPhase(RootModel[str]):
    """Environment phase as a string from API (flexible)."""
    pass

class EnvironmentPhaseExternal(RootModel[str]):
    """External environment phase as string (e.g., 'Ended')."""
    pass

class EnvironmentReservedResourceResponse(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    excluded_from_reserving: Optional[bool] = None
    excluded_from_reserving_reason: Optional[str] = None

__all__.append("EnvironmentReservedResourceResponse")

class EnvironmentStateResponse(BaseModel):
    grains: Optional[List[EnvironmentGrainResponse]] = None
    current_state: Optional[EnvironmentPhase] = Field(None, description="possible values: Initialized, PendingApproval, LaunchScheduled, Approved, Deploying, Importing, Active, Inactive, Terminating, Releasing, Updating, Aborted")
    execution: Optional[EnvironmentExecutionResponse] = None
    errors: Optional[List[EnvironmentErrorResponse]] = None
    outputs: Optional[List[EnvironmentOutputResponse]] = None
    eac_synced: Optional[bool] = None

__all__.append("EnvironmentStateResponse")

class ExecutionType(BaseModel):
    """possible values: GitOpsEnvironment, ManagedEnvironment, Workflow"""
    pass

class GrainAssetResponse(BaseModel):
    asset_name: Optional[str] = None
    asset_id: Optional[str] = None
    icon: Optional[str] = None
    custom_icon: Optional[BlueprintCustomIcon] = None

__all__.append("GrainAssetResponse")

class GrainDetailsResponse(BaseModel):
    type: str = ...

__all__.append("GrainDetailsResponse")

class GrainDriftResponse(BaseModel):
    deployment: Optional[DeploymentDriftResponse] = None
    asset: Optional[AssetDriftResponse] = None

__all__.append("GrainDriftResponse")

class GrainInputResponse(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None
    pattern: Optional[str] = None
    sensitive: Optional[bool] = None

__all__.append("GrainInputResponse")

class GrainSourceResponse(BaseModel):
    store: Optional[str] = None
    path: Optional[str] = None
    full_path: Optional[str] = None
    branch: Optional[str] = None
    commit: Optional[str] = None
    commit_date: Optional[str] = None
    author: Optional[str] = None
    commit_message: Optional[str] = None
    is_default_branch: Optional[bool] = None
    is_last_commit: Optional[bool] = None

__all__.append("GrainSourceResponse")

class GrainPhaseExternal(RootModel[str]):
    """Grain external phase as string (e.g., 'Terminated')."""
    pass

class IEnvironmentExecutionRetentionResponse(BaseModel):
    kind: Optional[str] = Field(None, description="The Retention kind")

__all__.append("IEnvironmentExecutionRetentionResponse")

class AttachEnvironmentLabelsRequest(BaseModel):
    added_labels: Optional[List[EnvironmentLabelRequest]] = None
    removed_labels: Optional[List[EnvironmentLabelRequest]] = None

__all__.append("AttachEnvironmentLabelsRequest")

class EnvironmentLabelRequest(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

__all__.append("EnvironmentLabelRequest")

class EnvironmentLabelResponse(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None
    system_label: Optional[bool] = Field(None, alias="system-label")
    origin: Optional[LabelOrigins] = Field(None, description="possible values: User, Blueprint, Automation")
    shared: Optional[bool] = None

__all__.append("EnvironmentLabelResponse")

class LabelOrigins(BaseModel):
    """possible values: User, Blueprint, Automation"""
    pass

class ExtendEnvironment(BaseModel):
    duration: Optional[str] = None

__all__.append("ExtendEnvironment")

class InstantiateWorkflowRequest(BaseModel):
    """Used by API"""
    blueprint_name: Optional[str] = None
    blueprint_store: Optional[str] = None
    cron_expression: Optional[List[str]] = None
    inputs: Optional[Dict[str, str]] = Field(None, description="The workflow inputs that the user send with the launch request")
    env_references_values: Optional[Dict[str, str]] = Field(None, description="The values for workflow's environment references that the user send with the launch request")
    enabled: Optional[bool] = None

__all__.append("InstantiateWorkflowRequest")

class ParameterDriftType(BaseModel):
    """possible values: Added, Updated, Deleted"""
    pass

class PolicyEnforcement(BaseModel):
    repository_url: Optional[str] = None
    repository_access_token: Optional[str] = None
    path_in_repository: Optional[str] = None
    variables: Optional[str] = None
    built_in: Optional[bool] = None
    policy_file_content: Optional[str] = None
    commit_hash: Optional[str] = None
    repository_type: Optional[RepositoryType] = None
    secret_manager_credential: Optional[RepositorySecretInfo] = None

__all__.append("PolicyEnforcement")

class EnvironmentParameterDriftResponse(BaseModel):
    drift_type: Optional[ParameterDriftType] = Field(None, description="possible values: Added, Updated, Deleted")
    parameter_name: Optional[str] = None
    current_value: Optional[str] = None
    new_value: Optional[str] = None
    sensitive: Optional[bool] = None

__all__.append("EnvironmentParameterDriftResponse")

class EnvironmentParametersExternalResponse(BaseModel):
    parameters: Optional[List[ParameterStoreItemInfoResponse]] = None
    parameters_drifts: Optional[List[EnvironmentParameterDriftResponse]] = None

__all__.append("EnvironmentParametersExternalResponse")

class EnvironmentPlanResultEnvironmentInfo(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    grains: Optional[List[EnvironmentPlanResultGrainInfo]] = None

__all__.append("EnvironmentPlanResultEnvironmentInfo")

class EnvironmentPlanResultGrainInfo(BaseModel):
    path: Optional[str] = None
    source_commit: Optional[str] = None
    target_commit: Optional[str] = None
    content: Optional[str] = None

__all__.append("EnvironmentPlanResultGrainInfo")

class EnvironmentPlanResultInfo(BaseModel):
    environment: Optional[EnvironmentPlanResultEnvironmentInfo] = None

__all__.append("EnvironmentPlanResultInfo")

class EvaluateConsumptionPoliciesResponse(BaseModel):
    canRunEnvironment: Optional[bool] = None
    reason: Optional[str] = None

__all__.append("EvaluateConsumptionPoliciesResponse")

class GetEnvironmentPlanResultResponse(BaseModel):
    status: Optional[PlanStatus] = Field(None, description="possible values: Executing, Done, Cancelled, Failed")
    errors: Optional[List[str]] = None
    plan: Optional[EnvironmentPlanResultInfo] = None

__all__.append("GetEnvironmentPlanResultResponse")

class ParameterStoreItemInfoResponse(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None
    sensitive: Optional[bool] = None
    read_only: Optional[bool] = None

__all__.append("ParameterStoreItemInfoResponse")

class PlanEnvironmentResponse(BaseModel):
    request_handle: Optional[str] = None

__all__.append("PlanEnvironmentResponse")

class PlanStatus(BaseModel):
    """possible values: Executing, Done, Cancelled, Failed"""
    pass

class ResourceActionData(BaseModel):
    action_name: Optional[str] = None
    resource_name: Optional[str] = None

__all__.append("ResourceActionData")

class SandboxTag(BaseModel):
    name: Optional[str] = Field(None, description="Tag name")
    value: Optional[str] = Field(None, description="Tag value")
    modified_by: Optional[str] = Field(None, description="Name of the last user who modified the tag")
    last_modified: Optional[str] = Field(None, description="Last modification data and time of the tag")
    created_by: Optional[str] = Field(None, description="Name of the user who created the tag")
    created_date: Optional[str] = Field(None, description="Creation date and time of the tag")
    scope: Optional[TagScope] = Field(None, description="Tag scope ('account', 'space', 'blueprint' or 'runtime')")
    possible_values: Optional[List[str]] = Field(None, description="Tag possible values <remarks>Tag value must be one of the possible values</remarks>")
    description: Optional[str] = Field(None, description="Tag description")
    tag_type: Optional[TagType] = Field(None, description="Tag type ('system', 'user_defined', 'override' or 'pre_defined')")

__all__.append("SandboxTag")

class TagScope(RootModel[str]):
    """Tag scope as string ('account', 'space', 'blueprint', 'runtime')."""
    pass

class TimeDataResponse(BaseModel):
    start: Optional[str] = None
    duration: Optional[str] = None

__all__.append("TimeDataResponse")

class KubeConfigDetails(BaseModel):
    contextName: Optional[str] = None
    kubeConfigSecretName: Optional[str] = None
    kubeConfigSecretNamespace: Optional[str] = None
    kubeConfigFilepath: Optional[str] = None

__all__.append("KubeConfigDetails")

class GetAccountPolicyInstancesResponse(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    last_synced: Optional[str] = None
    commit_hash: Optional[str] = None
    policy_template: Optional[PolicyTemplateDataForGetInstancesResponse] = None
    created_date: Optional[str] = None
    created_by: Optional[str] = None
    last_modified: Optional[str] = None
    last_modified_by: Optional[str] = None
    variables: Optional[List[PolicyInstanceVariableForGetResponse]] = None
    spaces: Optional[List[str]] = None
    is_enabled: Optional[bool] = None
    labels: Optional[List[str]] = None
    is_valid: Optional[bool] = None
    overridable: Optional[bool] = None
    manual_initialization: Optional[bool] = None
    approval_channel_name: Optional[str] = None
    errors: Optional[List[str]] = None
    policy_url: Optional[str] = None
    data: Optional[Any] = None
    repository_url: Optional[str] = None
    repository_name: Optional[str] = None

__all__.append("GetAccountPolicyInstancesResponse")

class PolicyInstanceVariableForGetResponse(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    values: Optional[List[str]] = None

__all__.append("PolicyInstanceVariableForGetResponse")

class PolicyTemplateDataForGetInstancesResponse(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    package_name: Optional[str] = None
    description: Optional[str] = None
    built_in: Optional[bool] = None

__all__.append("PolicyTemplateDataForGetInstancesResponse")

class OpaPolicyFileResponse(BaseModel):
    name: Optional[str] = None
    name_without_extension: Optional[str] = None
    repository_relative_url: Optional[str] = None
    repository_url: Optional[str] = None
    package_name: Optional[str] = None
    repository_name: Optional[str] = None
    exists: Optional[bool] = None
    errors: Optional[List[str]] = None

__all__.append("OpaPolicyFileResponse")

class GetInventoryMetricsResponse(BaseModel):
    total_count: Optional[int] = None
    reserved: Optional[int] = None
    available: Optional[int] = None
    managed_count: Optional[int] = None
    unmanaged_count: Optional[int] = None
    codified_count: Optional[int] = None
    top_providers: Optional[List[MetricSectionResponse]] = None
    top_resource_types: Optional[List[MetricSectionResponse]] = None
    top_resource_locations: Optional[List[MetricSectionResponse]] = None

__all__.append("GetInventoryMetricsResponse")

class MetricSectionResponse(BaseModel):
    name: Optional[str] = None
    count: Optional[int] = None

__all__.append("MetricSectionResponse")

class GetCustomResourceTypeResponse(BaseModel):
    name: Optional[str] = None
    provider_type: Optional[str] = None
    category: Optional[str] = None
    reservable: Optional[bool] = None
    curatable: Optional[bool] = None
    hourly_cost: Optional[float] = None
    attribute_definitions: Optional[List[AttributeDefinition]] = None

__all__.append("GetCustomResourceTypeResponse")

class AttributeDefinition(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    value_type: Optional[str] = None

__all__.append("AttributeDefinition")

class AttributeValue(BaseModel):
    name: Optional[str] = None
    value: Optional[Any] = None

__all__.append("AttributeValue")

class CreateCustomResourceRequest(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    attributes: Optional[List[AttributeValue]] = None
    tags: Optional[List[Tag]] = None

__all__.append("CreateCustomResourceRequest")

class CreateCustomResourceTypeRequest(BaseModel):
    name: Optional[str] = None
    provider_type: Optional[str] = None
    category: Optional[str] = None
    reservable: Optional[bool] = None
    curatable: Optional[bool] = None
    hourly_cost: Optional[float] = None
    attribute_definitions: Optional[List[AttributeDefinition]] = None

__all__.append("CreateCustomResourceTypeRequest")

class Tag(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

__all__.append("Tag")

class UpdateCustomResourceRequest(BaseModel):
    id: Optional[str] = None
    updated_id: Optional[str] = None
    excluded_from_reserving: Optional[ToggleResourceExcludedFromReservingRequest] = None
    name: Optional[str] = None
    type: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    attributes: Optional[List[AttributeValue]] = None
    tags: Optional[List[Tag]] = None

__all__.append("UpdateCustomResourceRequest")

class UpdateCustomResourceTypeRequest(BaseModel):
    type_name: Optional[str] = None
    name: Optional[str] = None
    provider_type: Optional[str] = None
    category: Optional[str] = None
    reservable: Optional[bool] = None
    curatable: Optional[bool] = None
    hourly_cost: Optional[float] = None
    attribute_definitions: Optional[List[AttributeDefinition]] = None

__all__.append("UpdateCustomResourceTypeRequest")

class ToggleResourceExcludedFromReservingRequest(BaseModel):
    excluded: Optional[bool] = None
    excluded_reason: Optional[str] = None

__all__.append("ToggleResourceExcludedFromReservingRequest")

class GetAllResourcesResponse(BaseModel):
    resources: Optional[List[GetResourceResponse]] = None
    paging_info: Optional[PagingInfoResponse] = None

__all__.append("GetAllResourcesResponse")

class GetResourceDataResponse(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    identifier: Optional[str] = None
    location: Optional[str] = None
    iac_status: Optional[str] = None
    reservation_status: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    category: Optional[str] = None
    provider: Optional[str] = None
    provider_type: Optional[str] = None
    last_sync: Optional[str] = None
    updated_at: Optional[str] = None
    excluded_from_reserving: Optional[bool] = None
    excluded_from_reserving_reason: Optional[str] = None
    tags: Optional[List[ResourceTagResponse]] = None
    attributes: Optional[List[ResourceAttributeResponse]] = None

__all__.append("GetResourceDataResponse")

class GetResourceResponse(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    identifier: Optional[str] = None
    location: Optional[str] = None
    iac_status: Optional[str] = None
    reservation_status: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    category: Optional[str] = None
    provider: Optional[str] = None
    provider_type: Optional[str] = None
    last_sync: Optional[str] = None
    updated_at: Optional[str] = None
    excluded_from_reserving: Optional[bool] = None
    excluded_from_reserving_reason: Optional[str] = None
    tags: Optional[List[ResourceTagResponse]] = None

__all__.append("GetResourceResponse")

class ResourceAttributeResponse(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    value_type: Optional[str] = None
    value: Optional[Any] = None

__all__.append("ResourceAttributeResponse")

class ResourceTagResponse(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

__all__.append("ResourceTagResponse")

class AddParameterRequest(BaseModel):
    """Request to add parameter to Parameter Store"""
    name: Optional[str] = Field(None, description="Parameter name <remarks> - Parameter Name is case-insensitive<br /> - Parameter Name may only contain URL-supported characters including letters, digits, underscores, dashes, etc. </remarks>")
    description: Optional[str] = Field(None, description="Parameter description")
    value: Optional[str] = Field(None, description="Parameter value")
    sensitive: Optional[bool] = Field(None, description="Indication whether the parameter is sensitive")

__all__.append("AddParameterRequest")

class ParameterStoreItemResponse(BaseModel):
    """Parameter Store item information"""
    name: Optional[str] = Field(None, description="Parameter name")
    description: Optional[str] = Field(None, description="Parameter description")
    value: Optional[str] = Field(None, description="Parameter value")
    sensitive: Optional[bool] = Field(None, description="Indication whether the parameter is sensitive")
    modified_by: Optional[str] = Field(None, description="Name of the last user who modified the parameter")
    last_modified: Optional[str] = Field(None, description="Last modification date and time of the parameter")

__all__.append("ParameterStoreItemResponse")

class SpaceParameterStoreItemResponse(BaseModel):
    overrides_account: Optional[bool] = Field(None, description="Indication whether there is an account parameter with the same name")
    name: Optional[str] = Field(None, description="Parameter name")
    description: Optional[str] = Field(None, description="Parameter description")
    value: Optional[str] = Field(None, description="Parameter value")
    sensitive: Optional[bool] = Field(None, description="Indication whether the parameter is sensitive")
    modified_by: Optional[str] = Field(None, description="Name of the last user who modified the parameter")
    last_modified: Optional[str] = Field(None, description="Last modification date and time of the parameter")

__all__.append("SpaceParameterStoreItemResponse")

class UpdateParameterRequest(BaseModel):
    """Request to update parameter in Parameter Store"""
    description: Optional[str] = Field(None, description="Parameter description")
    value: Optional[str] = Field(None, description="Parameter value")
    sensitive: Optional[bool] = Field(None, description="Indication whether the parameter is sensitive")

__all__.append("UpdateParameterRequest")

class PagingInfoResponse(BaseModel):
    full_count: Optional[int] = None
    requested_page: Optional[int] = None
    total_pages: Optional[int] = None

__all__.append("PagingInfoResponse")

class ErrorResponse(BaseModel):
    errors: Optional[List[Error]] = None

__all__.append("ErrorResponse")

class RepositorySecretInfo(BaseModel):
    roleArn: Optional[str] = None
    externalId: Optional[str] = None
    secretId: Optional[str] = None
    secretPath: Optional[str] = None

__all__.append("RepositorySecretInfo")
