
use std::io;
mod problems; // import all problems


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
        let result = dispatcher(choice);
        println!("{}", result);
        break;
    }
}

fn dispatcher(choice: u32) -> String {
    match choice {
        1 => problems::p1(),
        10 => problems::p10(),
        11 => problems::p11(),
        12 => problems::p12(),
        13 => problems::p13(),
        14 => problems::p14(),
        _ => "That problem is not available.".to_string(),
    }
}
