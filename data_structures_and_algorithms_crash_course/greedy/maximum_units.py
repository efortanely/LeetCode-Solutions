from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_boxes = sorted(boxTypes, key=lambda x: x[1])
        max_units = 0

        while len(sorted_boxes) and truckSize > 0:
            num_boxes, num_units = sorted_boxes.pop()

            boxes_fit = num_boxes if num_boxes <= truckSize else truckSize
            
            truckSize -= boxes_fit
            max_units += boxes_fit * num_units

        return max_units

def main():
    runner = Solution()

    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    ans = runner.maximumUnits(boxTypes, truckSize)
    print(ans)

if __name__ == "__main__":
    main()