from parse import parse
result = parse("hello, {name}", "hello, Matthew")
print(result.named)
