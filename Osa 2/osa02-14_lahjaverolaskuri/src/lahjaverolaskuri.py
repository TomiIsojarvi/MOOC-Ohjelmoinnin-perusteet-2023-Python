lahja = int(input("Lahjan suuruus? "))

if lahja < 5000:
    print("Ei veroa!")
elif lahja >= 5000 and lahja <= 25000:
    print("Vero:", 100 + (lahja - 5000) * 0.08, "euroa")
elif lahja >= 25000 and lahja <= 55000:
    print("Vero:", 1700 + (lahja - 25000) * 0.10, "euroa")
elif lahja >= 55000 and lahja <= 200000:
    print("Vero:", 4700 + (lahja - 55000) * 0.12, "euroa")
elif lahja >= 200000 and lahja <= 1000000:
    print("Vero:", 22100 + (lahja - 200000) * 0.15, "euroa")
else:
    print("Vero:", 142100 + (lahja - 1000000) * 0.17, "euroa")