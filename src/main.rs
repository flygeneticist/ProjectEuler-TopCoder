
use std::collections::HashMap;
use std::io;
// import all problems
mod problems;


fn main() {
    println!("Welcome to my Project Euler program.");

    let mut dispatch = HashMap::new();
    // add problems to dispacter hash table
    dispatch.insert(1, problems::p1());

    loop {
        println!(
            "Please enter the number of the Euler problem you wish to run:\n{:?}",
            dispatch.keys()
        );

        let mut choice = String::new();
        io::stdin()
            .read_line(&mut choice)
            .expect("failed to read line.");
        let choice: u32 = match choice.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Sorry, that's not a valid number.");
                continue;
            }
        };

        println!("You chose Problem #{}.", choice);

        match dispatch.get(&choice) {
            Some(x) => {
                println!("~~~ RUNNING PROBLEM #{} NOW ~~~", choice);
                println!("Solution is: {}", x);
                break;
            }
            None => {
                println!("That problem is not available.");
                continue;
            }
        };
    }
}
