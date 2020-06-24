function runningSum(nums: number[]): number[] {
    let previous: number = nums[0];
    for (let i:number = 1; i<nums.length; i++) {
        nums[i] = nums[i] + previous
        previous = nums[i]
    }
    return nums
};
