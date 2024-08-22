class Solution {
    public int maxOperations(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        int operations = 0;

        for(int num : nums){
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        for(int num : counter.keySet()){
            int numCount = counter.get(num);

            if(num >= k){
                continue;
            }

            int pair = k - num;

            if(num == pair){
                operations += numCount / 2;
                counter.put(num, counter.get(num) - (numCount / 2));
            }else if(counter.get(pair) != null){
                int pairCount = counter.get(pair);
                int numPairs = Math.min(numCount, pairCount);
                operations += numPairs;
                counter.put(num, counter.get(num) - numPairs);
                counter.put(pair, counter.get(pair) - numPairs);
            }
        }

        return operations;
    }
}