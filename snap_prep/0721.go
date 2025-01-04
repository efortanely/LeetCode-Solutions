func accountsMerge(accounts [][]string) [][]string {
    graph := map[string][]string{}
    emails_to_name := map[string]string{}
    
    for _, account := range(accounts) {
        name := account[0]
        emails := account[1:]
        first := emails[0]
        for _, email := range(emails){
            graph[first] = append(graph[first], email)
            graph[email] = append(graph[email], first)
            emails_to_name[email] = name
        }
    }
    
    seen := map[string]bool{}
    ans := [][]string{}
    for email, _ := range(graph){
        if seen[email] == false{
            seen[email] = true
            stack := []string{email}
            component := []string{}
            for len(stack) > 0{
                node := stack[len(stack)-1]
                stack = stack[:len(stack)-1]
                component = append(component, node)
                for _, nbr := range(graph[node]){
                    if seen[nbr] == false{
                        seen[nbr] = true
                        stack = append(stack, nbr)
                    }
                }
            }
            ans_append := []string{emails_to_name[email]}
            sort.Strings(component)
            ans_append = append(ans_append, component...)
            ans = append(ans, [][]string{ans_append}...)
        }
    }    
    
    return ans
}
