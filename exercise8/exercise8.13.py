def build_profile(first, last, **user_info):
    """Membangun dictionary berisi segala hal yang kita ketahui tentang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile(
    'kayla', 
    'kafka', 
    location='kebumen', 
    occupation='mahasiswa', 
    hobbies='reading'
)

print(my_profile)