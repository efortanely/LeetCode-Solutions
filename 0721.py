class Solution(object):
    def accountsMerge(self, accounts):
        graph = collections.defaultdict(set)
        emails_to_name = dict()

        for account in accounts:
            name, emails = account[0], account[1:]
            first = emails[0]
            for email in emails:
                graph[first].add(email)
                graph[email].add(first)
                emails_to_name[email] = name

        seen = set()
        ans = []
        for email in graph.keys():
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nbr in graph[node]:
                        if nbr not in seen:
                            seen.add(nbr)
                            stack.append(nbr)
                ans.append([emails_to_name[email]] + sorted(component))
        
        return ans
