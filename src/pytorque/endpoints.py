from __future__ import annotations
from abc import abstractmethod
from typing import Any, Dict, List, Optional
import httpx  # noqa: F401
from pydantic import BaseModel  # noqa: F401
from .models.generated import *  # noqa: F401,F403

# AUTO-GENERATED: Do not edit manually. Run scripts/generate_endpoints.py

from typing import Protocol, runtime_checkable
@runtime_checkable
class _SupportsRequest(Protocol):

    @abstractmethod
    def _handle_response(self, resp: Any) -> Any: ...

    @property
    @abstractmethod
    def torque_client(self) -> httpx.BaseClient: ... # type: ignore

class TorqueEndpointsMixin(_SupportsRequest):
    def post_accounts_by_account_login(self, account: str, body: Any | None = None, **kwargs) -> TokenResponse:
        """Get token
        Auto-generated from OpenAPI.
        """
        url = f"/accounts/{account}/login"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return TokenResponse.model_validate(data)

    def delete_long_token_by_space_name_by_token_id(self, token_id: str, space_name: str, **kwargs) -> Any:
        """Revoke long token
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/{token_id}"
        resp = self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    def post_long_token_by_space_name_longtoken(self, space_name: str, query: dict | None = None, **kwargs) -> TokenResponse:
        """Generate long token
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/longtoken"
        resp = self.torque_client.request("POST", url, params=query, **kwargs)
        data = self._handle_response(resp); return TokenResponse.model_validate(data)

    def get_long_token_by_space_name_longtokens(self, space_name: str, **kwargs) -> List[LongTokenSafeResponse]:
        """Get long tokens in space
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/longtokens"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ LongTokenSafeResponse.model_validate(d) for d in data ]

    def post_agent_k8s_by_agent_spaces_by_space_name(self, agent: str, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Associate k8s agent with a space
        Auto-generated from OpenAPI.
        """
        url = f"/agent/k8s/{agent}/spaces/{space_name}"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_settings_agents(self, query: dict | None = None, **kwargs) -> List[ComputeServiceResponse]:
        """Get agent list
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return [ ComputeServiceResponse.model_validate(d) for d in data ]

    def post_settings_agents(self, body: Any | None = None, **kwargs) -> Any:
        """Create new agent
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def delete_settings_agents(self, query: dict | None = None, **kwargs) -> Any:
        """Delete agent from account
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        resp = self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    def put_settings_agents_by_agent_name_new(self, agent_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update agent configuration
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents/{agent_name}/new"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_settings_agents_by_agent_name_usages(self, agent_name: str, **kwargs) -> List[ComputeServiceUsagesResponse]:
        """Get agent usages per account
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents/{agent_name}/usages"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ ComputeServiceUsagesResponse.model_validate(d) for d in data ]

    def get_spaces_by_space_name_agents(self, space_name: str, **kwargs) -> List[SpaceComputeServiceResponse]:
        """List agents in space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ SpaceComputeServiceResponse.model_validate(d) for d in data ]

    def delete_spaces_by_space_name_agents_by_agent_name(self, space_name: str, agent_name: str, **kwargs) -> Any:
        """Remove agent association from space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent_name}"
        resp = self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_agents_by_agent_name_usages(self, space_name: str, agent_name: str, **kwargs) -> List[SpaceComputeServiceResponse]:
        """Get agent usages per space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent_name}/usages"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ SpaceComputeServiceResponse.model_validate(d) for d in data ]

    def post_spaces_by_space_name_agents_by_agent(self, space_name: str, agent: str, **kwargs) -> Any:
        """Associate agent with space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent}"
        resp = self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    def get_audit(self, query: dict | None = None, **kwargs) -> PagedAuditEventsResponse:
        """Get audits events
        Auto-generated from OpenAPI.
        """
        url = f"/audit"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return PagedAuditEventsResponse.model_validate(data)

    def get_spaces_by_space_name_asset_library(self, space_name: str, **kwargs) -> List[BlueprintForGetAllResponse]:
        """Get all blueprints from asset library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ BlueprintForGetAllResponse.model_validate(d) for d in data ]

    def get_spaces_by_space_name_blueprints(self, space_name: str, query: dict | None = None, **kwargs) -> List[BlueprintForGetAllResponse]:
        """Get all blueprints
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return [ BlueprintForGetAllResponse.model_validate(d) for d in data ]

    def post_spaces_by_space_name_blueprints_by_blueprintname(self, space_name: str, blueprintName: str, body: Any | None = None, **kwargs) -> Any:
        """Update blueprint display name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/{blueprintName}"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_blueprints_ai_blueprints_generation_data(self, space_name: str, **kwargs) -> BlueprintForGetAllResponse:
        """Get ai_generation_data for a blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/ai/blueprints_generation_data"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return BlueprintForGetAllResponse.model_validate(data)

    def put_spaces_by_space_name_blueprints_display_name(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update blueprint display name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/display_name"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_designer_blueprints_simplified(self, space_name: str, query: dict | None = None, **kwargs) -> PagedSimplifiedBlueprintListItemResponse:
        """Get all blueprints in simplified form
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-blueprints/simplified"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return PagedSimplifiedBlueprintListItemResponse.model_validate(data)

    def get_spaces_by_space_name_designer_iac_assets_simplified(self, space_name: str, query: dict | None = None, **kwargs) -> PagedSimplifiedIACAssetListItemResponse:
        """Get all IAC assets in simplified form
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-iac-assets/simplified"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return PagedSimplifiedIACAssetListItemResponse.model_validate(data)

    def get_spaces_by_space_name_designer_iac_assets_summary(self, space_name: str, **kwargs) -> Any:
        """Get IAC assets summary
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-iac-assets/summary"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_iac_assets(self, space_name: str, query: dict | None = None, **kwargs) -> PagedIACAssetListItemResponse:
        """Get all IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return PagedIACAssetListItemResponse.model_validate(data)

    def get_spaces_by_space_name_iac_assets_by_name(self, space_name: str, name: str, **kwargs) -> IACAssetDetailResponse:
        """Get IAC asset
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/{name}"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return IACAssetDetailResponse.model_validate(data)

    def post_spaces_by_space_name_iac_assets_by_name_sync(self, space_name: str, name: str, **kwargs) -> Any:
        """Sync IAC asset
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/{name}/sync"
        resp = self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    def post_spaces_by_space_name_iac_assets_generate_blueprint_yaml(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Generate blueprint from IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/generate-blueprint-yaml"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_iac_assets_metrics(self, space_name: str, query: dict | None = None, **kwargs) -> IACAssetListMetricsResponse:
        """Get all IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/metrics"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return IACAssetListMetricsResponse.model_validate(data)

    def get_spaces_by_space_name_repositories_by_repositoryname_blueprints(self, space_name: str, repositoryName: str, query: dict | None = None, **kwargs) -> List[BlueprintForGetAllResponse]:
        """Get published blueprints
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repositoryName}/blueprints"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return [ BlueprintForGetAllResponse.model_validate(d) for d in data ]

    def post_spaces_by_space_name_validations_blueprints(self, space_name: str, body: Any | None = None, **kwargs) -> BlueprintValidationResponse:
        """Validate blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/validations/blueprints"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return BlueprintValidationResponse.model_validate(data)

    def post_spaces_by_space_name_asset_library_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs) -> Any:
        """Add blueprint to assets library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library/{blueprint_name}"
        resp = self.torque_client.request("POST", url, params=query, **kwargs)
        return self._handle_response(resp)

    def delete_spaces_by_space_name_asset_library_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs) -> Any:
        """Remove blueprint from assets library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library/{blueprint_name}"
        resp = self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_catalog(self, space_name: str, **kwargs) -> List[CatalogForGetAllResponse]:
        """Get blueprints in catalog
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ CatalogForGetAllResponse.model_validate(d) for d in data ]

    def put_spaces_by_space_name_catalog(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Edit Blueprint metadata
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def post_spaces_by_space_name_catalog(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Publish blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_catalog_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs) -> BlueprintDetailsResponse:
        """Get blueprint details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/{blueprint_name}"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return BlueprintDetailsResponse.model_validate(data)

    def delete_spaces_by_space_name_catalog_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs) -> Any:
        """Unpublish blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/{blueprint_name}"
        resp = self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    def put_spaces_by_space_name_catalog_labels(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Edit Blueprint labels
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/labels"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def put_spaces_by_space_name_catalog_launch_allowed(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Edit Blueprint launch allowed
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/launch_allowed"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_operation_hub(self, query: dict | None = None, **kwargs) -> EnvironmentsResponse:
        """Get environment list
        Auto-generated from OpenAPI.
        """
        url = f"/operation_hub"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return EnvironmentsResponse.model_validate(data)

    def get_settings_environmentfeed(self, query: dict | None = None, **kwargs) -> List[EnvironmentFeedResponse]:
        """Get all environment activity feed without pagination
        Auto-generated from OpenAPI.
        """
        url = f"/settings/environmentfeed"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return [ EnvironmentFeedResponse.model_validate(d) for d in data ]

    def get_spaces_by_space_name_eac(self, space_name: str, **kwargs) -> List[EacResponse]:
        """Get eac entries
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ EacResponse.model_validate(d) for d in data ]

    def put_spaces_by_space_name_eac_enable(self, space_name: str, body: Any | None = None, **kwargs) -> List[EacResponse]:
        """Set eac enablement
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/enable"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return [ EacResponse.model_validate(d) for d in data ]

    def post_spaces_by_space_name_eac_register(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Register eac file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/register"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_eac_registration_candidates(self, space_name: str, query: dict | None = None, **kwargs) -> List[EacCandidateResponse]:
        """Show eac registration candidates
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/registration_candidates"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return [ EacCandidateResponse.model_validate(d) for d in data ]

    def delete_spaces_by_space_name_eac_unregister(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Unregister eac file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/unregister"
        resp = self.torque_client.request("DELETE", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_edit_environment_session(self, space_name: str, query: dict | None = None, **kwargs) -> EnvEditListSessionsResponse:
        """List edit sessions
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return EnvEditListSessionsResponse.model_validate(data)

    def post_spaces_by_space_name_edit_environment_session(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Start new edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_edit_environment_session_by_session_name(self, space_name: str, session_name: str, **kwargs) -> EnvEditListSessionsResponse:
        """Get edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvEditListSessionsResponse.model_validate(data)

    def delete_spaces_by_space_name_edit_environment_session_by_session_name(self, space_name: str, session_name: str, **kwargs) -> Any:
        """Abort edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}"
        resp = self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    def put_spaces_by_space_name_edit_environment_session_by_session_name_apply(self, space_name: str, session_name: str, **kwargs) -> Any:
        """Apply edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/apply"
        resp = self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_edit_environment_session_by_session_name_plan(self, space_name: str, session_name: str, **kwargs) -> EnvEditPlanResponse:
        """Get plan for edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/plan"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvEditPlanResponse.model_validate(data)

    def put_spaces_by_space_name_edit_environment_session_by_session_name_save(self, space_name: str, session_name: str, body: Any | None = None, **kwargs) -> Any:
        """Save edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/save"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def post_spaces_by_space_name_environments(self, space_name: str, body: Any | None = None, **kwargs) -> CreateEnvResponse:
        """Start new environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return CreateEnvResponse.model_validate(data)

    def get_spaces_by_space_name_environments_by_environment_id(self, space_name: str, environment_id: str, **kwargs) -> EnvironmentResponse:
        """Gets environment details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvironmentResponse.model_validate(data)

    def delete_spaces_by_space_name_environments_by_environment_id(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs) -> Any:
        """Terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}"
        resp = self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    def post_spaces_by_space_name_environments_by_environment_id_by_grain_path_by_resource_id_run_action_by_action_id(self, space_name: str, environment_id: str, grain_path: str, resource_id: str, action_id: str, body: Any | None = None, **kwargs) -> Any:
        """Invoke environment action
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/{grain_path}/{resource_id}/run_action/{action_id}"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def post_spaces_by_space_name_environments_by_environment_id_driftcheck_by_grain_id(self, space_name: str, environment_id: str, grain_id: str, body: Any | None = None, **kwargs) -> Any:
        """Invoke environment drift check
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/driftcheck/{grain_id}"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_environments_by_environment_id_eac(self, space_name: str, environment_id: str, **kwargs) -> Any:
        """Export environment YAML file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    def delete_spaces_by_space_name_environments_by_environment_id_eac(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs) -> Any:
        """Terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac"
        resp = self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    def put_spaces_by_space_name_environments_by_environment_id_eac_detach(self, space_name: str, environment_id: str, **kwargs) -> Any:
        """Detach Eac environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac/detach"
        resp = self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    def put_spaces_by_space_name_environments_by_environment_id_extend(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> ExtendEnvDurationResponse:
        """Extend environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/extend"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return ExtendEnvDurationResponse.model_validate(data)

    def put_spaces_by_space_name_environments_by_environment_id_labels(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> Any:
        """Update environment labels
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/labels"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_environments_by_environment_id_parameters(self, space_name: str, environment_id: str, **kwargs) -> EnvironmentParametersExternalResponse:
        """Get environment parameters and their drifts
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/parameters"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvironmentParametersExternalResponse.model_validate(data)

    def post_spaces_by_space_name_environments_by_environment_id_plan(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> PlanEnvironmentResponse:
        """Plan environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/plan"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return PlanEnvironmentResponse.model_validate(data)

    def get_spaces_by_space_name_environments_by_environment_id_plan_by_request_id(self, space_name: str, environment_id: str, request_id: str, **kwargs) -> GetEnvironmentPlanResultResponse:
        """Get environment plan result
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/plan/{request_id}"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return GetEnvironmentPlanResultResponse.model_validate(data)

    def post_spaces_by_space_name_environments_by_environment_id_reconcile(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> Any:
        """Invoke environment reconcile
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/reconcile"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def delete_spaces_by_space_name_environments_by_environment_id_release(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs) -> ReleaseEnvResponse:
        """End environment without termination
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/release"
        resp = self.torque_client.request("DELETE", url, params=query, **kwargs)
        data = self._handle_response(resp); return ReleaseEnvResponse.model_validate(data)

    def put_spaces_by_space_name_environments_by_environment_id_update_env(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> Any:
        """Restart environment grains
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_env"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def post_spaces_by_space_name_environments_by_environment_id_update_v2(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> Any:
        """Update environment grains
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_environment_name_rename(self, space_name: str, environment_id: str, environment_name: str, **kwargs) -> Any:
        """Update environment name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{environment_name}/rename"
        resp = self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_grain_path_approve(self, space_name: str, environment_id: str, grain_path: str, **kwargs) -> Any:
        """Approve grain update
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{grain_path}/approve"
        resp = self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_grain_path_deny(self, space_name: str, environment_id: str, grain_path: str, **kwargs) -> Any:
        """Deny grain update
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{grain_path}/deny"
        resp = self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_environments_by_environment_id_workflows(self, environment_id: str, space_name: str, **kwargs) -> List[EnvironmentWorkflowResponse]:
        """List environment workflows
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/workflows"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ EnvironmentWorkflowResponse.model_validate(d) for d in data ]

    def put_spaces_by_space_name_environments_by_environment_id_workflows(self, environment_id: str, space_name: str, query: dict | None = None, **kwargs) -> Any:
        """Invoke environment workflow
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/workflows"
        resp = self.torque_client.request("PUT", url, params=query, **kwargs)
        return self._handle_response(resp)

    def patch_spaces_by_space_name_environments_cancel_scheduled_by_environment_id(self, space_name: str, environment_id: str, **kwargs) -> Any:
        """Cancel scheduled environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/cancel/scheduled/{environment_id}"
        resp = self.torque_client.request("PATCH", url, params=None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_environments_consumption_run_policies(self, space_name: str, query: dict | None = None, **kwargs) -> EvaluateConsumptionPoliciesResponse:
        """Run consumption policies
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/consumption/run_policies"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return EvaluateConsumptionPoliciesResponse.model_validate(data)

    def delete_spaces_by_space_name_environments_force_by_environment_id(self, space_name: str, environment_id: str, **kwargs) -> Any:
        """Force terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/force/{environment_id}"
        resp = self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    def post_spaces_by_space_name_environments_import(self, space_name: str, body: Any | None = None, **kwargs) -> ImportEnvResponse:
        """Import environment to Torque
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/import"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return ImportEnvResponse.model_validate(data)

    def post_spaces_by_space_name_environments_import_using_blueprint(self, space_name: str, body: Any | None = None, **kwargs) -> ImportEnvResponse:
        """Import environment with blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/import_using_blueprint"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return ImportEnvResponse.model_validate(data)

    def get_spaces_by_space_name_environments_runner_by_environment_id(self, space_name: str, environment_id: str, **kwargs) -> EnvironmentResponse:
        """Gets runner information
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/runner/{environment_id}"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvironmentResponse.model_validate(data)

    def get_spaces_by_space_name_environments_runner_by_environment_id_client_by_operation_id(self, space_name: str, environment_id: str, operation_id: str, **kwargs) -> EnvironmentResponse:
        """Gets runner information
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/runner/{environment_id}/client/{operation_id}"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvironmentResponse.model_validate(data)

    def post_spaces_by_space_name_environments_schedule(self, space_name: str, body: Any | None = None, **kwargs) -> ScheduleEnvironmentResponse:
        """Schedule new environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/schedule"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return ScheduleEnvironmentResponse.model_validate(data)

    def get_spaces_by_space_name_environments_v2(self, space_name: str, query: dict | None = None, **kwargs) -> EnvironmentsResponse:
        """Get environment list
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/v2"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return EnvironmentsResponse.model_validate(data)

    def post_accounts_users(self, body: Any | None = None, **kwargs) -> Any:
        """Add Users to Account without invitation
        Auto-generated from OpenAPI.
        """
        url = f"/accounts/users"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def post_policies_by_repository_name_discover(self, repository_name: str, **kwargs) -> List[OpaPolicyFileResponse]:
        """Discover policy candidates in repository
        Auto-generated from OpenAPI.
        """
        url = f"/policies/{repository_name}/discover"
        resp = self.torque_client.request("POST", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ OpaPolicyFileResponse.model_validate(d) for d in data ]

    def post_policies_by_repository_name_generate(self, repository_name: str, body: Any | None = None, **kwargs) -> List[GetAccountPolicyInstancesResponse]:
        """Generate policy instances from the chosen candidate files
        Auto-generated from OpenAPI.
        """
        url = f"/policies/{repository_name}/generate"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return [ GetAccountPolicyInstancesResponse.model_validate(d) for d in data ]

    def put_custom_resource(self, body: Any | None = None, **kwargs) -> Any:
        """Update custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def post_custom_resource(self, body: Any | None = None, **kwargs) -> Any:
        """Create custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_custom_resource_type(self, **kwargs) -> List[GetCustomResourceTypeResponse]:
        """Get custom resource type list
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ GetCustomResourceTypeResponse.model_validate(d) for d in data ]

    def post_custom_resource_type(self, body: Any | None = None, **kwargs) -> Any:
        """Create custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def put_custom_resource_type_by_type_name(self, type_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type/{type_name}"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def delete_custom_resource_type_by_type_name(self, type_name: str, query: dict | None = None, **kwargs) -> Any:
        """Remove custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type/{type_name}"
        resp = self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    def delete_custom_resource_by_id(self, id: str, query: dict | None = None, **kwargs) -> Any:
        """Remove custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource/{id}"
        resp = self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    def get_resource(self, query: dict | None = None, **kwargs) -> GetAllResourcesResponse:
        """Get resource list
        Auto-generated from OpenAPI.
        """
        url = f"/resource"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return GetAllResourcesResponse.model_validate(data)

    def get_resource_by_id(self, id: str, **kwargs) -> GetResourceDataResponse:
        """Get resource data by id
        Auto-generated from OpenAPI.
        """
        url = f"/resource/{id}"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return GetResourceDataResponse.model_validate(data)

    def put_resource_by_id_toggle_excluded_from_reserving(self, id: str, body: Any | None = None, **kwargs) -> Any:
        """Toggle resource exclusion from reservation by id
        Auto-generated from OpenAPI.
        """
        url = f"/resource/{id}/toggle_excluded_from_reserving"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_resource_metrics(self, query: dict | None = None, **kwargs) -> GetInventoryMetricsResponse:
        """Get resources metrics data
        Auto-generated from OpenAPI.
        """
        url = f"/resource/metrics"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return GetInventoryMetricsResponse.model_validate(data)

    def post_spaces_by_space_name_labels(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Add new label
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/labels"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def put_spaces_by_space_name_labels_update(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update label
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/labels/update"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_settings_parameters(self, **kwargs) -> List[ParameterStoreItemResponse]:
        """Get all parameters
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ ParameterStoreItemResponse.model_validate(d) for d in data ]

    def post_settings_parameters(self, body: Any | None = None, **kwargs) -> Any:
        """Create account parameter
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_settings_parameters_by_param_name(self, param_name: str, **kwargs) -> ParameterStoreItemResponse:
        """Get account parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return ParameterStoreItemResponse.model_validate(data)

    def put_settings_parameters_by_param_name(self, param_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update account level parameter
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def delete_settings_parameters_by_param_name(self, param_name: str, **kwargs) -> Any:
        """Delete an account parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        resp = self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_settings_parameters(self, space_name: str, **kwargs) -> List[SpaceParameterStoreItemResponse]:
        """Get space parameters
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ SpaceParameterStoreItemResponse.model_validate(d) for d in data ]

    def post_spaces_by_space_name_settings_parameters(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Create space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, **kwargs) -> SpaceParameterStoreItemResponse:
        """Get space parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return SpaceParameterStoreItemResponse.model_validate(data)

    def put_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def delete_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, **kwargs) -> Any:
        """Delete space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        resp = self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_repositories(self, space_name: str, **kwargs) -> List[RepositoryDetailsResponse]:
        """Get Repositories in space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories"
        resp = self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ RepositoryDetailsResponse.model_validate(d) for d in data ]

    def delete_spaces_by_space_name_repositories(self, space_name: str, query: dict | None = None, **kwargs) -> Any:
        """Remove repository from space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories"
        resp = self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    def put_spaces_by_space_name_repositories_by_name(self, space_name: str, name: str, body: Any | None = None, **kwargs) -> Any:
        """Update repository configuration
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{name}"
        resp = self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def post_spaces_by_space_name_repositories_by_repository_name_blueprints_by_blueprint_name_update(self, space_name: str, blueprint_name: str, repository_name: str, **kwargs) -> Any:
        """Invoke manual repository sync from repository
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repository_name}/blueprints/{blueprint_name}/update"
        resp = self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    def post_spaces_by_space_name_repositories_by_repository_name_update(self, space_name: str, repository_name: str, **kwargs) -> Any:
        """Initiate repository scanning
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repository_name}/update"
        resp = self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    def get_spaces_by_space_name_repositories_repository(self, space_name: str, query: dict | None = None, **kwargs) -> RepositoryDetailsResponse:
        """Get repository details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/repository"
        resp = self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return RepositoryDetailsResponse.model_validate(data)

    def post_spaces(self, body: Any | None = None, **kwargs) -> Any:
        """Create Space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces"
        resp = self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    def delete_spaces_by_space_name(self, space_name: str, **kwargs) -> Any:
        """Delete Space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}"
        resp = self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)


class AsyncTorqueEndpointsMixin(_SupportsRequest):
    async def post_accounts_by_account_login(self, account: str, body: Any | None = None, **kwargs) -> TokenResponse:
        """Get token
        Auto-generated from OpenAPI.
        """
        url = f"/accounts/{account}/login"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return TokenResponse.model_validate(data)

    async def delete_long_token_by_space_name_by_token_id(self, token_id: str, space_name: str, **kwargs) -> Any:
        """Revoke long token
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/{token_id}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_long_token_by_space_name_longtoken(self, space_name: str, query: dict | None = None, **kwargs) -> TokenResponse:
        """Generate long token
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/longtoken"
        resp = await self.torque_client.request("POST", url, params=query, **kwargs)
        data = self._handle_response(resp); return TokenResponse.model_validate(data)

    async def get_long_token_by_space_name_longtokens(self, space_name: str, **kwargs) -> List[LongTokenSafeResponse]:
        """Get long tokens in space
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/longtokens"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ LongTokenSafeResponse.model_validate(d) for d in data ]

    async def post_agent_k8s_by_agent_spaces_by_space_name(self, agent: str, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Associate k8s agent with a space
        Auto-generated from OpenAPI.
        """
        url = f"/agent/k8s/{agent}/spaces/{space_name}"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_settings_agents(self, query: dict | None = None, **kwargs) -> List[ComputeServiceResponse]:
        """Get agent list
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return [ ComputeServiceResponse.model_validate(d) for d in data ]

    async def post_settings_agents(self, body: Any | None = None, **kwargs) -> Any:
        """Create new agent
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def delete_settings_agents(self, query: dict | None = None, **kwargs) -> Any:
        """Delete agent from account
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def put_settings_agents_by_agent_name_new(self, agent_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update agent configuration
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents/{agent_name}/new"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_settings_agents_by_agent_name_usages(self, agent_name: str, **kwargs) -> List[ComputeServiceUsagesResponse]:
        """Get agent usages per account
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents/{agent_name}/usages"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ ComputeServiceUsagesResponse.model_validate(d) for d in data ]

    async def get_spaces_by_space_name_agents(self, space_name: str, **kwargs) -> List[SpaceComputeServiceResponse]:
        """List agents in space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ SpaceComputeServiceResponse.model_validate(d) for d in data ]

    async def delete_spaces_by_space_name_agents_by_agent_name(self, space_name: str, agent_name: str, **kwargs) -> Any:
        """Remove agent association from space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent_name}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_agents_by_agent_name_usages(self, space_name: str, agent_name: str, **kwargs) -> List[SpaceComputeServiceResponse]:
        """Get agent usages per space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent_name}/usages"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ SpaceComputeServiceResponse.model_validate(d) for d in data ]

    async def post_spaces_by_space_name_agents_by_agent(self, space_name: str, agent: str, **kwargs) -> Any:
        """Associate agent with space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent}"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_audit(self, query: dict | None = None, **kwargs) -> PagedAuditEventsResponse:
        """Get audits events
        Auto-generated from OpenAPI.
        """
        url = f"/audit"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return PagedAuditEventsResponse.model_validate(data)

    async def get_spaces_by_space_name_asset_library(self, space_name: str, **kwargs) -> List[BlueprintForGetAllResponse]:
        """Get all blueprints from asset library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ BlueprintForGetAllResponse.model_validate(d) for d in data ]

    async def get_spaces_by_space_name_blueprints(self, space_name: str, query: dict | None = None, **kwargs) -> List[BlueprintForGetAllResponse]:
        """Get all blueprints
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return [ BlueprintForGetAllResponse.model_validate(d) for d in data ]

    async def post_spaces_by_space_name_blueprints_by_blueprintname(self, space_name: str, blueprintName: str, body: Any | None = None, **kwargs) -> Any:
        """Update blueprint display name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/{blueprintName}"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_blueprints_ai_blueprints_generation_data(self, space_name: str, **kwargs) -> BlueprintForGetAllResponse:
        """Get ai_generation_data for a blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/ai/blueprints_generation_data"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return BlueprintForGetAllResponse.model_validate(data)

    async def put_spaces_by_space_name_blueprints_display_name(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update blueprint display name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/display_name"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_designer_blueprints_simplified(self, space_name: str, query: dict | None = None, **kwargs) -> PagedSimplifiedBlueprintListItemResponse:
        """Get all blueprints in simplified form
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-blueprints/simplified"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return PagedSimplifiedBlueprintListItemResponse.model_validate(data)

    async def get_spaces_by_space_name_designer_iac_assets_simplified(self, space_name: str, query: dict | None = None, **kwargs) -> PagedSimplifiedIACAssetListItemResponse:
        """Get all IAC assets in simplified form
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-iac-assets/simplified"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return PagedSimplifiedIACAssetListItemResponse.model_validate(data)

    async def get_spaces_by_space_name_designer_iac_assets_summary(self, space_name: str, **kwargs) -> Any:
        """Get IAC assets summary
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-iac-assets/summary"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_iac_assets(self, space_name: str, query: dict | None = None, **kwargs) -> PagedIACAssetListItemResponse:
        """Get all IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return PagedIACAssetListItemResponse.model_validate(data)

    async def get_spaces_by_space_name_iac_assets_by_name(self, space_name: str, name: str, **kwargs) -> IACAssetDetailResponse:
        """Get IAC asset
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/{name}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return IACAssetDetailResponse.model_validate(data)

    async def post_spaces_by_space_name_iac_assets_by_name_sync(self, space_name: str, name: str, **kwargs) -> Any:
        """Sync IAC asset
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/{name}/sync"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_iac_assets_generate_blueprint_yaml(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Generate blueprint from IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/generate-blueprint-yaml"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_iac_assets_metrics(self, space_name: str, query: dict | None = None, **kwargs) -> IACAssetListMetricsResponse:
        """Get all IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/metrics"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return IACAssetListMetricsResponse.model_validate(data)

    async def get_spaces_by_space_name_repositories_by_repositoryname_blueprints(self, space_name: str, repositoryName: str, query: dict | None = None, **kwargs) -> List[BlueprintForGetAllResponse]:
        """Get published blueprints
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repositoryName}/blueprints"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return [ BlueprintForGetAllResponse.model_validate(d) for d in data ]

    async def post_spaces_by_space_name_validations_blueprints(self, space_name: str, body: Any | None = None, **kwargs) -> BlueprintValidationResponse:
        """Validate blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/validations/blueprints"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return BlueprintValidationResponse.model_validate(data)

    async def post_spaces_by_space_name_asset_library_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs) -> Any:
        """Add blueprint to assets library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library/{blueprint_name}"
        resp = await self.torque_client.request("POST", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_asset_library_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs) -> Any:
        """Remove blueprint from assets library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library/{blueprint_name}"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_catalog(self, space_name: str, **kwargs) -> List[CatalogForGetAllResponse]:
        """Get blueprints in catalog
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ CatalogForGetAllResponse.model_validate(d) for d in data ]

    async def put_spaces_by_space_name_catalog(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Edit Blueprint metadata
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_catalog(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Publish blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_catalog_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs) -> BlueprintDetailsResponse:
        """Get blueprint details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/{blueprint_name}"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return BlueprintDetailsResponse.model_validate(data)

    async def delete_spaces_by_space_name_catalog_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs) -> Any:
        """Unpublish blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/{blueprint_name}"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_catalog_labels(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Edit Blueprint labels
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/labels"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_catalog_launch_allowed(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Edit Blueprint launch allowed
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/launch_allowed"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_operation_hub(self, query: dict | None = None, **kwargs) -> EnvironmentsResponse:
        """Get environment list
        Auto-generated from OpenAPI.
        """
        url = f"/operation_hub"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return EnvironmentsResponse.model_validate(data)

    async def get_settings_environmentfeed(self, query: dict | None = None, **kwargs) -> List[EnvironmentFeedResponse]:
        """Get all environment activity feed without pagination
        Auto-generated from OpenAPI.
        """
        url = f"/settings/environmentfeed"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return [ EnvironmentFeedResponse.model_validate(d) for d in data ]

    async def get_spaces_by_space_name_eac(self, space_name: str, **kwargs) -> List[EacResponse]:
        """Get eac entries
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ EacResponse.model_validate(d) for d in data ]

    async def put_spaces_by_space_name_eac_enable(self, space_name: str, body: Any | None = None, **kwargs) -> List[EacResponse]:
        """Set eac enablement
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/enable"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return [ EacResponse.model_validate(d) for d in data ]

    async def post_spaces_by_space_name_eac_register(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Register eac file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/register"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_eac_registration_candidates(self, space_name: str, query: dict | None = None, **kwargs) -> List[EacCandidateResponse]:
        """Show eac registration candidates
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/registration_candidates"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return [ EacCandidateResponse.model_validate(d) for d in data ]

    async def delete_spaces_by_space_name_eac_unregister(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Unregister eac file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/unregister"
        resp = await self.torque_client.request("DELETE", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_edit_environment_session(self, space_name: str, query: dict | None = None, **kwargs) -> EnvEditListSessionsResponse:
        """List edit sessions
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return EnvEditListSessionsResponse.model_validate(data)

    async def post_spaces_by_space_name_edit_environment_session(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Start new edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_edit_environment_session_by_session_name(self, space_name: str, session_name: str, **kwargs) -> EnvEditListSessionsResponse:
        """Get edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvEditListSessionsResponse.model_validate(data)

    async def delete_spaces_by_space_name_edit_environment_session_by_session_name(self, space_name: str, session_name: str, **kwargs) -> Any:
        """Abort edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_edit_environment_session_by_session_name_apply(self, space_name: str, session_name: str, **kwargs) -> Any:
        """Apply edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/apply"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_edit_environment_session_by_session_name_plan(self, space_name: str, session_name: str, **kwargs) -> EnvEditPlanResponse:
        """Get plan for edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/plan"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvEditPlanResponse.model_validate(data)

    async def put_spaces_by_space_name_edit_environment_session_by_session_name_save(self, space_name: str, session_name: str, body: Any | None = None, **kwargs) -> Any:
        """Save edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/save"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments(self, space_name: str, body: Any | None = None, **kwargs) -> CreateEnvResponse:
        """Start new environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return CreateEnvResponse.model_validate(data)

    async def get_spaces_by_space_name_environments_by_environment_id(self, space_name: str, environment_id: str, **kwargs) -> EnvironmentResponse:
        """Gets environment details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvironmentResponse.model_validate(data)

    async def delete_spaces_by_space_name_environments_by_environment_id(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs) -> Any:
        """Terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_by_environment_id_by_grain_path_by_resource_id_run_action_by_action_id(self, space_name: str, environment_id: str, grain_path: str, resource_id: str, action_id: str, body: Any | None = None, **kwargs) -> Any:
        """Invoke environment action
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/{grain_path}/{resource_id}/run_action/{action_id}"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_by_environment_id_driftcheck_by_grain_id(self, space_name: str, environment_id: str, grain_id: str, body: Any | None = None, **kwargs) -> Any:
        """Invoke environment drift check
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/driftcheck/{grain_id}"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_by_environment_id_eac(self, space_name: str, environment_id: str, **kwargs) -> Any:
        """Export environment YAML file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_environments_by_environment_id_eac(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs) -> Any:
        """Terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_eac_detach(self, space_name: str, environment_id: str, **kwargs) -> Any:
        """Detach Eac environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac/detach"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_extend(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> ExtendEnvDurationResponse:
        """Extend environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/extend"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return ExtendEnvDurationResponse.model_validate(data)

    async def put_spaces_by_space_name_environments_by_environment_id_labels(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> Any:
        """Update environment labels
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/labels"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_by_environment_id_parameters(self, space_name: str, environment_id: str, **kwargs) -> EnvironmentParametersExternalResponse:
        """Get environment parameters and their drifts
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/parameters"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvironmentParametersExternalResponse.model_validate(data)

    async def post_spaces_by_space_name_environments_by_environment_id_plan(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> PlanEnvironmentResponse:
        """Plan environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/plan"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return PlanEnvironmentResponse.model_validate(data)

    async def get_spaces_by_space_name_environments_by_environment_id_plan_by_request_id(self, space_name: str, environment_id: str, request_id: str, **kwargs) -> GetEnvironmentPlanResultResponse:
        """Get environment plan result
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/plan/{request_id}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return GetEnvironmentPlanResultResponse.model_validate(data)

    async def post_spaces_by_space_name_environments_by_environment_id_reconcile(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> Any:
        """Invoke environment reconcile
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/reconcile"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_environments_by_environment_id_release(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs) -> ReleaseEnvResponse:
        """End environment without termination
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/release"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        data = self._handle_response(resp); return ReleaseEnvResponse.model_validate(data)

    async def put_spaces_by_space_name_environments_by_environment_id_update_env(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> Any:
        """Restart environment grains
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_env"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_by_environment_id_update_v2(self, space_name: str, environment_id: str, body: Any | None = None, **kwargs) -> Any:
        """Update environment grains
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_environment_name_rename(self, space_name: str, environment_id: str, environment_name: str, **kwargs) -> Any:
        """Update environment name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{environment_name}/rename"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_grain_path_approve(self, space_name: str, environment_id: str, grain_path: str, **kwargs) -> Any:
        """Approve grain update
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{grain_path}/approve"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_grain_path_deny(self, space_name: str, environment_id: str, grain_path: str, **kwargs) -> Any:
        """Deny grain update
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{grain_path}/deny"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_by_environment_id_workflows(self, environment_id: str, space_name: str, **kwargs) -> List[EnvironmentWorkflowResponse]:
        """List environment workflows
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/workflows"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ EnvironmentWorkflowResponse.model_validate(d) for d in data ]

    async def put_spaces_by_space_name_environments_by_environment_id_workflows(self, environment_id: str, space_name: str, query: dict | None = None, **kwargs) -> Any:
        """Invoke environment workflow
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/workflows"
        resp = await self.torque_client.request("PUT", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def patch_spaces_by_space_name_environments_cancel_scheduled_by_environment_id(self, space_name: str, environment_id: str, **kwargs) -> Any:
        """Cancel scheduled environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/cancel/scheduled/{environment_id}"
        resp = await self.torque_client.request("PATCH", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_consumption_run_policies(self, space_name: str, query: dict | None = None, **kwargs) -> EvaluateConsumptionPoliciesResponse:
        """Run consumption policies
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/consumption/run_policies"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return EvaluateConsumptionPoliciesResponse.model_validate(data)

    async def delete_spaces_by_space_name_environments_force_by_environment_id(self, space_name: str, environment_id: str, **kwargs) -> Any:
        """Force terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/force/{environment_id}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_import(self, space_name: str, body: Any | None = None, **kwargs) -> ImportEnvResponse:
        """Import environment to Torque
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/import"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return ImportEnvResponse.model_validate(data)

    async def post_spaces_by_space_name_environments_import_using_blueprint(self, space_name: str, body: Any | None = None, **kwargs) -> ImportEnvResponse:
        """Import environment with blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/import_using_blueprint"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return ImportEnvResponse.model_validate(data)

    async def get_spaces_by_space_name_environments_runner_by_environment_id(self, space_name: str, environment_id: str, **kwargs) -> EnvironmentResponse:
        """Gets runner information
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/runner/{environment_id}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvironmentResponse.model_validate(data)

    async def get_spaces_by_space_name_environments_runner_by_environment_id_client_by_operation_id(self, space_name: str, environment_id: str, operation_id: str, **kwargs) -> EnvironmentResponse:
        """Gets runner information
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/runner/{environment_id}/client/{operation_id}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return EnvironmentResponse.model_validate(data)

    async def post_spaces_by_space_name_environments_schedule(self, space_name: str, body: Any | None = None, **kwargs) -> ScheduleEnvironmentResponse:
        """Schedule new environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/schedule"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return ScheduleEnvironmentResponse.model_validate(data)

    async def get_spaces_by_space_name_environments_v2(self, space_name: str, query: dict | None = None, **kwargs) -> EnvironmentsResponse:
        """Get environment list
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/v2"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return EnvironmentsResponse.model_validate(data)

    async def post_accounts_users(self, body: Any | None = None, **kwargs) -> Any:
        """Add Users to Account without invitation
        Auto-generated from OpenAPI.
        """
        url = f"/accounts/users"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def post_policies_by_repository_name_discover(self, repository_name: str, **kwargs) -> List[OpaPolicyFileResponse]:
        """Discover policy candidates in repository
        Auto-generated from OpenAPI.
        """
        url = f"/policies/{repository_name}/discover"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ OpaPolicyFileResponse.model_validate(d) for d in data ]

    async def post_policies_by_repository_name_generate(self, repository_name: str, body: Any | None = None, **kwargs) -> List[GetAccountPolicyInstancesResponse]:
        """Generate policy instances from the chosen candidate files
        Auto-generated from OpenAPI.
        """
        url = f"/policies/{repository_name}/generate"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        data = self._handle_response(resp); return [ GetAccountPolicyInstancesResponse.model_validate(d) for d in data ]

    async def put_custom_resource(self, body: Any | None = None, **kwargs) -> Any:
        """Update custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def post_custom_resource(self, body: Any | None = None, **kwargs) -> Any:
        """Create custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_custom_resource_type(self, **kwargs) -> List[GetCustomResourceTypeResponse]:
        """Get custom resource type list
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ GetCustomResourceTypeResponse.model_validate(d) for d in data ]

    async def post_custom_resource_type(self, body: Any | None = None, **kwargs) -> Any:
        """Create custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def put_custom_resource_type_by_type_name(self, type_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type/{type_name}"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def delete_custom_resource_type_by_type_name(self, type_name: str, query: dict | None = None, **kwargs) -> Any:
        """Remove custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type/{type_name}"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def delete_custom_resource_by_id(self, id: str, query: dict | None = None, **kwargs) -> Any:
        """Remove custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource/{id}"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_resource(self, query: dict | None = None, **kwargs) -> GetAllResourcesResponse:
        """Get resource list
        Auto-generated from OpenAPI.
        """
        url = f"/resource"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return GetAllResourcesResponse.model_validate(data)

    async def get_resource_by_id(self, id: str, **kwargs) -> GetResourceDataResponse:
        """Get resource data by id
        Auto-generated from OpenAPI.
        """
        url = f"/resource/{id}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return GetResourceDataResponse.model_validate(data)

    async def put_resource_by_id_toggle_excluded_from_reserving(self, id: str, body: Any | None = None, **kwargs) -> Any:
        """Toggle resource exclusion from reservation by id
        Auto-generated from OpenAPI.
        """
        url = f"/resource/{id}/toggle_excluded_from_reserving"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_resource_metrics(self, query: dict | None = None, **kwargs) -> GetInventoryMetricsResponse:
        """Get resources metrics data
        Auto-generated from OpenAPI.
        """
        url = f"/resource/metrics"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return GetInventoryMetricsResponse.model_validate(data)

    async def post_spaces_by_space_name_labels(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Add new label
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/labels"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_labels_update(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update label
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/labels/update"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_settings_parameters(self, **kwargs) -> List[ParameterStoreItemResponse]:
        """Get all parameters
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ ParameterStoreItemResponse.model_validate(d) for d in data ]

    async def post_settings_parameters(self, body: Any | None = None, **kwargs) -> Any:
        """Create account parameter
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_settings_parameters_by_param_name(self, param_name: str, **kwargs) -> ParameterStoreItemResponse:
        """Get account parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return ParameterStoreItemResponse.model_validate(data)

    async def put_settings_parameters_by_param_name(self, param_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update account level parameter
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def delete_settings_parameters_by_param_name(self, param_name: str, **kwargs) -> Any:
        """Delete an account parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_settings_parameters(self, space_name: str, **kwargs) -> List[SpaceParameterStoreItemResponse]:
        """Get space parameters
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ SpaceParameterStoreItemResponse.model_validate(d) for d in data ]

    async def post_spaces_by_space_name_settings_parameters(self, space_name: str, body: Any | None = None, **kwargs) -> Any:
        """Create space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, **kwargs) -> SpaceParameterStoreItemResponse:
        """Get space parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return SpaceParameterStoreItemResponse.model_validate(data)

    async def put_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, body: Any | None = None, **kwargs) -> Any:
        """Update space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, **kwargs) -> Any:
        """Delete space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_repositories(self, space_name: str, **kwargs) -> List[RepositoryDetailsResponse]:
        """Get Repositories in space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        data = self._handle_response(resp); return [ RepositoryDetailsResponse.model_validate(d) for d in data ]

    async def delete_spaces_by_space_name_repositories(self, space_name: str, query: dict | None = None, **kwargs) -> Any:
        """Remove repository from space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_repositories_by_name(self, space_name: str, name: str, body: Any | None = None, **kwargs) -> Any:
        """Update repository configuration
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{name}"
        resp = await self.torque_client.request("PUT", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_repositories_by_repository_name_blueprints_by_blueprint_name_update(self, space_name: str, blueprint_name: str, repository_name: str, **kwargs) -> Any:
        """Invoke manual repository sync from repository
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repository_name}/blueprints/{blueprint_name}/update"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_repositories_by_repository_name_update(self, space_name: str, repository_name: str, **kwargs) -> Any:
        """Initiate repository scanning
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repository_name}/update"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_repositories_repository(self, space_name: str, query: dict | None = None, **kwargs) -> RepositoryDetailsResponse:
        """Get repository details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/repository"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        data = self._handle_response(resp); return RepositoryDetailsResponse.model_validate(data)

    async def post_spaces(self, body: Any | None = None, **kwargs) -> Any:
        """Create Space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces"
        resp = await self.torque_client.request("POST", url, params=None, json=(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name(self, space_name: str, **kwargs) -> Any:
        """Delete Space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)
