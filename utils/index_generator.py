"""
LeetCode Index Generator

This script generates index files for LeetCode solutions by scanning docstrings
in solution files and organizing them by difficulty, topic, etc.
"""

import os
import re
from collections import defaultdict
from pathlib import Path


class LeetCodeIndexGenerator:
    def __init__(self, solutions_dir="solutions", indexes_dir="indexes"):
        """Initialize with directories to scan and output to."""
        self.solutions_dir = Path(solutions_dir)
        self.indexes_dir = Path(indexes_dir)
        
        # Ensure the indexes directory exists
        os.makedirs(self.indexes_dir, exist_ok=True)
        
        # Data structures to hold categorized problems
        self.by_difficulty = defaultdict(list)
        self.by_topic = defaultdict(list)
        self.problems = []

    def scan_solutions(self):
        """Scan solution files and extract metadata."""
        solution_files = list(self.solutions_dir.glob("p*.py"))
        
        for file_path in solution_files:
            metadata = self._extract_metadata(file_path)
            if metadata:
                self.problems.append(metadata)
                
                # Categorize by difficulty
                self.by_difficulty[metadata["difficulty"]].append(metadata)
                
                # Categorize by topic
                for topic in metadata["topics"]:
                    self.by_topic[topic].append(metadata)

    
    def _extract_metadata(self, file_path):
        """Extract metadata from a solution file's docstring."""
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Extract problem number and name from filename
        filename = file_path.name
        match = re.match(r"p(\d+)_(.+)\.py", filename)
        if not match:
            return None
        
        problem_id = int(match.group(1))
        problem_name = match.group(2).replace("_", " ").title()
        
        # Extract metadata from docstring
        docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
        if not docstring_match:
            return {
                "id": problem_id,
                "name": problem_name,
                "difficulty": "Unknown",
                "topics": [],
                "companies": [],
                "file_path": file_path
            }
        
        docstring = docstring_match.group(1).strip()
        
        # Extract difficulty
        difficulty_match = re.search(r'Difficulty:\s*(\w+)', docstring)
        difficulty = difficulty_match.group(1) if difficulty_match else "Unknown"
        
        # Extract topics
        topics_match = re.search(r'Topics:\s*(.*?)(?:\n|$)', docstring)
        topics = []
        if topics_match:
            topics = [topic.strip() for topic in topics_match.group(1).split(",")]
        
        # Extract companies (optional)
        companies_match = re.search(r'Companies:\s*(.*?)(?:\n|$)', docstring)
        companies = []
        if companies_match:
            companies = [company.strip() for company in companies_match.group(1).split(",")]
        
        # Extract URL (optional)
        url_match = re.search(r'URL:\s*(\S+)', docstring)
        url = url_match.group(1) if url_match else None
        
        return {
            "id": problem_id,
            "name": problem_name,
            "difficulty": difficulty,
            "topics": topics,
            "companies": companies,
            "url": url,
            "file_path": file_path
        }

    def generate_indexes(self):
        """Generate all index files."""
        self._generate_difficulty_index()
        self._generate_topic_index()
        self._generate_main_index()
    
    def _generate_difficulty_index(self):
        """Generate index by difficulty."""
        with open(self.indexes_dir / "by_difficulty.md", "w", encoding="utf-8") as f:
            f.write("# Problems by Difficulty\n\n")
            
            # Sort difficulties in a sensible order
            difficulties = sorted(self.by_difficulty.keys(), 
                                 key=lambda x: {"Easy": 0, "Medium": 1, "Hard": 2}.get(x, 3))
            
            for difficulty in difficulties:
                f.write(f"## {difficulty}\n")
                
                # Sort problems by ID
                problems = sorted(self.by_difficulty[difficulty], key=lambda x: x["id"])
                
                for problem in problems:
                    topics_str = ", ".join(problem["topics"]) if problem["topics"] else ""
                    rel_path = os.path.relpath(problem["file_path"], self.indexes_dir)
                    
                    # Format: [1. Two Sum](../solutions/p0001_two_sum.py) - Hash Table, Array
                    f.write(f"- [{problem['id']}. {problem['name']}]({rel_path})")
                    if topics_str:
                        f.write(f" - {topics_str}")
                    f.write("\n")
                
                f.write("\n")
    
    def _generate_topic_index(self):
        """Generate index by topic."""
        with open(self.indexes_dir / "by_topic.md", "w", encoding="utf-8") as f:
            f.write("# Problems by Topic\n\n")
            
            # Sort topics alphabetically
            topics = sorted(self.by_topic.keys())
            
            for topic in topics:
                f.write(f"## {topic}\n")
                
                # Sort problems by ID
                problems = sorted(self.by_topic[topic], key=lambda x: x["id"])
                
                for problem in problems:
                    rel_path = os.path.relpath(problem["file_path"], self.indexes_dir)
                    
                    # Format: [1. Two Sum](../solutions/p0001_two_sum.py) - Easy
                    f.write(f"- [{problem['id']}. {problem['name']}]({rel_path}) - {problem['difficulty']}\n")
                
                f.write("\n")

    
    def _generate_main_index(self):
        """Generate main index with all problems."""
        with open(self.indexes_dir / "all_problems.md", "w", encoding="utf-8") as f:
            f.write("# All LeetCode Problems\n\n")
            
            # Sort all problems by ID
            problems = sorted(self.problems, key=lambda x: x["id"])
            
            for problem in problems:
                rel_path = os.path.relpath(problem["file_path"], self.indexes_dir)
                
                # Format: [1. Two Sum](../solutions/p0001_two_sum.py) - Easy - Hash Table, Array
                topics_str = ", ".join(problem["topics"]) if problem["topics"] else ""
                f.write(f"- [{problem['id']}. {problem['name']}]({rel_path}) - {problem['difficulty']}")
                if topics_str:
                    f.write(f" - {topics_str}")
                f.write("\n")


def main():
    """Main function to run the index generator."""
    generator = LeetCodeIndexGenerator()
    print("Scanning solution files...")
    generator.scan_solutions()
    print("Generating index files...")
    generator.generate_indexes()
    print("Done! Index files have been generated in the 'indexes' directory.")


if __name__ == "__main__":
    main()