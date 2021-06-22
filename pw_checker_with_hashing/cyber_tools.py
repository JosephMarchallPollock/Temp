import hashlib


def show_algorithms_available():
    print(hashlib.algorithms_guaranteed)


def hashes_match(h1, h2):
    if (h1 == h2):
        return True
    else:
        return False


def get_popular_passwords_from_file(file_name, p_list):
    with open(file_name) as file:
        for line in file:
            line = line.rstrip("\n")
            p_list.append(line)


def get_hashed_password(plaintext_password, algo="sha1"):

    pw = plaintext_password.encode()

    if algo == "sha1":
        hash_object = hashlib.sha1(pw)
    elif algo == "sha256":
        hash_object = hashlib.sha256(pw)
    elif algo == "sha512":
        hash_object = hashlib.sha512(pw)
    elif algo == "sha224":
        hash_object = hashlib.sha224(pw)
    elif algo == "sha384":
        hash_object = hashlib.sha384(pw)
    elif algo == "md5":
        hash_object = hashlib.md5(pw)
    else:
        hash_object = None

    hex_dig = hash_object.hexdigest()
    return hex_dig
