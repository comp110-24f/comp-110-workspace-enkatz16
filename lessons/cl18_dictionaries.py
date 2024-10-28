"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "stawberry": 4}
# len evaluates to the number of entries
print(len(ice_cream))
# add key-value entry by directly assigning to a key
ice_cream["mint"] = 3
# access entries by their key
print(ice_cream["chocolate"])
# test if "pbj" is a key in ice_cream
has_pbj: bool = "pbj" in ice_cream
# to remove, we use the pop method and give a key

print(ice_cream)

ice_cream.pop("strawberry")
# to iterate over every key in a loop, use for... in
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders")