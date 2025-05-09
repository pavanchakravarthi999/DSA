class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_count = 0
        count = [0] * 26  # Array to count character frequencies
        left = 0

        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[right]) - ord('A')])

            # Shrink the window if the number of replacements exceeds k
            while (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length
