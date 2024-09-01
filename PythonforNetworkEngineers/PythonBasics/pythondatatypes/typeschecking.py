# types checking
i = 1

print(f"{i}:", 'message'.isdigit());i+=1
print(f"{i}:", 'mes45'.isdigit());i+=1
print(f"{i}:", '45'.isdigit());i+=1
print(f"{i}:", 'mes45'.isalpha());i+=1
print(f"{i}:", 'mes'.isalpha());i+=1
print(f"{i}:", 'mes '.isalpha());i+=1
print(f"{i}:", 'mes..'.isalpha());i+=1
print(f"{i}:", 'mes45'.isalnum());i+=1
print(f"{i}:", type('message') == str);i+=1


