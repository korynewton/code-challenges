int rob(int *nums, int numsSize)
{
    // base cases
    switch (numsSize)
    {
    case 0:
        return 0;
    case 1:
        return nums[0];
    default:
        break;
    };

    //set second index to first index if first index is greater
    if (nums[0] > nums[1])
    {
        nums[1] = nums[0];
    }

    //loop through nums using dynamic programming to keep track of largest count throughout
    for (int i = 2; i < numsSize; i++)
    {
        nums[i] = nums[i] + nums[i - 2] > nums[i - 1] ? nums[i] + nums[i - 2] : nums[i - 1];
    }

    return nums[numsSize - 1];
}
