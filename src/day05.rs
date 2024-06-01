use std::fs;

fn three_vowels(input: &str) -> bool {
    let mut counter = 0;
    
    for vowel in vec!['a', 'e', 'i', 'o', 'u'] {
        counter += input.chars().filter(|c| *c == vowel).count();
    }
    
    return counter >= 3;
}

fn twice_in_a_row(input: &str) -> bool {
    input.chars().zip(input.chars().skip(1)).any(|(c1, c2)| c1 == c2)
    // .zip() zips the iterator with a second iterator where we skip the first letter
    // then we compare if the two iterators, that are misplaced by one, show the same character with .any()
    
}

fn bad_strings(input: &str) -> bool {
    for bad_string in vec!["ab", "cd", "pq", "xy"] {
        if input.contains(&bad_string) {
            return false;
        }
    }
    return true;
}

// TODO
fn pair_appears_twice(input: &str) -> bool {
    let x = input.chars().zip(input.chars().skip(1)).filter(|(c1, c2)| c1 == c2);
    let counter = 0;
    for elem in x {
        println!("{} {}", elem.0, elem.1);
    }
    return false;
}


fn main() {
    let contents = fs::read_to_string("inputs/day05.txt")
        .expect("Should have been able to read the file");

    let mut nice_strings = 0;

    for line in contents.lines() {
        if three_vowels(line) & twice_in_a_row(line) & bad_strings(line) {
            nice_strings += 1;
        }
        let a = pair_appears_twice(line);
    }

    println!("Given the old ridiculous rules, {} strings are nice.", nice_strings);
    
}