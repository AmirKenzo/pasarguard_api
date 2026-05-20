from __future__ import annotations

from ._imports import (
    Any,
    BulkNodeSelection,
    BulkNodesActionResponse,
    Dict,
    List,
    NodeCoreUpdate,
    NodeCreate,
    NodeGeoFilesUpdate,
    NodeModify,
    NodeOutboundsLatencyResponse,
    NodeRealtimeStats,
    NodeResponse,
    NodeSettings,
    NodeStatsList,
    NodeStatus,
    NodeUsageStatsList,
    NodesResponse,
    NodesSimpleResponse,
    Optional,
    Period,
    RemoveNodesResponse,
    Union,
    UsageTable,
    UserCountMetric,
    UserCountMetricStatsList,
    UserIPList,
    UserIPListAll,
    datetime,
)


class NodeMixin:
    async def get_node_settings(self, token: str) -> NodeSettings:
        url = '/api/node/settings'
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeSettings)

    async def get_usage(self, token: str, period: Optional[Period] = 'hour', node_id: Optional[int] = None, group_by_node: Optional[bool] = False, start: Optional[datetime] = None, end: Optional[datetime] = None) -> NodeUsageStatsList:
        url = '/api/node/usage'
        params = {'period': period, 'node_id': node_id, 'group_by_node': group_by_node, 'start': start, 'end': end}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeUsageStatsList)

    async def get_user_count_metric(self, metric: UserCountMetric, token: str, period: Optional[Period] = 'hour', node_id: Optional[int] = None, group_by_node: Optional[bool] = False, start: Optional[datetime] = None, end: Optional[datetime] = None) -> UserCountMetricStatsList:
        url = '/api/node/user_counts/{metric}'.format(metric=metric)
        params = {'period': period, 'node_id': node_id, 'group_by_node': group_by_node, 'start': start, 'end': end}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserCountMetricStatsList)

    async def get_nodes(self, token: str, core_id: Optional[int] = None, offset: Optional[int] = None, limit: Optional[int] = None, ids: Optional[List[int]] = None, status: Optional[Union[NodeStatus, List[NodeStatus]]] = None, enabled: Optional[bool] = False, search: Optional[str] = None) -> NodesResponse:
        url = '/api/nodes'
        params = {'core_id': core_id, 'offset': offset, 'limit': limit, 'ids': ids, 'status': status, 'enabled': enabled, 'search': search}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodesResponse)

    async def get_nodes_simple(self, token: str, ids: Optional[List[int]] = None, offset: Optional[int] = None, limit: Optional[int] = None, search: Optional[str] = None, sort: Optional[str] = None, all: Optional[bool] = False) -> NodesSimpleResponse:
        url = '/api/nodes/simple'
        params = {'ids': ids, 'offset': offset, 'limit': limit, 'search': search, 'sort': sort, 'all': all}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodesSimpleResponse)

    async def reconnect_all_node(self, token: str, core_id: Optional[int] = None) -> Any:
        url = '/api/nodes/reconnect'
        params = {'core_id': core_id}
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def create_node(self, node: NodeCreate, token: str) -> NodeResponse:
        url = '/api/node'
        params = None
        headers = None
        payload = self._validate_payload(node, NodeCreate)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, NodeResponse)

    async def get_node(self, node_id: int, token: str) -> NodeResponse:
        url = '/api/node/{node_id}'.format(node_id=node_id)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeResponse)

    async def modify_node(self, node_id: int, node: NodeModify, token: str) -> NodeResponse:
        url = '/api/node/{node_id}'.format(node_id=node_id)
        params = None
        headers = None
        payload = self._validate_payload(node, NodeModify)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, NodeResponse)

    async def remove_node(self, node_id: int, token: str) -> None:
        url = '/api/node/{node_id}'.format(node_id=node_id)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def update_node(self, node_id: int, token: str) -> Any:
        url = '/api/node/{node_id}/update'.format(node_id=node_id)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def update_core(self, node_id: int, node_core_update: NodeCoreUpdate, token: str) -> Any:
        url = '/api/node/{node_id}/core_update'.format(node_id=node_id)
        params = None
        headers = None
        payload = self._validate_payload(node_core_update, NodeCoreUpdate)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def update_geofiles(self, node_id: int, node_geo_files_update: NodeGeoFilesUpdate, token: str) -> Any:
        url = '/api/node/{node_id}/geofiles'.format(node_id=node_id)
        params = None
        headers = None
        payload = self._validate_payload(node_geo_files_update, NodeGeoFilesUpdate)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def reset_node_usage(self, node_id: int, token: str) -> NodeResponse:
        url = '/api/node/{node_id}/reset'.format(node_id=node_id)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeResponse)

    async def reconnect_node(self, node_id: int, token: str) -> Any:
        url = '/api/node/{node_id}/reconnect'.format(node_id=node_id)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def sync_node(self, node_id: int, token: str, flush_users: Optional[bool] = False) -> Any:
        url = '/api/node/{node_id}/sync'.format(node_id=node_id)
        params = {'flush_users': flush_users}
        headers = None
        response = await self._request('PUT', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def node_logs(self, node_id: int, token: str) -> Any:
        url = '/api/node/{node_id}/logs'.format(node_id=node_id)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def get_node_stats_periodic(self, node_id: int, token: str, period: Optional[Period] = 'hour', start: Optional[datetime] = None, end: Optional[datetime] = None) -> NodeStatsList:
        url = '/api/node/{node_id}/stats'.format(node_id=node_id)
        params = {'period': period, 'start': start, 'end': end}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeStatsList)

    async def realtime_node_stats(self, node_id: int, token: str) -> NodeRealtimeStats:
        url = '/api/node/{node_id}/realtime_stats'.format(node_id=node_id)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeRealtimeStats)

    async def node_outbounds_latency(self, node_id: int, token: str, name: Optional[str] = '', timeout: Optional[int] = None) -> NodeOutboundsLatencyResponse:
        url = '/api/node/{node_id}/outbounds_latency'.format(node_id=node_id)
        params = {'name': name, 'timeout': timeout}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, NodeOutboundsLatencyResponse)

    async def realtime_nodes_stats(self, token: str) -> Dict[str, Optional[NodeRealtimeStats]]:
        url = '/api/nodes/realtime_stats'
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Dict[str, Optional[NodeRealtimeStats]])

    async def user_online_ip_list_all_nodes(self, username: str, token: str) -> UserIPListAll:
        url = '/api/node/online_stats/{username}/ip'.format(username=username)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserIPListAll)

    async def user_online_stats(self, node_id: int, username: str, token: str) -> Dict[str, int]:
        url = '/api/node/{node_id}/online_stats/{username}'.format(node_id=node_id, username=username)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Dict[str, int])

    async def user_online_ip_list(self, node_id: int, username: str, token: str) -> UserIPList:
        url = '/api/node/{node_id}/online_stats/{username}/ip'.format(node_id=node_id, username=username)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserIPList)

    async def clear_usage_data(self, table: UsageTable, token: str, start: Optional[datetime] = None, end: Optional[datetime] = None) -> Any:
        url = '/api/nodes/clear_usage_data/{table}'.format(table=table)
        params = {'start': start, 'end': end}
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def bulk_delete_nodes(self, bulk: BulkNodeSelection, token: str) -> RemoveNodesResponse:
        url = '/api/nodes/bulk/delete'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveNodesResponse)

    async def bulk_disable_nodes(self, bulk: BulkNodeSelection, token: str) -> BulkNodesActionResponse:
        url = '/api/nodes/bulk/disable'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkNodesActionResponse)

    async def bulk_enable_nodes(self, bulk: BulkNodeSelection, token: str) -> BulkNodesActionResponse:
        url = '/api/nodes/bulk/enable'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkNodesActionResponse)

    async def bulk_reset_nodes_usage(self, bulk: BulkNodeSelection, token: str) -> BulkNodesActionResponse:
        url = '/api/nodes/bulk/reset'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkNodesActionResponse)

    async def bulk_reconnect_nodes(self, bulk: BulkNodeSelection, token: str) -> BulkNodesActionResponse:
        url = '/api/nodes/bulk/reconnect'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkNodesActionResponse)

    async def bulk_update_nodes(self, bulk: BulkNodeSelection, token: str) -> BulkNodesActionResponse:
        url = '/api/nodes/bulk/update'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkNodeSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkNodesActionResponse)
