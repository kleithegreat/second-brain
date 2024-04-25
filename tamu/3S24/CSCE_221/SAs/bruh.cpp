vector<int> intersectionOfTwoArrays(vector<int>& nums, vector<int>& otherNums) {
    unordered_map<int, int> numCounts;
    
    // Count occurrences of elements in nums
    for (int num : nums) {
        numCounts[num]++;
    }
    
    vector<int> result;
    
    // Check for common elements in otherNums
    for (int num : otherNums) {
        if (numCounts[num] > 0) {
            result.push_back(num);
            numCounts[num]--;
        }
    }
    
    return result;
}




int ropesGameCost(vector<int>& ropes) {
    priority_queue<int, vector<int>, greater<int>> pq(ropes.begin(), ropes.end());
    
    int totalCost = 0;
    
    while (pq.size() > 1) {
        int rope1 = pq.top();
        pq.pop();
        int rope2 = pq.top();
        pq.pop();
        
        int combinedRope = rope1 + rope2;
        totalCost += combinedRope;
        
        pq.push(combinedRope);
    }
    
    return totalCost;
}
