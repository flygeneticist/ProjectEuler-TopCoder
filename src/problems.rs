pub fn p1() -> String {
    // OBJECTIVE: Find the sum of all the multiples of 3 or 5 below 1000.
    // SOLUTION:
    // The sum of all numbers divisible by 3 is:
    // n=1 to 333: Σ(3n) --> n=1 to 333: 3*Σ(n) --> 3*(333*334)/2
    let threes: u32 = 3 * 333 * 344 / 2;
    // The sum of all numbers divisible by 5 is:
    // n=1 to 199: Σ(5n) --> n=1 to 199: 5*Σ(n) --> 5*(199*200)/2
    let fives: u32 = 5 * 199 * 200 / 2;
    // We count multiples of 15 in both the sums above we need to subtract them out
    // The sum of all numbers divisible by 15 is:
    // n=1 to 66: Σ(15n) --> n=1 to 66: Σ(15n) --> 15*(66*67)/2
    let fifteens: u32 = 15 * 66 * 67 / 2;
    // Finally add threes and fives and subtract fifteens to yield the answer!
    (threes + fives - fifteens).to_string()
}

pub fn p2() -> String {
    // OBJECTiVE: Find the sum of all the primes below two million.
    // ex. The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    // SOLUTION:
    // Use Sieve of Eratosthenes to find all primes less than `n`.
    let n: usize = 2_000_000;
    let mut primes = vec![true; n + 1];

    for p in 2..n + 1 {
        // if prime[p] is not changed => prime
        if primes[p] {
            // update all multiples of p
            for i in ((p * p)..(n + 1)).step_by(p) {
                primes[i] = false
            }
        }
    }

    // sum up all prime numbers
    let mut sum = 0;
    for i in 2..n {
        if primes[i] {
            sum += i;
        }
    }
    sum.to_string()
}
