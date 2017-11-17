# This program adds two numbers

# numbers
first_num = 2
second_num = 3

# calculate and print result
sum = first_num + second_num
print "%d  + %d = %d" % (first_num, second_num, sum)

# now with user provided numbers
first_num = int(raw_input("Enter the first number: "));
second_num = int(raw_input("Enter the second number: "));

# calculate and print result
print "The sum is: %d" % (first_num + second_num);
