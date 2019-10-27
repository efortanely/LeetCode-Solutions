class Solution {
public:
    bool isMatch(string s, string p) {
        bool M[s.length() + 1][p.length() + 1];
        memset(M, false, sizeof(bool) * (s.length() + 1) * (p.length() + 1));
        M[s.length()][p.length()] = true;
        for(int i = s.length(); i >= 0; i--){
            for(int j = p.length() - 1; j >= 0; j--){
                int first_ch = i < s.length() && (p[j] == '.' || p[j] == s[i]);
                //Case 1: Ignore the wildcard and skip the pattern
                //Case 2: Keep the wildcard and continue using the pattern
                if(j + 1 < p.length() && p[j+1] == '*'){
                    M[i][j] = M[i][j+2] || (first_ch && M[i+1][j]);
                //Case 3: Use the single c/. value
                }else{
                    M[i][j] = first_ch && M[i+1][j+1];
                }
            }
        }
        return M[0][0];
    }
};    
