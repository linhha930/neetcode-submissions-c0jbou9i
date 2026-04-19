class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        car_times = []

        # sorted_arr = (curr_pos, curr_speed)
        sorted_arr = sorted(zip(position, speed), reverse=True) 
        for curr_pos, curr_speed in sorted_arr:
            remain_miles = target - curr_pos
            time = remain_miles / curr_speed
            car_times.append(time)

        fleets = 0
        max_time = 0
        for i, time in enumerate(car_times):
            if time > max_time:
                max_time = time
                fleets += 1

        return fleets