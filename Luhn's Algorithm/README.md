## Luhn Algorithm

This is a simple checksum formula that is used to validate identification numbers such as credit card numbers, IMEI numbers and so on.

It is also known as **modulus 10 or mod 10 algorithm**.

### Steps in Luhn Algorithm
* Starting from the rightmost digit, double the value of every second digit
*  If doubling results in a number > 9, add the digits of the product, to get a single number
* Take the sum of the all the digits
* If the total % 10 is equal to 0, then the number is VALID, otherwise it is INVALID