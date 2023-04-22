def fBMI(obvod_hrudniku, delka_nohy):
    return ((obvod_hrudniku/0.7062 - delka_nohy) / 0.9156) - delka_nohy


obvod = int(input('Zadej obvod hrudniku: '))
delkanohy = int(input('Zadej delku zadni nohy: '))

print(f"fBMI je {fBMI(obvod, delkanohy)}")