# LeetCode Grind
Documenting My Solution Keys to [LeetCode](https://leetcode.com/) Questions for Interview Preparations.

LeetCode Profile: [sbhatoolaul](https://leetcode.com/sbhatoolaul/).

The solutions are also organized by topics to make it easier to review for interviews. I picked questions from the [Blind75](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions) problems and organized the topics like [NeetCode](https://neetcode.io/) did. Some of the questions I picked are also from NeetCode's 150.


## Solution Keys by Topic 💻

### Arrays & Hashing
| Question                                                  | Keys           |
| ----------------------------------------------------------| -------------- |
| Contains Duplicate                                        | Use a set.   |
| Valid Anagram                                             | Use 2 dictionaries to count the occurence of each letter in both words. Return True if they match, False otherwise. |
| Two Sum                                                   |  More space-efficient solution: Sort, then use two pointers—decrement the right pointer if you need less sum, or increment the left pointer if you need more sum. This solution only works if you need the two numbers, not the indices, since sorting would shuffle that. More time-efficient solution: Go through the array and store each number in a dictionary to see if we can add this number to a number we already seen to get the target sum.  |
| Group Anagrams                                            | Get frequency of each character for each word. Group the unique ones using a dictionary. |
| Top K Frequent Elements                                   | Use bucket sort... or a max heap (less time-efficient). |
| Product of Array Except Self                              | Use prefix-product, and suffix-product to find pattern. |
| Encode & Decode Strings                                   | To encode properly (i.e. dealing with any character) use something like str(len(str)) + "#" + str, that way we know how many characters to skip over to get to the next string. |
| Longest Consecutive Sequence                              | Convert the arary to a set. Then, go through each number, and check if it is the start of a sequence by checking if the number before it exists. If it is the start, keep checking if next number exists. Return the longest of these sequences. |

### Two Pointers
| Question                                                  | Keys          |
| --------------------------------------------------------- | ------------- |
| Valid Palindrome                                          | Convert all to lower case, use two pointers from start to end to check if palindrome, jump over alphanumerical characters. |
| 3Sum                                                      | Same as 2Sum, but as you go through the array, set each number as the pivot, and look for 2Sum in the rest of the array. Sort at the beginning and ignore duplicates to bring runtime down.  |
| Container with Most Water                                 | Initialize a pointer at the start and end of the array. Set new maximum produced with current start and end indices, if it's bigger than our current maxium. Next, if the value at the start pointer is less than the value at the end pointer, move it up one, else move the end pointer down one, and do this until the pointers reach other, then return the maximum 


### Sliding Window
| Question                                                  | Keys          |
| --------------------------------------------------------- | ------------- |
| Best Time to Buy And Sell Stock                           | Go through array, and keep track of lowest price (start of the window). At each iteration, compare current price - lowest price and update maximum. |
| Longest Substring Without Repeating Characters            | Use a set to keep track of characters we've seen. Set `start` of window to the start of the string. Iterate through the characters, keep track of maximum window size at each iteration, and if we run into a character we've seen before, increment start while popping character at `string\[start]` until the duplicate is removed.|
| Longest Repeating Character Replacement                   | Iterate through the characters, keep track of most frequent character at each iteration. If more than k different characters from the most frequent character in window, shrink window.  |
| Minimum Window Substring                                  | Get frequency of character in string `t`. Go through characters in string `s` and try to get `len(t)` matches. If we hit `len(t)` matches, try to shrink window, while keeping `len(t)` matches.  |


### Stack
| Question                                                  | Keys          |
| --------------------------------------------------------- | ------------- |
| Valid Parentheses                                         | Iterate through the string. Push open brackets to stack. If we come across a closed bracket, pop from stack, and make sure the type is correct, else return False. Return True if stack is empty at end.  |