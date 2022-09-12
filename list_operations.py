l = [11, 4, 8, 16, 32, 64, 128, 100, 256]

print(l[2:-4]) #[8,16,32]

print(l[::1]) #will just print the list as it is
print(l[::2]) #[11, 8, 32, 128, 256]

print(l[-1] + l[-1:])