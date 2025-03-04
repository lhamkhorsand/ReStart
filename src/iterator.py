import random
words= words = ["کتاب", "کامپیوتر", "پایتون", "ماشین", "خانه", "درخت", "دریا", "آسمان", "دستگاه", "موزیک",
         "شهر", "کوه", "رودخانه", "سیاره", "فضا", "نور", "ستاره", "جزیره", "فصل", "گلابی"]

steps = 10

word_iter = iter(words)

for _ in range(steps):
      step_size = random.randint(1, 4)

      for _ in range(step_size):
            word = next(word_iter)

      print(f"گام {step_size}: کلمه '{word}'")
