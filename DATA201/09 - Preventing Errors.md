### Integrity Constraints
 - Defining what the response should look like
	- Realistic range constraint, type constraint
 - Do not prevent bad data
 - Enforcing constraints may lead to frustration

### Prediction and Friction
 - Use data quality measures to predict how likely a value is to be correct
 - Adjust the interface to add friction when entering unlikely responses
	 - Example: "Are you sure you want to enter [weird input]"

### Minimize Sensor Errors
 - Check sensors before deployment
 - Periodically revalidate equipment
 - Use redundant sensors
 - Check data against historical logs or computed models
 - Use common sense

### Double Data Entry
 - Perform all data entry twice
 - Identify mismatches, then discard or repair

### Data Auditing & Error Detection
- Look for outliers and anomalies
- Examine data types
- Schema checking
