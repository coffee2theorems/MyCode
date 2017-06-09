--defines a factorial function
function fact (n)
    if n == 0 then
        return 1
    else
        return n * fact(n-1)
    end
end

print("Enter a number:")
a = io.read("*n") -- reads a number
while a <= 0 do
    print("Error: Please enter a number greater than 0")
    print("Enter a number:")
    a = io.read("*n")
end
print(fact(a))
