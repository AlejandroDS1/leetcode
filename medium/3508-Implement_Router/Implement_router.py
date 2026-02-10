import queue
class Router:
    def __init__(self, memoryLimit: int):
        self.packet_queue = queue.Queue(maxsize = memoryLimit)
        self.maxSize = memoryLimit
        self.set_packet_list = set()
        self.packets = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:

        # Check if there is no duplicates:
        incoming_package = (source, destination, timestamp)

        if incoming_package in self.set_packet_list: return False

        if self.packet_queue.full():
            deleted_package = self.packet_queue.get(block = False)
            self.packets[deleted_package[1]].popleft()
            self.set_packet_list.remove(deleted_package)
            #print(f"First item removed, current list: {self.packet_queue}")

        self.packet_queue.put(incoming_package, block=False)
        self.packets[destination].append(timestamp)
        self.set_packet_list.add(incoming_package)

        #print(f"Package added: {incoming_package}. Current list: {self.packet_queue}")
        return True


    def forwardPacket(self) -> List[int]:

        if self.packet_queue.empty(): return []

       #print(f"Forward, current list: {self.packet_queue}")
        dp = self.packet_queue.get(block=False)
        self.set_packet_list.remove(dp)
        self.packets[dp[1]].popleft()

        #print(f"Forward, elment removed: {dp}")
        return [*dp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        return bisect.bisect_right(self.packets[destination], endTime) - bisect.bisect_left(self.packets[destination], startTime)