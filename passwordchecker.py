import requests
import hashlib
import sys


def request_api_data(query_char):  # (query_char) => hashed pass
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError("Error fetching: API! with error " + str(res.status_code))
    return res


def get_password_leaks_count(hashes, hash_to_check):  # (hashed pass, tail)
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        # if tail matches:
        if h == hash_to_check:
            return count
    return 0


# Hashing passwords:
def pwned_api_check(password):
    # Check password if it exists in API response:
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    # Store first 5 char in a var, and store the rest in another var:
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times. You should probably change your password.")
        else:
            print(f"{password} was found {count} times. This is a good password.")

        return "Password check complete!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
