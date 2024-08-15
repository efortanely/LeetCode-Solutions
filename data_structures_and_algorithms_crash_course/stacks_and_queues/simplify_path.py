class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for p in path.split("/"):
            if not p or p == ".":
                pass
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return "/" + "/".join(stack)

def main():
    runner = Solution()

    path = "/home/"
    ans = runner.simplifyPath(path)
    print(ans)

if __name__ == "__main__":
    main()