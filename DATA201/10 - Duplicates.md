### Detecting Duplicates
 - Three methods:
	 - **Levenshtein Distance**
		 - Comparing two text entries and counting how many edits are needed to convert one value to another
		 - The shorter the distance, the more likely they are to be the same
	 - **Soundex/Metaphone**
		 - Comparing how similar different entries sound
	 - **Fingerprinting**
		 - Strip away all unnecessary details (punctuation, capitals, etc)

### Fixing Duplicates
 - **Questions to think about**:
	 - Which duplicate to keep?
	 - Outliers: keep, remove, or repair?
	 - How to deal with bad formats?
 - **Some ways to fix problems**:
	 - Fuzzy matching systems
	 - Machine learning to detect/resolve errors
	 - Usually requires human judgement (especially for new data)
 - **Common Operations**:
	 - Correct and remove errors
	 - Change formats
	 - Remove formatting
