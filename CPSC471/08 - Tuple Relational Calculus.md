### Relational Calculus
 - A tuple relational calculus expression creates a new relation, specified in terms of variables that range over rows of the stored database relations
 - In a calculus expression, there is no order of operations to specify how to retrieve the query result, a calculus expression specifies only what information the result should contain
	 - Main distinguising feature between relational algebra and relational calculus
 - Considered to be *nonprocedural* or *declarative*
 - This differs from relational algebra, must write a sequence of operations to specify a retrieval request (relational algebra can be considered as a procedural way of stating a query)
 - Reminder: `p -> q` is equivalent to `(not p) or q`

### Predicate Logic
 - A predicate is a parametric statement involving variables
	 - Monkey(x) : x is a monkey
	 - Likes(x, y) : x likes y
 - These are not propositions, but can be converted to propositions
	 - Monkey(Curious George) is a true proposition
	 - Monkey(Road Runner) is false
 - Predicates are converted to propositions using *quantifiers*
 - There are two quantifiers
	 - Existential: ∃
	 - Universal: ∀
 - Truth values of quantifiers require a *universe of discourse*
 - Examples: Universe of Discourse is the 471 class
	 - ∀x Male(x) is false
	 - ∃x Female(x) is true
	 - ∃x (Female(x) and Smart(x)) is true
	 - ∀x (Female(x) and Smart(x)) is false
	 - ∀x (Female(x) -> Smart(x)) is true

### Quantifier Equivalence
 - ∀x P(x) is equivalent to not ∃x (not P(x))
 - ∃x P(x) is equivalent to not ∀x (not P(x))
 - Demorgan's Rules:
	 - not(p and q) = (not p) or (not q)
	 - not(p or q) = (not p) and (not q)

### Tuple Relational Calculus
 - A simple RC query has the structure:
	 - `{t | COND(t)}`
 - t is a tuple variable
	 - Usually ranges over a particular database relation
	 - EMPLOYEE(t): we require t to be an employee
 - COND(t) is a conditional expression involving t
 - The result of such a query is the set of all tuples t that satisfy COND(t)
 - Example:
	 - Retrieve the first and last names of all employees whose salary is above $50000
	 - `{e.Fname, e.Lname | EMPLOYEE(e) and e.Salary > 50000}`
	 - The condition EMPLOYEE(e) specifies that the range relation of tuple variable e is EMPLOYEE