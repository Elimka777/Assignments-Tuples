def merge_catalogs(*catalogs):
    combined_catalog = tuple()
    for catalog in catalogs:
        combined_catalog += catalog
    return combined_catalog

# Example Catalogs
catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

# Example usage
merged_catalog = merge_catalogs(catalog1, catalog2)
print(merged_catalog)
