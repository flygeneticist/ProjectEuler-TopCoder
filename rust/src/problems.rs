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

pub fn p11() -> String {
    // OBJECTIVE: What is the greatest product of four adjacent numbers in the same direction
    // (up, down, left, right, or diagonally) in the 20x20 grid?
    // SOLUTION:
    let mut max_product: i32 = 0;
    let mut grid = vec![];

    // data file to build the grid
    let f = File::open("../euler_prob_11_data.txt").unwrap();
    let file = BufReader::new(&f);
    // for each line in the file...
    for (_num, line) in file.lines().enumerate() {
        // 1. split line on spaces, parse into i32, and collect into Vector
        let a: Vec<i32> = line.unwrap().trim().split(' ')
            .map(|s| s.parse::<i32>().unwrap())
            .collect();
        // 2. add array to grid
        grid.push(a);
    }

    for l in 0..20 {
        for m in 0..16 {
            // let n = n as i32;
            // right/left products
            let prod = grid[l][m]*grid[l][m+1]*grid[l][m+2]*grid[l][m+3];
            if prod > max_product {
                max_product = prod;
            }
            // up/down products
            let prod = grid[m][l]*grid[m+1][l]*grid[m+2][l]*grid[m+3][l];
            if prod > max_product {
                max_product = prod;
            }
        }
    }

    // find all diagonal products
    for l in 0..16 {
        for m in 0..16 {
            let prod = grid[l][m]*grid[l+1][m+1]*grid[l+2][m+2]*grid[l+3][m+3];
            if prod > max_product {
                max_product = prod;
            }
        }
    }
    for l in 3..20 {
        for m in 0..16 {
            let prod = grid[l][m]*grid[l-1][m+1]*grid[l-2][m+2]*grid[l-3][m+3];
            if prod > max_product {
                max_product = prod;
            }
        }
    }
    format!("{}", max_product)
}

pub fn p12() -> String {
    // OBJECTIVE: What is the value of the first triangle number to have
    // over five hundred divisors?
    // SOLUTION:
    let mut x = 20;
    let mut tri_num = euler_lib::triangle_number(x);
    let mut factors = euler_lib::find_factors(tri_num);

    while factors.len() < 500 {
        x = x + 1;
        tri_num = euler_lib::triangle_number(x);
        factors = euler_lib::find_factors(tri_num);
    }
    format!("Triangle Number: {}\nNumber of factors: {}", tri_num, factors.len())
}

pub fn p13() -> String {
    // OBJECTiVE: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    // SOLUTION:
    let mut sum: f64 = 0.0;
    // Read in the file
    let f = File::open("../euler_prob_13_data.txt").unwrap();
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
