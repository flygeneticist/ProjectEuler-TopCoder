use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

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

pub fn p10() -> String {
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

pub fn p13() -> String {
    // OBJECTiVE: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    // SOLUTION:
    let mut sum: f64 = 0.0;
    // Read in the file
    let f = File::open("euler_prob_13_data.txt").unwrap();
    let file = BufReader::new(&f);
    // for each line in the file...
    for (_num, line) in file.lines().enumerate() {
        // 1. convert to f64
        let n = line.unwrap().parse::<f64>().unwrap();
        // 2. add to a growing sum value
        sum = sum + n;
    }
    // take only the first 10 char of sum
    match sum.to_string().get(0..10) {
        Some(x) => x.to_string(),
        None => "".to_string(),
    }
}

pub fn p12() -> String {
    // Project Euler - Problem 12 - Highly divisible triangular number
    // The sequence of triangle numbers is generated by adding the natural numbers.
    // So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
    // The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55,...

    // OBJECTiVE: What is the value of the first triangle number to have over five hundred divisors?
    // SOLUTION:

    "Done!".to_string()
}