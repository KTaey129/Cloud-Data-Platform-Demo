# Week 1 Foudations & Stateful Workloads

## Linux
### Why do we use systemd?
to manage system settings and services.systemd organizes tasks into components called units and groups of units into targets.
essential for functionalities such as servicem anagement, dependency tracking, logging, resource managements, socket activation and system control.

#### What is systemd?
systemd is a system and service manager for Linux operating systems.
default initalization system for major Linux distritbutions.
installed through the /sbin/init
started during the early boot

a service is a component that performs a specific function, such as managing a web server or an SSH connection. While a full systemd implementation is not running in the container to save resources, the service command provides a simplified way to manage these background programs, allowing you to start, stop, or check the status of each one individually.

#### Units and Targets
A target is a special type of unit that serves a specific purpose: it's used to group other units together. 
Think of it as a state or a collection of services that define a particular system setup. 
For example, the multi-user.target unit defines the state where the system is ready for multiple users to log in, but without a graphical interface. 
graphical.target includes everything from multi-user.target plus the services needed for a desktop environment.

