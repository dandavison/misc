use console;
use std::cmp::min;

use itertools::Itertools;

/// Return string formed from a byte slice starting at byte position `start`, where the index skips
/// bytes in ANSI escape sequences.
pub fn ansi_preserving_slice(s: &str, start: usize) -> String {
    console::AnsiCodeIterator::new(s)
        .scan(0, |i, (s, is_ansi)| {
            let s = if *i > start {
                s
            } else if is_ansi {
                s
            } else if s.is_empty() {
                s
            } else {
                &s[min(s.len(), start - *i)..]
            };
            if !is_ansi {
                *i += s.len();
            }
            Some(s)
        })
        .join("")
}

#[cfg(test)]
mod tests {

    use crate::ansi::ansi_preserving_slice;

    #[test]
    fn test_ansi_preserving_slice_1() {
        assert_eq!(ansi_preserving_slice("", 0), "");
    }

    #[test]
    fn test_ansi_preserving_slice_2() {
        assert_eq!(ansi_preserving_slice("a", 0), "a");
    }

    #[test]
    fn test_ansi_preserving_slice_3() {
        assert_eq!(ansi_preserving_slice("a", 1), "");
    }

    #[test]
    fn test_ansi_preserving_slice_4() {
        assert_eq!(
            ansi_preserving_slice("\x1b[1;35m-2222.2222.2222.2222\x1b[0m", 1),
            "\x1b[1;35m2222.2222.2222.2222\x1b[0m"
        );
    }

    #[test]
    fn test_ansi_preserving_slice_5() {
        assert_eq!(
            ansi_preserving_slice("\x1b[1;35m-2222.2222.2222.2222\x1b[0m", 15),
            "\x1b[1;35m.2222\x1b[0m"
        );
    }
}
