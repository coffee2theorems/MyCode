#!/usr/bin/env lua
-- file: SlimShady.lua
-- Exercise 1.5: Write a simple script that prints
-- it's own name without knowing it in advance.

-- the script name is always the first
-- parameter in arg
print("My name is: " .. arg[0])
a = io.read()
-- print("You just entered:" .. a) -- Testing what .. does in a print statement
