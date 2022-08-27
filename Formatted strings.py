                                                            # Formatted strings are useful for generating
                                                            # Dynamic content with variables
first = "John"
last = "Smith"
message = first + ' [' +last+ '] is a coder'
print(message)                                      #  this is the output we wanted,but it's difficult to visualize this
                                                    #  as text gets more complex and complicated due to the method we used.
                                                    #  Therefore, we have formatted strings method for easy visualization
msg = f'{first} [{last}] is a coder'
print(msg)                                          #  To easily input text, we use formatted strings and we use it by using
                                                    #  small letter f followed by message in quotes. Wherever we need to use
                                                    #  variable, we use curly braces for that.
msg = f"""{first} is a brilliant coder since he is a {last}"""
print(msg)                                          #  We can use triple double quotes and single double quotes the same way
