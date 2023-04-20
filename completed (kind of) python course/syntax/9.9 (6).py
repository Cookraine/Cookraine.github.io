import sys

# old_data = list(input().split())
data = list(map(int, input().split()))
print(data)

if data[0] == 12 and data[1] < 32 and data[1] > 0:
	astro_sign = 'Sagittarius' if (data[0] < 22) else 'capricorn'
elif data[0] == 1 and data[1] < 32 and data[1] > 0:
	astro_sign = 'Capricorn' if (data[0] < 20) else 'aquarius'
elif data[0] == 2 and data[1] < 30 and data[1] > 0:
	astro_sign = 'Aquarius' if (data[0] < 19) else 'pisces'
elif data[0] == 3 and data[1] < 32 and data[1] > 0:
	astro_sign = 'Pisces' if (data[0] < 21) else 'aries'
elif data[0] == 4 and data[1] < 31 and data[1] > 0:
	astro_sign = 'Aries' if (data[0] < 20) else 'taurus'
elif data[0] == 5 and data[1] < 32 and data[1] > 0:
	astro_sign = 'Taurus' if (data[0] < 21) else 'gemini'
elif data[0] == 6 and data[1] < 31 and data[1] > 0:
	astro_sign = 'Gemini' if (data[0] < 21) else 'cancer'
elif data[0] == 7 and data[1] < 32 and data[1] > 0:
	astro_sign = 'Cancer' if (data[0] < 23) else 'leo'
elif data[0] == 8 and data[1] < 32 and data[1] > 0:
	astro_sign = 'Leo' if (data[0] < 23) else 'virgo'
elif data[0] == 9 and data[1] < 31 and data[1] > 0:
	astro_sign = 'Virgo' if (data[0] < 23) else 'libra'
elif data[0] == 10 and data[1] < 32 and data[1] > 0:
	astro_sign = 'Libra' if (data[0] < 23) else 'scorpio'
elif data[0] == 11 and data[1] < 31 and data[1] > 0:
	astro_sign = 'scorpio' if (data[0] < 22) else 'sagittarius'
else:
	print("invalid date")
	exit()
print("Your Astrological sign is :",astro_sign)
