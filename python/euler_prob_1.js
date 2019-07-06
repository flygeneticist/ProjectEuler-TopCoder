//Find the sum of all the multiples of 3 or 5 below 1000.
var sum = 0;
for (var num=999; num>2; num--) {
	if ((num%5 == 0) || (num%3 == 0)) {
		sum += num;
	}
}

alert(sum); // 233168