class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(start, parts):
            # If we have 4 parts
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            # Try 1, 2, or 3 digits
            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Leading zero is not allowed
                if len(part) > 1 and part[0] == "0":
                    continue

                # Value must be <= 255
                if int(part) > 255:
                    continue

                parts.append(part)
                backtrack(start + length, parts)
                parts.pop()

        backtrack(0, [])

        return result