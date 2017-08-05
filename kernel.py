from jupyter_client import BlockingKernelClient


class HydrogenClient(BlockingKernelClient):

    def kernel_information(self):
        self.kernel_info()
