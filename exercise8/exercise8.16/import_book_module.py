# 1. Menggunakan: import module_name
import book_module
book_module.favorite_book("Alice in Wonderland")

# 2. Menggunakan: from module_name import function_name
from book_module import favorite_book
favorite_book("The Lord of the Rings")

# 3. Menggunakan: from module_name import function_name as fn
from book_module import favorite_book as fb
fb("Atomic Habits")

# 4. Menggunakan: import module_name as mn
import book_module as bm
bm.favorite_book("Python Crash Course")

# 5. Menggunakan: from module_name import *
from book_module import *
favorite_book("Clean Code")