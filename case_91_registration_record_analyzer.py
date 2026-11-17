records = [
    "24CSE0123|Aarav Kumar|2024|CSE",
    "24ECE0456|Nisha Rao|2024|ECE",
    "24CSE0123|Aarav Kumar|2024|CSE",
    "24CS0123|Dev Shah|2024|CSE",
]
valid_ids = []
valid_count = 0
duplicate_count = 0
invalid_count = 0

for record in records:
    fields = record.split("|")
    valid_format = len(fields) == 4
    if valid_format:
        identifier = fields[0]
        valid_format = (len(identifier) == 9 and identifier[0:2].isdigit()
                        and identifier[2:5].isalpha() and identifier[2:5].isupper()
                        and identifier[5:9].isdigit() and fields[1] != "")
    if not valid_format:
        print(f"INVALID   {fields[0]}   (identifier format is incorrect)")
        invalid_count += 1
    elif identifier in valid_ids:
        print(f"DUPLICATE {identifier}  (already listed)")
        duplicate_count += 1
    else:
        valid_ids.append(identifier)
        print(f"VALID     {identifier}  {fields[1]:<12} {fields[3]}  {fields[2]}")
        valid_count += 1

print(f"\nSummary: {valid_count} valid unique records, {duplicate_count} duplicate, {invalid_count} invalid record")
