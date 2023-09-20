### Secure Shell
 - A cryptographic network protocol for operating network services securely over an unsecured network

### Operating System
 - Collection of software that directs a computer's operations, including:
	 - Controlling and scheduling the execution of other programs
	 - Managing storage, input/output, communications
 - Facilitates sharing resources among a set of users
 - Provides access control mechanisms
	 - Authorization requires identification and authentication

### Unix users and superusers
 - Each user has a username (UID), group name (GID), password
 - `root` is an administrator/superuser (UID 0)
	 - Can read or write any file or system resource
	 - Can modify the operating system
	 - Can become any other user
		 - Execute commands on behalf of any users' ID
	 - Cannot read other users passwords as they aren't stored directly on the machine
		 - Root can change any user's password
 - `SUDO`: a Unix program that allows users to run programs with the privileges of another user (by default, the superuser)
	 - *s*uper*u*ser *do*
	 - Not to be confused with `su`
		 - `su` requires root password, `sudo` can be invoked with non-root password
	 - Sudoers are specified in `/etc/sudoers`
		 - Formatted as follows:
		 - `<username> <machine name>=(<user>:<group>) <command>`
		 - `root ALL=(ALL:ALL) ALL`
			 - Root can use sudo, on ALL hosts, to run ALL commands, as ALL users (and ALL groups)
		 - `alex localhost=(bob) cat dog`
			 - Alex can use sudo, on localhost, to run cat or dog as user bob
	 - Run `[/usr/bin/]visudo`, must be run as root

### Unix access control
 - **Everything is a file, everything**
	 - Files are laid out in a tree
	 - Each file associated with an inode data structure
 - inode holds information about the file
	 - UID and GID of the file owner
	 - Type, size, physical location on disk
	 - Time of last access (atime), last inode modification (ctime), last file content modification (mtime)
	 - Permission bits
	 - ...
 - `<filetype><owner><group><everyone> <# of hard links> <owner> <group> <size> <mtime> <filename>`
 - `-rw-r--r-- 1 alexander.stevenson cpsc525 3771 Apr  4  2018 .bashrc `
 - Filetypes:
	 - `-` regular
	 - `d` directory
	 - `b` block device
	 - `c` character file
	 - `l` symbolic link
	 - `p` pipe
	 - `s` socket
 - Permission bits:
	 - `r` read
	 - `w` write
	 - `x` execute (directories: traverse)
	 - `s` setuid, setgid (directories: files have gid of dir owner)
	 - `t` sticky bit (directories: make append only)
