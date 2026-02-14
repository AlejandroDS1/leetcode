from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def change_gas_station(lap_done):
            if (current_gas_station + 1) == n:
                lap_done = True
            return (current_gas_station + 1) % n, lap_done

        n = len(gas)

        gas_index = 0
        current_gas_station = 0

        lap_done = False
        gas_tank = 0

        # While we didn't make a whole lap
        while gas_index != (n):

            # First thing we do, fill our tank
            gas_tank += gas[current_gas_station]

            # If we can not go to the next station,
            # Our current gas index is going to be this gas station
            if 0 > (gas_tank - cost[current_gas_station]):
                
                if lap_done: return -1 # If we have faild and we already made a lap, return -1

                current_gas_station, lap_done = change_gas_station(lap_done) # Update it considering a looping road
                gas_index = current_gas_station
                gas_tank = 0
            else:
                # If we can reach the next gas station,
                # 1.- Update the gas_tank
                gas_tank = gas_tank - cost[current_gas_station]

                # 2.- Update the current_gas_station
                current_gas_station, lap_done = change_gas_station(lap_done)

                # If the reached gas station is the gas_index, the solution is found
                if gas_index == current_gas_station: return gas_index