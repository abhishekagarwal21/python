with open('files\write.txt','a') as write_file:
    write_file.write('Welcome to write file test program.')

with open('files\write.txt', 'a') as write_file:
    write_file.write('\n This is next line into write.txt.')

quotes = [
    '\nThis is quotes 1.',
    '\nThis is quote 2.',
    '\nThis is quote 3'
]

with open('files\write.txt', 'a') as write_file:
    write_file.writelines(quotes)
