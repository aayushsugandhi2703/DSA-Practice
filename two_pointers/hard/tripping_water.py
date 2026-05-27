# You are given an array of non-negative integers height which represent an elevation map. 
# Each value height[i] represents the height of a bar, which has a width of 1.
# Return the maximum area of water that can be trapped between the bars.

def trap(heights):
    left, right = 0, len(heights)-1
    max_water = 0
    left_max, right_max = heights[left], heights[right]

    while left<right:
        if heights[left] < heights[right]:
            left +=1
            left_max = max(left_max, heights[left])
            max_water +=  left_max - heights[left]
        else:
            right -=1
            right_max = max(right_max, heights[right])
            max_water += right_max - heights[right]
    return max_water
#complexity: O(n) time and O(1) space

def main():
    heights = [0,2,0,3,1,0,1,3,2,1]
    result = trap(heights)
    print(f"The maximum area of water that can be trapped between the bars is: {result}")

if __name__ == "__main__":
    main()