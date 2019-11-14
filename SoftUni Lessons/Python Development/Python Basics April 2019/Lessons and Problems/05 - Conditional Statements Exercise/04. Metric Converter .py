number = float(input())
entry_m = input()
exit_m = input()

mm_to_m = number / 1000
mm_to_cm = number / 10

cm_to_mm = number * 10
cm_to_m = number / 100

m_to_mm = number * 1000
m_to_cm = number * 100

if entry_m == "mm" and exit_m == "m":
    print(f"{mm_to_m:.3f}")
elif entry_m == "mm" and exit_m == "cm":
    print(f"{mm_to_cm:.3f}")
elif entry_m == "mm" and exit_m == "mm":
    print(f"{number:.3f}")
elif entry_m == "cm" and exit_m == "mm":
    print(f"{cm_to_mm:.3f}")
elif entry_m == "cm" and exit_m == "m":
    print(f"{cm_to_m:.3f}")
elif entry_m == "cm" and exit_m == "cm":
    print(f"{number:.3f}")
elif entry_m == "m" and exit_m == "mm":
    print(f"{m_to_mm:.3f}")
elif entry_m == "m" and exit_m == "cm":
    print(f"{m_to_cm:.3f}")
elif entry_m == "m" and exit_m == "m":
    print(f"{number:.3f}")
