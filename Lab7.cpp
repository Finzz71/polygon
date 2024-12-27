#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxChunksToSorted(vector<int>& arr)
{
    int chunks = 0;

    vector<int> sortedArr = arr;
    sort(sortedArr.begin(), sortedArr.end());

    long long prefixSumArr = 0;
    long long prefixSumSorted = 0;

    for (int i = 0; i < arr.size(); ++i) {
        prefixSumArr += arr[i];
        prefixSumSorted += sortedArr[i];

        if (prefixSumArr == prefixSumSorted) {
            ++chunks;
        }
    }

    return chunks;
}

int main()
{
    vector<int> nums = { 1,3,4,5,1,2,3 };
    int result = maxChunksToSorted(nums);
    cout << "Number of chunks: " << result << std::endl;

    return 0;
}