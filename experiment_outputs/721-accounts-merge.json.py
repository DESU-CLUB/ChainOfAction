```python
class Solution:
    def dfs(self, graph, node, visited, emails):
        if node in visited:
            return
        visited.add(node)
        emails.append(node)
        for neighbor in graph[node]:
            self.dfs(graph, neighbor, visited, emails)
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Step 1: Create a graph where each node is an email and edges connect emails belonging to the same account.
        graph = defaultdict(set)
        email_to_name = {}
        
        # Step 3: Iterate over the accounts to build the graph and keep track of the email to name mapping.
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                graph[first_email].add(email)
                graph[email].add(first_email)
                email_to_name[email] = name
        
        # Step 4: Initialize a set to keep track of visited emails.
        visited = set()
        merged_accounts = []
        
        # Step 5: Iterate over each email in the graph.
        for email in graph:
            if email not in visited:
                emails = []
                # Step 5a: Perform a DFS to collect all connected emails.
                self.dfs(graph, email, visited, emails)
                # Step 5b: Sort the collected emails and prepend the associated name.
                emails.sort()
                merged_accounts.append([email_to_name[email]] + emails)
        
        # Step 6: Return the merged account list.
        return merged_accounts
```