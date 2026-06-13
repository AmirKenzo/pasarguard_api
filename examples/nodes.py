"""
Node management.

Methods covered:
- get_node_settings, get_usage, get_user_count_metric
- get_nodes, get_nodes_simple
- create_node, get_node, modify_node, remove_node
- update_node, update_core, update_geofiles
- reset_node_usage, reconnect_node, sync_node, node_logs
- get_node_stats_periodic, realtime_node_stats, node_outbounds_latency
- realtime_nodes_stats
- user_online_ip_list, user_online_stats, user_online_ip_list_all_nodes
- clear_usage_data, reconnect_all_node, bulk node operations

Run: python nodes.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import BulkNodeSelection, PasarguardAPI, Period, UserCountMetric

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        await api.get_node_settings(token=token)
        print("OK get_node_settings")

        nodes = await api.get_nodes(token=token, limit=10)
        print(f"OK get_nodes -> {len(nodes.nodes)} of {nodes.total}")

        simple = await api.get_nodes_simple(token=token, limit=10)
        print(f"OK get_nodes_simple -> {len(simple.nodes)} nodes")

        usage = await api.get_usage(token=token, period=Period.DAY)
        print(f"OK get_usage -> {len(usage.stats)} keys")

        metric = await api.get_user_count_metric(
            metric=UserCountMetric.ONLINE, token=token, period=Period.HOUR
        )
        print("OK get_user_count_metric")

        all_stats = await api.realtime_nodes_stats(token=token)
        print(f"OK realtime_nodes_stats -> {len(all_stats)} nodes")

        if not simple.nodes:
            print("No nodes found")
            return

        node_id = simple.nodes[0].id
        node = await api.get_node(node_id=node_id, token=token)
        print(f"OK get_node -> {node.name}")

        rt = await api.realtime_node_stats(node_id=node_id, token=token)
        print(f"OK realtime_node_stats -> cpu={rt.cpu_usage}%")

        stats = await api.get_node_stats_periodic(node_id=node_id, token=token, period=Period.HOUR)
        print(f"OK get_node_stats_periodic -> {len(stats.stats)} records")

        await api.node_outbounds_latency(node_id=node_id, token=token)
        print("OK node_outbounds_latency")

        users = await api.get_users_simple(token=token, limit=1)
        if users.users:
            user_id = users.users[0].id
            ips = await api.user_online_ip_list(node_id=node_id, user_id=user_id, token=token)
            print(f"OK user_online_ip_list -> {len(ips.ips)} IPs")

            online = await api.user_online_stats(node_id=node_id, user_id=user_id, token=token)
            print(f"OK user_online_stats -> {online}")

            await api.user_online_ip_list_all_nodes(user_id=user_id, token=token)
            print("OK user_online_ip_list_all_nodes")

        bulk = BulkNodeSelection(ids=[node_id])
        # await api.update_node(node_id=node_id, token=token)
        # await api.update_core(node_id=node_id, node_core_update=NodeCoreUpdate(core_version="1.8.0"), token=token)
        # await api.update_geofiles(node_id=node_id, node_geo_files_update=NodeGeoFilesUpdate(region=GeoFilseRegion.IRAN), token=token)
        # await api.reset_node_usage(node_id=node_id, token=token)
        # await api.reconnect_node(node_id=node_id, token=token)
        # await api.sync_node(node_id=node_id, token=token, flush_users=False)
        # await api.node_logs(node_id=node_id, token=token)
        # await api.reconnect_all_node(token=token)
        # await api.clear_usage_data(table=UsageTable.NODE_USAGES, token=token)
        # await api.bulk_disable_nodes(bulk, token=token)
        # await api.bulk_enable_nodes(bulk, token=token)
        # await api.bulk_reset_nodes_usage(bulk, token=token)
        # await api.bulk_reconnect_nodes(bulk, token=token)
        # await api.bulk_update_nodes(bulk, token=token)
        # await api.bulk_delete_nodes(bulk, token=token)

        print("INFO modify/reconnect/sync/bulk — commented out")
        print("\nDone — nodes reviewed")


if __name__ == "__main__":
    asyncio.run(main())
