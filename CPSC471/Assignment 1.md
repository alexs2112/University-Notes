### Entities:
 - Author: **Email**, Name(First, Last)
 - Paper: **Identifier**, Title, Abstract, Filename, *Authors*(Contact Author), *Topics*
	 - Short
	 - Long
 - System: ***Papers***(NumPages, NumFigures, NumTables, NumReferences)
	 - These attributes should be derived
 - Reviewer: **Email**, Name(First, Last), Phone Number, Affiliation, *Topics*
 - Review: `Ratings`(Technical, Readability, Originality, Relevance), `Recommendation`
 - Comment: `Text`, Review?
	 - Confidential
	 - Feedback

**bolded** attributes are key attributes
*italicized* attributes are multivalued attributes
`inline` attributes are partial key attributes

### Relationships:
 - Author Writes Paper (N-M, Full-Full)
 - System AssignsID to Paper (1-N, Full-Full)
 - Reviewer Assigned Paper (N-M, Full-Partial)
 - Reviewer Writes Review (1-1, Full-Full)
 - Paper Receives Review (1-1, Partial-Full)
 - Review Contains Comment (1-N, Full-Full)

### Assumptions:
 - Every author needs to write at least one paper to be a part of the database
 - Authors and Reviewers cannot be the same person in a given conference
 - Every reviewer needs to be assigned at least one paper to write a review to be a part of the database
 - A paper does not need to be assigned a reviewer in order to exist in the database
