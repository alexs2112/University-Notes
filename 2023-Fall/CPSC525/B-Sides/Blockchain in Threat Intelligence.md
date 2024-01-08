### Limitations of Traditional CTI (Cyber Threat Intelligence) Models
 - Inadequate threat actor understanding hinders effective defense
 - Data overload and scattered information types and sources hampers efficient threat analysis
 - Lack of real-time intelligence delays response efforts
 - Lack of clear quality assurance criteria results in dissemination of low quality information
 - CTIs are rarely shared between corporations for security, privacy, and competition concerns

### Why Use Blockchain for CTI
 - CTI demand is growing, need to be able to share CTIs and intelligence without compromising privacy

**Blockchain Offers**:
	 - Tamper proof data ensuring data integrity
	 - Utilizes reputation mechanism to build trust within CTI sharing community
	 - Enforces quality standards for CTI finds
	 - Reliable sources, sufficient context, consistent data models, defined processes, automation

**Application Roles**:
	 - Submitter: Submits intel with attribution and proof
	 - Validator: Evaluates intel, assigns a score. If the mean score is greater than acceptable quality score, it is added to the blockchain
	 - Consumer: Any user who wants to use the CTI information, able to search for IOCs and see related info. Consumers would pay a subscription fee to use this service, which is distributed between the submitter and validator.

### Summary
 - Cyber Threat Intelligence (CTI) models are highly sought after by corporations, with many corporations developing and evaluating their own set of Indicators of Compromise (IOC) to complete a set of security models.
 - There is of wasted effort as there is a lot of duplicated work between these corporations as they create a database of IOCs.
 - Sharing IOCs and CTI models is not encouraged. These models are typically more specific for each corporation, and there are concerns around security, privacy, and corporate competition.
 - A blockchain can be used to ensure data integrity and enforced quality standards for provided CTIs such that users can submit and search for CTIs without concern.

**My Opinion**:
 - I don't see why a blockchain is necessary for this purpose. You need some third party of validators who evaluate submitted intelligence before adding them to the blockchain database. You also need a third party in charge of distributing the subscription fee between users.
 - The blockchain can just be replaced with a regular database controlled by some third party, the unique advantages that a blockchain offers are not super relevant here.
 - If corporations are already averse to sharing their CTI models, I doubt they would be any more willing to share them just because they are stored on a blockchain, this fails to resolve the problems listed above in any reasonable capacity.
