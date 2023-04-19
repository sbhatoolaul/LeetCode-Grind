# LeetCode Grind
Documenting My Solution Keys to [LeetCode](https://leetcode.com/) Questions for Interview Preparations.

LeetCode Profile: [sbhatoolaul](https://leetcode.com/sbhatoolaul/).

The solutions are also organized by topics to make it easier to review for interviews. I picked questions from the [Blind75](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions) problems and organized the topics like [NeetCode](https://neetcode.io/) did. Some of the questions I picked are also from NeetCode's 150.


## Solution Keys by Topic 💻

### Arrays & Hashing
| Question                      | Keys           |
| ----------------------------- | ------------- |
| Contains Duplicate            | Use a set.   |
| Valid Anagram                 | Use 2 dictionaries to count the occurence of each letter in both words. Return True if they match, False otherwise. |
| Two Sum                       |  More space-efficient solution: Sort, then use two pointers—decrement the right pointer if you need less sum, or increment the left pointer if you need more sum. This solution only works if you need the two numbers, not the indices, since sorting would shuffle that. More time-efficient solution: Go through the array and store each number in a dictionary to see if we can add this number to a number we already seen to get the target sum.  |
| Group Anagrams                | Get frequency of each character for each word. Group the unique ones using a dictionary. |
| Top K Frequent Elements       | Use bucket sort... or a max heap (less time-efficient). |
| Product of Array Except Self  | Use prefix-product, and suffix-product to find pattern. |
| Encode & Decode Strings       | To encode properly (i.e. dealing with any character) use something like str(len(str)) + "#" + str, that way we know how many characters to skip over to get to the next string. |
| Longest Consecutive Sequence  | Convert the arary to a set. Then, go through each number, and check if it is the start of a sequence by checking if the number before it exists. If it is the start, keep checking if next number exists. Return the longest of these sequences. |

### Two Pointers
| Question                      | Process       |
| ----------------------------- | ------------- |
| Valid Palindrome              |  |
| 3Sum                          |  |
| Container with Most Water     |  |