// Task 1
**Datatype check:** (by dtypes attributes and .unique() method)
- product_id -> integer value
- category -> string value
- animal -> string value
- size -> string value
- price -> string value (Not correct)
- sales -> float value
- rating -> float value
- repeat_purchase -> integer value


**Missing Value check: (by .isna() and .sum() methods)**
- product_id -> none
- category -> none
- animal -> none
- size -> none
- price -> none
- sales -> none
- rating -> 150x null value
- repeat_purchase -> none

**Data range check: (by .unique() method)**
- category -> Not correct, null value is replaced with "-" but not "Unknown"
- animal -> Correct
- size -> Not correct, same data is in different form
- rating -> Correct, 1~9

**Data Precision check, Rounded value: (by .unique() method) **
-> price -> Not float datatype (Not correct)
-> sales -> Rounded to 2 decimal place


** Actions: **
- Null value in category column should be replaced with "Unknown"
- Data in the size table should be unified (small, Small, SMALL -> Small)
- Datatype in price column should be replaced with float instead of string
- 150x missing value should be replaced with 0 (pending)


**Summary :**
- 1. Description of product_id, animal, sales and repeated_purchase are correct 
- 2. Data in the size table should be unified -> Action done
- 3. Null value in category column should be replaced with "Unknown" -> Action done
- 4. Datatype in price column should be replaced with float instead of string -> Action done
- 5. 150x missing value should be replaced with 0 -> Action done






// Task 2