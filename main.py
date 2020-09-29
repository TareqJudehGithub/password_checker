import requests
import hashlib
import sys
import time


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError("Unable to fetch API! with error " + str(response.status_code))
    return response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        # if password tail matches:
        if h == hash_to_check:
            return count
    return 0


# Hashing passwords:
def pwned_api_check(password):
    # Check password if it exists in API response:
    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    # Store first 5 char in a var, and store the rest in another var:
    first5_char, tail = hashed_password[:5], hashed_password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times. You should probably change your password.")
        else:
            print(f"{password} was found {count} times. This is a good password.")
    time.sleep(1)
    return "Password check complete!"


print("")

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) 


# From Terminal, run: $ python3 main.py <your password>

