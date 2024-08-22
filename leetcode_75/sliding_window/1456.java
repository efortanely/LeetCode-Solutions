class Solution {
    public int maxVowels(String s, int k) {
        int vowels = 0;
        int maxVowels = 0;
        Set<Character> vowelsSet = Set.of('a', 'e', 'i', 'o', 'u');

        for(int i = 0; i < k; i++){
            char c = s.charAt(i);
            if(vowelsSet.contains(c)){
                maxVowels++;
            }
        }

        vowels = maxVowels;

        for(int i = k; i < s.length(); i++){
            if(vowelsSet.contains(s.charAt(i-k))){
                vowels--;
            }
            if(vowelsSet.contains(s.charAt(i))){
                vowels++;
            }

            maxVowels = Math.max(maxVowels, vowels);
        }

        return maxVowels;
    }
}