from __future__ import annotations
from abc import abstractmethod, abstractproperty
from typing import Any, Dict, List, Optional, Protocol

import httpx  # noqa: F401  (placeholders for future typing)

class _SupportsRequest(Protocol):
    def _handle_response(self, resp): ...  # type: ignore
    
    @property
    @abstractmethod
    def torque_client(self) -> httpx.BaseClient: ... # type: ignore

# AUTO-GENERATED: Do not edit manually. Run scripts/generate_endpoints.py

class TorqueEndpointsMixin(_SupportsRequest):
    def post_accounts_by_account_login(self, account: str, **kwargs):
        """Get token
        Auto-generated from OpenAPI.
        """
        url = f"/accounts/{account}/login"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def delete_long_token_by_space_name_by_token_id(self, token_id: str, space_name: str, **kwargs):
        """Revoke long token
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/{token_id}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=None, **kwargs))

    def post_long_token_by_space_name_longtoken(self, space_name: str, query: dict | None = None, **kwargs):
        """Generate long token
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/longtoken"
        return self._handle_response(self.torque_client.request("POST", url, params=query, **kwargs))

    def get_long_token_by_space_name_longtokens(self, space_name: str, **kwargs):
        """Get long tokens in space
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/longtokens"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def post_agent_k8s_by_agent_spaces_by_space_name(self, agent: str, space_name: str, **kwargs):
        """Associate k8s agent with a space
        Auto-generated from OpenAPI.
        """
        url = f"/agent/k8s/{agent}/spaces/{space_name}"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_settings_agents(self, query: dict | None = None, **kwargs):
        """Get agent list
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def post_settings_agents(self, **kwargs):
        """Create new agent
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def delete_settings_agents(self, query: dict | None = None, **kwargs):
        """Delete agent from account
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        return self._handle_response(self.torque_client.request("DELETE", url, params=query, **kwargs))

    def put_settings_agents_by_agent_name_new(self, agent_name: str, **kwargs):
        """Update agent configuration
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents/{agent_name}/new"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def get_settings_agents_by_agent_name_usages(self, agent_name: str, **kwargs):
        """Get agent usages per account
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents/{agent_name}/usages"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def get_spaces_by_space_name_agents(self, space_name: str, **kwargs):
        """List agents in space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def delete_spaces_by_space_name_agents_by_agent_name(self, space_name: str, agent_name: str, **kwargs):
        """Remove agent association from space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent_name}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=None, **kwargs))

    def get_spaces_by_space_name_agents_by_agent_name_usages(self, space_name: str, agent_name: str, **kwargs):
        """Get agent usages per space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent_name}/usages"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def post_spaces_by_space_name_agents_by_agent(self, space_name: str, agent: str, **kwargs):
        """Associate agent with space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent}"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_audit(self, query: dict | None = None, **kwargs):
        """Get audits events
        Auto-generated from OpenAPI.
        """
        url = f"/audit"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def get_spaces_by_space_name_asset_library(self, space_name: str, **kwargs):
        """Get all blueprints from asset library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def get_spaces_by_space_name_blueprints(self, space_name: str, query: dict | None = None, **kwargs):
        """Get all blueprints
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def post_spaces_by_space_name_blueprints_by_blueprintname(self, space_name: str, blueprintName: str, **kwargs):
        """Update blueprint display name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/{blueprintName}"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_spaces_by_space_name_blueprints_ai_blueprints_generation_data(self, space_name: str, **kwargs):
        """Get ai_generation_data for a blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/ai/blueprints_generation_data"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def put_spaces_by_space_name_blueprints_display_name(self, space_name: str, **kwargs):
        """Update blueprint display name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/display_name"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def get_spaces_by_space_name_designer_blueprints_simplified(self, space_name: str, query: dict | None = None, **kwargs):
        """Get all blueprints in simplified form
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-blueprints/simplified"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def get_spaces_by_space_name_designer_iac_assets_simplified(self, space_name: str, query: dict | None = None, **kwargs):
        """Get all IAC assets in simplified form
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-iac-assets/simplified"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def get_spaces_by_space_name_designer_iac_assets_summary(self, space_name: str, **kwargs):
        """Get IAC assets summary
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-iac-assets/summary"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def get_spaces_by_space_name_iac_assets(self, space_name: str, query: dict | None = None, **kwargs):
        """Get all IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def get_spaces_by_space_name_iac_assets_by_name(self, space_name: str, name: str, **kwargs):
        """Get IAC asset
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/{name}"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def post_spaces_by_space_name_iac_assets_by_name_sync(self, space_name: str, name: str, **kwargs):
        """Sync IAC asset
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/{name}/sync"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def post_spaces_by_space_name_iac_assets_generate_blueprint_yaml(self, space_name: str, **kwargs):
        """Generate blueprint from IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/generate-blueprint-yaml"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_spaces_by_space_name_iac_assets_metrics(self, space_name: str, query: dict | None = None, **kwargs):
        """Get all IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/metrics"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def get_spaces_by_space_name_repositories_by_repositoryname_blueprints(self, space_name: str, repositoryName: str, query: dict | None = None, **kwargs):
        """Get published blueprints
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repositoryName}/blueprints"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def post_spaces_by_space_name_validations_blueprints(self, space_name: str, **kwargs):
        """Validate blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/validations/blueprints"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def post_spaces_by_space_name_asset_library_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs):
        """Add blueprint to assets library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library/{blueprint_name}"
        return self._handle_response(self.torque_client.request("POST", url, params=query, **kwargs))

    def delete_spaces_by_space_name_asset_library_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs):
        """Remove blueprint from assets library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library/{blueprint_name}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=query, **kwargs))

    def get_spaces_by_space_name_catalog(self, space_name: str, **kwargs):
        """Get blueprints in catalog
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def put_spaces_by_space_name_catalog(self, space_name: str, **kwargs):
        """Edit Blueprint metadata
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def post_spaces_by_space_name_catalog(self, space_name: str, **kwargs):
        """Publish blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_spaces_by_space_name_catalog_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs):
        """Get blueprint details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/{blueprint_name}"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def delete_spaces_by_space_name_catalog_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs):
        """Unpublish blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/{blueprint_name}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=query, **kwargs))

    def put_spaces_by_space_name_catalog_labels(self, space_name: str, **kwargs):
        """Edit Blueprint labels
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/labels"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def put_spaces_by_space_name_catalog_launch_allowed(self, space_name: str, **kwargs):
        """Edit Blueprint launch allowed
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/launch_allowed"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def get_operation_hub(self, query: dict | None = None, **kwargs):
        """Get environment list
        Auto-generated from OpenAPI.
        """
        url = f"/operation_hub"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def get_settings_environmentfeed(self, query: dict | None = None, **kwargs):
        """Get all environment activity feed without pagination
        Auto-generated from OpenAPI.
        """
        url = f"/settings/environmentfeed"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def get_spaces_by_space_name_eac(self, space_name: str, **kwargs):
        """Get eac entries
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def put_spaces_by_space_name_eac_enable(self, space_name: str, **kwargs):
        """Set eac enablement
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/enable"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def post_spaces_by_space_name_eac_register(self, space_name: str, **kwargs):
        """Register eac file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/register"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_spaces_by_space_name_eac_registration_candidates(self, space_name: str, query: dict | None = None, **kwargs):
        """Show eac registration candidates
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/registration_candidates"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def delete_spaces_by_space_name_eac_unregister(self, space_name: str, **kwargs):
        """Unregister eac file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/unregister"
        return self._handle_response(self.torque_client.request("DELETE", url, params=None, **kwargs))

    def get_spaces_by_space_name_edit_environment_session(self, space_name: str, query: dict | None = None, **kwargs):
        """List edit sessions
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def post_spaces_by_space_name_edit_environment_session(self, space_name: str, **kwargs):
        """Start new edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_spaces_by_space_name_edit_environment_session_by_session_name(self, space_name: str, session_name: str, **kwargs):
        """Get edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def delete_spaces_by_space_name_edit_environment_session_by_session_name(self, space_name: str, session_name: str, **kwargs):
        """Abort edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=None, **kwargs))

    def put_spaces_by_space_name_edit_environment_session_by_session_name_apply(self, space_name: str, session_name: str, **kwargs):
        """Apply edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/apply"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def get_spaces_by_space_name_edit_environment_session_by_session_name_plan(self, space_name: str, session_name: str, **kwargs):
        """Get plan for edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/plan"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def put_spaces_by_space_name_edit_environment_session_by_session_name_save(self, space_name: str, session_name: str, **kwargs):
        """Save edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/save"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def post_spaces_by_space_name_environments(self, space_name: str, **kwargs):
        """Start new environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))
    
    def get_spaces_by_space_name_environments(self, space_name: str, **kwargs):
        """Get environments
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def get_spaces_by_space_name_environments_by_environment_id(self, space_name: str, environment_id: str, **kwargs):
        """Gets environment details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def delete_spaces_by_space_name_environments_by_environment_id(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs):
        """Terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=query, **kwargs))

    def post_spaces_by_space_name_environments_by_environment_id_by_grain_path_by_resource_id_run_action_by_(self, space_name: str, environment_id: str, grain_path: str, resource_id: str, action_id: str, **kwargs):
        """Invoke environment action
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/{grain_path}/{resource_id}/run_action/{action_id}"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def post_spaces_by_space_name_environments_by_environment_id_driftcheck_by_grain_id(self, space_name: str, environment_id: str, grain_id: str, **kwargs):
        """Invoke environment drift check
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/driftcheck/{grain_id}"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_spaces_by_space_name_environments_by_environment_id_eac(self, space_name: str, environment_id: str, **kwargs):
        """Export environment YAML file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def delete_spaces_by_space_name_environments_by_environment_id_eac(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs):
        """Terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac"
        return self._handle_response(self.torque_client.request("DELETE", url, params=query, **kwargs))

    def put_spaces_by_space_name_environments_by_environment_id_eac_detach(self, space_name: str, environment_id: str, **kwargs):
        """Detach Eac environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac/detach"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def put_spaces_by_space_name_environments_by_environment_id_extend(self, space_name: str, environment_id: str, **kwargs):
        """Extend environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/extend"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def put_spaces_by_space_name_environments_by_environment_id_labels(self, space_name: str, environment_id: str, **kwargs):
        """Update environment labels
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/labels"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def get_spaces_by_space_name_environments_by_environment_id_parameters(self, space_name: str, environment_id: str, **kwargs):
        """Get environment parameters and their drifts
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/parameters"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def post_spaces_by_space_name_environments_by_environment_id_plan(self, space_name: str, environment_id: str, **kwargs):
        """Plan environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/plan"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_spaces_by_space_name_environments_by_environment_id_plan_by_request_id(self, space_name: str, environment_id: str, request_id: str, **kwargs):
        """Get environment plan result
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/plan/{request_id}"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def post_spaces_by_space_name_environments_by_environment_id_reconcile(self, space_name: str, environment_id: str, **kwargs):
        """Invoke environment reconcile
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/reconcile"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def delete_spaces_by_space_name_environments_by_environment_id_release(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs):
        """End environment without termination
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/release"
        return self._handle_response(self.torque_client.request("DELETE", url, params=query, **kwargs))

    def put_spaces_by_space_name_environments_by_environment_id_update_env(self, space_name: str, environment_id: str, **kwargs):
        """Restart environment grains
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_env"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def post_spaces_by_space_name_environments_by_environment_id_update_v2(self, space_name: str, environment_id: str, **kwargs):
        """Update environment grains
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_environment_name_rename(self, space_name: str, environment_id: str, environment_name: str, **kwargs):
        """Update environment name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{environment_name}/rename"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_grain_path_approve(self, space_name: str, environment_id: str, grain_path: str, **kwargs):
        """Approve grain update
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{grain_path}/approve"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_grain_path_deny(self, space_name: str, environment_id: str, grain_path: str, **kwargs):
        """Deny grain update
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{grain_path}/deny"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def get_spaces_by_space_name_environments_by_environment_id_workflows(self, environment_id: str, space_name: str, **kwargs):
        """List environment workflows
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/workflows"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def put_spaces_by_space_name_environments_by_environment_id_workflows(self, environment_id: str, space_name: str, query: dict | None = None, **kwargs):
        """Invoke environment workflow
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/workflows"
        return self._handle_response(self.torque_client.request("PUT", url, params=query, **kwargs))

    def patch_spaces_by_space_name_environments_cancel_scheduled_by_environment_id(self, space_name: str, environment_id: str, **kwargs):
        """Cancel scheduled environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/cancel/scheduled/{environment_id}"
        return self._handle_response(self.torque_client.request("PATCH", url, params=None, **kwargs))

    def get_spaces_by_space_name_environments_consumption_run_policies(self, space_name: str, query: dict | None = None, **kwargs):
        """Run consumption policies
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/consumption/run_policies"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def delete_spaces_by_space_name_environments_force_by_environment_id(self, space_name: str, environment_id: str, **kwargs):
        """Force terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/force/{environment_id}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=None, **kwargs))

    def post_spaces_by_space_name_environments_import(self, space_name: str, **kwargs):
        """Import environment to Torque
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/import"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def post_spaces_by_space_name_environments_import_using_blueprint(self, space_name: str, **kwargs):
        """Import environment with blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/import_using_blueprint"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_spaces_by_space_name_environments_runner_by_environment_id(self, space_name: str, environment_id: str, **kwargs):
        """Gets runner information
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/runner/{environment_id}"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def get_spaces_by_space_name_environments_runner_by_environment_id_client_by_operation_id(self, space_name: str, environment_id: str, operation_id: str, **kwargs):
        """Gets runner information
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/runner/{environment_id}/client/{operation_id}"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def post_spaces_by_space_name_environments_schedule(self, space_name: str, **kwargs):
        """Schedule new environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/schedule"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_spaces_by_space_name_environments_v2(self, space_name: str, query: dict | None = None, **kwargs):
        """Get environment list
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/v2"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def post_accounts_users(self, **kwargs):
        """Add Users to Account without invitation
        Auto-generated from OpenAPI.
        """
        url = f"/accounts/users"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def post_policies_by_repository_name_discover(self, repository_name: str, **kwargs):
        """Discover policy candidates in repository
        Auto-generated from OpenAPI.
        """
        url = f"/policies/{repository_name}/discover"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def post_policies_by_repository_name_generate(self, repository_name: str, **kwargs):
        """Generate policy instances from the chosen candidate files
        Auto-generated from OpenAPI.
        """
        url = f"/policies/{repository_name}/generate"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def put_custom_resource(self, **kwargs):
        """Update custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def post_custom_resource(self, **kwargs):
        """Create custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_custom_resource_type(self, **kwargs):
        """Get custom resource type list
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def post_custom_resource_type(self, **kwargs):
        """Create custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def put_custom_resource_type_by_type_name(self, type_name: str, **kwargs):
        """Update custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type/{type_name}"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def delete_custom_resource_type_by_type_name(self, type_name: str, query: dict | None = None, **kwargs):
        """Remove custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type/{type_name}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=query, **kwargs))

    def delete_custom_resource_by_id(self, id: str, query: dict | None = None, **kwargs):
        """Remove custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource/{id}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=query, **kwargs))

    def get_resource(self, query: dict | None = None, **kwargs):
        """Get resource list
        Auto-generated from OpenAPI.
        """
        url = f"/resource"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def get_resource_by_id(self, id: str, **kwargs):
        """Get resource data by id
        Auto-generated from OpenAPI.
        """
        url = f"/resource/{id}"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def put_resource_by_id_toggle_excluded_from_reserving(self, id: str, **kwargs):
        """Toggle resource exclusion from reservation by id
        Auto-generated from OpenAPI.
        """
        url = f"/resource/{id}/toggle_excluded_from_reserving"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def get_resource_metrics(self, query: dict | None = None, **kwargs):
        """Get resources metrics data
        Auto-generated from OpenAPI.
        """
        url = f"/resource/metrics"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def post_spaces_by_space_name_labels(self, space_name: str, **kwargs):
        """Add new label
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/labels"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def put_spaces_by_space_name_labels_update(self, space_name: str, **kwargs):
        """Update label
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/labels/update"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def get_settings_parameters(self, **kwargs):
        """Get all parameters
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def post_settings_parameters(self, **kwargs):
        """Create account parameter
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_settings_parameters_by_param_name(self, param_name: str, **kwargs):
        """Get account parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def put_settings_parameters_by_param_name(self, param_name: str, **kwargs):
        """Update account level parameter
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def delete_settings_parameters_by_param_name(self, param_name: str, **kwargs):
        """Delete an account parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=None, **kwargs))

    def get_spaces_by_space_name_settings_parameters(self, space_name: str, **kwargs):
        """Get space parameters
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def post_spaces_by_space_name_settings_parameters(self, space_name: str, **kwargs):
        """Create space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, **kwargs):
        """Get space parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def put_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, **kwargs):
        """Update space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def delete_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, **kwargs):
        """Delete space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=None, **kwargs))

    def get_spaces_by_space_name_repositories(self, space_name: str, **kwargs):
        """Get Repositories in space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories"
        return self._handle_response(self.torque_client.request("GET", url, params=None, **kwargs))

    def delete_spaces_by_space_name_repositories(self, space_name: str, query: dict | None = None, **kwargs):
        """Remove repository from space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories"
        return self._handle_response(self.torque_client.request("DELETE", url, params=query, **kwargs))

    def put_spaces_by_space_name_repositories_by_name(self, space_name: str, name: str, **kwargs):
        """Update repository configuration
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{name}"
        return self._handle_response(self.torque_client.request("PUT", url, params=None, **kwargs))

    def post_spaces_by_space_name_repositories_by_repository_name_blueprints_by_blueprint_name_update(self, space_name: str, blueprint_name: str, repository_name: str, **kwargs):
        """Invoke manual repository sync from repository
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repository_name}/blueprints/{blueprint_name}/update"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def post_spaces_by_space_name_repositories_by_repository_name_update(self, space_name: str, repository_name: str, **kwargs):
        """Initiate repository scanning
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repository_name}/update"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def get_spaces_by_space_name_repositories_repository(self, space_name: str, query: dict | None = None, **kwargs):
        """Get repository details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/repository"
        return self._handle_response(self.torque_client.request("GET", url, params=query, **kwargs))

    def post_spaces(self, **kwargs):
        """Create Space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces"
        return self._handle_response(self.torque_client.request("POST", url, params=None, **kwargs))

    def delete_spaces_by_space_name(self, space_name: str, **kwargs):
        """Delete Space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}"
        return self._handle_response(self.torque_client.request("DELETE", url, params=None, **kwargs))


class AsyncTorqueEndpointsMixin(_SupportsRequest):
    async def post_accounts_by_account_login(self, account: str, **kwargs):
        """Get token
        Auto-generated from OpenAPI.
        """
        url = f"/accounts/{account}/login"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_long_token_by_space_name_by_token_id(self, token_id: str, space_name: str, **kwargs):
        """Revoke long token
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/{token_id}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_long_token_by_space_name_longtoken(self, space_name: str, query: dict | None = None, **kwargs):
        """Generate long token
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/longtoken"
        resp = await self.torque_client.request("POST", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_long_token_by_space_name_longtokens(self, space_name: str, **kwargs):
        """Get long tokens in space
        Auto-generated from OpenAPI.
        """
        url = f"/long-token/{space_name}/longtokens"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_agent_k8s_by_agent_spaces_by_space_name(self, agent: str, space_name: str, **kwargs):
        """Associate k8s agent with a space
        Auto-generated from OpenAPI.
        """
        url = f"/agent/k8s/{agent}/spaces/{space_name}"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_settings_agents(self, query: dict | None = None, **kwargs):
        """Get agent list
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def post_settings_agents(self, **kwargs):
        """Create new agent
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_settings_agents(self, query: dict | None = None, **kwargs):
        """Delete agent from account
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def put_settings_agents_by_agent_name_new(self, agent_name: str, **kwargs):
        """Update agent configuration
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents/{agent_name}/new"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_settings_agents_by_agent_name_usages(self, agent_name: str, **kwargs):
        """Get agent usages per account
        Auto-generated from OpenAPI.
        """
        url = f"/settings/agents/{agent_name}/usages"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_agents(self, space_name: str, **kwargs):
        """List agents in space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_agents_by_agent_name(self, space_name: str, agent_name: str, **kwargs):
        """Remove agent association from space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent_name}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_agents_by_agent_name_usages(self, space_name: str, agent_name: str, **kwargs):
        """Get agent usages per space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent_name}/usages"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_agents_by_agent(self, space_name: str, agent: str, **kwargs):
        """Associate agent with space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/agents/{agent}"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_audit(self, query: dict | None = None, **kwargs):
        """Get audits events
        Auto-generated from OpenAPI.
        """
        url = f"/audit"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_asset_library(self, space_name: str, **kwargs):
        """Get all blueprints from asset library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_blueprints(self, space_name: str, query: dict | None = None, **kwargs):
        """Get all blueprints
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_blueprints_by_blueprintname(self, space_name: str, blueprintName: str, **kwargs):
        """Update blueprint display name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/{blueprintName}"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_blueprints_ai_blueprints_generation_data(self, space_name: str, **kwargs):
        """Get ai_generation_data for a blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/ai/blueprints_generation_data"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_blueprints_display_name(self, space_name: str, **kwargs):
        """Update blueprint display name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/blueprints/display_name"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_designer_blueprints_simplified(self, space_name: str, query: dict | None = None, **kwargs):
        """Get all blueprints in simplified form
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-blueprints/simplified"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_designer_iac_assets_simplified(self, space_name: str, query: dict | None = None, **kwargs):
        """Get all IAC assets in simplified form
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-iac-assets/simplified"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_designer_iac_assets_summary(self, space_name: str, **kwargs):
        """Get IAC assets summary
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/designer-iac-assets/summary"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_iac_assets(self, space_name: str, query: dict | None = None, **kwargs):
        """Get all IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_iac_assets_by_name(self, space_name: str, name: str, **kwargs):
        """Get IAC asset
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/{name}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_iac_assets_by_name_sync(self, space_name: str, name: str, **kwargs):
        """Sync IAC asset
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/{name}/sync"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_iac_assets_generate_blueprint_yaml(self, space_name: str, **kwargs):
        """Generate blueprint from IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/generate-blueprint-yaml"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_iac_assets_metrics(self, space_name: str, query: dict | None = None, **kwargs):
        """Get all IAC assets
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/iac-assets/metrics"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_repositories_by_repositoryname_blueprints(self, space_name: str, repositoryName: str, query: dict | None = None, **kwargs):
        """Get published blueprints
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repositoryName}/blueprints"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_validations_blueprints(self, space_name: str, **kwargs):
        """Validate blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/validations/blueprints"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_asset_library_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs):
        """Add blueprint to assets library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library/{blueprint_name}"
        resp = await self.torque_client.request("POST", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_asset_library_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs):
        """Remove blueprint from assets library
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/asset-library/{blueprint_name}"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_catalog(self, space_name: str, **kwargs):
        """Get blueprints in catalog
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_catalog(self, space_name: str, **kwargs):
        """Edit Blueprint metadata
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_catalog(self, space_name: str, **kwargs):
        """Publish blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_catalog_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs):
        """Get blueprint details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/{blueprint_name}"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_catalog_by_blueprint_name(self, space_name: str, blueprint_name: str, query: dict | None = None, **kwargs):
        """Unpublish blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/{blueprint_name}"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_catalog_labels(self, space_name: str, **kwargs):
        """Edit Blueprint labels
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/labels"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_catalog_launch_allowed(self, space_name: str, **kwargs):
        """Edit Blueprint launch allowed
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/catalog/launch_allowed"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_operation_hub(self, query: dict | None = None, **kwargs):
        """Get environment list
        Auto-generated from OpenAPI.
        """
        url = f"/operation_hub"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_settings_environmentfeed(self, query: dict | None = None, **kwargs):
        """Get all environment activity feed without pagination
        Auto-generated from OpenAPI.
        """
        url = f"/settings/environmentfeed"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_eac(self, space_name: str, **kwargs):
        """Get eac entries
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_eac_enable(self, space_name: str, **kwargs):
        """Set eac enablement
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/enable"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_eac_register(self, space_name: str, **kwargs):
        """Register eac file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/register"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_eac_registration_candidates(self, space_name: str, query: dict | None = None, **kwargs):
        """Show eac registration candidates
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/registration_candidates"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_eac_unregister(self, space_name: str, **kwargs):
        """Unregister eac file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/eac/unregister"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_edit_environment_session(self, space_name: str, query: dict | None = None, **kwargs):
        """List edit sessions
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_edit_environment_session(self, space_name: str, **kwargs):
        """Start new edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_edit_environment_session_by_session_name(self, space_name: str, session_name: str, **kwargs):
        """Get edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_edit_environment_session_by_session_name(self, space_name: str, session_name: str, **kwargs):
        """Abort edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_edit_environment_session_by_session_name_apply(self, space_name: str, session_name: str, **kwargs):
        """Apply edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/apply"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_edit_environment_session_by_session_name_plan(self, space_name: str, session_name: str, **kwargs):
        """Get plan for edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/plan"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_edit_environment_session_by_session_name_save(self, space_name: str, session_name: str, **kwargs):
        """Save edit session
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/edit_environment/session/{session_name}/save"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments(self, space_name: str, **kwargs):
        """Start new environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_by_environment_id(self, space_name: str, environment_id: str, **kwargs):
        """Gets environment details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_environments_by_environment_id(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs):
        """Terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_by_environment_id_by_grain_path_by_resource_id_run_action_by_(self, space_name: str, environment_id: str, grain_path: str, resource_id: str, action_id: str, **kwargs):
        """Invoke environment action
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/{grain_path}/{resource_id}/run_action/{action_id}"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_by_environment_id_driftcheck_by_grain_id(self, space_name: str, environment_id: str, grain_id: str, **kwargs):
        """Invoke environment drift check
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/driftcheck/{grain_id}"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_by_environment_id_eac(self, space_name: str, environment_id: str, **kwargs):
        """Export environment YAML file
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_environments_by_environment_id_eac(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs):
        """Terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_eac_detach(self, space_name: str, environment_id: str, **kwargs):
        """Detach Eac environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/eac/detach"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_extend(self, space_name: str, environment_id: str, **kwargs):
        """Extend environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/extend"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_labels(self, space_name: str, environment_id: str, **kwargs):
        """Update environment labels
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/labels"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_by_environment_id_parameters(self, space_name: str, environment_id: str, **kwargs):
        """Get environment parameters and their drifts
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/parameters"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_by_environment_id_plan(self, space_name: str, environment_id: str, **kwargs):
        """Plan environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/plan"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_by_environment_id_plan_by_request_id(self, space_name: str, environment_id: str, request_id: str, **kwargs):
        """Get environment plan result
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/plan/{request_id}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_by_environment_id_reconcile(self, space_name: str, environment_id: str, **kwargs):
        """Invoke environment reconcile
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/reconcile"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_environments_by_environment_id_release(self, space_name: str, environment_id: str, query: dict | None = None, **kwargs):
        """End environment without termination
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/release"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_update_env(self, space_name: str, environment_id: str, **kwargs):
        """Restart environment grains
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_env"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_by_environment_id_update_v2(self, space_name: str, environment_id: str, **kwargs):
        """Update environment grains
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_environment_name_rename(self, space_name: str, environment_id: str, environment_name: str, **kwargs):
        """Update environment name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{environment_name}/rename"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_grain_path_approve(self, space_name: str, environment_id: str, grain_path: str, **kwargs):
        """Approve grain update
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{grain_path}/approve"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_update_v2_by_grain_path_deny(self, space_name: str, environment_id: str, grain_path: str, **kwargs):
        """Deny grain update
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/update_v2/{grain_path}/deny"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_by_environment_id_workflows(self, environment_id: str, space_name: str, **kwargs):
        """List environment workflows
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/workflows"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_environments_by_environment_id_workflows(self, environment_id: str, space_name: str, query: dict | None = None, **kwargs):
        """Invoke environment workflow
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/{environment_id}/workflows"
        resp = await self.torque_client.request("PUT", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def patch_spaces_by_space_name_environments_cancel_scheduled_by_environment_id(self, space_name: str, environment_id: str, **kwargs):
        """Cancel scheduled environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/cancel/scheduled/{environment_id}"
        resp = await self.torque_client.request("PATCH", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_consumption_run_policies(self, space_name: str, query: dict | None = None, **kwargs):
        """Run consumption policies
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/consumption/run_policies"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_environments_force_by_environment_id(self, space_name: str, environment_id: str, **kwargs):
        """Force terminate environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/force/{environment_id}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_import(self, space_name: str, **kwargs):
        """Import environment to Torque
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/import"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_import_using_blueprint(self, space_name: str, **kwargs):
        """Import environment with blueprint
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/import_using_blueprint"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_runner_by_environment_id(self, space_name: str, environment_id: str, **kwargs):
        """Gets runner information
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/runner/{environment_id}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_runner_by_environment_id_client_by_operation_id(self, space_name: str, environment_id: str, operation_id: str, **kwargs):
        """Gets runner information
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/runner/{environment_id}/client/{operation_id}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_environments_schedule(self, space_name: str, **kwargs):
        """Schedule new environment
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/schedule"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_environments_v2(self, space_name: str, query: dict | None = None, **kwargs):
        """Get environment list
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/environments/v2"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def post_accounts_users(self, **kwargs):
        """Add Users to Account without invitation
        Auto-generated from OpenAPI.
        """
        url = f"/accounts/users"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_policies_by_repository_name_discover(self, repository_name: str, **kwargs):
        """Discover policy candidates in repository
        Auto-generated from OpenAPI.
        """
        url = f"/policies/{repository_name}/discover"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_policies_by_repository_name_generate(self, repository_name: str, **kwargs):
        """Generate policy instances from the chosen candidate files
        Auto-generated from OpenAPI.
        """
        url = f"/policies/{repository_name}/generate"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_custom_resource(self, **kwargs):
        """Update custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_custom_resource(self, **kwargs):
        """Create custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_custom_resource_type(self, **kwargs):
        """Get custom resource type list
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_custom_resource_type(self, **kwargs):
        """Create custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_custom_resource_type_by_type_name(self, type_name: str, **kwargs):
        """Update custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type/{type_name}"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_custom_resource_type_by_type_name(self, type_name: str, query: dict | None = None, **kwargs):
        """Remove custom resource type
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource_type/{type_name}"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def delete_custom_resource_by_id(self, id: str, query: dict | None = None, **kwargs):
        """Remove custom resource
        Auto-generated from OpenAPI.
        """
        url = f"/custom_resource/{id}"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_resource(self, query: dict | None = None, **kwargs):
        """Get resource list
        Auto-generated from OpenAPI.
        """
        url = f"/resource"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def get_resource_by_id(self, id: str, **kwargs):
        """Get resource data by id
        Auto-generated from OpenAPI.
        """
        url = f"/resource/{id}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_resource_by_id_toggle_excluded_from_reserving(self, id: str, **kwargs):
        """Toggle resource exclusion from reservation by id
        Auto-generated from OpenAPI.
        """
        url = f"/resource/{id}/toggle_excluded_from_reserving"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_resource_metrics(self, query: dict | None = None, **kwargs):
        """Get resources metrics data
        Auto-generated from OpenAPI.
        """
        url = f"/resource/metrics"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_labels(self, space_name: str, **kwargs):
        """Add new label
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/labels"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_labels_update(self, space_name: str, **kwargs):
        """Update label
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/labels/update"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_settings_parameters(self, **kwargs):
        """Get all parameters
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_settings_parameters(self, **kwargs):
        """Create account parameter
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_settings_parameters_by_param_name(self, param_name: str, **kwargs):
        """Get account parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_settings_parameters_by_param_name(self, param_name: str, **kwargs):
        """Update account level parameter
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_settings_parameters_by_param_name(self, param_name: str, **kwargs):
        """Delete an account parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/settings/parameters/{param_name}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_settings_parameters(self, space_name: str, **kwargs):
        """Get space parameters
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_settings_parameters(self, space_name: str, **kwargs):
        """Create space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, **kwargs):
        """Get space parameter by name
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, **kwargs):
        """Update space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_settings_parameters_by_param_name(self, space_name: str, param_name: str, **kwargs):
        """Delete space parameter
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/settings/parameters/{param_name}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_repositories(self, space_name: str, **kwargs):
        """Get Repositories in space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories"
        resp = await self.torque_client.request("GET", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name_repositories(self, space_name: str, query: dict | None = None, **kwargs):
        """Remove repository from space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories"
        resp = await self.torque_client.request("DELETE", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def put_spaces_by_space_name_repositories_by_name(self, space_name: str, name: str, **kwargs):
        """Update repository configuration
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{name}"
        resp = await self.torque_client.request("PUT", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_repositories_by_repository_name_blueprints_by_blueprint_name_update(self, space_name: str, blueprint_name: str, repository_name: str, **kwargs):
        """Invoke manual repository sync from repository
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repository_name}/blueprints/{blueprint_name}/update"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def post_spaces_by_space_name_repositories_by_repository_name_update(self, space_name: str, repository_name: str, **kwargs):
        """Initiate repository scanning
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/{repository_name}/update"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def get_spaces_by_space_name_repositories_repository(self, space_name: str, query: dict | None = None, **kwargs):
        """Get repository details
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}/repositories/repository"
        resp = await self.torque_client.request("GET", url, params=query, **kwargs)
        return self._handle_response(resp)

    async def post_spaces(self, **kwargs):
        """Create Space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces"
        resp = await self.torque_client.request("POST", url, params=None, **kwargs)
        return self._handle_response(resp)

    async def delete_spaces_by_space_name(self, space_name: str, **kwargs):
        """Delete Space
        Auto-generated from OpenAPI.
        """
        url = f"/spaces/{space_name}"
        resp = await self.torque_client.request("DELETE", url, params=None, **kwargs)
        return self._handle_response(resp)
