import secrets
import string
import random
import argparse
import pyperclip # برای کپی در کلیپ‌بورد

def generate_secure_password(length: int, exclude_ambiguous: bool, no_special: bool) -> str:
    # ۱. تعریف مجموعه‌های کاراکتری
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # ویژگی اول: حذف کاراکترهای گیج‌کننده (Ambiguous)
    if exclude_ambiguous:
        ambiguous = "lI1O0o"
        for char in ambiguous:
            lowercase = lowercase.replace(char, "")
            uppercase = uppercase.replace(char, "")
            digits = digits.replace(char, "")
            special = special.replace(char, "")

    # اگر کاربر علامت خاص نخواست
    if no_special:
        special = ""

    # ۲. ساخت لیست نهایی کاراکترهای مجاز
    all_chars = lowercase + uppercase + digits + special
    
    # ۳. تضمین وجود حداقل یک کاراکتر از هر دسته موجود
    password_chars = []
    if lowercase: password_chars.append(secrets.choice(lowercase))
    if uppercase: password_chars.append(secrets.choice(uppercase))
    if digits: password_chars.append(secrets.choice(digits))
    if special: password_chars.append(secrets.choice(special))

    # ۴. پر کردن باقی‌مانده طول رمز
    password_chars += [secrets.choice(all_chars) for _ in range(length - len(password_chars))]

    # ۵. بر زدن امن
    random.SystemRandom().shuffle(password_chars)
    
    return "".join(password_chars)

def main():
    # ویژگی دوم: استفاده از argparse برای مدیریت ورودی‌های خط فرمان
    parser = argparse.ArgumentParser(description="Professional Secure Password Generator")
    
    parser.add_argument("-l", "--length", type=int, default=24, help="طول رمز عبور (پیش‌فرض: ۲۴)")
    parser.add_argument("-a", "--ambiguous", action="store_true", help="حذف کاراکترهای مشابه (مثل I, l, 1, 0, O)")
    parser.add_argument("-ns", "--no-special", action="store_true", help="تولید رمز بدون علائم خاص")
    parser.add_argument("-nc", "--no-copy", action="store_true", help="غیرفعال کردن کپی خودکار در کلیپ‌بورد")

    args = parser.parse_args()

    try:
        password = generate_secure_password(args.length, args.ambiguous, args.no_special)
        
        print(f"\n[+] Generated Password: {password}")
        print(f"[+] Length: {len(password)}")

        # ویژگی سوم: کپی در کلیپ‌بورد
        if not args.no_copy:
            try:
                pyperclip.copy(password)
                print("[*] Password copied to clipboard!")
            except pyperclip.PyperclipException:
                print("[!] Clipboard not available on this system. Install xclip, xsel, or wl-clipboard.")

    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    main()
