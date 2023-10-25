random_list = [105, 3.1, "Hello", 737, "python", 2.7, "World", 412, 5.5, "AI"]

# Filter untuk memisahkan nilai float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int_value(value):
    ratusan = value // 100
    puluhan = (value // 10) % 10
    satuan = value % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

int_mapped_values = list(map(map_int_value, int_values))

# Output
print("Data Float:", float_values)
print("Data Int:")
for item in int_mapped_values:
    print(item)
print("Data String:", string_values)