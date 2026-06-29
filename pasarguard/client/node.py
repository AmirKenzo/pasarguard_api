from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
)

from ..enums import (
    NodeStatus,
    Period,
    UsageTable,
    UserCountMetric,
)
from ..models import (
    BulkNodesActionResponse,
    BulkNodeSelection,
    NodeCoreUpdate,
    NodeCreate,
    NodeGeoFilesUpdate,
    NodeModify,
    NodeOutboundsLatencyResponse,
    NodeRealtimeStats,
    NodeResponse,
    NodeSettings,
    NodesResponse,
    NodesSimpleResponse,
    NodeStatsList,
    NodeUsageStatsList,
    RemoveNodesResponse,
    UserCountMetricStatsList,
    UserIPList,
    UserIPListAll,
)


class NodeMixin:
    async def get_node_settings(self, token: str | None = None) -> NodeSettings:
        url = "/api/node/settings"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeSettings)

    async def get_usage(
        self,
        token: str | None = None,
        period: Period | None = "hour",
        node_id: int | None = None,
        group_by_node: bool | None = False,
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> NodeUsageStatsList:
        url = "/api/node/usage"
        params = {"period": period, "node_id": node_id, "group_by_node": group_by_node, "start": start, "end": end}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeUsageStatsList)

    async def get_user_count_metric(
        self,
        metric: UserCountMetric,
        token: str | None = None,
        period: Period | None = "hour",
        node_id: int | None = None,
        group_by_node: bool | None = False,
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> UserCountMetricStatsList:
        url = f"/api/node/user_counts/{metric}"
        params = {"period": period, "node_id": node_id, "group_by_node": group_by_node, "start": start, "end": end}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserCountMetricStatsList)

    async def get_nodes(
        self,
        token: str | None = None,
        core_id: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
        ids: list[int] | None = None,
        status: NodeStatus | list[NodeStatus] | None = None,
        enabled: bool | None = False,
        search: str | None = None,
    ) -> NodesResponse:
        url = "/api/nodes"
        params = {
            "core_id": core_id,
            "offset": offset,
            "limit": limit,
            "ids": ids,
            "status": status,
            "enabled": enabled,
            "search": search,
        }
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodesResponse)

    async def get_nodes_simple(
        self,
        token: str | None = None,
        ids: list[int] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        search: str | None = None,
        sort: str | None = None,
        all: bool | None = False,
    ) -> NodesSimpleResponse:
        url = "/api/nodes/simple"
        params = {"ids": ids, "offset": offset, "limit": limit, "search": search, "sort": sort, "all": all}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodesSimpleResponse)

    async def reconnect_all_node(self, token: str | None = None, core_id: int | None = None) -> Any:
        url = "/api/nodes/reconnect"
        params = {"core_id": core_id}
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def create_node(self, node: NodeCreate, token: str | None = None) -> NodeResponse:
        url = "/api/node"
        params = None
        headers = None
        payload = self._validate_payload(node, NodeCreate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, NodeResponse)

    async def get_node(self, node_id: int, token: str | None = None) -> NodeResponse:
        url = f"/api/node/{node_id}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeResponse)

    async def modify_node(self, node_id: int, node: NodeModify, token: str | None = None) -> NodeResponse:
        url = f"/api/node/{node_id}"
        params = None
        headers = None
        payload = self._validate_payload(node, NodeModify)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, NodeResponse)

    async def remove_node(self, node_id: int, token: str | None = None) -> None:
        url = f"/api/node/{node_id}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def update_node(self, node_id: int, token: str | None = None) -> Any:
        url = f"/api/node/{node_id}/update"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def update_core(self, node_id: int, node_core_update: NodeCoreUpdate, token: str | None = None) -> Any:
        url = f"/api/node/{node_id}/core_update"
        params = None
        headers = None
        payload = self._validate_payload(node_core_update, NodeCoreUpdate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def update_geofiles(
        self, node_id: int, node_geo_files_update: NodeGeoFilesUpdate, token: str | None = None
    ) -> Any:
        url = f"/api/node/{node_id}/geofiles"
        params = None
        headers = None
        payload = self._validate_payload(node_geo_files_update, NodeGeoFilesUpdate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def reset_node_usage(self, node_id: int, token: str | None = None) -> NodeResponse:
        url = f"/api/node/{node_id}/reset"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeResponse)

    async def reconnect_node(self, node_id: int, token: str | None = None) -> Any:
        url = f"/api/node/{node_id}/reconnect"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def sync_node(self, node_id: int, token: str | None = None, flush_users: bool | None = True) -> Any:
        url = f"/api/node/{node_id}/sync"
        params = {"flush_users": flush_users}
        headers = None
        response = await self._request("PUT", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def node_logs(self, node_id: int, token: str | None = None) -> Any:
        url = f"/api/node/{node_id}/logs"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def get_node_stats_periodic(
        self,
        node_id: int,
        token: str | None = None,
        period: Period | None = "hour",
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> NodeStatsList:
        url = f"/api/node/{node_id}/stats"
        params = {"period": period, "start": start, "end": end}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeStatsList)

    async def realtime_node_stats(self, node_id: int, token: str | None = None) -> NodeRealtimeStats:
        url = f"/api/node/{node_id}/realtime_stats"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeRealtimeStats)

    async def node_outbounds_latency(
        self, node_id: int, token: str | None = None, name: str | None = "", timeout: int | None = None
    ) -> NodeOutboundsLatencyResponse:
        url = f"/api/node/{node_id}/outbounds_latency"
        params = {"name": name, "timeout": timeout}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeOutboundsLatencyResponse)

    async def realtime_nodes_stats(self, token: str | None = None) -> dict[str, NodeRealtimeStats | None]:
        url = "/api/nodes/realtime_stats"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, dict[str, NodeRealtimeStats | None])

    async def user_online_ip_list_all_nodes(self, user_id: int, token: str | None = None) -> UserIPListAll:
        url = f"/api/node/online_stats/{user_id}/ip"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserIPListAll)

    async def user_online_stats(self, node_id: int, user_id: int, token: str | None = None) -> dict[str, int]:
        url = f"/api/node/{node_id}/online_stats/{user_id}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, dict[str, int])

    async def user_online_ip_list(self, node_id: int, user_id: int, token: str | None = None) -> UserIPList:
        url = f"/api/node/{node_id}/online_stats/{user_id}/ip"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserIPList)

    async def clear_usage_data(
        self, table: UsageTable, token: str | None = None, start: datetime | None = None, end: datetime | None = None
    ) -> Any:
        url = f"/api/nodes/clear_usage_data/{table}"
        params = {"start": start, "end": end}
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def bulk_delete_nodes(self, bulk: BulkNodeSelection, token: str | None = None) -> RemoveNodesResponse:
        url = "/api/nodes/bulk/delete"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveNodesResponse)

    async def bulk_disable_nodes(self, bulk: BulkNodeSelection, token: str | None = None) -> BulkNodesActionResponse:
        url = "/api/nodes/bulk/disable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkNodesActionResponse)

    async def bulk_enable_nodes(self, bulk: BulkNodeSelection, token: str | None = None) -> BulkNodesActionResponse:
        url = "/api/nodes/bulk/enable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkNodesActionResponse)

    async def bulk_reset_nodes_usage(
        self, bulk: BulkNodeSelection, token: str | None = None
    ) -> BulkNodesActionResponse:
        url = "/api/nodes/bulk/reset"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkNodesActionResponse)

    async def bulk_reconnect_nodes(self, bulk: BulkNodeSelection, token: str | None = None) -> BulkNodesActionResponse:
        url = "/api/nodes/bulk/reconnect"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkNodesActionResponse)

    async def bulk_update_nodes(self, bulk: BulkNodeSelection, token: str | None = None) -> BulkNodesActionResponse:
        url = "/api/nodes/bulk/update"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkNodesActionResponse)
