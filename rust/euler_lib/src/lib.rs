pub fn triangle_number(n: i32) -> i32 {
    // find the sum of natural numbers where n represents the Nth Triangle number
    (n*(n+1))/2
}

pub fn find_factors(n: i32) -> Vec<i32> {
    // find all factors of a given number
	let mut factors = vec![];
    let n_float = n as f32;
	let x = n_float.sqrt().ceil() as i32;
    for i in 1..x {
        if n%i == 0 {
            factors.push(i);
            factors.push(n/i);
        }
    }
	factors
}
