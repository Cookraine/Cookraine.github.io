sentence = list(input().split())
del sentence[0]
del sentence[len(sentence) - 1]

print(' '.join(sentence))