use std::io;

fn main() {
    println!("Welcome to my Project Euler program.");

    loop {
        println!("Please enter the number of the Euler problem you wish to run:");
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
        println!("~~~ RUNNINNG PROBLEM #{} NOW ~~~", choice);
        break;
    }
}
