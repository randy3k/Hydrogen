from jupyter_core.paths import jupyter_runtime_dir
from jupyter_client.channels import HBChannel
import os
import glob
import time

from .kernel import HydrogenClient


def get_connection_files(active_only=False):
    cfs = glob.glob(os.path.join(jupyter_runtime_dir(), "kernel-*.json"))
    if active_only:
        clients = []
        for cf in cfs:
            hc = HydrogenClient(connection_file=cf)
            clients.append(hc)
            hc.load_connection_file()
            hc.start_channels()

        # HBChannel.time_to_dead is 1.0
        time.sleep(HBChannel.time_to_dead + 0.1)
        active_clients = [hc for hc in clients if hc.hb_channel.is_beating()]
        active_cfs = [hc.connection_file for hc in active_clients]

        for hc in clients:
            hc.stop_channels()

        return (active_cfs)
    else:
        return(cfs)
