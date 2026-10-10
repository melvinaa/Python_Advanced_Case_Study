
import re
from datetime import datetime


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not re.fullmatch(r"[A-Za-z0-9]{5,}", value):
            raise ValueError(
                "Username minimal 5 karakter dan hanya boleh berisi huruf/angka."
            )
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not re.fullmatch(r"(?=.*\d).{8,}", value):
            raise ValueError(
                "Password minimal 8 karakter dan wajib mengandung angka."
            )
        self._password = value


def audit_log(login_function):
    """Mencatat setiap percobaan login."""

    def wrapper(user, password):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            hasil, alasan = login_function(user, password)
        except Exception as error:
            hasil, alasan = False, str(error)

        status = "BERHASIL" if hasil else f"DITOLAK - {alasan}"
        print(
            f"[{timestamp}] User: {user.username:<10} | Status: {status}"
        )
        return hasil

    return wrapper


@audit_log
def login(user, password):
    if not re.fullmatch(r"[A-Za-z0-9]{5,}", user.username):
        return False, "Format username tidak sesuai"

    if not re.fullmatch(r"(?=.*\d).{8,}", password):
        return False, "Password minimal 8 karakter dan wajib mengandung angka"

    if password != user.password:
        return False, "Password salah"

    return True, "Login valid"


def main():
    print("=== SISTEM KEAMANAN AKUN & AUDIT LOG ===")

    # 1. Username tidak valid
    print("\n1. Uji username tidak valid:")
    try:
        User("Ayu!", "Password1")
    except ValueError as error:
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"[{waktu}] User: Ayu!       | "
            f"Status: DITOLAK - {error}"
        )

    # 2. Password terlalu pendek
    print("\n2. Uji password terlalu pendek:")
    try:
        User("Ayu123", "Pass1")
    except ValueError as error:
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"[{waktu}] User: Ayu123     | "
            f"Status: DITOLAK - {error}"
        )

    # 3. Password tidak mengandung angka
    print("\n3. Uji password tanpa angka:")
    try:
        User("Budi123", "Password")
    except ValueError as error:
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"[{waktu}] User: Budi123    | "
            f"Status: DITOLAK - {error}"
        )

    # 4. Login sukses
    print("\n4. Uji login sukses:")
    user_valid = User("Cantika", "Cantika123")
    login(user_valid, "Cantika123")

    # 5. Login dengan password salah
    print("\n5. Uji login dengan password salah:")
    login(user_valid, "Salah1234")


if __name__ == "__main__":
    main()