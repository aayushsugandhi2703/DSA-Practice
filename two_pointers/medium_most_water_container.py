# You are given an integer array heights where heights[i] represents the height of the ith bar. 
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

def trap(heights):
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        current_water = width * height
        max_water = max(max_water, current_water)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water
#complexity: O(n) time and O(1) space

def main():
    heights = [0,2,0,3,1,0,1,3,2,1]
    result = trap(heights)
    print(f"The maximum amount of water a container can store is: {result}")

if __name__ == "__main__":
    main()