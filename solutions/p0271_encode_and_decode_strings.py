"""
LeetCode #271: Encode and Decode Strings
Difficulty: Medium
Topics: Array, String, Design
Companies: Microsoft, Google, Meta, Amazon, OpenAI
URL: https://leetcode.com/problems/encode-and-decode-strings/
"""

from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""
        
        delimiter = "[#]"
        output_str = delimiter.join(str_item for str_item in strs)
        return output_str

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return [""]
        
        delimiter = "[#]"
        output_list = s.split(delimiter)
        return output_list
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))