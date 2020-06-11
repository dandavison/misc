use fancy_regex::Regex;

#[derive(Copy, Clone, Debug, Eq, PartialEq)]
pub struct Match<'t> {
    text: &'t str,
    start: usize,
    end: usize,
}

impl<'t> Match<'t> {
    pub fn start(&self) -> usize {
        self.start
    }

    pub fn end(&self) -> usize {
        self.end
    }
}

pub fn regex_find_iter<'a>(regex: &Regex, text: &'a str) -> Vec<Match<'a>> {
    let mut matches = Vec::<Match>::new();
    let mut offset = 0;
    while let Some(_match) = regex.find(&text[offset..]).unwrap() {
        matches.push(Match {
            text,
            start: offset + _match.start(),
            end: offset + _match.end(),
        });
        offset += _match.end();
    }
    matches
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_regex_find_iter() {
        let text = "Retroactively relinquishing remunerations is reprehensible.";
        let regex = Regex::new(r"\b\w{13}\b").unwrap();
        let matches: Vec<(usize, usize)> = regex_find_iter(&regex, text)
            .iter()
            .map(|m| (m.start(), m.end()))
            .collect();
        assert_eq!(&matches, &[(0, 13), (14, 27), (28, 41), (45, 58)]);
    }
}
