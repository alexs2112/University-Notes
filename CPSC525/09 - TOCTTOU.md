### Overview
 - Time Of Check To Time Of Use
	 - **Check**: Establish some precondition
	 - **Use**: Act, assuming precondition is (still) satisfied
 - Essentially, a race condition being created as an exploit
 - Dangers: Validating if a user can access a file, and then opening the file
	 - The file can be switched out between checking and using the file
**The Fix**:
 - Idea: Force victim program to perform an expensive I/O operation
	 - While waiting for I/O to complete, victim will yield CPU to attacker, giving an opportunity to switch symlinks
 - But how:
	 - Make sure file being accessed is not in file system cache
	 - Force victim to traverse very deep directory structures
 - Symlink attack: Each symlink directing to a huge number of other symlinks and inodes, causing the executable to sleep until the intended file is fetched
	 - While it is traversing the maze to check if the file is safe to open, you can replace the first symlink.
	 - It will see that the original file is safe to open, then goes to open the symlink again which is now pointing at an evil file

### TOCTTOU Defenses
 - When performing privileged actions, ensure all access control information remains constant between time of check and time of use
	 - Keep a private copy of requests so it can't be altered
	 - When possible, act directly on object
	 - [finish]
